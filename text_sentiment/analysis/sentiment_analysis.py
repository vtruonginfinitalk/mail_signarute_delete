"""
Analyzing Sentiment in a String

"""
import pprint
import os

from google.cloud import language_v1
from google.cloud.language_v1 import enums

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = \
    os.path.abspath(__file__ + "/../../../Development-project.json")


def sample_analyze_sentiment(text):
    """
    Analyzing Sentiment By Google API

    Args:
      text The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    document = {"content": text, "type": type_}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_sentiment(document, encoding_type=encoding_type)

    # Get sentiment for all sentences in the document
    sentences = []

    # Get sentiment for all sentences in the document
    for sentence in response.sentences:
        print(u"Sentence text: {}".format(sentence.text.content))
        print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
        print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))
        sentences.append({
            "content": sentence.text.content,
            "textSentimentScore": sentence.sentiment.score,
            "textSentimentMagnitude": sentence.sentiment.magnitude
        })

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(u"Language of the text: {}".format(response.language))

    result = {
        "success": True,
        "sentimentScore": response.document_sentiment.score,
        "sentimentMagnitude": response.document_sentiment.magnitude,
        "sentences": sentences,
    }
    return result


def test_sentiment():
    assert sample_analyze_sentiment('truong')["success"] == True

if __name__ == '__main__':
    pprint.pprint(sample_analyze_sentiment('fafa'))
