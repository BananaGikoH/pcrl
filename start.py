#!/usr/bin/python
import json

#読み込み
f = open("testdata.json")
jsonData = json.load(f)
st = json.dumps(jsonData,ensure_ascii=False,indent=4)
print(st)

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

#書き込み
f = open("testdata.json", "w")
json.dump(jsonData, f, ensure_ascii=False,indent=4)