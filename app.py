from flask import Flask, g, Response
from routes.ebay_scrape_route import ebay_scrape_bp


app = Flask(__name__)
# app.secret_key = "super secret key"

app.register_blueprint(ebay_scrape_bp)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
