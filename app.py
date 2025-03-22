from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.title("LLM機能を搭載したWebアプリ")

st.write("##### 動作モード1: 健康の専門家")
st.write("入力フォームに健康に関する質問を入力し、「実行」ボタンを押すことでアドバイスがもらえます。")
st.write("##### 動作モード2: 歴史の専門家")
st.write("入力フォームに歴史に関する質問を入力し、「実行」ボタンを押すことで情報がもらえます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["健康に関する質問", "歴史に関する質問"]
)

st.divider()

if selected_item == "健康に関する質問":
    input_message = st.text_input(label="歴史に関する質問をを入力してください。")
    text_count = len(input_message)

else:
    input_message = st.text_input(label="歴史に関する質問をを入力してください。")
    text_count = len(input_message)

if st.button("実行"):
    st.divider()

    if selected_item == "健康に関する質問":
        if input_message:
            st.write(f"文字数: **{text_count}**")

        else:
            st.error("カウント対象となるテキストを入力してから「実行」ボタンを押してください。")
            
    elif selected_item == "歴史に関する質問":
        if input_message:
            st.write(f"文字数: **{text_count}**")

    else:
        st.error("カウント対象となるテキストを入力してから「実行」ボタンを押してください。")