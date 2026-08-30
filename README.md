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
