import schedule, time, requests

def hello_world():
    print("Hello World", time.ctime())

def alert_lesson():
    print("Здравствуйте, сегодня у вас урок в 18:00")

def get_btc_price():
    url = 'https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
    response = requests.get(url=url).json()
    price = round(float(response['price']), 3)
    print(f"Цена биткоина {price} USD")

def parsing_sulpak():
    from bs4 import BeautifulSoup
    url = 'https://www.sulpak.kg/f/smartfoniy/osh/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)
    all_phones = soup.find_all('div', class_='product__item-name')
    all_prices = soup.find_all('div', class_='product__item-price')
    all_pictures = soup.find_all('img', class_='image-size-cls')
    # print(all_pictures)
    for image in all_pictures:
        result = image['src']
        print(result)
    for name, price in zip(all_phones, all_prices):
        current_price = "".join(price.text.split())
        print(name.text, current_price)

schedule.every(20).seconds.do(parsing_sulpak)
# schedule.every(1).seconds.do(hello_world)
# schedule.every(1).minutes.do(hello_world)
# schedule.every().day.at("18:33").do(hello_world)
# schedule.every().monday.at("18:36").do(hello_world)
# schedule.every().monday.at("18:39").do(alert_lesson)
# schedule.every().hours.at(":42").do(alert_lesson)
# schedule.every(3).seconds.do(get_btc_price)


while True:
    schedule.run_pending()