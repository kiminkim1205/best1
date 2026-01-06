import streamlit as st
import random
import time

# 페이지 설정
st.set_page_config(page_title="가위바위보 챔피언!", page_icon="✊")

st.title("✊✌️🖐️ 가위바위보 챔피언십")
st.write("컴퓨터를 이기고 최다 연승 기록에 도전하세요!")

# 세션 상태 초기화 (점수 및 기록 저장)
if 'streak' not in st.session_state:
    st.session_state.streak = 0
if 'max_streak' not in st.session_state:
    st.session_state.max_streak = 0

# 게임 함수
def play_game(user_choice):
    options = ["가위", "바위", "보"]
    computer_choice = random.choice(options)
    
    st.write(f"### 당신: {user_choice} vs 컴퓨터: {computer_choice}")
    
    if user_choice == computer_choice:
        st.info("🤔 비겼습니다!")
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        st.session_state.streak += 1
        if st.session_state.streak > st.session_state.max_streak:
            st.session_state.max_streak = st.session_state.streak
        st.success(f"🔥 이겼습니다! 현재 {st.session_state.streak}연승 중!")
        st.balloons()
    else:
        st.error(f"💀 패배했습니다... 최종 기록: {st.session_state.streak}연승")
        st.session_state.streak = 0

# 사용자 인터페이스 (버튼)
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✌️ 가위", use_container_width=True):
        play_game("가위")
with col2:
    if st.button("✊ 바위", use_container_width=True):
        play_game("바위")
with col3:
    if st.button("🖐️ 보", use_container_width=True):
        play_game("보")

# 점수판 레이아웃
st.divider()
c1, c2 = st.columns(2)
c1.metric("현재 연승", f"{st.session_state.streak} 🔥")
c2.metric("최고 기록", f"{st.session_state.max_streak} 🏆")

if st.button("기록 초기화"):
    st.session_state.streak = 0
    st.session_state.max_streak = 0
    st.rerun()
