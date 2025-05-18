from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st  # Streamlitをインポート

st.title("Lesson21　Chapter 6 【提出課題】LLM機能を搭載したWebアプリ")

from langchain.chat_models import ChatOpenAI  # 修正済み
from langchain.schema import SystemMessage, HumanMessage

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# Webアプリの概要と操作方法を表示
st.write("### Webアプリの概要")
st.write("このアプリでは、選択した専門家の視点で入力されたプロンプトに対する回答を生成します。")
st.write("1. 専門家の種類を選択してください（ファッションスタイリストまたは料理人）。")
st.write("2. プロンプトを入力し、送信ボタンを押してください。")
st.write("3. 選択した専門家の視点での回答が表示されます。")
st.write("---")  # 水平線を追加

# 専門家の種類を選択するラジオボタンを追加
st.write("### LLMに振る舞わせる専門家を選択してください：")  # Webアプリの概要と同じ文字サイズ
expert_type = st.radio(
    "",
    ["ファッションスタイリスト", "料理人"]
)

# LLM処理を行う関数を定義
def get_llm_response(user_input, expert_type):
    """
    入力テキストと選択された専門家の種類を基にLLMからの回答を取得します。

    Args:
        user_input (str): ユーザーが入力したテキスト。
        expert_type (str): 選択された専門家の種類。

    Returns:
        str: LLMからの回答。
    """
    if expert_type == "ファッションスタイリスト":
        system_message = "あなたは優秀なファッションスタイリストです。"
    elif expert_type == "料理人":
        system_message = "あなたはプロの料理人です。"

    # LangChainを使ってLLMにプロンプトを渡す
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=user_input)
    ]

    result = llm(messages)
    return result.content

# 入力フォームを作成
user_input = st.text_area(label="プロンプトを入力してください：", height=150)

if st.button("送信"):
    if user_input:
        # 関数を利用してLLMからの回答を取得
        response = get_llm_response(user_input, expert_type)

        # 結果を画面に表示
        st.write("### 回答:")
        st.write(response)
    else:
        st.error("プロンプトを入力してください。")