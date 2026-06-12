import pickle
import numpy as np

from tensorflow.keras.models import load_model

from features.audio_features import extract_features

# Load model
model = load_model(
    "models/emotion_model.h5"
)

# Load label encoder
with open(
    "models/label_encoder.pkl",
    "rb"
) as f:
    encoder = pickle.load(f)

emotion_labels = list(
    encoder.classes_
)


def predict_emotion(audio_file):

    feature = extract_features(
        audio_file
    )

    feature = feature.reshape(
        1,
        feature.shape[0],
        1
    )

    prediction = model.predict(
        feature,
        verbose=0
    )

    emotion_index = np.argmax(
        prediction
    )

    emotion = encoder.inverse_transform(
        [emotion_index]
    )[0]

    confidence = float(
        np.max(prediction)
    )

    probs = prediction[0]

    return (
        emotion,
        confidence,
        probs
    )