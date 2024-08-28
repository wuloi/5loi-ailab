import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

import streamlit as st

st.title("🦜🔗 Langchain - 博客大纲生成器")

# 在侧边栏中获取 OpenAI API 密钥
openai_api_key = st.sidebar.text_input("OpenAI API 密钥", type="password")

# 定义生成博客大纲的函数
def blog_outline(topic):
    # 实例化 LLM 模型
    llm = OpenAI(model_name="text-davinci-003", openai_api_key=openai_api_key)
    # 提示模板
    template = "作为一名经验丰富的数据科学家和技术作家，请为关于 {topic} 的博客生成一个大纲。"
    prompt = PromptTemplate(input_variables=["topic"], template=template)
    prompt_query = prompt.format(topic=topic)
    # 运行 LLM 模型
    response = llm(prompt_query)
    # 打印结果
    return st.info(response)

# 创建表单
with st.form("myform"):
    # 文本输入框，允许用户输入博客主题
    topic_text = st.text_input("输入提示：", "")
    submitted = st.form_submit_button("提交")
    # 如果没有设置 OpenAI API 密钥，则显示提示信息
    if not openai_api_key:
        st.info("请设置你的 OpenAI API 密钥")
    # 如果用户提交了表单，则调用博客大纲生成函数
    elif submitted:
        blog_outline(topic_text)