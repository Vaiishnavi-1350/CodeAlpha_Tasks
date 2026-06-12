def chatbot_response(emotion):

    emotion = emotion.lower()

    if emotion == "happy":
        return """
😊 AI Wellness Coach

You sound positive and energetic.

Suggestions:
• Continue your current activities
• Set a new personal goal today
• Share your positive energy with others
"""

    elif emotion == "sad":
        return """
💙 AI Wellness Coach

You seem a little low today.

Suggestions:
• Take a short walk
• Listen to uplifting music
• Talk with a trusted friend
• Practice gratitude journaling
"""

    elif emotion == "angry":
        return """
😌 AI Wellness Coach

Signs of frustration detected.

Suggestions:
• Take a 5-minute break
• Drink water
• Try deep breathing
• Avoid making rushed decisions
"""

    elif emotion == "fearful":
        return """
🧘 AI Wellness Coach

Anxiety indicators detected.

Suggestions:
• Focus on slow breathing
• Break tasks into smaller steps
• Avoid information overload
"""

    elif emotion == "calm":
        return """
🌿 AI Wellness Coach

You sound relaxed and composed.

Suggestions:
• Great time for focused work
• Maintain your routine
• Consider learning something new
"""

    elif emotion == "neutral":
        return """
⚖️ AI Wellness Coach

Your emotional state appears balanced.

Suggestions:
• Continue your current activities
• Monitor your energy levels
"""

    return "Emotion detected successfully."