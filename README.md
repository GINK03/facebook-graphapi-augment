# facebook-graphapi-augment
facebookのgraphapiで様々なサイトのページfacebookの評価を得ることで、Webページにたいして、データオーギュメントを行います。

## 課題
Yahoo Newsを日々スクレイピングして、ニュースのコーパスとして、私的利用の範囲内で利用しているのでが、Yahoo Newsはページのアクセス数やコメントの数などはわかりません。

## 解決
Yahoo Newsの運営者でもなければ何もわからないのですが、幸いにしてYahoo NewsはURLでFaceBookに公開できるUIになっており、これが記事の人気度などと考えることができそうです。

### Facebook Developerの登録
[このURL](https://developers.facebook.com/?locale=ja_JP)から登録できます。

### Graph APIのアクセストークンの発行
[このURL](https://developers.facebook.com/tools/explorer?method=GET&path=me%3Ffields%3Did%2Cname&version=v3.1)から登録する

## サンプルクエリ
Python等でラップアップしているととても便利です
```python
import requests
import json

acc = input()
for url in ['https://headlines.yahoo.co.jp/hl?a=20180928-00000367-oric-ent']:
  query = f'https://graph.facebook.com/?id={url}&fields=og_object{{engagement}},engagement&access_token={acc}'
  r = requests.get(query)
  obj = json.loads(r.text)
  print(json.dumps(obj, indent=2))
```

## サンプル出力
このように、リアクションの個数、コメントの個数、シェアの個数がわかります
```json
{
  "engagement": {
    "reaction_count": 56,
    "comment_count": 14,
    "share_count": 28,
    "comment_plugin_count": 0
  },
  "id": "https://headlines.yahoo.co.jp/hl?a=20180928-00000367-oric-ent"
}
```
