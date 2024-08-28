import streamlit as st

from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun

with st.sidebar:
    openai_api_key = st.text_input(
        "OpenAI API 密钥", key="langchain_search_api_key_openai", type="password"
    )
    "[申请一个 OpenAI API 密钥](https://platform.openai.com/account/api-keys)"
    "[查看我们的源代码](https://github.com/wuloi/llm-labs/blob/main/pages/2_Chat_with_search.py)"
    "[![在 GitHub Codespaces 中打开](https://github.com/codespaces/badge.svg)](https://codespaces.new/wuloi/llm-labs?quickstart=1)"

import streamlit as st

st.title("🔎 LangChain - 带搜索的聊天")

"""
在这个示例中，我们使用 `StreamlitCallbackHandler` 在交互式的 Streamlit 应用中显示代理的思考和行动。
尝试更多 LangChain 🤝 Streamlit 代理示例，请访问 [github.com/langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent)。
"""

# 检查会话状态中是否已经有消息列表，如果没有则初始化
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "嗨，我是一个可以搜索网络的聊天机器人。我能帮你什么？"}
    ]

# 显示会话状态中的消息
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# 用户输入问题
if prompt := st.chat_input(placeholder="2024年最受欢迎的普通人是谁？"):
    # 将用户输入添加到会话状态的消息列表中
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # 如果没有设置 OpenAI API 密钥，则显示提示信息并停止执行
    if not openai_api_key:
        st.info("请设置你的 OpenAI API 密钥")
        st.stop()

    # 初始化聊天机器人和搜索引擎代理
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, streaming=True)
    search = DuckDuckGoSearchRun(name="Search")
    search_agent = initialize_agent(
        [search], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True
    )
    # 使用 Streamlit 回调处理程序显示代理的回答
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)