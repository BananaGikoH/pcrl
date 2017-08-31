#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

#def読み込み
#indexでバージョン表示
def getDefinition():
    #ファイルの格納場所の指定は後日
    f = open("../../testDef.json")
    definition = json.load(f)
    return definition
    

if __name__ == "__main__":
    print(str(getDefinition()))