import streamlit as st
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# .envファイルからAPIキーを読み込む
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# LLMの初期化
llm = ChatOpenAI(openai_api_key=api_key, model_name="GPT-4o mini", temperature=0)

# 専門家の選択肢（自分で追加も可）
expert_options = {
    "医療の専門家": "あなたは優秀な医師です。正確かつ思いやりをもって健康に関する質問に答えてください。",
    "法律の専門家": "あなたは経験豊富な弁護士です。法律に関する質問に的確に答えてください。",
    "キャリアコンサルタント": "あなたは熟練のキャリアアドバイザーです。仕事・転職・キャリアに関するアドバイスを行ってください。"
}

# StreamlitのUI部分
st.title("🔍 LLM専門家チャットアプリ")
st.write("下の入力欄に質問を入力し、専門家を選んで送信してください。")

selected_expert = st.radio("専門家を選んでください", list(expert_options.keys()))
user_input = st.text_input("質問を入力してください")

if st.button("送信"):
    if user_input:
        # 会話履歴の定義（Systemメッセージ + ユーザー入力）
        messages = [
            SystemMessage(content=expert_options[selected_expert]),
            HumanMessage(content=user_input)
        ]
        with st.spinner("回答を生成中..."):
            response = llm.invoke(messages)
        st.success("回答:")
        st.write(response.content)
    else:
        st.warning("質問を入力してください。")

        import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# 2. APIキーの読み込み
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 3. Streamlit UIの構成
st.title("💬 専門家に聞いてみよう！")
st.write("質問を入力し、専門家の分野を選択してください。")

# ラジオボタン：専門家の種類
expert_type = st.radio("専門家を選んでください", ("栄養士", "歴史学者", "投資アドバイザー"))

# テキスト入力
user_input = st.text_input("ご質問をどうぞ")

# 4. 「質問する」ボタンが押されたら実行
if st.button("質問する") and user_input:
    # システムプロンプトを選択肢に応じて変更
    system_prompt = {
        "栄養士": "あなたはプロの栄養士として、健康と食生活について専門的なアドバイスを提供してください。",
        "歴史学者": "あなたは歴史学者として、歴史的背景について詳しく解説してください。",
        "投資アドバイザー": "あなたは信頼できる投資アドバイザーとして、初心者に向けたアドバイスをわかりやすく説明してください。"
    }[expert_type]

    # LangChainでLLM呼び出し
    llm = ChatOpenAI(openai_api_key=api_key, model_name="gpt-4o-mini", temperature=0)
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ]
    response = llm(messages)

    # 5. 回答の表示
    st.markdown("### 回答")
    st.write(response.content)