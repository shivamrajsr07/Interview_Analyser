def final_score(eye, sentiment, body, anxiety):
    sentiment_norm = (sentiment + 100) / 2

    # Anxiety is inverse (more anxiety = worse)
    anxiety_score = 100 - anxiety

    score = (
        0.3 * eye +
        0.25 * sentiment_norm +
        0.25 * body +
        0.2 * anxiety_score
    )

    return round(score, 2)