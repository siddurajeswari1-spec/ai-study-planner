import streamlit as st
import openai
from datetime import datetime

# 🔑 API Key
openai.api_key = "YOUR_API_KEY_HERE"

# 🌐 Page Config
st.set_page_config(page_title="AI Study Planner", page_icon="📚", layout="wide")

# 🎨 Custom CSS for UI
st.markdown("""
    <style>
        .main {
            background-color: #0e1117;
        }
        .title {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            color: #4CAF50;
        }
        .card {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.5);
        }
    </style>
""", unsafe_allow_html=True)

# 🧠 Title
st.markdown('<p class="title">📚 AI Study Planner</p>', unsafe_allow_html=True)

# 📌 Sidebar
st.sidebar.header("⚙️ Settings")

subject = st.sidebar.text_input("📖 Subject")
topics = st.sidebar.text_area("📝 Topics (comma separated)")
days = st.sidebar.slider("📅 Study Days", 1, 30, 7)
hours = st.sidebar.slider("⏰ Hours per Day", 1, 10, 3)

generate = st.sidebar.button("🚀 Generate Plan")

# 📊 Main Layout
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📌 Study Info")
    st.write(f"**Subject:** {subject}")
    st.write(f"**Days:** {days}")
    st.write(f"**Hours/Day:** {hours}")
    st.progress(days / 30)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧾 Generated Plan")

    if generate:
        if subject and topics:
            with st.spinner("🤖 AI is generating your plan..."):

                prompt = f"""
                Create a detailed {days}-day study plan.

                Subject: {subject}
                Topics: {topics}
                Study time per day: {hours} hours

                Format clearly with Day-wise breakdown.
                """

                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-4o-mini",
                        messages=[{"role": "user", "content": prompt}]
                    )

                    plan = response['choices'][0]['message']['content']

                    st.success("✅ Plan Ready!")
                    st.markdown(plan)

                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("⚠️ Fill all fields")
    else:
        st.info("Click 'Generate Plan' from sidebar")

    st.markdown('</div>', unsafe_allow_html=True)