# module5-AI-Tools---Mini-Project
# Emotion Classifier

## Project Overview

The Emotion Classifier is a machine learning application that predicts
the emotion expressed in a given piece of text.

The application classifies text into six emotion categories:

- Sadness
- Joy
- Love
- Anger
- Fear
- Surprise

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF
- Joblib
- Streamlit

## Dataset

The project uses a labeled text emotion dataset containing six emotion
categories.

## Machine Learning Approach

The text data was converted into numerical features using TF-IDF
(Term Frequency-Inverse Document Frequency).

The transformed features were then used to train a machine learning
classification model.

## Model Evaluation

The model achieved approximately 86.8% accuracy on the test dataset.

The model was further evaluated using precision, recall, F1-score,
and a confusion matrix.

## Model Deployment

The trained ML model and fitted TF-IDF vectorizer were saved using
Joblib and reused in the Streamlit application. This allows the
application to make predictions on new text without retraining the model.

## Application

A Streamlit-based interface was developed where the user can enter
a sentence and receive the predicted emotion.

## AI Tools Used

ChatGPT was used as a learning and development assistant for:

- Understanding Python and machine learning concepts
- Debugging errors
- Understanding TF-IDF and model evaluation
- Developing the Streamlit application
- Organizing project documentation

All AI-assisted suggestions were reviewed, tested, and adapted during
development.

## Limitations

The model may produce incorrect predictions for ambiguous, unfamiliar,
or context-dependent sentences because it relies on patterns learned
from the training dataset.

## Future Improvements

- Use a larger and more diverse dataset
- Compare multiple machine learning algorithms
- Improve text preprocessing
- Experiment with advanced NLP models
- Add confidence scores to predictions

## How to Run the Emotion Classifier

Follow these steps to run the application locally:

### 1. Clone or download the repository

Download the project from GitHub and open the project folder in **VS Code**.

### 2. Install the required libraries

Open the VS Code terminal and run:

```bash
pip install -r requirements.txt
```

### 3. Make sure the required files are present

The project folder should contain:

```text
Emotion-Classifier/
│
├── app.py
├── emotion_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
└── README.md
```

### 4. Run the Streamlit application

In the VS Code terminal, run:

```bash
streamlit run app.py
```

### 5. Open the application

After running the command, Streamlit will provide a local address such as:

```text
http://localhost:8501
```

Open this address in your web browser.

### 6. Use the application

1. Enter a sentence or text in the input box.
2. Click **Predict Emotion**.
3. The application will display the predicted emotion.

### 7. Stop the application

To stop the Streamlit server, return to the terminal and press:

```text
Ctrl + C
```

> **Note:** The `emotion_model.pkl` and `tfidf_vectorizer.pkl` files are required for the application to work. They contain the trained model and fitted TF-IDF vectorizer used to make predictions.
