import requests
import json
from pprint import pprint

requests.packages.urllib3.disable_warnings()

headers = {"Accept": "application/yang-data+json"}

device = {"host": "sandbox-iosxe-latest-1.cisco.com",
          "username": "developer",
          "password": "C1sco12345",
          "port": 443}

url = f"https://{device['host']}:{device['port']}/restconf/data/openconfig-interfaces:interfaces?content=nonconfig"
response = requests.get(
    url=url,
    headers=headers,
    auth=(f"{device['username']}", f"{device['password']}"),
    verify=False)

output = json.loads(response.content.decode("utf-8"))
pprint(output)
# print(response.text)
