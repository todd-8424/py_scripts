
"""
Author: Todd A. Kearney
Support: none
Date: 9 March 2021
Description: Used to search AD server for users 
Requirements: This will search the AD server of choice all required variable are asked for or just set them in the script. 
"""

from ldap3 import Server, Connection, ALL, NTLM
import sys
import getpass
import argparse

# Vars
server=""
ad_user=""
search_base=""
domain=""
search_filter="(&(objectclass=user))"


def getArgs():
    global server
    global ad_user
    global domain
    parser=argparse.ArgumentParser(description='Connect to AD and search OU for all users')
    parser.add_argument('-domain', help='Please supply the domain')
    parser.add_argument('-user', help='Please supply username in "domain\\user" format' )
    parser.add_argument('-server', help='Supply server to connect to')
    parser.add_argument('-search', help='Supply search DN')
    args = parser.parse_args()
    server = args.server
    ad_user = args.user
    domain = args.domain
    return server, ad_user, domain

getArgs()

ad_user="\""+domain+"\\"+ad_user+"\""
ad_password = getpass.getpass(prompt='Please enter password for '+ad_user)
server = Server(server, get_info=ALL)
con = Connection(server, ad_user, ad_password, authentication=NTLM, auto_bind=True)
con.search(search_base,"(objectClass=user)", attributes=['sn', 'displayName', 'objectclass'])
print(con.entries)
con.unbind()
