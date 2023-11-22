# from dotenv import load_dotenv
# load_dotenv()
# from langchain.llms import OpenAI
# llms = OpenAI()
# result = llms.predict("Hi, my name is John and I am a software engineer. 그리고 이걸 한글로도 해보자.")
# print(result)


from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()

import streamlit as st

st.title("LangChain 인공지능 시인")
st.title("Language Mo다! 임마!:blue[cool] :sunglasses:")

content = st.text_input('시의 주제를 적어주세요!', '')

if st.button("시 작성 요청하기", type="primary"):
    with st.spinner('Wait for it...'):
        result = chat_model.predict(content + "에 대해 시를 써줘")
        st.write(result)


