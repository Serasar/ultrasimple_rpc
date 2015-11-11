import json
import random
import requests

RPC_URL     = "http://127.0.0.1:18332"
RPC_USER    = "user"
RPC_PASS    = "password"


def rpc(method, params=None):
    rpc_id = random.getrandbits(32)

    callstr = json.dumps({"id": rpc_id, "method": method, "params": params})

    request = requests.get(RPC_URL, auth=(RPC_USER, RPC_PASS), data=callstr)
    response = request.json()

    if response['id'] != rpc_id:
        raise ValueError("invalid response id!")
    elif response['error'] != None:
        raise ValueError("rpc error: %s" % json.dumps(response['error']))

    return response['result']

print(rpc("getinfo", []))