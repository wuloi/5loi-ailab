# 🌿 5Loi AILab

欢迎访问我的网站 [5loi.com](https://5loi.com/about_loi)，了解更多信息，并与我交流您的想法！

[![在 GitHub Codespaces 中打开](https://github.com/codespaces/badge.svg)](https://codespaces.new/wuloi/5loi-ailab?quickstart=1) 


使用 Streamlit 构建 LLM 应用的入门示例。

## 应用概述

这个应用展示了一个不断增长的 LLM 最小工作示例集合。

当前示例包括：

- [聊天机器人]((https://github.com/wuloi/5loi-ailab/blob/main/Chatbot.py))
- [文件问答](https://github.com/wuloi/5loi-ailab/blob/main/pages/1_File_Q%26A.py)
- [带互联网搜索的聊天](https://github.com/wuloi/5loi-ailab/blob/main/pages/2_Chat_with_search.py)
- [LangChain 快速开始](https://github.com/wuloi/5loi-ailab/blob/main/pages/3_Langchain_Quickstart.py)
- [LangChain 提示模板](https://github.com/wuloi/5loi-ailab/blob/main/pages/4_Langchain_PromptTemplate.py)

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

## 加入社区 🌿

欢迎访问我的网站 [5loi.com](https://5loi.com/about_loi)，了解更多信息，并与我交流您的想法！

产品社区资源：

- 欢迎加入 🌿觅识 社区 [AI PM「人工智能产品管理」](https://roadmaps.feishu.cn/wiki/RykrwFxPiiU4T7kZ63bc7Lqdnch)

技术研究资源：

- [Generative-AI-Solutions](https://github.com/wuloi/Generative-AI-Solutions) 
- [Building-LLM-powered-Solutions](https://github.com/wuloi/Building-LLM-powered-Solutions) 
- [Generative-AI-on-BigOne](https://github.com/wuloi/Generative-AI-on-BigOne)