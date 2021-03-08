import os
import sys
import json
from pprint import pprint

print(sys.executable)

print("OS Env:")
pprint(os.environ)
print("sys.argv:")
pprint(sys.argv)
print("morpheus:")
pprint(morpheus)

j_morpheus = json.loads(morpheus)
j_morpheus_str = json.dumps(j_morpheus, indent=4)
print(j_morpheus_str)