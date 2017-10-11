#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import bin.sys.work_json

#def読み込み
#indexでバージョン表示
def getDefinition():
    #ファイルの格納場所の指定は後日
    definition = bin.sys.work_json.open_json("testDef.json")
    return definition
    

if __name__ == "__main__":
    print("{0}".format(getDefinition()))