from flask import Flask, Response, request
from flask_cors import CORS


import Scrapper as scrap


app = Flask(__name__)
CORS(app)
    

@app.route('/postLink', methods=['POST'])
def sendData():
    if request.is_json:
        data = request.json
        cyberOrData = data.get('choice')
        if cyberOrData == "cyber":
            url = "https://www.infosecurity-magazine.com/risk-management/"
        else:
            url = "https://www.infosecurity-magazine.com/risk-management/"
        post = scrap.to_site(url)
        return Response(post), 200
    else:
        return Response("cheeeeeef"), 400

    

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

