import requests
import json

acc = input()
for url in ['https://headlines.yahoo.co.jp/hl?a=20180928-00000367-oric-ent']:
  query = f'https://graph.facebook.com/?id={url}&fields=og_object{{engagement}},engagement&access_token={acc}'
  r = requests.get(query)
  obj = json.loads(r.text)
  print(json.dumps(obj, indent=2))
