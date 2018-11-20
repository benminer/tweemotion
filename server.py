from flask import Flask, jsonify, request
from twitter import getTweets, getRateLimit

app = Flask('tweemotion')


@app.route('/tweets', methods=['POST'])
def search_tweets():
    print(request.json['query'])
    query = request.json['query']
    tweets = getTweets(query)
    return jsonify({'results': tweets}), 200


@app.route('/rate', methods=['GET'])
def get_rate_limit():
    res = getRateLimit()
    return  jsonify({'res': res}), 200


if __name__ == '__main__':
    app.run(debug=True)