import os
import pickle
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from tensorflow.keras.utils import to_categorical

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import (
    Conv1D,
    MaxPooling1D,
    LSTM,
    Dense,
    Dropout,
    Flatten
)

from features.audio_features import (
    extract_features
)

dataset_path = "data/RAVDESS"

emotion_map = {
    "01":"neutral",
    "02":"calm",
    "03":"happy",
    "04":"sad",
    "05":"angry",
    "06":"fearful",
    "07":"disgust",
    "08":"surprised"
}

X=[]
y=[]

for root,dirs,files in os.walk(
    dataset_path
):

    for file in files:

        if file.endswith(".wav"):

            emotion = emotion_map[
                file.split("-")[2]
            ]

            path = os.path.join(
                root,
                file
            )

            feature = extract_features(
                path
            )

            X.append(feature)

            y.append(emotion)

X=np.array(X)

encoder = LabelEncoder()

y = encoder.fit_transform(y)

pickle.dump(
    encoder,
    open(
        "models/label_encoder.pkl",
        "wb"
    )
)

y = to_categorical(y)

X = X.reshape(
    X.shape[0],
    X.shape[1],
    1
)

X_train,X_test,y_train,y_test = (
    train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
)

model = Sequential()

model.add(
    Conv1D(
        128,
        3,
        activation='relu',
        input_shape=(
            X.shape[1],
            1
        )
    )
)

model.add(
    MaxPooling1D(2)
)

model.add(
    LSTM(
        128,
        return_sequences=True
    )
)

model.add(
    Flatten()
)

model.add(
    Dense(
        256,
        activation='relu'
    )
)

model.add(
    Dropout(0.4)
)

model.add(
    Dense(
        y.shape[1],
        activation='softmax'
    )
)

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(
    X_train,
    y_train,
    validation_data=(
        X_test,
        y_test
    ),
    epochs=50,
    batch_size=32
)

model.save(
    "models/emotion_model.h5"
)

print("Training Completed")