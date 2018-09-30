
from pathlib import Path
import gzip
from bs4 import BeautifulSoup as BS
import re
import json
from hashlib import sha256


hash_obj = {}
for path in Path('./facebook_score_v2').glob('*'):
  obj = json.load(path.open())
  print(list(obj.keys()))
  url_hash = sha256(bytes(obj['url'], 'utf8')).hexdigest()
  max_date = max([x for x in obj.keys() if x != 'url'])
  num = sum(obj[max_date]['engagement'].values())
  if num == 0:
    continue
  hash_obj[url_hash] = {'date':max_date, 'num':num } 

for path in Path('./htmls').glob('*'):
  url_hash = str(path).split('/').pop().replace('.gz','')
  print(url_hash)
  if hash_obj.get(url_hash) is None:
    continue
  try:
    a = gzip.decompress(path.open('rb').read()).decode()
  except Exception as ex:
    print(ex)
    continue
  soup = BS(a, 'html.parser')
  try:
    head = soup.find('div', {'class':'hd'}).text
    text = soup.find('div', {'class':'articleMain'}).text
  except Exception as ex:
    print(ex)
    ...
  title = re.sub(r'\s{1,}', ' ', head)
  body = re.sub(r'\s{1,}', ' ', text)
  hash_obj[url_hash]['title'] = title
  hash_obj[url_hash]['body']  = body

json.dump(hash_obj, fp=open('hash_obj.json', 'w'), indent=2, ensure_ascii=False)
  #print(head, text)
