import hashlib

def identify_speaker(
    audio_bytes
):

    speaker_id = hashlib.md5(
        audio_bytes
    ).hexdigest()[:8]

    return speaker_id