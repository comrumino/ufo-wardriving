#!/usr/bin/python
'''
//=============================================================================
//
//	File : fastgui.py
//	Creation date : Wed Dec 05 14:30:48 CEST 2012
//	Working on this file:	^4st3r1X^ (Cristian Steri)
//							Grifisx (Antonino G. Imbesi)
// 	This file is part of the Ufo Wardriving distribution
//
//	Websites: http://thc-scripting.it
//
// 	This program is FREE software. You can redistribute it and/or
// 	modify it under the terms of the GNU General Public License
// 	as published by the Free Software Foundation; either version 2
// 	of the License, or (at your opinion) any later version.
//
//	This program is distributed in the HOPE that it will be USEFUL,
// 	but WITHOUT ANY WARRANTY; without even the implied warranty of
// 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
// 	See the GNU General Public License for more details.
//
// 	You should have received a copy of the GNU General Public License
// 	along with this program. If not, write to the Free Software Foundation,
// 	Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
//
//=============================================================================
'''

import os
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os.path

from core import ufo_fastwebdecode
from core.ufo_picsfinder import getQIcon


class fastGuiWidget(QWidget):
    @staticmethod
    def findKey(self):
        ssid_fast = str(self.macLineEdit.text())
        stdouterr_fast = ufo_fastwebdecode.calc(ssid_fast)
        if stdouterr_fast:
            self.outputTextEdit.setText(stdouterr_fast)
        else:
            self.outputTextEdit.setText(self.tr("No key found."))

    def __init__(self, parent=None):
        super(fastGuiWidget, self).__init__(parent)
        hBoxLayout = QHBoxLayout()
        hBoxLayout.setSpacing(5)

        vBoxLayout = QVBoxLayout()
        vBoxLayout.setSpacing(5)

        self.macLabel = QLabel("SSID:", self)
        self.macLineEdit = QLineEdit(self)
        self.macLineEdit.setToolTip("SSID " + self.tr("Compatible") + " : Fastweb-1-*")
        self.macLineEdit.setInputMask("HHHHHHHHHHHH;-")
        self.macLineEdit.setMaxLength(12)

        self.outputTextEdit = QTextEdit(self)
        self.outputTextEdit.setReadOnly(True)

        self.calcPushButton = QPushButton(self.tr("Find"), self)
        self.calcPushButton.setIcon(getQIcon("key.png"))
        self.calcPushButton.setEnabled(0)

        hBoxLayout.addWidget(self.macLabel)
        hBoxLayout.addWidget(self.macLineEdit)
        hBoxLayout.addWidget(self.calcPushButton)
        vBoxLayout.addLayout(hBoxLayout)
        vBoxLayout.addWidget(self.outputTextEdit)

        self.setLayout(vBoxLayout)

        def slotFindKey():
            self.findKey(self)

        def enableBtn():
            if self.macLineEdit.text().length() == 12:
                self.calcPushButton.setEnabled(1)
            else:
                self.calcPushButton.setEnabled(0)

        self.macLineEdit.textChanged.connect(enableBtn)
        self.calcPushButton.clicked.connect(slotFindKey)
