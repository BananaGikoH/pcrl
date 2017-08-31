#!/usr/bin/python
# -*- coding: utf-8 -*-

import bin.__setting__.situation

def boot(args):
    
    #args読み込み
    for i in range(len(args)):
        print(args[i])
        #文字確認
    
    param = bin.__setting__.situation.Parameter()
    
    #UI選択
    
    
    #print("bootstrap ...")

    #コマンドライン引数の確認
    str = "Command Line arguments : "
    for i in range(len(args)):
        str = str + "{0}".format(args[i]) + " "
    
    print(str)
    
    #print("bootstrap end ...")
    return args


if __name__ == "__main__":
    boot(["foo","bar"])
    boot(["--mode","CUI"])