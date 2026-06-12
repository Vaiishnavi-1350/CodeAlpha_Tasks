import plotly.express as px

def emotion_distribution(df):

    fig = px.pie(
        df,
        names="emotion",
        title="Emotion Distribution"
    )

    return fig

def confidence_trend(df):

    fig = px.line(
        df,
        y="confidence",
        title="Confidence Trend"
    )

    return fig