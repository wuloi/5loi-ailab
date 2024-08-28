from ai21 import AI21Client
from ai21.models.chat import ChatMessage, ResponseFormat, DocumentSchema, FunctionToolDefinition, ToolDefinition, ToolParameters
from constants import AI21_jamba_MODEL
import streamlit as st

with st.sidebar:
    ai21_api_key = st.text_input("LLM API 密钥", key="chatbot_api_key", type="password")
    "[免费申请 LLM API 密钥](https://studio.ai21.com/account/api-key)"
    "[看看源代码](https://github.com/wuloi/5loi-ailab/blob/main/Chatbot.py)"
    "[![在 GitHub Codespaces 中打开](https://github.com/codespaces/badge.svg)](https://codespaces.new/wuloi/5loi-ailab?quickstart=1)"

st.title("🌿 5Loi AILab")
st.caption("🐬5Loi的大脑🧠 被大语言模型加持")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "你想我怎样帮你？"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not ai21_api_key:
        st.info("请先设置好你的大语言模型API密钥。")
        st.stop()
        
    st.chat_message("user").write(prompt)
    
    client = AI21Client(api_key=ai21_api_key)
    
    response = client.chat.completions.create(
		model=AI21_jamba_MODEL,
		messages=[ChatMessage(
            role="user",
            content=prompt
            )],
		n=1,
		max_tokens=1024,
		temprature=0.4,
		top_p=1,
		stop=[],
		response_format=ResponseFormat(type="text"),
  )
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
