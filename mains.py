import os
from PIL import Image
import streamlit as  st
from streamlit_option_menu import option_menu

from gemini import (load_gemini_pro_model,gemini_pro_vision_response,embeddings_model_response,gemini_pro_response)

#from gemini import load_gemini_pro_model

working_directory = os.path.dirname(os.path.abspath(__file__))

## setting up the pages

st.set_page_config(
    page_title="Gemini_Ai",
    page_icon="🧠",
    layout = "centered"
)
with st.sidebar:

    selected = option_menu(menu_title="Gemini Ai",
                           options=["ChatBot",
                            "image Captioning",
                            "Embed text",
                            "Ask me Anything"],
                           menu_icon="robot",icons=['chat-dots-fill','image-fill',
                                                    'textarea-t','patch-question-fill'],
                         default_index=0)

## function to transalate role b/w gemini -pro and stramlit terminlogy

def translate_role_for_streamlit(user_role):
    if user_role=='model':
        return "assistant"
    else:
        return user_role


if selected == "ChatBot":
    model = load_gemini_pro_model()

    ## intialize chat session in streamlit if not already present

    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    # streamlit page title
    st.title("🤖 Chat_Bot")

    # display the chat history

    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    # input field for user message

    user_prompt = st.chat_input("Ask Gemini.Pro")

    if user_prompt:
        st.chat_message("user").markdown(user_prompt)

        gemini_response = st.session_state.chat_session.send_message(user_prompt)

        # display gemini-pro response

        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)


# Image captioning page

if selected == "image Captioning":

    st.title("📷 Snap Narrate")

    uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

    if st.button("Generate Caption"):
        image = Image.open(uploaded_image)

        col1, col2 = st.columns(2)

        with col1:
            resized_img = image.resize((800, 500))
            st.image(resized_img)

        default_prompt = "write a short caption for this image"  # change this prompt as per your requirement

        # get the caption of the image from the gemini-pro-vision LLM
        caption = gemini_pro_vision_response(default_prompt, image)

        with col2:
            st.info(caption)

# text embedding model
if selected == "Embed text":

    st.title("🔡 Embed Text")

    # text box to enter prompt
    user_prompt = st.text_area(label='', placeholder="Enter the text to get embeddings")

    if st.button("Get Response"):
        response = embeddings_model_response(user_prompt)
        st.markdown(response)


# text embedding model
if selected == "Ask me Anything":

    st.title("❓ Ask me a question")

    # text box to enter prompt
    user_prompt = st.text_area(label='', placeholder="Ask me Anything...")

    if st.button("Get Response"):
        response = gemini_pro_response(user_prompt)
        st.markdown(response)



