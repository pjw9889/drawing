from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QPushButton, QApplication, QWidget, QListView, QVBoxLayout, QHBoxLayout)
from mpldatacursor import datacursor

import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class MainUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        self.setAcceptDrops(True) # set drop
        self.setWindowTitle("Hello world")
        self.setGeometry(300, 300, 500, 500)
        self.model = QStandardItemModel()

        self.listView = QListView()
        self.listView.setModel(self.model)

        btnExecute = QPushButton()
        btnExecute.setText("실행")
        btnExecute.clicked.connect(self.executeMatplot)

        topLayout = QHBoxLayout()
        topLayout.addWidget(btnExecute)

        bottomLayout =QVBoxLayout();
        bottomLayout.addWidget(self.listView)

        vBox = QVBoxLayout()
        vBox.addLayout(topLayout)
        vBox.addLayout(bottomLayout)

        self.setLayout(vBox)

    def executeMatplot(self):
        print("clicked", self.model.rowCount())
        if(self.model.rowCount() > 0):
            i = 0
            while self.model.item(i):
                if self.model.item(i).checkState():
                    self.showChart(self.model.item(i).text())
                i += 1
            plt.show()

    def showChart(self, path):
        data = np.loadtxt(path)

        df = pd.DataFrame(data, columns=['A', 'B', 'C'])
        df = df.drop('A', 1)
        df.plot(title=path.split("/")[-1])

        #datacursor(hover=True, point_labels=df['B'])


    def dragEnterEvent(self, e):
        print("dragEnterEvent", )
        e.accept()
        # if e.mimeData().hasFormat("text/plain"):
        #
        # else:
        #     e.ignore()

    def dropEvent(self, e):
        fileArray = e.mimeData().text().split("\n")
        if len(fileArray) > 1:
            fileArray = fileArray[:-1]

        for item in fileArray:
            filePath = item.split(":///")[1]
            item = QStandardItem(filePath)
            item.setCheckable(True)
            self.model.appendRow(item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()
