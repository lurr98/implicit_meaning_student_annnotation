import re, uuid
import streamlit as st
from core.scripts.utils import display_progress, read_json_from_file, load_annotation, TASK_INFO

def remove_punctuation(text: str) -> str:

    text = "\n".join([el for el in text.split("\n") if el])

    # remove timestamps
    text = re.sub(r"Timestamp.*Z", "", text)
    text = re.sub(r"\s+(?=\d)", " ", text)
    # remove listed numbers before a line break
    text = re.sub(r"^(?=\d)", "´", text)
    text = re.sub(r"\d+\.?\n*$", "", text)
    
    # remove whitespace at beginning of lines for letters
    text = re.sub(r"\n\s+(?=\W)", "", text, flags=re.MULTILINE)
    # remove URLs
    text = re.sub(r"http[s]?://\S+|www\.\S+|<a href.+</a>", "<URL>", text)
    return re.sub(r"[”#*\+<=>\[\]\\^_`{|}~]", "", text)


def format_sample(question: dict) -> None:

    def labeled_paragraph(label, text, font_size="16px", font_weight="normal", indent="45"):
        st.markdown(
            f"""
            <div style="margin-left: 0; padding-left: {indent}px; text-indent: -{indent}px; font-size: {font_size}; font-weight: {font_weight}">
                <span style="background-color: rgba(210, 215, 225, 0.32); color: inherit; padding: 2px 4px; border-radius: 4px;">
                    {label}
                </span>
                {text}
            </div>
            """,
            unsafe_allow_html=True
        )

    # sentence 1 and 2 are switched bc we decided to put the revision first
    match = re.findall(r"<(.*)>", question["sentence_2"])
    blue_background = re.sub(r"<.*>", f":blue-background[{match[0]}]", question["sentence_2"])

    st.markdown(f":grey-background[*Article name:*] &emsp;{question["article_name"]}")
    st.markdown("")
    st.markdown(":grey-background[Read the following text and focus on the **bold sentence**.]")
    st.markdown(f"> {remove_punctuation(question["context_before"])}  \n> **{question["sentence_1"]}**  \n> {remove_punctuation(question["context_after"])}")
    st.markdown("")
    st.markdown("")
    st.markdown(":grey-background[Now read the modified text:]")
    st.markdown(f"> {remove_punctuation(question["context_before"])}  \n> **{blue_background}**  \n> {remove_punctuation(question["context_after"])}")
    st.markdown("")
    st.markdown("")
    st.markdown(":grey-background[What would most readers say?]")
    st.markdown(":grey-background[Would altering the bold sentence meaningfully change how they understand the text?]")

    
def check_all_checkboxes(implicit: str, checkboxes: list, comment: str, confidence: str) -> bool:

    if confidence:
        if implicit == "Yes":
            return True
        elif implicit == "No" and checkboxes[-1]:
            if comment:
                return True
        elif implicit == "No" and len([box for box in checkboxes[:-1] if box]) >= 1:
            return True
        else:
            return False
    else:
        return False


def print_annotation_schema(index: int, subtask: str="annotation") -> tuple[dict, str, list, str, str, int, bool]:
    """
    Prints the annotation schema that is seen on the qualification and annotation page.

    :param subtask: qualification or annotation
    :param index: The number sample to show
    :return: The sentence and widget inputs in the order they are displayed to the user.
    """
    if subtask == "qualification":
        samples = read_json_from_file(TASK_INFO["implicit_meaning_task"]["qualification_filepath"])
    else:
        samples = read_json_from_file(TASK_INFO["implicit_meaning_task"]["annotation_filepath"])

    # load values previously filled in checkboxes or None if this is first time annotating this sample
    sample_preload = load_annotation(subtask, index)
    if sample_preload is None:
        # implicit_val, context_val, reasoning_val, complement_val, instruction_val, other_val = None, None, None, None, None, None
        implicit_val, context_val, reasoning_val, background_val, other_val, confidence_pre = None, None, None, None, None, None
        comment_implicit_val, comment_general_val = "", ""
    else:
        implicit_val, context_val, reasoning_val, background_val, other_val, confidence_pre = (sample_preload["implicit_meaning"], 
                                                                                                sample_preload["if_implicit"][0], 
                                                                                                sample_preload["if_implicit"][1], 
                                                                                                sample_preload["if_implicit"][2], 
                                                                                                sample_preload["if_implicit"][3],
                                                                                                sample_preload["confidence_score"]
                                                                                                )
        comment_implicit_val, comment_general_val = (sample_preload["comment_implicit"], sample_preload["comment_general"])

    question = samples[str(index)]
    # # display the "Sample 1/5" thing
    display_progress(key=subtask)

    format_sample(question)

    context, reasoning, background, other = False, False, False, False
    comment_implicit, comment_general = "", ""
    # implicit = st.radio(
    #     ":grey-background[Does the first sentence implicitely convey the same meaning as the second one?]",
    #     ["Yes", "No"],
    #     key="implicit",
    #     horizontal=True,
    #     index=None,)

    implicit = st.segmented_control("", ["Yes", "No"], key=10 * index + 1, default=implicit_val)
    # col1, col2 = st.columns(2)
    # with col1:
    #     implicit = st.checkbox(key=10 * index + 1, label="Yes", value=None)
    # with col2:
    #     not_implicit = st.checkbox(key=10 * index + 2, label="No", value=None) 
    if implicit == "No":
        st.markdown("Please specify one or multiple reasons for your choice:")

        col1, col2 = st.columns(2)

        with col1:
            context = st.checkbox(key=10 * index + 2, label="Context", value=context_val, help="The added information is recoverable from the context.")
            reasoning = st.checkbox(key=10 * index + 3, label="Logical Reasoning", value=reasoning_val, help="The added information is a logical premise or consequence of the given text.")
            background = st.checkbox(key=10 * index + 4, label="Background Knowledge", value=background_val, help="The information in the added text was already anticipated due to existing background knowledge.")
            #complement = st.checkbox(key=10 * index + 4, label="Expected Information", value=complement_val, help="The type of information that was added is usually expected by the reader for the specific verb.")
            # instruction = st.checkbox(key=10 * index + 5, label="Recoverable Instruction", value=instruction_val, help="The same action could be performed from both instructions.")

        with col2:
            other = st.checkbox("Other", value=other_val)
            comment_implicit = st.text_input(key=10 * index + 6, label="If applicable, specify other reasons for your decision:", value=comment_implicit_val, max_chars=200)
            if comment_implicit:
                st.write(r"$\textsf{\scriptsize Thanks for your input!}$")

    checkboxes = [context, reasoning, background, other]
    
    # st.markdown("How confident are you about your annotation?")
    # confidence = st.slider(
    #     label="1 = Not at all, 5 = Very much",
    #     min_value=1,
    #     max_value=5,
    #     value=3,
    #     step=1,
    #     key=10 * index + 10
    # )
    st.write("")
    st.write("")
    radio_selection = ["1", "2", "3", "4", "5"]
    confidence = st.radio(
    "How confident are you about your annotation?\n\n1 corresponds to 'Not at all' and 5 to 'Very much'.",
    radio_selection,
    index=radio_selection.index(str(confidence_pre)) if confidence_pre else None,
    key=question["ID"],
    horizontal=True
    )

    st.write("")
    comment_general = st.text_input(key=10 * index + 7, label="Anything you'd like to point out?", value=comment_general_val, max_chars=200)
    if comment_general:
        st.write(r"$\textsf{\scriptsize Thanks for your input!}$")


    if check_all_checkboxes(implicit, checkboxes, comment_implicit, confidence):
        confidence = int(confidence)
        next_input = st.button(key = 10 * index + 8, label="Next", help="Save this annotation and advance to the next one.")
    else:
        next_input = None

    return question, implicit, checkboxes, comment_implicit, comment_general, confidence, next_input