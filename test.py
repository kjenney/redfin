import os
from redfin import Redfin

client = Redfin()

address = '256 Speen St, Natick, Massachusetts'

status = client.login(os.environ.get('REDFIN_USER'), os.environ.get('REDFIN_PWD'))
print('login status:', status)
assert(status == 200)
response = client.search(address)
url = response['payload']['exactMatch']['url']
initial_info = client.initial_info(url)
property_id = initial_info['payload']['propertyId']
owner_estimate = client.owner_estimate(property_id)
print(owner_estimate)
client.save_cookies()
