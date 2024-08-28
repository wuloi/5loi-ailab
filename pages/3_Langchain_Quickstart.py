import streamlit as st
from langchain.llms import OpenAI

st.title("🦜🔗 Langchain 快速开始")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API 密钥", type="password")
    # 原文链接被注释掉，因为无法解析网页内容，下面是中文翻译
    # "[申请一个 OpenAI API 密钥](https://platform.openai.com/account/api-keys)"

def generate_response(input_text):
    # 假设 OpenAI 类已经被正确导入
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form("my_form"):
    text = st.text_area("输入文本:", "学习编程的三个关键建议是什么？")
    submitted = st.form_submit_button("提交")
    if not openai_api_key:
        st.info("请设置你的 OpenAI API 密钥")
    elif submitted:
        generate_response(text)
