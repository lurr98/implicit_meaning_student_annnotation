
import sys, random, string
import streamlit as st
from captcha.image import ImageCaptcha

# define the costant
length_captcha = 4
width = 200
height = 150

# define the function for the captcha control
def captcha_control():
    #control if the captcha is correct
    if not st.session_state.verified or st.session_state.verified == False:
        st.markdown("## Before proceeding, please complete the captcha below to verify that you are human:")
        
        # define the session state for control if the captcha is correct
        st.session_state.verified = False
        col1, col2 = st.columns(2)
        
        # define the session state for the captcha text because it doesn't change during refreshes 
        if 'captcha' not in st.session_state:
                st.session_state.captcha = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length_captcha))
        print("the captcha is: ", st.session_state.captcha)
        
        #setup the captcha widget
        image = ImageCaptcha(width=width, height=height)
        data = image.generate(st.session_state.captcha)
        col1.image(data)
        capta2_text = col2.text_input('Enter captcha text')
        
        if st.button("Verify the code") or capta2_text:
            print(capta2_text, st.session_state.captcha)
            capta2_text = capta2_text.replace(" ", "")
            # if the captcha is correct, the controllo session state is set to True
            if st.session_state.captcha.lower() == capta2_text.lower().strip():
                st.session_state.verified = True
                del st.session_state.captcha
                col1.empty()
                col2.empty()
            else:
                # if the captcha is wrong, the controllo session state is set to False and the captcha is regenerated
                st.error("🚨 The captcha is wrong, try again!")
                del st.session_state.captcha
                del st.session_state.verified
        else:
            #wait for the button click
            st.stop()


st.session_state.page = "main_page"

if not st.session_state.user_id:
    st.markdown("""
    # Welcome!
                
    This is the annotation website for the Natural Language Understanding Lab at UTN Nuremberg.

    ## Are you here for annotation?
                
    If you were redirected here for the purpose of annotation, find the 'Log In' option in the sidebar to your left.
    Then, enter the unique annotator ID that we shared with you.
    Once you have successfully logged in, new options will become available to you so you can start reading the introduction and taking the qualification test.
    """)

else:
    st.markdown("""
        # Welcome!
                    
        This is the annotation website for the Natural Language Understanding Lab at UTN Nuremberg.
        """)
    
    if st.session_state.user_id != "admin" and not st.session_state.verified:
        st.markdown("""
        ## Are you here for annotation?
                    
        **You have successfully logged in as an annotator.**
                        
        """)
        captcha_control()
    elif st.session_state.user_id == "admin":
        st.markdown("""
        ## You have successfully logged in as an admin.
        """)
    else:
        st.markdown("""
        ## You're human!\n\n Please proceed to the instruction now. Select **Implicit Meaning Task Intro** on the navigation bar.
        """)
