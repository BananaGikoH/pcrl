#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

def open_json(address:str):
    jsonfile = {}
    try:
        f = open(address)
        jsonfile = json.load(f)
    except OSError:
        print("ファイルが開けませんでした。")
    except json.decoder.JSONDecodeError:
        print("ファイルのjsonが正しくありません。")
        print("File : "+address)
    return jsonfile

