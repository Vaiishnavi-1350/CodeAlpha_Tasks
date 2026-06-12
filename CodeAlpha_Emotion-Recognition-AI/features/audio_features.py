import librosa
import numpy as np

def extract_features(file_path):

    audio,sr = librosa.load(
        file_path,
        duration=3,
        offset=0.5
    )

    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sr,
        n_mfcc=40
    )

    chroma = librosa.feature.chroma_stft(
        y=audio,
        sr=sr
    )

    mel = librosa.feature.melspectrogram(
        y=audio,
        sr=sr
    )

    features = np.hstack([
        np.mean(mfcc.T,axis=0),
        np.mean(chroma.T,axis=0),
        np.mean(mel.T,axis=0)
    ])

    return features