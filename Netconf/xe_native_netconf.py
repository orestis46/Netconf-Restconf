from ncclient import manager

from scrapli_netconf import NetconfDriver

XE = {
    "host": "ios-xe-mgmt-latest.cisco.com",
    "auth_username": "developer",
    "auth_password": "C1sco12345",
    "auth_strict_key": False,
}

XE_NCC = {
    "host": "ios-xe-mgmt-latest.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "hostkey_verify": False,
}

config_data = '''
 <config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>100</name>
                <ip>
                    <address>
                        <primary>
                            <address>10.10.10.10</address>
                            <mask>255.255.255.255</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
'''
with NetconfDriver(**XE) as conn:
    rpc_reply = conn.edit_config(target="running", config=config_data)
    print(rpc_reply)

# Does not work with NCCLIENT responds with <bad-element>config</bad-element> error-info
with manager.connect(**XE_NCC) as conn:
    rpc_reply = conn.edit_config(target="running", config=config_data)
    print(rpc_reply)
