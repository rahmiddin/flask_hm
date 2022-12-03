from flask import Flask, jsonify
from view import AdsView

app = Flask('app')

app.add_url_rule('/api_v1', view_func=AdsView.as_view('ads_view'), methods=['GET', 'POST', 'PATCH', 'DELETE'])

if __name__ == '__main__':
    app.run()
    