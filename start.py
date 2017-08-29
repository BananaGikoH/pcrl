#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

#読み込み
f = open("testdata.json")
jsonData = json.load(f)
st = json.dumps(jsonData,ensure_ascii=False,indent=4)
#print(st)

#判定
bool = True
if jsonData["Decision"]:
    bool = False
else:
    bool = True

#表示
print("")
print("Now Decision ...")
#https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q12174941742
print("Decision : "+ str(jsonData["Decision"]) +" -> "+str(bool))

#編集
jsonData["Decision"] = bool


#template読み込み
PP = open("testTemplate.json")
template = json.load(PP)

print("")
#keysを読み出してDataの中身を表示
for keys in template["keys"]:
    print(keys +" : " +jsonData[keys])
print("")

#changeをもう一回変更
if True == jsonData[template["keys_change"]]:
    jsonData[template["keys_change"]] = False
    print("Decision : True -> False")
else:
    jsonData[template["keys_change"]] = True
    print("Decision : False -> True")

#書き込み
f = open("testdata.json", "w")
json.dump(jsonData, f, ensure_ascii=False,indent=4)

import hashlib
import hmac
print(hmac.new(bytearray("綾波レイ","UTF-8"),bytearray("惣流・アスカ・ラングレー","UTF-8"), hashlib.sha256).hexdigest())

#testDef読み込み
dd = open("testDef.json")
jsondef = json.load(dd)

