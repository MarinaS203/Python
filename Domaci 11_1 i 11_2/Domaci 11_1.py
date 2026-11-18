import requests

# 1. Informacije o svemirskoj stanici
# Napisati funkciju get_space_station() -> dict koja preko Open
# Notify API-ja (http://api.open-notify.org/iss-now.json) preuzima
# trenutnu poziciju Međunarodne svemirske stanice (ISS) i vraća
# rečnik koji sadrži:
# geografsku širinu (latitude),
# geografsku dužinu (longitude)

def get_space_station() -> dict:
    url='http://api.open-notify.org/iss-now.json'
    response=requests.get(url)
    response.raise_for_status()
    return response.json()['iss_position']

get_space_station()

# 2. Pretraga univerziteta
# Napisati funkciju get_universities(country: str) -> list koja preko
# Hipolabs API-ja (http://universities.hipolabs.com/search) preuzima
# univerzitete iz zadate države i vraća listu njihovih naziva.
# Koristiti params={'country': country} za prosleđivanje naziva države API-ju.

def get_universities(country: str) -> list:
    url='http://universities.hipolabs.com/search'
    response=requests.get(url, params={'country': country})
    response.raise_for_status()
    data=response.json()
    return [d['name'] for d in data]

get_universities('Serbia')

# 3. Informacije o kursu valuta
# Napisati funkciju get_exchange_rate(base: str, target: str) -> float
# koja preko Frankfurter API-ja (https://api.frankfurter.dev/v1/latest)
# preuzima kurs između dve valute.
# Funkcija treba da vrati koliko jedinica ciljne valute (target) se dobija
# za jednu jedinicu početne valute (base).

# Input: get_exchange_rate("EUR","RSD")
# Output: 117.2

def get_exchange_rate(base: str, target: str) -> float:
    url='https://api.frankfurter.dev/v1/latest'
    params={
        'base':base
    }
    response=requests.get(url, params=params)
    response.raise_for_status()
    return response.json()['rates'][target]
get_exchange_rate('EUR', 'CAD')


#verzija koja radi i sa dinarima

def get_exchange_rate(base: str, target: str) -> float:
    url='https://api.frankfurter.dev/v2/rates'
    params={
        'base':base,
        'quotes': target
    }
    response=requests.get(url, params=params)
    response.raise_for_status()
    return response.json()[0]['rate']
get_exchange_rate('EUR', 'RSD')
