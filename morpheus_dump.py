"""
Author: Todd A. Kearney
Support: none
Date: 9 March 2021
Description: Dump the python environment and the variables passed to the Python task 
Requirements: This script is designed to be used with Morphues as a Python task in an operational workflow or just a single task. 
"""

import os
import sys
import json
from pprint import pprint

print("-----------")
print("Executable:")
print("-----------")
print(sys.executable)
print("-----------")
print("OS Env:")
print("-----------")
print(json.dumps(dict(os.environ), indent=4))
print("-----------")
print("sys.argv:")
print("-----------")
pprint(sys.argv)
print("-----------")
print("Morpheus:")
print("-----------")
j_morpheus=json.dumps(morpheus)
j_morpheus_data=json.loads(j_morpheus)
print(json.dumps(j_morpheus_data, indent=4))
print("-----------")
print("example access key")
print("-----------")
print("Current User: "+j_morpheus_data['morpheus']['customOptions'])