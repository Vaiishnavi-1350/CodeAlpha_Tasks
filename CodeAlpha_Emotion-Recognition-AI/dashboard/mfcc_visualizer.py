import librosa
import librosa.display
import matplotlib.pyplot as plt

def create_mfcc_plot(
    audio_path
):

    audio,sr = librosa.load(
        audio_path
    )

    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sr,
        n_mfcc=40
    )

    fig,ax = plt.subplots(
        figsize=(10,4)
    )

    librosa.display.specshow(
        mfcc,
        x_axis="time"
    )

    plt.colorbar()

    return fig