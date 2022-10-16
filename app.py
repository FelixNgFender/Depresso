from flask import Flask, render_template, jsonify, request
import googleDocsParser
import quoteGenerator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/_get_url')
def _get_url():
    url = request.args.get('url', default=None, type=str)
    print("_get_url called!")
    print(url)
    googleDocsParser.updateIdFromURL(url)
    raw_pred, dep_pred = googleDocsParser.parse()
    response = jsonify({"raw_pred": str(raw_pred), "dep_pred": str(dep_pred)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/_get_quote')
def _get_quote():
    print("_get_quote called!")
    quote = quoteGenerator.get_random_quote()
    response = jsonify(quote)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    quoteGenerator.initialize_quotes()
    app.run(debug=True)
