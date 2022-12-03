from flask import Flask, jsonify
from views import AdsView
from errors import ApiException

app = Flask('app')


@app.errorhandler(ApiException)
def error_handler(error: ApiException):
    response = jsonify({
            'status': 'error',
            'message': error.message
        })
    response.status_code = error.status_code
    return response


app.add_url_rule('/api_v1/<int:ads_id>', view_func=AdsView.as_view('ads_view'),
                 methods=['GET', 'PATCH', 'DELETE'])

app.add_url_rule('/api_v1/create', view_func=AdsView.as_view('ads_create'), methods=['POST'])


if __name__ == '__main__':
    app.run()
    