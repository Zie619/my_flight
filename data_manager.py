import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/9a0db69bffc80e04da55422598a90cf6/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/9a0db69bffc80e04da55422598a90cf6/flightDeals/users"
SHEETY_USERS = "https://api.sheety.co/f0967e8b95ec5724a9457579627014ec/myflights/users/"
SHEETY_LOCATIONS = "https://api.sheety.co/f0967e8b95ec5724a9457579627014ec/myflights/locations/"


class DataManagerMail:

    def __init__(self):
        self.destination_data = {}

    def WriteMail(self, _first_name, _last_name, _email, _number):
        data = {
            "user": {
                "firstname": _first_name,
                "lastname": _last_name,
                "email": _email,
                "number": _number
            }
        }
        response = requests.post(url=SHEETY_USERS, json=data)
        print(response.text)
        return self.destination_data

    def UpdateMail(self, _first_name, _last_name, _email, _number, _id):
        new_data = {
            "user": {
                "firstname": _first_name,
                "lastname": _last_name,
                "email": _email,
                "number": _number
            }
        }
        response = requests.put(url=f"{SHEETY_USERS}/{_id}", json=new_data)
        print(response.text)
        return self.destination_data

    def DeleteMail(self, _id):
        response = requests.delete(
            url=f"{SHEETY_USERS}/{_id}"
        )
        return self.destination_data

    def GetMail(self):
        response = requests.get(url=SHEETY_USERS)
        data = response.json()
        #self.destination_data = data["users"][0]["firstname"]
        self.destination_data = data["users"]
        print(response.text)
        return self.destination_data


class DataManagerLocations:

    def __init__(self):
        self.destination_price = {}

    def WritePrice(self, _city, _iata_code, _lowest_price):
        data = {
            'location': {
                'city': _city,
                'iataCode': _iata_code,
                'lowestPrice': _lowest_price
            }
        }
        response = requests.post(url=SHEETY_LOCATIONS, json=data)
        print(response.text)
        return self.destination_price

    def UpdatePrice(self, _city, _iata_code, _lowest_price, _id):
        new_data = {
            'location': {
                'city': _city,
                'iataCode': _iata_code,
                'lowestPrice': _lowest_price
            }
        }
        response = requests.put(
            url=f"{SHEETY_LOCATIONS}/{_id}",
            json=new_data
        )
        print(response.text)
        return self.destination_price

    def DeletePrice(self, _id):
        response = requests.delete(
            url=f"{SHEETY_LOCATIONS}/{_id}"
        )
        print(response.text)
        return self.destination_price

    def GetPrice(self):
        response = requests.get(url=SHEETY_LOCATIONS)
        data = response.json()
        self.destination_price = data["locations"]
        print(response.text)
        return self.destination_price

# test = DataManagerLocations()
# test.destination_data = 'destination_data'
# test.delete_Price(3)