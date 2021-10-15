from nornir import InitNornir
from nornir_http.tasks import http_method
from nornir.core.task import Result
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
    url = f"https://{task.host.hostname}:443/restconf/data/openconfig-interfaces:interfaces?content=nonconfig"
    #url = f"https://{task.host.hostname}:443/restconf/data/native"

    result = requests.get(
        url=url,
        headers=headers,
        auth=(f"{task.host.username}",
              f"{task.host.password}"),
        verify=False)
    #task.host["facts"] = result.text
    #result = json.loads(result.content.decode("utf-8"))
    return Result(host=task.host, result=result)


nr = InitNornir(config_file="config.yaml")


result = nr.run(task=get_restconf)
print_result(result)
# ipdb.set_trace()
