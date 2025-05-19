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

        forecasts = jaunas_lapas_saturs.find(data_title_="Forecast")
        print(forecasts)

        #paregojums = jaunas_lapas_saturs.find(class_="-mt-2 text-center text-xl font-semibold")
        #print(paregojums.find("span").text)
    else:
        print("Netika atrastas akcijas.")

else:
    print(f"kļūda pieslēdzoties mājaslapai - {lapa.status_code}")