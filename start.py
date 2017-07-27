#!/usr/bin/python
# -*- coding: utf-8 -*-

# http://qiita.com/kenasman/items/70a3ef914b0e7e55a123

import sys
from PyQt5.QtWidgets import *

def main():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)
    w.setWindowTitle('Window01')
    w.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
