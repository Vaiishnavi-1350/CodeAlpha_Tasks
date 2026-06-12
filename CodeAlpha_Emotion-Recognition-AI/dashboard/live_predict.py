import tempfile

from prediction.predictor import (
    predict_emotion
)

def process_live_audio(
    audio_bytes
):

    with tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    ) as f:

        f.write(
            audio_bytes
        )

        file_path = f.name

    emotion, confidence, probs = (
        predict_emotion(
            file_path
        )
    )

    return (
        emotion,
        confidence,
        probs
    )