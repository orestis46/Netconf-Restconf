from scrapli_netconf import NetconfDriver
from ncclient import manager

arista = {"host": "172.16.21.46",
          "auth_username": "netadmin",
          "auth_password": "netadmin",
          "auth_strict_key": False,
          "port": 830,
          }

iosxe = {"host": "sandbox-iosxe-latest-1.cisco.com",
         "username": "developer",
         "password": "C1sco12345",
         "hostkey_verify": False,
         "port": 830,
         }

filt = """
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
<interface>
"""
filt2 = """
<interfaces xmlns="http://openconfig.net/yang/interfaces">
</interfaces>
"""
ncc_filt = "<interfaces xmlns=\"urn:ietf:params:xml:ns:yang:ietf-interfaces\"/>"
ncc_filt2 = "<interfaces xmlns=\"http://openconfig.net/yang/interfaces\"/>"

# with NetconfDriver(**arista) as conn:
#     result = conn.get_config(
#         source="running", filter_type="subtree", filters=filt)
# # result = conn.get_config()
# print(result.result)

# with manager.connect(**iosxe) as ncc:
#     response = ncc.get_config(
#         source="running", filter=("subtree", ncc_filt2))
#     print(response)

with manager.connect(**iosxe) as ncc:
    response = ncc.get_config(
        source="running", filter=("xpath", "/native"))
    print(response)
