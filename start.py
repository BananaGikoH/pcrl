#!/usr/bin/python
import json

#読み込み
f = open("testdata.json")
jsonData = json.load(f)
str = json.dumps(jsonData,ensure_ascii=False,indent=4)
print(str)

#編集


#書き込み
