import streamlit as st

with open("implicit_meaning_task/resources/annotation_guidelines_implicit_meaning_updated.md", "r") as md:
    markdown = md.read()

split_md = markdown.split("==SPLIT==")
first_md, second_md = split_md[0], split_md[1]

st.write(first_md)
implicit = st.segmented_control("", ["Yes", "No"])
 
if implicit == "No":
    st.markdown("Please specify one or multiple reasons for your choice:")
    col1, col2 = st.columns(2)
    with col1:
        context = st.checkbox(label="Context", help="The added information is recoverable from the context.")
        reasoning = st.checkbox(label="Logical Reasoning", help="The added information is a logical premise or consequence of the given text.")
        background = st.checkbox(label="Background Knowledge", help="The information in the added text was already anticipated due to existing background knowledge.")
    with col2:
        other = st.checkbox("Other")
        comment_implicit = st.text_input(label="If applicable, specify other reasons for your decision:", max_chars=200)
        if comment_implicit:
            st.write(r"$\textsf{\scriptsize Thanks for your input!}$")

st.write("")
st.write("")
confidence = st.radio(
"How confident are you about your annotation?\n\n1 corresponds to 'Not at all' and 5 to 'Very much'.",
["1", "2", "3", "4", "5"],
index=None,
horizontal=True
)
st.write("")
comment_not_implicit = st.text_input(label="Anything you'd like to point out?", max_chars=200)
if comment_not_implicit:
    st.write(r"$\textsf{\scriptsize Thanks for your input!}$")


st.write(second_md)