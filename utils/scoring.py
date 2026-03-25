def final_score(eye, sentiment, body):
    sentiment_norm = (sentiment + 100) / 2

    score = (
        0.4 * eye +
        0.3 * sentiment_norm +
        0.3 * body
    )

    return round(score, 2)