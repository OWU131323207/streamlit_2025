import streamlit as st
import datetime

# --- サイドバー ---
st.sidebar.title("基本情報")

today = datetime.date.today()

name = st.sidebar.text_input('名前を入力してね')
birthday = st.sidebar.date_input('誕生日を入力してね', value=datetime.date(2000, 1, 1) , 
                                 min_value=datetime.date(today.year - 100, today.month, today.day) , 
                                 max_value=datetime.date(today.year + 100, today.month, today.day)
)
anniversary = st.sidebar.date_input('記念日を入力してね', value=datetime.date.today())
color = st.sidebar.color_picker('イメージカラーを選んでね')

# --- メイン画面 ---
if name:
    st.title(name + "との思い出記録")
else:
    st.title("思い出記録")

# --- 記念日カウント ---
days_since_anniversary = (today - anniversary).days

st.subheader("記念日カウント❤️")
st.write(f" {anniversary}から{days_since_anniversary}日 経ちました。")

# --- カレンダー（簡易的な予定追加） --
st.subheader("カレンダー📅")
with st.form("event_form"):
    event_date = st.date_input("日付")
    event_text = st.text_input("内容")
    event_submitted = st.form_submit_button("追加")

if event_submitted:
    if "event" not in st.session_state:
        st.session_state.event = []
    st.session_state.event.append((event_date, event_text))

# --- 予定の表示 ---
if "event" in st.session_state and st.session_state.event:
    st.subheader("予定一覧")
    for e_date, e_text in sorted(st.session_state.event):
        st.markdown(f"{e_date}:{e_text}")

# --- 日記機能 ---
st.subheader("日記📕")
with st.form("diary_form"):
    diary_date = st.date_input("日付", value=today, key="diary_date")
    diary_text = st.text_area("内容", height=200)
    diary_submitted = st.form_submit_button("保存")

if diary_submitted:
    if "diary" not in st.session_state:
        st.session_state.diary = []
    st.session_state.diary.append((diary_date, diary_text))

# --- 日記の表示 ---
if "diary" in st.session_state and st.session_state.diary:
    for d_date, d_text in sorted(st.session_state.diary, reverse=False):
        st.subheader("日記一覧")
        st.markdown(f"{d_date}")
        st.write(d_text)
