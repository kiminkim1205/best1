import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="나의 재미있는 웹사이트", page_icon="🎈")

# 2. 제목과 설명
st.title("✨ 환영합니다! 저의 첫 웹사이트예요")
st.write("이곳에서 간단한 소통을 해보세요.")

# 3. 사용자 입력 받기
name = st.text_input("당신의 이름(또는 별명)을 알려주세요!", placeholder="예: 홍길동")

# 4. 재미있는 로직 추가
if name:
    st.success(f"반가워요, {name}님! 오늘 기분은 어떠신가요?")
    
    # 선택 상자
    mood = st.select_slider(
        "오늘의 기분 점수!",
        options=["😭", "😟", "😐", "😊", "😆"]
    )
    
    if st.button("행운의 메시지 뽑기"):
        messages = [
            "오늘은 맛있는 걸 먹게 될 거예요!",
            "뜻밖의 행운이 찾아올 지도 몰라요.",
            "지금 모습 그대로도 충분히 멋져요!",
            "오늘은 스트림릿 공부하기 딱 좋은 날씨네요."
        ]
        st.info(random.choice(messages))
        st.balloons()  # 화면에 풍선이 터지는 효과!

# 5. 사이드바 꾸미기
with st.sidebar:
    st.header("정보")
    st.write("이 사이트는 Streamlit으로 만들어졌습니다.")

# 이미지나 데이터프레임도 쉽게 넣을 수 있습니다.
