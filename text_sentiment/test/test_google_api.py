# content of test_class.py
import text_sentiment.analysis.sentiment_analysis as sentiment_analysis

class TestClass:
    def test_api(self):
        x = "this"
        response = sentiment_analysis.google_analyze_sentiment(x)
        assert response['success'] == True
