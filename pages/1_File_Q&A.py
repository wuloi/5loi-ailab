import streamlit as st
import anthropic

with st.sidebar:
    anthropic_api_key = st.text_input("Anthropic API 密钥", key="file_qa_api_key", type="password")
    "[查看我们的源代码](https://github.com/wuloi/5loi-ailab/blob/main/pages/1_File_Q%26A.py)"
    "[![在 GitHub Codespaces 中打开](https://github.com/codespaces/badge.svg)](https://codespaces.new/wuloi/5loi-ailab?quickstart=1)"

import streamlit as st
import anthropic

st.title("📝 使用 Anthropic 进行文件问答")

# 文件上传器，允许用户上传 txt 或 md 类型的文件
uploaded_file = st.file_uploader("上传一篇文章", type=("txt", "md"))

# 文本输入框，允许用户输入关于文章的问题
question = st.text_input(
    "关于文章的问题",
    placeholder="你能给我一个简短的摘要吗？",
    disabled=not uploaded_file,  # 如果没有上传文件，则禁用输入框
)

# 如果用户上传了文件并且输入了问题，但未设置 Anthropic API 密钥，则显示提示信息
if uploaded_file and question and not anthropic_api_key:
    st.info("请设置你的 Anthropic API 密钥")

# 如果用户上传了文件并且输入了问题，并且设置了 Anthropic API 密钥，则进行问答
if uploaded_file and question and anthropic_api_key:
    # 读取上传的文件内容并解码
    article = uploaded_file.read().decode()
    # 构建提示信息
    prompt = f"""{anthropic.HUMAN_PROMPT} 这是一篇文章：
\n\n<article>
    {article}
\n\n</article>
\n\n{question}{anthropic.AI_PROMPT}"""

    # 创建 Anthropic 客户端实例
    client = anthropic.Client(api_key=anthropic_api_key)
    # 发送请求并获取回答
    response = client.completions.create(
        prompt=prompt,
        stop_sequences=[anthropic.HUMAN_PROMPT],
        model="claude-v1",  # "claude-2" 用于 Claude 2 模型
        max_tokens_to_sample=100,
    )
    # 显示回答
    st.write("### 回答")
    st.write(response.completion)
