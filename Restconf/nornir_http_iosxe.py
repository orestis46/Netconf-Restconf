# Modules
from nornir import InitNornir
# from nornir_http.tasks import http_method
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from nornir.core.exceptions import NornirExecutionError
import json
import requests
from pprint import pprint
import ipdb


def get_restconf(task):

    requests.packages.urllib3.disable_warnings()
    headers = {"Accept": "application/yang-data+json"}
    # USE filter ?content=config or ?content=nonconfig for configuration or state/operational data only respectively
    # NX-OS does not respond to ?content=nonconfig (no <model>-oper found in yang models)
    #url = f"https://{task.host.hostname}:443/restconf/data/openconfig-interfaces:interfaces?content=nonconfig"
    #url = f"https://{task.host.hostname}:443/restconf/data/native"
    url = f"https://{task.host.hostname}:443/restconf/data/openconfig-interfaces:interfaces?content=config"

    result = requests.get(
        url=url,
        headers=headers,
        auth=(f"{task.host.username}",
              f"{task.host.password}"),
        verify=False)
    # IOS-XE returns content that will be formated in <dict> while NX-OS response will be in <str>
    if(task.host.platform == "ios"):
        result = json.loads(result.content.decode("utf-8"))
    else:
        result = result.text
    #task.host["facts"] = result.text
    return Result(host=task.host, result=result)


nr = InitNornir(config_file="config.yaml")


result = nr.run(task=get_restconf)
print_result(result)
# ipdb.set_trace()
