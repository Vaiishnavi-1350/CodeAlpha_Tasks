import webrtcvad

vad = webrtcvad.Vad()

vad.set_mode(2)

def speech_detected(
    frame,
    sample_rate=16000
):

    return vad.is_speech(
        frame,
        sample_rate
    )