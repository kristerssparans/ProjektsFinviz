import requests
from bs4 import BeautifulSoup

adrese = "https://stockanalysis.com/stocks/screener/"

lapa = requests.get(adrese)

if lapa.status_code == 200:
    print("Savienojums tika izveidots.")
    lapas_saturs = BeautifulSoup(lapa.content, "html.parser")

    symbol = input("Ievadi akcijas simbolu ko meklē(piemēram - AAPL): ")

    link = "https://stockanalysis.com/stocks/" + symbol + "/"
    jauna_lapa = requests.get(link)

    if jauna_lapa.status_code == 200:
        print(f"{symbol} - was found")
        jaunas_lapas_saturs = BeautifulSoup(jauna_lapa.content, "html.parser")

        navigation = jaunas_lapas_saturs.find(class_="navmenu").find_all("a")
        for value in navigation:
            if value.text == "Forecast":
                forecast_page = "https://stockanalysis.com" + value.attrs["href"]

                open_forecast = requests.get(forecast_page)

                if open_forecast.status_code == 200:
                    forecast_saturs = BeautifulSoup(open_forecast.content, "html.parser")

                    paregojums = forecast_saturs.find(class_="-mt-2 text-center text-xl font-semibold")
                    print(f"Expertu viedoklis par izvēlēto akciju - {paregojums.find("span").text}")
                    exists = True
                
        if exists != True:
            print("Nav pieejams ekspertu viedoklis.")
    else:
        print("Netika atrastas akcijas.")

else:
    print(f"kļūda pieslēdzoties mājaslapai - {lapa.status_code}")
