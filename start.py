#!/usr/bin/python
import json
f = open("testdata.json")
jsonString = json.load(f)
print(jsonString["index"])