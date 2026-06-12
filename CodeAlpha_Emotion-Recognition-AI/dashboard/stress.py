def detect_stress(emotion):

    stress_map = {

        "happy": "Low",
        "calm": "Low",

        "neutral": "Medium",

        "sad": "High",
        "fearful": "High",
        "angry": "High",
        "disgust": "High",

        "surprised": "Medium"
    }

    return stress_map.get(
        emotion.lower(),
        "Unknown"
    )


def calculate_stress_score(
    emotion,
    confidence
):

    weights = {

        "happy": 10,
        "calm": 5,
        "neutral": 20,
        "sad": 60,
        "fearful": 80,
        "angry": 90,
        "disgust": 70,
        "surprised": 30
    }

    weight = weights.get(
        emotion.lower(),
        20
    )

    return round(
        weight * confidence,
        2
    )