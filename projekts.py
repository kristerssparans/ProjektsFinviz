import requests
from bs4 import BeautifulSoup

adrese = "https://stockanalysis.com/stocks/screener/"

lapa = requests.get(adrese)

if lapa.status_code == 200:
    print("Savienojums tika izveidots.")
    lapas_saturs = BeautifulSoup(lapa.content, "html.parser")

    print("Izvēles iespējas:")
    print("1. Akcijas atrašana + ekspertu viedoklis")
    print("2. Top5 akciju pareģojumu izvade nākamajiem 12 mēnešiem.")
    izvele = input("Ievadi skaitli: ")

    if izvele == "1":
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
                        print(f"Expertu viedoklis par izvēlēto akciju - {paregojums.find('span').text}")
                        exists = True

            if exists != True:
                print("Nav pieejams ekspertu viedoklis.")
        else:
            print("Netika atrastas akcijas.")

    elif izvele == "2":
        top5 = ["MSFT", "NVDA", "AAPL", "AMZN", "GOOG"]
        print("Top5 akcijas:")

        for stock in top5:
            stockpage = "https://stockanalysis.com/stocks/" + stock + "/forecast/"
            openpage = requests.get(stockpage)

            if openpage.status_code == 200:
                openpage_saturs = BeautifulSoup(openpage.content, "html.parser")
                paregojums = openpage_saturs.find(class_="-mt-2 text-center text-xl font-semibold")
                cena = openpage_saturs.find(class_="text-green-700 dark:text-green-500")
                print(f"{stock} - {paregojums.find('span').text} {cena.text}")
            else:
                print("Kļūda datu ieguvē.")


    else:
        print("Nepareizi veikta izvēle")

else:
    print(f"kļūda pieslēdzoties mājaslapai - {lapa.status_code}")
