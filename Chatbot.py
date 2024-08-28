from openai import OpenAI
import streamlit as st

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API 密钥", key="chatbot_api_key", type="password")
    "[申请一个 OpenAI API 密钥](https://platform.openai.com/account/api-keys)"
    "[查看我们的源代码](https://github.com/wuloi/5loi-ailab/blob/main/Chatbot.py)"
    "[![在 GitHub Codespaces 中打开](https://github.com/codespaces/badge.svg)](https://codespaces.new/wuloi/5loi-ailab?quickstart=1)"

st.title("🌿 5Loi AILab")
st.caption("🐬5Loi的大脑🧠 被大语言模型加持")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "你想吴磊 [5loi](https://5loi.com/about_loi) 怎么帮你？"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("请设置你的 OpenAI API 密钥")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
