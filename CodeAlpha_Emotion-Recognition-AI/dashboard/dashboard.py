import streamlit as st
import pandas as pd
import plotly.express as px

from prediction.predictor import (
    predict_emotion,
    emotion_labels
)

from dashboard.database_utils import (
    save_prediction,
    get_user_history
)

from dashboard.analytics import (
    emotion_distribution,
    confidence_trend
)

from dashboard.stress import (
    detect_stress,
    calculate_stress_score
)

from dashboard.chatbot import (
    chatbot_response
)

from reports.pdf_report import (
    generate_report
)
from reports.pdf_report import (
    generate_report
)

print("Imported from:", generate_report.__module__)
print("Function:", generate_report)
print("Argument count:", generate_report.__code__.co_argcount)
print("Arguments:", generate_report.__code__.co_varnames)

from dashboard.wellness import (
    calculate_wellness
)

from dashboard.realtime_audio import (
    microphone_input
)

from dashboard.speaker_id import (
    identify_speaker
)

from dashboard.live_predict import (
    process_live_audio
)


# -----------------------------
# UI CONFIG
# -----------------------------

emotion_icons = {
    "happy": "😄",
    "sad": "😢",
    "angry": "😡",
    "fearful": "😨",
    "neutral": "😐",
    "surprised": "😲",
    "calm": "😊",
    "disgust": "🤢"
}

emotion_advice = {
    "happy": "Positive mood detected.",
    "sad": "Signs of sadness detected.",
    "angry": "Possible frustration detected.",
    "fearful": "Anxiety indicators found.",
    "neutral": "Balanced emotional state.",
    "surprised": "Unexpected emotional reaction.",
    "calm": "Relaxed voice detected.",
    "disgust": "Negative reaction detected."
}


def dashboard_page(username):

    # -----------------------------
    # SIDEBAR
    # -----------------------------

    st.sidebar.title("EmotionSenseAI")

    st.sidebar.write(
        f"Logged in as: {username}"
    )

    if st.sidebar.button(
        "Logout"
    ):
        st.session_state.logged_in = False
        st.rerun()

    # -----------------------------
    # HEADER
    # -----------------------------

    st.title(
        "🎙 Emotion Analytics Dashboard"
    )

    st.markdown(
        """
        Upload speech or use your microphone
        to detect emotions in real time.
        """
    )

    # -----------------------------
    # LIVE MICROPHONE SECTION
    # -----------------------------

    st.divider()

    st.subheader("🎤 Live Microphone Recording")

    audio = microphone_input()

    st.write(
        "Audio Output:",
        audio
    )

    if (
        audio is not None
        and isinstance(audio, dict)
        and "bytes" in audio
    ):

        try:

            emotion_live, confidence_live, probs_live = (
                process_live_audio(
                    audio["bytes"]
                )
            )

            speaker = identify_speaker(
                audio["bytes"]
            )

            st.subheader(
                "⚡ Real-Time Emotion Detection"
            )

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Emotion",
                emotion_live.upper()
            )

            col2.metric(
                "Confidence",
                f"{confidence_live * 100:.2f}%"
            )

            col3.metric(
                "Speaker ID",
                speaker
            )

            st.success(
                f"Detected Emotion: {emotion_live}"
            )

        except Exception as e:

            st.error(
                f"Live prediction failed: {e}"
            )

    else:

        st.info("Click Start Recording and record your voice.")

    # -----------------------------
    # FILE UPLOAD SECTION
    # -----------------------------

    st.divider()

    uploaded_file = st.file_uploader(
        "Upload Speech Audio",
        type=["wav"]
    )

    emotion = None
    confidence = None
    stress_score = None

    if uploaded_file is not None:

        with open("temp.wav", "wb") as f:
            f.write(
                uploaded_file.read()
            )

        emotion, confidence, probs = (
            predict_emotion(
                "temp.wav"
            )
        )

        save_prediction(
            username,
            emotion,
            float(confidence)
        )

        stress_level = detect_stress(
            emotion
        )

        stress_score = calculate_stress_score(
            emotion,
            confidence
        )

        # -----------------------------
        # METRICS
        # -----------------------------

        st.subheader("📊 Prediction Results")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Emotion",
            emotion.upper()
        )

        col2.metric(
            "Confidence",
            f"{confidence * 100:.2f}%"
        )

        col3.metric(
            "Stress",
            stress_level
        )

        col4.metric(
            "Stress Score",
            stress_score
        )

        st.markdown(
            f"## {emotion_icons.get(emotion,'🙂')} "
            f"{emotion.upper()}"
        )

        st.success(
            emotion_advice.get(
                emotion,
                "Emotion detected."
            )
        )

        # -----------------------------
        # PROBABILITY TABLE
        # -----------------------------

        min_len = min(
            len(emotion_labels),
            len(probs)
        )

        prob_df = pd.DataFrame({
            "Emotion":
                emotion_labels[:min_len],

            "Probability":
                probs[:min_len]
        })

        prob_df["Probability"] = (
            prob_df["Probability"] * 100
        ).round(2)

        st.subheader("Emotion Probability Distribution")

        st.dataframe(
            prob_df,
            use_container_width=True
        )

        # -----------------------------
        # BAR CHART
        # -----------------------------

        fig_bar = px.bar(
            prob_df.sort_values(
                "Probability",
                ascending=False
            ),
            x="Emotion",
            y="Probability",
            text="Probability",
            title="Emotion Confidence (%)"
        )

        fig_bar.update_traces(
            textposition="outside"
        )

        st.plotly_chart(
            fig_bar,
            use_container_width=True
        )

        # -----------------------------
        # TOP 3 EMOTIONS
        # -----------------------------

        top3 = prob_df.sort_values(
            by="Probability",
            ascending=False
        ).head(3)

        st.subheader("🏆 Top 3 Emotions")

        st.dataframe(
            top3,
            use_container_width=True
        )

        fig_pie = px.pie(
            top3,
            names="Emotion",
            values="Probability",
            title="Top 3 Emotion Distribution"
        )

        st.plotly_chart(
            fig_pie,
            use_container_width=True
        )

        # -----------------------------
        # CONFIDENCE METER
        # -----------------------------

        st.subheader("Prediction Confidence")

        st.progress(float(confidence))

        # -----------------------------
        # AI WELLNESS COACH
        # -----------------------------

        st.subheader("🤖 AI Wellness Coach")

        st.info(
            chatbot_response(
                emotion
            )
        )

    # -----------------------------
    # HISTORY
    # -----------------------------

    history = get_user_history(
        username
    )

    if not history.empty:

        st.divider()

        st.subheader(
            "📜 Prediction History"
        )

        st.dataframe(
            history,
            use_container_width=True
        )

        # -----------------------------
        # WELLNESS INDEX
        # -----------------------------

        wellness = calculate_wellness(
            history
        )

        st.subheader( "🧠 Mental Wellness Index")

        st.metric(
            "Wellness Score",
            f"{wellness}/100"
        )

        st.progress(wellness / 100)

        # -----------------------------
        # EMOTION TIMELINE
        # -----------------------------

        st.subheader( "📈 Emotion Timeline" )

        fig_timeline = px.line(
            history,
            x="timestamp",
            y="confidence",
            color="emotion",
            markers=True,
            title="Confidence Trend"
        )

        st.plotly_chart(
            fig_timeline,
            use_container_width=True
        )

        # -----------------------------
        # ANALYTICS
        # -----------------------------

        st.subheader("📊 Analytics")

        col1, col2 = st.columns(2)

        with col1:

            st.plotly_chart(
                emotion_distribution(
                    history
                ),
                use_container_width=True
            )

        with col2:

            st.plotly_chart(
                confidence_trend(
                    history
                ),
                use_container_width=True
            )

        # -----------------------------
        # PDF REPORT
        # -----------------------------

        st.subheader( "📄 Download Report")

        if (
            emotion is not None
            and confidence is not None
            and stress_score is not None
        ):

            if st.button(
                "Generate PDF Report"
            ):

                pdf_path = generate_report(
                    username,
                    emotion,
                    confidence,
                    stress_score
                )

                with open(
                    pdf_path,
                    "rb"
                ) as pdf:

                    st.download_button(
                        label="Download PDF",
                        data=pdf,
                        file_name=pdf_path,
                        mime="application/pdf"
                    )

        else:

            st.info(
                "Upload an audio file first to generate a PDF report."
            )

    else:

        st.info(
            "No prediction history available yet."
        )

