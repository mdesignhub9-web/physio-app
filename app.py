import streamlit as st
import pandas as pd

# App title and description
st.set_page_config(page_title="Physiotherapy Treatment Recommender", layout="wide")

st.title("🏥 AI Physiotherapy Treatment Recommender")
st.write("Get tailored physiotherapy exercises and treatment plans for a variety of medical conditions.")

# Sidebar options
st.sidebar.title("Select Patient Details")

# Patient information
age = st.sidebar.slider("Patient Age", 1, 100, 30)
gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
condition_category = st.sidebar.selectbox(
    "Condition Category",
    [
        "Musculoskeletal",
        "Neurological",
        "Cardiac & Respiratory",
        "Women's Health",
        "Other (Fatigue, Cancer, Post-Surgery)"
    ]
)

# Subconditions based on selected category
condition_mapping = {
    "Musculoskeletal": ["Back Pain", "Arthritis", "Sports Injuries", "Joint Problems"],
    "Neurological": ["Stroke", "Parkinson's", "Multiple Sclerosis", "Cerebral Palsy"],
    "Cardiac & Respiratory": ["Post-Heart Attack", "High Blood Pressure", "Asthma", "COPD"],
    "Women's Health": ["Incontinence", "Pelvic Pain"],
    "Other (Fatigue, Cancer, Post-Surgery)": ["Chronic Fatigue Syndrome", "Lymphedema", "Post-Surgery Rehab"]
}

selected_condition = st.sidebar.selectbox("Specific Condition", condition_mapping[condition_category])

st.markdown("### 📝 Patient Summary")
st.write(f"**Age**: {age}  \n**Gender**: {gender}  \n**Condition**: {selected_condition}")

# Dummy recommendations
def get_recommendations(condition):
    recommendations = {
        "Back Pain": [
            "Pelvic tilts",
            "Cat-Cow stretch",
            "Bridging exercises",
            "Low-impact aerobic conditioning"
        ],
        "Stroke": [
            "Balance training",
            "Functional electrical stimulation",
            "Gait training",
            "Range of motion exercises"
        ],
        "Asthma": [
            "Pursed-lip breathing",
            "Diaphragmatic breathing",
            "Aerobic training",
            "Airway clearance techniques"
        ],
        "Incontinence": [
            "Kegel exercises",
            "Pelvic floor muscle training",
            "Bladder training"
        ],
        "Post-Surgery Rehab": [
            "Gradual range of motion",
            "Muscle strengthening",
            "Pain management strategies"
        ]
    }
    return recommendations.get(condition, ["Customized plan will be created by physiotherapist."])

# Show recommendations
st.markdown("### 🧘 Recommended Physiotherapy Plan")

recommendations = get_recommendations(selected_condition)
for i, rec in enumerate(recommendations, start=1):
    st.write(f"**{i}.** {rec}")

st.info("This is a preliminary recommendation. Always consult with a licensed physiotherapist.")

# Footer
st.markdown("---")
st.markdown("Created with ❤️ for patient wellness | Powered by Streamlit on Hugging Face")






