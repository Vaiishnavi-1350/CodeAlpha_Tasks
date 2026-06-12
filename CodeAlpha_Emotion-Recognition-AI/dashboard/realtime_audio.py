from streamlit_mic_recorder import mic_recorder

def microphone_input():

    audio = mic_recorder(
        start_prompt="🎤 Start Recording",
        stop_prompt="⏹ Stop Recording",
        just_once=True
    )

    return audio