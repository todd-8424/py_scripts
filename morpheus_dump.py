import os
import sys
import json
from pprint import pprint
morpheus=""
print(sys.executable)

print("OS Env:")
j_env = json.loads(os.environ)
j_env_str = json.dumps(j_env, indent=4)
print(j_env_str)
print("sys.argv:")
pprint(sys.argv)
print("morpheus:")
pprint(morpheus)

j_morpheus = json.loads(morpheus)
j_morpheus_str = json.dumps(j_morpheus, indent=4)
print(j_morpheus_str)