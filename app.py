from openai.api_resources import answer
import streamlit as st
import qna
from PIL import Image



def get_text():
    input_text = st.text_input("What's your query on Savlon Bangladesh?")
    return str (input_text)

def show_reply():
    image = Image.open('savlon.png')
    st.image(image, caption='')
    question = get_text()
    try:
        answer = qna.extract_answer(question)
        st.text_area("Bot:", value=answer, height=200, max_chars=None, key=None)
    except:
        st.text_area("Savlon Q and A:", value="...")



if __name__ == "__main__":
    show_reply()




