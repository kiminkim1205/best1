import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="업다운 숫자 맞추기", page_icon="🎮")

# 제목과 설명
st.title("🎮 숫자 맞추기 게임")
st.write("1부터 100 사이의 숫자를 맞춰보세요!")

# 게임 초기화 함수
def init_game():
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# 세션 상태 초기화 (처음 접속 시)
if 'target_number' not in st.session_state:
    init_game()

# 게임 UI
with st.container():
    guess = st.number_input("숫자를 입력하세요 (1~100)", min_value=1, max_value=100, key="guess_input")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("정답 확인!") and not st.session_state.game_over:
            st.session_state.attempts += 1
            if guess < st.session_state.target_number:
                st.warning("⬆️ UP! 더 큰 숫자예요.")
            elif guess > st.session_state.target_number:
                st.warning("⬇️ DOWN! 더 작은 숫자예요.")
            else:
                st.success(f"🎉 정답입니다! {st.session_state.attempts}번 만에 맞추셨네요!")
                st.balloons()
                st.session_state.game_over = True
                
    with col2:
        if st.button("다시 시작하기"):
            init_game()
            st.rerun()

# 점수판
st.divider()
st.sidebar.header("📊 현재 기록")
st.sidebar.write(f"도전 횟수: {st.session_state.attempts}")
if st.session_state.game_over:
    st.sidebar.info("새 게임을 시작하려면 '다시 시작하기'를 누르세요!")
