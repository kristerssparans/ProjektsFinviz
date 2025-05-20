# ProjektsStockAnalysis
Projekta darbs, ko izstrādājuši Kristers Sparāns un Matīss Šķēle, izmantojot mājaslapu StockAnalysis un 'web scraping'.

Projekta mērķis ir saprast, kā pielietot "web-scraping" metodi sev noderīgi. Mūsu izveidotais projekts atrod piecas populārākās akcijas un passaka, vai citi akciju tirgus speciālisti iesaka izvēlēto akciju pirkt. Izmantojot "web-scraping" un python prasmes, spējām izveidot kodu, kas nosaka piecas populārākās akcijas vai atsevišķu akciju investoru viedokļus. Pati programma atvieglo pašam manuāli pārskatīt katru akciju individuāli un ļauj lietotājam ietaupīt savu laiku. 

Darbības gaita:

1. Izdomāt pašu ideju.
2. Atrast nepieciešamo mājaslapu, kas atļauj izmantot pašu "web-scraping" metodi.
3. Izveidot kodu.
5. Pārbaudīt koda darbību.
6. Pēdējie uzlabojumi.

Koda darbība:

1. import requests, from bs4 import BeautifulSoup - Python bibliotēka, lai varētu izmantot "web-scraping" metodi.

2. adrese = ... , lapa = request.get(adrese) - atļauj piekļuvi mājaslapai

3. If lapa.status_code = 200 - pārbauda savienojumu ar mājaslapu 

4. Lapas_saturs = BeautifulSoup(lapa.content, "html.parser") - Atļauj piekļūt kodam pie funkcijas "inspect"

5. Symbol = input... - Lietotājam atļauj ievadīt izvēlētās akcijas simbolus

6. link = "..." + symbol + "/" - Atrod mājaslapā nepieciešamās akcijas informāciju

7. jauna_lapa = request.get(link) - kodam tiek pie izvēlētās akcijas, kas atrodas mājaslapā.

8. paregojums = jaunas_lapas_saturs.find... - Varētu atrast to sadaļu, kas pasaka vai noteikto akciju vajag pirkt, pārdot vai turēt.







