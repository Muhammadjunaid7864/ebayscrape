from flask import Blueprint
from controllers.ebay_scrape_controller import ebay_scrape_data, ebay_scrape_request_history, get_ebay_request_history, request_history

ebay_scrape_bp = Blueprint('ebay_scrape_bp', __name__)

ebay_scrape_bp.route('/home', methods=["GET", "POST"])(ebay_scrape_data)
ebay_scrape_bp.route('/ebay_scrape_request_history',
                     methods=['GET', 'POST'])(ebay_scrape_request_history)
ebay_scrape_bp.route('/get_ebay_request_history', methods=[
                     "GET", "POST"])(get_ebay_request_history)
ebay_scrape_bp.route('/get_request_history',
                     methods=['GET', 'POST'])(request_history)
