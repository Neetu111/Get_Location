import requests
import json;req = requests.get('https://www.whizapi.com/api/v2/util/ui/in/indian-postal-codes?project-app-key=k6oyhd6vvi3sdh5m8w2rc7k5&search=delhi')
json_data = json.loads(req.content)
pincodes = [data['Pincode'] for data in json_data['Data']]
print(pincodes)