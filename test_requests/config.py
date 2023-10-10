from requests.auth import HTTPBasicAuth
import json
from api_constants import API, PRIVATE

BASE_URL = 'https://bit.team/trade/api'

# from requests.auth import HTTPBasicAuth
# basic = HTTPBasicAuth('user', 'pass')
# requests.get('https://httpbin.org/basic-auth/user/pass', auth=basic)
basic_auth = HTTPBasicAuth(API, PRIVATE)

def write_json_file(data, name_file):
    path_to_file = f'json/{name_file}.json'
    try:
        with open(path_to_file, 'w') as file:
            json.dump(data, file, indent=4, sort_keys=True)
    except Exception as error:
        print(error)
