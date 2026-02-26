import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

# Page config
st.set_page_config(
    page_title="Heat Hurt - Hair Damage Predictor",
    page_icon="🔥",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .main { background-color: #1a1a2e; }
    .stApp { background-color: #1a1a2e; color: white; }
    h1, h2, h3 { color: #e94560; }
    .stButton>button {
        background-color: #e94560;
        color: white;
        border-radius: 10px;
        width: 100%;
        padding: 10px;
        font-size: 18px;
    }
    .result-box {
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Training data (from original project)
data = {
    'age': [24,31,19,27,35,22,29,41,18,33,26,38,21,30,45,23,28,36,20,32,25,40,17,34,29],
    'hair_type': [3,1,2,4,1,3,2,4,1,3,2,1,4,3,1,2,4,3,1,2,4,1,3,2,4],
    'tool_type': [3,1,2,3,1,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1],
    'temperature_range': [230,150,185.5,225,175,220.75,145,230,180.5,150,225.5,155,210,190.25,152,175.5,228,222.75,148,185,226.5,150,229,178.25,152.5],
    'duration_min': [45,15,30,60,20,50,10,55,25,10,50,15,40,35,10,25,60,45,12,30,55,10,50,20,15],
    'usage_freq': [3,1,2,3,2,3,1,3,2,1,3,1,3,2,1,2,3,3,1,2,3,1,3,2,1],
    'total_usage_months': [18,6,12,24,9,20,3,30,7,2,22,4,16,11,5,8,28,19,3,10,25,2,21,6,4],
    'damage_score': [5,1,3,5,2,4,0,5,1,2,5,0,4,3,1,2,5,5,1,3,5,0,5,2,3]
}

df = pd.DataFrame(data)
X = df.drop(columns=['damage_score'])
y = df['damage_score']

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

def risk_warning(score):
    if score == 0:
        return "✅ No risk, your hair is healthy!", "#27ae60"
    elif score == 1:
        return "🟡 Very mild risk, keep an eye on your hair!", "#f1c40f"
    elif score == 2:
        return "🟠 Mild risk, consider reducing heat usage!", "#e67e22"
    elif score == 3:
        return "🔴 Moderate risk, reduce heat styling frequency!", "#e74c3c"
    elif score == 4:
        return "❗ High risk, significantly reduce heat usage!", "#c0392b"
    elif score == 5:
        return "🚨 Severe risk, stop heat styling immediately!", "#8e0000"

# Header
st.title("🔥 Heat Hurt")
st.subheader("AI-Powered Hair Damage Predictor")
st.markdown("---")
st.write("Enter your hair details below to predict your hair damage risk score.")

# Input form
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Your Age", min_value=10, max_value=100, value=25)
    hair_type = st.selectbox("Hair Type", ["Straight", "Wavy", "Curly", "Coily"])
    tool_type = st.selectbox("Heat Tool Used", ["Hair Dryer", "Curler", "Straightener"])

with col2:
    temperature = st.slider("Temperature (°C)", min_value=100, max_value=250, value=180)
    duration = st.slider("Duration per Session (minutes)", min_value=5, max_value=90, value=30)
    usage_freq = st.selectbox("How Often Do You Use Heat?", ["Monthly", "Weekly", "Daily"])

months = st.slider("How Many Months Have You Been Using Heat Tools?", min_value=1, max_value=60, value=12)

# Encode inputs
hair_map = {"Straight": 1, "Wavy": 2, "Curly": 3, "Coily": 4}
tool_map = {"Hair Dryer": 1, "Curler": 2, "Straightener": 3}
freq_map = {"Monthly": 1, "Weekly": 2, "Daily": 3}

if st.button("Predict My Hair Damage Risk 🔍"):
    input_data = pd.DataFrame([{
        'age': age,
        'hair_type': hair_map[hair_type],
        'tool_type': tool_map[tool_type],
        'temperature_range': temperature,
        'duration_min': duration,
        'usage_freq': freq_map[usage_freq],
        'total_usage_months': months
    }])

    prediction = model.predict(input_data)[0]
    message, color = risk_warning(prediction)

    st.markdown(f"""
    <div class="result-box" style="background-color: {color}; color: white;">
        Damage Score: {prediction}/5<br>{message}
    </div>
    """, unsafe_allow_html=True)

    # Tips
    st.markdown("### 💡 Hair Care Tips")
    if prediction >= 3:
        st.error("⚠️ Your hair is at significant risk! Consider:")
        st.write("- Use heat protectant spray before styling")
        st.write("- Reduce heat tool temperature below 180°C")
        st.write("- Take breaks from heat styling for at least 2-3 days per week")
        st.write("- Deep condition your hair weekly")
    elif prediction >= 1:
        st.warning("⚠️ Moderate risk detected. Tips to keep hair healthy:")
        st.write("- Always use heat protectant")
        st.write("- Limit sessions to under 20 minutes")
        st.write("- Try air drying occasionally")
    else:
        st.success("Your hair routine looks great! Keep it up!")
        st.write("- Continue using low heat settings")
        st.write("- Regular conditioning will maintain healthy hair")

st.markdown("---")
st.caption("Heat Hurt | AI Hair Damage Predictor | Built with Python, scikit-learn & Streamlit")
