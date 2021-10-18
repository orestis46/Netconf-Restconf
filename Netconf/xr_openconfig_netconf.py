#from ncclient import manager
from scrapli_netconf import NetconfDriver


from scrapli_netconf import NetconfDriver

XR = {
    "host": "sandbox-iosxr-1.cisco.com",
    "auth_username": "admin",
    "auth_password": "C1sco12345",
    "auth_strict_key": False,
}

configuration = """
<nc:config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:oc-if="http://openconfig.net/yang/interfaces" xmlns:oc-ip="http://openconfig.net/yang/interfaces/ip" xmlns:oc-eth="http://openconfig.net/yang/interfaces/ethernet" xmlns:oc-yang="http://openconfig.net/yang/types/yang" xmlns:oc-lag="http://openconfig.net/yang/interfaces/aggregate" xmlns:oc-eth-ext="http://openconfig.net/yang/interfaces/ethernet-ext" xmlns:oc-ip-ext="http://openconfig.net/yang/interfaces/ip-ext" xmlns:if="urn:ietf:params:xml:ns:yang:ietf-interfaces" xmlns:oc-ift="http://openconfig.net/yang/openconfig-if-types" xmlns:oc-ext="http://openconfig.net/yang/openconfig-ext" xmlns:oc-types="http://openconfig.net/yang/openconfig-types" xmlns:oc-tun="http://openconfig.net/yang/interfaces/tunnel" xmlns:oc-vlan-types="http://openconfig.net/yang/vlan-types" xmlns:oc-1x="http://openconfig.net/yang/interfaces/8021x" xmlns:yang="urn:ietf:params:xml:ns:yang:ietf-yang-types" xmlns:oc-poe="http://openconfig.net/yang/poe" xmlns:oc-vlan="http://openconfig.net/yang/vlan" xmlns:oc-inet="http://openconfig.net/yang/types/inet">
    <oc-if:interfaces>
        <oc-if:interface>
            <oc-if:name>GigabitEthernet0/0/0/2</oc-if:name>
            <oc-if:config>
                <oc-if:name>GigabitEthernet0/0/0/2</oc-if:name>
                <oc-if:type xmlns:idx="urn:ietf:params:xml:ns:yang:iana-if-type">idx:ethernetCsmacd</oc-if:type>
            </oc-if:config>
            <oc-if:subinterfaces>
                <oc-if:subinterface>
                    <oc-if:index>0</oc-if:index>
                    <oc-if:config>
                        <oc-if:index>0</oc-if:index>
                    </oc-if:config>
                    <oc-ip:ipv6>
                        <oc-ip:addresses>
                            <oc-ip:address>
                                <oc-ip:ip>2001:cafe:cafe::1</oc-ip:ip>
                                <oc-ip:config>
                                    <oc-ip:ip>2001:cafe:cafe::1</oc-ip:ip>
                                    <oc-ip:prefix-length>64</oc-ip:prefix-length>
                                </oc-ip:config>
                            </oc-ip:address>
                        </oc-ip:addresses>
                    </oc-ip:ipv6>
                </oc-if:subinterface>
            </oc-if:subinterfaces>
        </oc-if:interface>
        <oc-if:interface>
            <oc-if:name>GigabitEthernet0/0/0/3</oc-if:name>
            <oc-if:config>
                <oc-if:name>GigabitEthernet0/0/0/3</oc-if:name>
                <oc-if:type xmlns:idx="urn:ietf:params:xml:ns:yang:iana-if-type">idx:ethernetCsmacd</oc-if:type>
            </oc-if:config>
            <oc-if:subinterfaces>
                <oc-if:subinterface>
                    <oc-if:index>0</oc-if:index>
                    <oc-if:config>
                        <oc-if:index>0</oc-if:index>
                    </oc-if:config>
                    <oc-ip:ipv6>
                        <oc-ip:addresses>
                            <oc-ip:address>
                                <oc-ip:ip>2001:cafe:cafe:1::1</oc-ip:ip>
                                <oc-ip:config>
                                    <oc-ip:ip>2001:cafe:cafe:1::1</oc-ip:ip>
                                    <oc-ip:prefix-length>64</oc-ip:prefix-length>
                                </oc-ip:config>
                            </oc-ip:address>
                        </oc-ip:addresses>
                    </oc-ip:ipv6>
                </oc-if:subinterface>
            </oc-if:subinterfaces>
        </oc-if:interface>
    </oc-if:interfaces>
</nc:config>
"""

conn = NetconfDriver(**XR)
conn.open()
result = conn.lock(target="candidate")
print(result.result)

result = conn.edit_config(config=configuration, target="candidate")
print(result.result)
conn.commit()
print(result.result)
conn.close()
