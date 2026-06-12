from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)
print("Loaded pdf_report from:", __file__)

def generate_report(
    username,
    emotion,
    confidence,
    stress_score
):

    filename = f"{username}_report.pdf"

    doc = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "EmotionSenseAI Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            f"User: {username}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Detected Emotion: {emotion}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Confidence: {confidence * 100:.2f}%",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Stress Score: {stress_score}",
            styles["Normal"]
        )
    )

    doc.build(elements)

    return filename

