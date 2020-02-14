from gpiozero import LED
from time import sleep
print('hi')
led_green = LED(17)
led_red = LED(16)

while True:
 try:
    #program determines if btc price went up or down
    import urllib3
    from bs4 import BeautifulSoup
    import requests
    response = requests.get('https://api.kraken.com/0/public/OHLC?pair=ETHUSD&interval=1')
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    eth_string=str(soup)
    eth_string=eth_string[-210:]
    price1=eth_string[eth_string.find("[158"):]
    price2=price1
    price1=price1[price1.find(','):]
    price1=price1[2:]
    price1=price1[:price1.find(',')-1]
    print(price1)
    price2=price2[5:]
    price2=price2[price2.find('[158'):]
    price2=price2[price2.find(','):]
    price2=price2[2:]
    price2=price2[:price2.find(',')-1]
    print(price2)

    if float(price1)>float(price2):
        print('etherum went down')
        led_red.on()
        sleep(4)
        led_red.off()
    else:
        print('etherum went up')
        led_green.on()
        sleep(4)
        led_green.off()
       
 except Exception as e:
     print(e)
    

