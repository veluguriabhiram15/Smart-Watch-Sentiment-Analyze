import streamlit as st
from textblob import TextBlob
import datetime

st.set_page_config(page_title="Smartwatch Sentiment Analyzer", layout="centered")

st.sidebar.title("Project Info")
st.sidebar.write("Project: Smartwatch Sentiment Analyzer")
st.sidebar.write("Product: ABC X1 Smartwatch")
st.sidebar.write("Technology: Streamlit & TextBlob")
st.sidebar.write("Domain: Natural Language Processing")

st.sidebar.markdown("---")
st.sidebar.subheader("Example Reviews")
st.sidebar.write("1. This watch is amazing!")
st.sidebar.write("2. Battery life is very poor.")
st.sidebar.write("3. The watch is Average.")

st.title("⌚ ABC X1 Smartwatch - Sentiment Analyzer")
st.write("This tool analyzes customer reviews and classifies them as Positive, Negative, or Neutral.")

st.subheader("Enter Your Review")
review = st.text_area("Type your smartwatch review below:", height=120)

word_count = len(review.split())
st.write("Word Count:", word_count)

if "history" not in st.session_state:
    st.session_state.history = []

col1, col2 = st.columns(2)

with col1:
    analyze_button = st.button("Analyze Sentiment")

with col2:
    clear_button = st.button("Clear")

if clear_button:
    st.rerun()

if analyze_button:
    if review.strip() == "":
        st.warning("Please enter a review before analyzing.")
    else:
        analysis = TextBlob(review)
        polarity = analysis.sentiment.polarity
        subjectivity = analysis.sentiment.subjectivity

        if polarity > 0.15:
            sentiment = "Positive"
            st.success("✅ Sentiment: Positive 😊")
        elif polarity < -0.15:
            sentiment = "Negative"
            st.error("❌ Sentiment: Negative 😞")
        else:
            sentiment = "Neutral"
            st.info("⚠️ Sentiment: Neutral 😐")

        st.write("### Sentiment Scores")
        st.write("Polarity Score:", polarity)
        st.write("Subjectivity Score:", subjectivity)

        st.session_state.history.append({
            "time": datetime.datetime.now().strftime("%H:%M:%S"),
            "review": review,
            "sentiment": sentiment,
            "polarity": polarity
        })

st.markdown("---")
st.subheader("📊 Analysis History")

if len(st.session_state.history) == 0:
    st.write("No reviews analyzed yet.")
else:
    for item in reversed(st.session_state.history):
        st.write("🕒 Time:", item["time"])
        st.write("📝 Review:", item["review"])
        st.write("📌 Sentiment:", item["sentiment"])
        st.write("📈 Polarity:", item["polarity"])
        st.markdown("---")

st.markdown("✅ Developed as part of Smartwatch Sentiment Analysis Mini Project")
