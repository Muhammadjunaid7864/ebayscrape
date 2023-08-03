from utilities.helper import get_db_connection


class srcape_request_data:

    @classmethod
    def put_request_history(cls, request_name, location_url_val, location_text, exclude_location, condition_url_val, buy_format_url_val, buy_format_text, min_price, max_price, sold_item, condition_text):
        connection, cursor = get_db_connection()
        cursor.execute("""INSERT INTO save_ebay_request_history(request_name,location_url_val,location_text_name,exclude_location,condition_url_val,buy_format_url_val,buy_format_text_name,min_price,max_price,sold_item,condition_text_name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                       (request_name, location_url_val, location_text, exclude_location, condition_url_val, buy_format_url_val, buy_format_text, min_price, max_price, sold_item, condition_text))

        connection.commit()

    @classmethod
    def get_request_history(cls):
        connection, cursor = get_db_connection()
        cursor.execute("""SELECT request_name, location_text_name,exclude_location,buy_format_text_name,min_price,max_price,sold_item,condition_text_name from save_ebay_request_history""")
        row = cursor.fetchall()
        return row
