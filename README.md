# facebook-graphapi-augment

facebookのGraphAPIで様々なサイトのページの評価を得ることで、Webページのデータオーギュメントを行います。　　

例えば、毎日大量に投稿されるYahooNewsは記事によって大きくアクセス数が違うはずですが、アクセス数等が公開されていなく、 GraphAPIを用いると自動化した記事取得の中から、何が今よく参照されているのがよくわかったりします。  

何がよく参照されているかわからないまま、全体のコーパスを平等に用いるより、なんらかのデータオーギュメントしたものを用いるほうが一般的に良いです。

## 課題
Yahoo Newsを日々スクレイピングして、自然言語のコーパスとして、私的利用の範囲内で利用しているのでが、Yahoo Newsはページのアクセス数やSNSで共有した数などはわかりません。

そのため、日々膨大な記事が投稿されるYahoo Newsなどのサイトのいてコーパスだけでなく、何かのデータを拡張する手段が必須になってきます。

## 解決
Yahoo Newsの運営者でもなければ誰からどのようなアクセスがあったかなど、何もわからないのですが、幸いにしてYahoo NewsはURLでFaceBookに公開できるUIになっており、これが記事の間接的な人気度などと考えることができそうです。  

FaceBookのGraphAPIを利用することで、記事が書かているURLに対してFB内部でのイイネ数などの数値が表現されるので、これを用いることができます。  

GraphAPIを利用するには開発者登録と、アクセストークンの発行が必要です。  

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

## プログラムの概要

**[GitHub](https://github.com/GINK03/facebook-graphapi-augment)**

**00-pooling.py**  
10-xml_parse.py, 20-darturl-clean.pyをラップして10分に一度、最新のYahoo Newsがを取得します

**30-facebook_scores.py**  
graph apiを通じて、Yahoo NewsのFBの反応をJSON形式で取得します。  
ご自身のFBアプリを登録してtokenをtokensというテキストファイルに書き出しておく必要があります  

**40-parse.py**  
graph apiの結果とYahoo Newsでスクレイピングした結果を突合して、一つのファイルにまとめます。  


ここまでやったら、株価でも、なんでもこの世の中の事象を学習すると多少の改善が見込めているはずです。  

