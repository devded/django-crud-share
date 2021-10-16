import mechanicalsoup

class StartechPriceService:
    def get_price(product_name):
        browser = mechanicalsoup.StatefulBrowser()
        browser.open(f"https://www.startech.com.bd/product/search?search={product_name}")
        raw_names = browser.page.find_all("h4", class_="p-item-name")

        raw_prices = browser.page.find_all("div", class_="p-item-price")

        # for name in raw_names:
        #   print(name.a.text.strip())
        #   print(name.a.attrs['href'])

        # for price in raw_prices:
        #   print(price.span.text.strip())

        clean_names = []
        clean_urls = []
        clean_prices = []

        for name in raw_names:
            # print(name.a.text.strip())
            # print(name.a.attrs['href'])
            clean_names.append(name.a.text.strip())
            clean_urls.append(name.a.attrs['href'])

        for price in raw_prices:
            # print(price.text.strip())
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