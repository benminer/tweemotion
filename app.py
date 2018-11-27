from flask import Flask, jsonify, request
from twitter import getTweets, getRateLimit
from predict import predict_sentiment

app = Flask('tweemotion')


sentiments = {
    0: 'negative',
    1: 'neutral',
    2: 'positive'
}


@app.route('/tweets', methods=['POST'])
def search_tweets():
    query = request.json['query']
    tweets = getTweets(query)
    predictions = predict_sentiment(tweets)
    predictions = [sentiments[prediction.index(max(prediction))] for prediction in predictions]
    sentiment_counts = {'negative': 0, 'neutral': 0, 'positive': 0}
    for sentiment in predictions:
        sentiment_counts[sentiment] += 1
    return jsonify({'results': sentiment_counts}), 200


@app.route('/rate', methods=['GET'])
def get_rate_limit():
    res = getRateLimit()
    return jsonify({'res': res}), 200


@app.route('/predict_tweet', methods=['POST'])
def predict_tweet():
    tweet = request.json['tweet']
    prediction = predict_sentiment([tweet])
    sentiment = sentiments[prediction[0].index(max(prediction[0]))]
    return jsonify({'sentiment': sentiment}), 200


if __name__ == '__main__':
    app.run(debug=True)