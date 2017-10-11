#!/usr/bin/python
# -*- coding: utf-8 -*-

import bin.bootstrap.bootstrap
import bin.sys.system
import sys

def start():
    args = sys.argv
    #先頭には実行ファイルの場所が格納される
    del args[0]
    
    #コマンドライン引数を利用するには上記の状態でargsを使用する
    
    #bootstrap 引数処理等
    if(0!=bin.bootstrap.bootstrap.boot(args)):
        return 0
    #基幹バージョンの表示
    bin.sys.system.getDefinition()
    
'''
# 項目選択
何の処理をするか選択→
template→dataの項目を選択
(templateを元にdataを書き込む処理に移行)

template読み込み
before読み込み
indexでtemplateであることを確認
basedonでstandardであることを確認

during読み込み
templateのkeyを捜索する
templateの各keyの値を取得
json型作成
json型のindex書き込み
templateの中で「これは問いかけるものか」の因子があるか確かめる
因子があるものに対してデータ入力させる
入力データをjson型に代入
json型データ生成

json型データ保存

何の処理をするか選択→
template→templateの項目を選択
'''

if __name__ == "__main__":
    "{0}".format(start())