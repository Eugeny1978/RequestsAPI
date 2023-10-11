from requests.auth import HTTPBasicAuth
import json
from api_keys import API, PRIVATE


basic_auth = HTTPBasicAuth(API, PRIVATE)
# requests.get(url, auth=basic)
