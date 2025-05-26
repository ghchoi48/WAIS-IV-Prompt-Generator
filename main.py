import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import QFile
from ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.PromptButton.clicked.connect(self.PromptButton_clicked)
        self.ui.CopyButton.clicked.connect(self.CopyButton_clicked)

    def CopyButton_clicked(self):
        self.ui.plainTextEdit.selectAll()
        self.ui.plainTextEdit.copy()

    def PromptButton_clicked(self):
        Age = self.ui.Input_Age.text()
        FSIQ = self.ui.Input_FSIQ.text()
        VCI = self.ui.Input_VCI.text()
        PRI = self.ui.Input_PRI.text()
        WMI = self.ui.Input_WMI.text()
        PSI = self.ui.Input_PSI.text()
        BD = self.ui.Input_BD.text()
        SI = self.ui.Input_SI.text()
        DS = self.ui.Input_DS.text()
        MR = self.ui.Input_MR.text()
        VC = self.ui.Input_VC.text()
        AR = self.ui.Input_AR.text()
        SS = self.ui.Input_SS.text()
        VP = self.ui.Input_VP.text()
        IN = self.ui.Input_IN.text()
        CD = self.ui.Input_CD.text()
        self.ui.plainTextEdit.setPlainText(f"K-WAIS-IV를 {Age}세 학생에게 시행했는데, FSIQ는 {FSIQ}, VCI는 {VCI}, PRI는 {PRI}, WMI는{WMI}, PSI는 {PSI}로 나타났어. 소검사 환산점수는 각각 토막짜기 {BD}점, 공통성 {SI}점, 숫자 {DS}점, 행렬추론 {MR}점, 어휘 {VC}점, 산수 {AR}점, 동형찾기 {SS}점, 퍼즐 {VP}점, 상식 {IN}점, 기호쓰기 {CD}점이야. 이 수검자의 인지적 특성을 알려줘.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
