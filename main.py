import streamlit as st

# 페이지 설정 (브라우저 탭에 표시될 내용)
st.set_page_config(page_title="내 첫 웹사이트", page_icon="🚀")

# 헤더와 텍스트
st.title("안녕하세요! 스트림릿 웹사이트입니다")
st.header("깃허브를 통해 배포 중입니다.")

# 위젯 추가 (버튼, 입력창 등)
name = st.text_input("당신의 이름은 무엇인가요?")

if st.button("인사하기"):
    st.write(f"{name}님, 반갑습니다! 사이트가 성공적으로 작동하네요.")

# 이미지나 데이터프레임도 쉽게 넣을 수 있습니다.
