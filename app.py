import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Student Data Analysis",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Student Data Analysis Web Service")
st.write("학생 정보를 입력하고 간단한 데이터 분석과 시각화를 확인할 수 있는 웹 서비스입니다.")

st.divider()

st.subheader("1. Student Information")

name = st.text_input("Student Name", placeholder="Enter your name")
age = st.number_input("Age", min_value=1, max_value=100, value=20, step=1)
score = st.slider("Score", min_value=0, max_value=100, value=80)

if st.button("Analyze", type="primary"):
    if not name.strip():
        st.warning("Please enter your name.")
    else:
        if score >= 90:
            grade = "A"
            message = "Excellent!"
        elif score >= 80:
            grade = "B"
            message = "Good job!"
        elif score >= 70:
            grade = "C"
            message = "Keep improving!"
        elif score >= 60:
            grade = "D"
            message = "More practice is needed."
        else:
            grade = "F"
            message = "Let's study a little more."

        data = pd.DataFrame({
            "Category": ["Score"],
            "Value": [score]
        })

        st.divider()
        st.subheader("2. Analysis Result")

        col1, col2, col3 = st.columns(3)
        col1.metric("Name", name)
        col2.metric("Age", age)
        col3.metric("Score", score)

        st.success(f"Grade: {grade} — {message}")

        st.subheader("3. Score Visualization")

        fig, ax = plt.subplots(figsize=(6, 3.5))
        ax.bar(["Score"], [score])
        ax.set_ylim(0, 100)
        ax.set_ylabel("Score")
        ax.set_title("Student Score")
        ax.grid(axis="y", alpha=0.25)
        st.pyplot(fig)

        st.subheader("4. Data")
        st.dataframe(data, use_container_width=True)

st.divider()
st.caption("Created with Python, Pandas, Matplotlib and Streamlit.")
