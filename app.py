import streamlit as st
import joblib


# -----------------------------
# Load trained model
# -----------------------------

tfidf = joblib.load("tfidf_vectorizer.pkl")
model = joblib.load("emotion_model.pkl")


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="Emotion Classifier",
    page_icon="🎭"
)


# -----------------------------
# Application title
# -----------------------------

st.title("🎭 Emotion Classifier")

st.write(
    "Enter a sentence or text below and the AI model "
    "will predict the emotion expressed in the text."
)


# -----------------------------
# User input
# -----------------------------

user_text = st.text_area(
    "Enter your text:",
    placeholder="Example: I am extremely happy today!"
)


# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Emotion"):

    if user_text.strip() == "":
        st.warning("Please enter some text first.")

    else:

        # Convert user's text into TF-IDF features
        text_vector = tfidf.transform([user_text])

        # Predict emotion label
        prediction = model.predict(text_vector)

        # Convert NumPy integer to normal Python integer
        predicted_label = int(prediction[0])

        # Convert label number to emotion name
        emotion_labels = [
            "sadness",
            "joy",
            "love",
            "anger",
            "fear",
            "surprise"
        ]

        predicted_emotion = emotion_labels[predicted_label]

        # Emotion emojis
        emotion_emoji = {
            "sadness": "😢",
            "joy": "😊",
            "love": "❤️",
            "anger": "😠",
            "fear": "😨",
            "surprise": "😲"
        }

        emoji = emotion_emoji.get(
            predicted_emotion,
            "🎭"
        )

        # Display result
        st.success(
            f"{emoji} Predicted Emotion: "
            f"{predicted_emotion.upper()}"
        )