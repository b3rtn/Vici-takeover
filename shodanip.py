import shodan
import sys

pagen = sys.argv[1]

SHODAN_API_KEY = "keyhere"

api = shodan.Shodan(SHODAN_API_KEY)

results = api.search('Asterisk PBX vici ',page=int(pagen))
for result in results['matches']:
  print(str(result['ip_str']))
