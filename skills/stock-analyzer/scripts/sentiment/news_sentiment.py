"""
News sentiment analysis module.
Uses TextBlob for polarity and subjectivity scoring of news headlines.
"""

from textblob import TextBlob


class NewsSentimentAnalyzer:
    """Analyze sentiment of news headlines."""

    def analyze(self, news_items):
        """
        Analyze sentiment for a list of news items.

        Args:
            news_items: list of dicts with at least a 'title' key

        Returns:
            dict with individual scores and averages
        """
        if not news_items:
            return {"articles": [], "average_polarity": 0, "average_subjectivity": 0, "overall": "neutral"}

        results = []
        total_polarity = 0
        total_subjectivity = 0

        for item in news_items:
            title = item.get("title", "")
            if not title:
                continue
            blob = TextBlob(title)
            polarity = round(blob.sentiment.polarity, 4)
            subjectivity = round(blob.sentiment.subjectivity, 4)
            total_polarity += polarity
            total_subjectivity += subjectivity

            sentiment_label = "neutral"
            if polarity > 0.1:
                sentiment_label = "positive"
            elif polarity < -0.1:
                sentiment_label = "negative"

            results.append({
                "title": title,
                "publisher": item.get("publisher", ""),
                "polarity": polarity,
                "subjectivity": subjectivity,
                "sentiment": sentiment_label,
            })

        count = len(results) if results else 1
        avg_polarity = round(total_polarity / count, 4)
        avg_subjectivity = round(total_subjectivity / count, 4)

        overall = "neutral"
        if avg_polarity > 0.1:
            overall = "positive"
        elif avg_polarity < -0.1:
            overall = "negative"

        return {
            "articles": results,
            "average_polarity": avg_polarity,
            "average_subjectivity": avg_subjectivity,
            "overall": overall,
        }
