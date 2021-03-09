"""
Author: Todd A. Kearney
Support: none
Date: 9 March 2021
Description: This should be used to create a group in AD in the group_ou defined. Currently uses the servername for the group name. 
Requirements: This script is designed to be used with Morphues as a Python task in an operational workflow or just a single task.
              task must have a conext with the server variable present. Script also utilizes morpheuscypher and ldap3 which will 
              need to be in the additional packages in the python task.
"""

#imports
from ldap3 import Server, Connection, ALL, NTLM
from morpheuscypher import Cypher

#Variables
realm=Cypher(morpheus=morpheus).get('secret/realm')
realm_admin=Cypher(morpheus=morpheus).get('secret/realm_admin')
password=Cypher(morpheus=morpheus).get('secret/realm_password')
group_ou=Cypher(morpheus=morpheus).get('secret/group_ou')

# print realm
# print realm_admin
# print password
# print group_ou

#code
server = Server(realm)
conn = Connection(server, user=realm_admin, password=password, authentication=NTLM)
groupDN = 'CN='+morpheus['server']['hostname']+","+group_ou
print groupDN

conn.bind()
conn.add(groupDN, 'group')
conn.unbind()