
import requests

try:
    resp = requests.get('http://localhost:5000/api/word-network')
    data = resp.json()
    nodes = data.get('nodes', [])
    for n in nodes:
        if n.get('label') in ['en', 'Enrich', 'enrich']:
            print(n)
except Exception as e:
    print('Failed:', e)
