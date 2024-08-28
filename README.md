# 🌿 5Loi AILab


[![在 GitHub Codespaces 中打开](https://github.com/codespaces/badge.svg)](https://codespaces.new/wuloi/5loi-ailab?quickstart=1) 


使用 Streamlit 构建 LLM 应用的入门示例。

## 应用概述

这个应用展示了一个不断增长的 LLM 最小工作示例集合。

当前示例包括：

- 聊天机器人
- 文件问答
- 带互联网搜索的聊天
- LangChain 快速开始
- LangChain 提示模板
- 带用户反馈的聊天

## 演示应用

[![Streamlit 应用](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://5loi-ailab.streamlit.app/) 

### 获取 OpenAI API 密钥

你可以通过以下步骤获取自己的 OpenAI API 密钥：

1. 访问 https://platform.openai.com/account/api-keys. 
2. 点击 `+ 创建新密钥` 按钮。
3. 然后，输入一个标识名称（可选）并点击 `创建密钥` 按钮。

### 在 Streamlit 社区云中输入 OpenAI API 密钥

要在 Streamlit 应用中将 OpenAI API 密钥设置为环境变量，请执行以下操作：

1. 在右下角点击 `<管理应用`，然后点击垂直的 "..." 接着点击 `设置`。
2. 这将打开 **应用设置**，接下来点击 `密钥` 标签，并将 API 密钥按照以下格式粘贴到文本框中：

```sh
OPENAI_API_KEY='xxxxxxxxxx'
```

## 本地运行

```sh
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run Chatbot.py
```
