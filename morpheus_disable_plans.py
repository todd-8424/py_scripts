import requests
import json
import logging
import logging.config
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASEURL = ''
CLOUD = morpheus['customOptions']['cloud']
plan_ids = []
logger = logging.getLogger("fileLogger")
logging.basicConfig(filename='/tmp/test.log', format='%(filename)s: %(message)s',level=logging.DEBUG)

j_morpheus=json.dumps(morpheus, indent=4)
j_morpheus_data=json.loads(j_morpheus)
access_token=j_morpheus_data['morpheus']['apiAccessToken']

def getPlans(access_token,CLOUD):
    global plan_ids
    headers = {'Authorization': 'BEARER '+access_token}
    plan_api_url = BASEURL+'/api/service-plans'
    params={'phrase': CLOUD, 'max': '1000'}
    r = requests.get(plan_api_url, headers=headers, params=params, verify=False )
    plans = r.json()
    serv_plans = plans.get('servicePlans')
    print(len(serv_plans))
    for desc in serv_plans:
        desc.get('description')
        print(desc.get('name'))
        plan_ids.append(desc.get('id'))
    return plan_ids
    

def disablePlan(plan_ids):
    headers = {'Authorization': 'BEARER '+access_token}
    for id in plan_ids:
        id = str(id)
        disable_plan_url = BASEURL+'/api/service-plans/'+id+'/deactivate'
        r = requests.put(disable_plan_url, headers=headers, verify=False )
        print(id, r)
    
getPlans(access_token,CLOUD)
disablePlan(plan_ids)
logger.info("Cloud Selected: "+CLOUD)