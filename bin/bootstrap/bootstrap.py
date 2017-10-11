#!/usr/bin/python
# -*- coding: utf-8 -*-

import bin.__setting__.situation
import bin.sys.work_json

def boot(args):
    param = bin.__setting__.situation.Parameter()
    
    #print(args)
    #もしargsが入っているなら
    if([]!=args):
        #commandfile引数指定なら
        if("--commandfile"==args[0]):
            #ファイル読み込み
            print("Now read "+args[1])
            commandfile = bin.sys.work_json.open_json(args[1])
            param.setParams(commandfile)
            
        elif("--help"==args[0]):
            print("See help ...")
            #jsonファイルでhelpの中身書いても良いかも
            
        #--mode ～で個別にモード選択等いいかも
        
        else:
            #ここはエラー処理をさせたい
            print("Error : "+"引数が間違っています。")
            print("コマンドライン引数の指定については、\"--help\"を参照して下さい。")
            return -1

    
    
    # CUI
    
    # debug modeか否か
    if (param.getParams()["Mode"]["Mode_debug"] == True):
        print("now debug mode ...")
    #UI選択
    print("bootstrap ...")
    
    print("bootstrap end ...")
    #とりあえずGUIで作成する
    
    print("test")
    return 0


if __name__ == "__main__":
    boot(["foo", "bar"])
    boot(["--help"])
    boot(["--commandfile","C:/Users/pecopeco/Documents/GitHub/pcrl/commandFile.json"])