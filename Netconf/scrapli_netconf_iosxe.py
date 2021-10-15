from scrapli_netconf import NetconfDriver

iosxe = {"host": "sandbox-iosxe-latest-1.cisco.com",
         "auth_username": "developer",
         "auth_password": "C1sco12345",
         "auth_strict_key": False,
         "port": 830,
         }

filtering = "/native"
conn = NetconfDriver(**iosxe)
conn.open()
result = conn.get_config(filter_type="xpath", filter_=filtering)
print(result.result)
conn.close()
