# content of test_class.py
from text_sentiment.analysis import sentiment_analysis
class TestClass:
    def test_api(self):
        x = "this"
        response = sentiment_analysis.sample_analyze_sentiment(x)
        print(response)
        assert response['success'] == True
    def test_2(self):
        x = "this"
        assert 'h' in x