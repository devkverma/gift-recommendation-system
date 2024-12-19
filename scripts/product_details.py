import requests
from dotenv import load_dotenv
import os

class ProductDetails:

    def __init__(self):
        load_dotenv()

        self.API_KEY = os.getenv("RAPIDAPI_KEY")

    def fetchDetails(self, productID):

        url = "https://axesso-axesso-amazon-data-service-v1.p.rapidapi.com/amz/amazon-lookup-product"

        querystring = {"url":f"https://www.amazon.com/dp/{productID}/"}

        headers = {
            "x-rapidapi-key": self.API_KEY,
            "x-rapidapi-host": "axesso-axesso-amazon-data-service-v1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        remaining_requests = int(response.headers.get("x-ratelimit-requests-remaining", 0))
        time_to_renew = response.headers.get("x-ratelimit-reset","unknown")

        if remaining_requests <= 0:
            print(time_to_renew)
            return [496, time_to_renew]
        else:
            if response.status_code != 200:
                return ['error',response.status_code]
            
            else:
                result = response.json()
                details = {
                    "title": result['productTitle'] if result['productTitle'] else 'unavailable',
                    "description": result['features'][0] if result['features'] else '* No description available *',
                    "price": result['price'] if result['price'] else 'unavailable',
                    "image": result['imageUrlList'][0] if result['imageUrlList'] else 'https://placehold.jp/300x300.png',
                }
                return details
