from flask import render_template, jsonify, request
import requests
from models.ebay_request_history_model import srcape_request_data
import re
from bs4 import BeautifulSoup
from threading import Thread


def ebay_scrape_data():
    if request.method == 'POST':
        location_val = request.form.getlist('location')
        condition_val = request.form.getlist('condition[]')
        buy_format_val = request.form.getlist('buy_format')
        min_val = request.form.get('min')
        max_val = request.form.get('max')
        item_sold_val = request.form.get('item_sold')
        search_box = request.form.get('searchtext')
        for location_val in location_val:
            location_val = location_val
        for buy_format_val in buy_format_val:
            buy_format_val = buy_format_val
        condition_list = []
        if len(condition_val) > 1:
            for condition_val in condition_val:
                condition_val = '%7C'+condition_val
                condition_list.append(condition_val)
            item = ''.join(str(item) for item in condition_list)
            url = f"https://www.ebay.com/sch/i.html?&_nkw={search_box}&_sacat=&_ipg=60rt=nc&LH_PrefLoc={location_val}&{buy_format_val}&rt=nc&_udlo={min_val}&_udhi={max_val}&LH_ItemCondition={item}&{item_sold_val}&rt=nc"

        else:
            for condition_val in condition_val:
                condition_val = condition_val
                url = f"https://www.ebay.com/sch/i.html?&_nkw={search_box}&_sacat=&_ipg=60rt=nc&LH_PrefLoc={location_val}&{buy_format_val}&rt=nc&_udlo={min_val}&_udhi={max_val}&LH_ItemCondition={condition_val}&{item_sold_val}&rt=nc"

        # print(search_box)
        # print(location_val, condition_val, buy_formate_val,
        #       min_val, max_val, item_sold_val)
        print(url)
        get_request = requests.get(url)
        get_request_text = get_request.text
        soup = BeautifulSoup(get_request_text, 'html.parser')
        results = soup.find_all('div', {'class': 's-item__wrapper clearfix'})
        data = []
        location = ""
        location_href = ""
        for item in results:
            title = item.find('div', {'class': 's-item__info clearfix'}
                              ).find('div', {'class': 's-item__title'}).find('span').text
            img = item.find(
                'div', {'class': 's-item__image-wrapper image-treatment'}).find('img')['src']
            condition = item.find('span', {'class': 'SECONDARY_INFO'}).text
            price = item.find('span', {'class': 's-item__price'}).text
            details_page_link = item.find(
                'a', {'class': 's-item__link'})['href']
            get_request_details = requests.get(details_page_link)
            soup_details = BeautifulSoup(
                get_request_details.text, 'html.parser')
            location_page_link = soup_details.find(
                'div', {'class': 'ux-seller-section__item--seller'})
            if location_page_link:
                location_href = location_page_link.find('a')['href']
                get_location_page = requests.get(f"{location_href}#tab1")
                soup_location = BeautifulSoup(
                    get_location_page.text, 'html.parser')
                section = soup_location.find(
                    'section', {'class': 'str-about-description__seller-info'})
                if section:
                    section_span = section.find(
                        'span', {'class': 'str-text-span BOLD'}).text
                    if section_span == "United States":
                        location = section_span

            if location == "United States":
                location = location

                print(location, title, details_page_link, location_href)
                data.append({
                    'title': title,
                    'img': img,
                    'condition': condition,
                    'price': price,
                    'location': location,
                })
            response = {
                'aaData': data
            }
            # print(response)
        return jsonify(response)

    return render_template('tables.html')


def ebay_scrape_request_history():
    if request.method == 'POST':
        location_url_val = request.form.getlist('location_url_val')
        location_text = request.form.getlist('location_text')
        exclude_location_val = request.form.get('exclude_location')
        condition_url_val = request.form.getlist('condition_url_val[]')
        condition_text = request.form.get('condition_text')
        buy_format_url = request.form.getlist('buy_format_url_val')
        buy_format_text = request.form.get('buy_format')
        min_price = request.form.get('min')
        max_price = request.form.get('max')
        sold_item_val = request.form.get('item_sold')
        search_text_val = request.form.get('searchtext')
        for location_url_val in location_url_val:
            location_url_val = location_url_val
        for condition_url_val in condition_url_val:
            condition_url_val = condition_url_val
        for buy_format_url in buy_format_url:
            buy_format_url = buy_format_url

        exclude_location_val = exclude_location_val.strip()

        srcape_request_data.put_request_history(
            request_name=search_text_val, location_url_val=location_url_val, location_text=location_text, exclude_location=exclude_location_val, condition_url_val=condition_url_val, buy_format_url_val=buy_format_url, buy_format_text=buy_format_text, min_price=min_price, max_price=max_price, sold_item=sold_item_val, condition_text=condition_text)

    return 'OK'


def get_ebay_request_history():
    data = srcape_request_data.get_request_history()
    return jsonify(data)


def request_history():
    return render_template('ebayscraphistory.html')
