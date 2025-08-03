import requests

def fetch_data_api(api_url):
    response = requests.get(api_url)

    # print(response.status_code)
    # print(response.json())

    if response.status_code == 200:
        data = response.json()
        quotation = float(data['USDBRL']['bid'])
        print(f"Current USD to BRL exchange rate: {quotation:.2f}")

def main():
    api_url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    fetch_data_api(api_url)

if __name__ == "__main__":
    main()