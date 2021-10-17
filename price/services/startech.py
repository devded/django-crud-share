import mechanicalsoup


class StartechPriceService:
    def get_price(product_name):
        browser = mechanicalsoup.StatefulBrowser()
        browser.open(f"https://www.startech.com.bd/product/search?search={product_name}")
        raw_names = browser.page.find_all("h4", class_="p-item-name")
        raw_prices = browser.page.find_all("div", class_="p-item-price")

        clean_names = []
        clean_urls = []
        clean_prices = []

        for name in raw_names:
            clean_names.append(name.a.text.strip())
            clean_urls.append(name.a.attrs['href'])

        for price in raw_prices:
            clean_prices.append(price.span.text.strip())

        data_list = []

        for name, price, url in zip(clean_names, clean_prices, clean_urls):
            data_format = {
                "product_name": name,
                "product_price": price,
                "product_url": url,
            }
            data_list.append(data_format)

        return data_list
