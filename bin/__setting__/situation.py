#!/usr/bin/python
# -*- coding: utf-8 -*-

class Parameter:
    __params = {}

    def __init__(self):
        #Mode
        self.__params["Mode"] = {}
        #Mode Mode_Test
        self.__params["Mode"]["Mode_Test"] = False
        #Mode Mode_CommandlineUserInterface
        self.__params["Mode"]["Mode_CUI"] = False
        #FirstStartUp
        self.__params["FirstStartUp"] = False

    # Mode Mode_Test
    # テストモード
    def Mode_test(self,bool:bool):
        self.__params["Mode"]["Mode_Test"] = bool

    # Mode Mode_CommandlineUserInterface
    # CUIモード
    def Mode_CUI(self,bool:bool):
        self.__params["Mode"]["Mode_CUI"] = bool

    # FirstStartUp
    # 初めて起動した時、初期設定を行う
    def FirstStartUp(self,bool:bool):
        self.__params["FirstStartUp"] = bool
     
    def getParams(self):
        return self.__params
        
if __name__ == "__main__":
    ss = Parameter()
    print("nomal : " + str(ss.getParams()))
    ss.Mode_test(True)
    print("Mode_test : "+str(ss.getParams()))
    ss.Mode_test(False)
    
    ss.Mode_CUI(True)
    print("Mode_CUI : "+str(ss.getParams()))
    ss.Mode_CUI(False)
    
    ss.FirstStartUp(True)
    print("FirstStartUp : "+str(ss.getParams()))
    ss.FirstStartUp(False)

    print("nomal : " + str(ss.getParams()))