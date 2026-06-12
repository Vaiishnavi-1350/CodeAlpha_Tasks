def calculate_wellness(
    history
):

    if history.empty:
        return 50

    positive = (
        history["emotion"]
        .isin(
            ["happy", "calm"]
        )
        .sum()
    )

    score = (
        positive /
        len(history)
    ) * 100

    return round(
        score,
        2
    )