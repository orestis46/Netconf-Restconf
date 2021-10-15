# Nornir Modules
from nornir import InitNornir
from nornir_scrapli.tasks import netconf, netconf_get, netconf_get_config, netconf_edit_config, netconf_lock, netconf_unlock, netconf_commit
from nornir_netconf.plugins.tasks import netconf_get, netconf_get_config, netconf_edit_config
from nornir_utils.plugins.functions import print_result
from nornir.core.exceptions import NornirExecutionError
from nornir.core.task import Task, Result

# Netconf modules
from ncclient import manager


def main():
    """ Main Function
    """
    nr = InitNornir(config_file="config.yaml")
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
    ncc_filt = "<interfaces xmlns=\"urn:ietf:params:xml:ns:yang:ietf-interfaces\"/>"
    ncc_filt2 = "<interfaces xmlns=\"http://openconfig.net/yang/interfaces\"/>"
    ncc_xr_lpts_oper = "<lpts-ifib xmlns=\"http://cisco.com/ns/yang/Cisco-IOS-XR-lpts-ifib-oper\"/>"
    ncc_xe_oper = "<interfaces xmlns=\"http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper\"/>"

    result_1 = nr.run(task=scr_netconf, filtro=filt2)
    print_result(result_1)
    result_2 = nr.run(task=ncc_netconf, filtro=ncc_filt2)
    print_result(result_2)


def scr_netconf(task, filtro):

    task.run(task=netconf_get_config, source="running",
             filter_type="subtree", filters=filtro)
    print("="*40)
    print("\n")
    print(f"\n\n********** {task.host.hostname} **********\n\n")
    print("="*40)


def ncc_netconf(task, filter):
    pass


def nr_netconf(task, filtro):
    task.run(task=netconf_get_config, source="running",
             filter=("subtree", filtro))
    print("="*40)
    print("\n")
    print(f"\n\n********** {task.host.hostname} **********\n\n")
    print("="*40)


if __name__ == "__main__":
    main()
