from scrapli_netconf import NetconfDriver
from ncclient import manager

# Arista vEOS and Cisco IOS-XR - NXOS don't support XPATH filtering, only the mandatory SUBTREE filtering
# Examples with RPC <get-config> for configuration and RPC <get> that can retrieve both configuration and operational data
# Both ncclient and scrapli_netconf are used

arista = {"host": "172.16.21.46",
          "auth_username": "netadmin",
          "auth_password": "netadmin",
          "auth_strict_key": False,
          "port": 830,
          }

ncc_arista = {"host": "172.16.21.46",
              "username": "netadmin",
              "password": "netadmin",
              "hostkey_verify": False,
              "port": 830,
              }

iosxe = {"host": "sandbox-iosxe-latest-1.cisco.com",
         "auth_username": "developer",
         "auth_password": "C1sco12345",
         "auth_strict_key": False,
         "port": 830,
         }

ncc_iosxe = {"host": "sandbox-iosxe-latest-1.cisco.com",
             "username": "developer",
             "password": "C1sco12345",
             "hostkey_verify": False,
             "port": 830,
             }

iosxr = {"host": "sandbox-iosxr-1.cisco.com",
         "auth_username": "admin",
         "auth_password": "C1sco12345",
         "auth_strict_key": False,
         #  "port": 830,
         }

ncc_iosxr = {"host": "sandbox-iosxr-1.cisco.com",
             "username": "admin",
             "password": "C1sco12345",
             "hostkey_verify": False,
             #  "port": 830,
             }

nxos = {"host": "sandbox-nxos-1.cisco.com",
        "auth_username": "admin",
        "auth_password": "Admin_1234!",
        "auth_strict_key": False,
        #  "port": 830,
        }

ncc_nxos = {"host": "sandbox-nxos-1.cisco.com",
            "username": "admin",
            "password": "Admin_1234!",
            "hostkey_verify": False,
            #  "port": 830,
            }

filt = """
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
<interface>
"""
filt2 = """
<interfaces xmlns="http://openconfig.net/yang/interfaces">
</interfaces>
"""
xr_lpts_oper = """ 
<lpts-ifib xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-lpts-ifib-oper">
</lpts-ifib>
"""
xe_oper = """
<interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper">
<interface>
"""
nxos_oper = """
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
<interface>
"""

ncc_filt = "<interfaces xmlns=\"urn:ietf:params:xml:ns:yang:ietf-interfaces\"/>"
ncc_filt2 = "<interfaces xmlns=\"http://openconfig.net/yang/interfaces\"/>"
ncc_xr_lpts_oper = "<lpts-ifib xmlns=\"http://cisco.com/ns/yang/Cisco-IOS-XR-lpts-ifib-oper\"/>"
ncc_xe_oper = "<interfaces xmlns=\"http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper\"/>"

# RPC <get-config> examples with ncclient/scrapli_netconf, XPATH/SUBTREE filtering for Arista/IOS-XE/IOS-XR/NX-OS

# with NetconfDriver(**arista) as conn:
#     result = conn.get_config(
#         source="running", filter_type="subtree", filters=filt)
# # result = conn.get_config()
# print(result.result)

# with NetconfDriver(**iosxe) as conn:
#     result = conn.get_config(
#         source="running", filter_type="subtree", filters=filt)
# # result = conn.get_config()
# print(result.result)

# with NetconfDriver(**iosxe) as conn:
#     result = conn.get_config(
#         source="running", filter_type="xpath", filter_="/native//ikev2")
# # result = conn.get_config()
# print(result.result)

# with manager.connect(**ncc_iosxr) as ncc:
#     response = ncc.get_config(
#         source="running", filter=("subtree", ncc_filt2))
#     print(response)

# with manager.connect(**ncc_iosxe) as ncc:
#     response = ncc.get_config(
#         source="running", filter=("xpath", "/native"))
# print(f"---------- {ncc_iosxe['host']} ----------\n\n\n")
# print(response)
# print("*"*40)
# print("\n\n")
# print("*"*40)
# with NetconfDriver(**iosxr) as conn:
#     result = conn.get_config(
#         source="running", filter_type="subtree", filter_=filt2)
# # result = conn.get_config()
# print(f"---------- {iosxr['host']} ----------\n\n\n")
# print(result.result)
with NetconfDriver(**nxos) as conn:
    result = conn.get_config(
        source="running", filter_type="subtree", filter_=filt2)
# result = conn.get_config()
print(f"---------- {nxos['host']} ----------\n\n\n")
print(result.result)
print("*"*40)
print("\n\n")
print("*"*40)

with manager.connect(**ncc_nxos) as ncc:
    response = ncc.get_config(
        source="running", filter=("subtree", ncc_filt2))
print(f"---------- {nxos['host']} ----------\n\n\n")
print("*"*40)
print("\n\n")
print(response)
print("*"*40)


# RPC <get> examples with ncclient/scrapli_netconf, XPATH/SUBTREE filtering for Arista/IOS-XE/IOS-XR/NXOS

# with manager.connect(**ncc_iosxe) as ncc:
#     response = ncc.get(filter=("subtree", ncc_xe_oper))
# print(f"---------- {ncc_iosxe['host']} ----------\n\n\n")
# print(response)
# print("*"*40)
# print("\n\n")
# print("*"*40)
# with NetconfDriver(**iosxr) as conn:
#     result = conn.get(filter_type="subtree", filter_=xr_lpts_oper)
# # result = conn.get_config()
# print(f"---------- {iosxr['host']} ----------\n\n\n")
# print(result.result)
# print("*"*40)
# print("\n\n")
# print("*"*40)
with NetconfDriver(**nxos) as conn:
    result = conn.get(filter_type="subtree", filter_=xr_lpts_oper)
# result = conn.get_config()
