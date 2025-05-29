import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog, QTextEdit, QVBoxLayout, QMessageBox, QPushButton)
from PySide6.QtCore import QFile
from ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.PromptButton.clicked.connect(self.PromptButton_clicked)
        self.ui.CopyButton.clicked.connect(self.CopyButton_clicked)
        self.ui.HistoryButton.clicked.connect(self.HistoryButton_clicked)

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
        prompt_text = f"K-WAIS-IV를 {Age}세 학생에게 시행했는데, FSIQ는 {FSIQ}, VCI는 {VCI}, PRI는 {PRI}, WMI는{WMI}, PSI는 {PSI}로 나타났어. 소검사 환산점수는 각각 토막짜기 {BD}점, 공통성 {SI}점, 숫자 {DS}점, 행렬추론 {MR}점, 어휘 {VC}점, 산수 {AR}점, 동형찾기 {SS}점, 퍼즐 {VP}점, 상식 {IN}점, 기호쓰기 {CD}점이야. 이 수검자의 인지적 특성을 알려줘."
        self.ui.plainTextEdit.setPlainText(prompt_text)

        try:
            with open("history.txt", "a", encoding="utf-8") as f:
                f.write(prompt_text + "\n")
        except (IOError, OSError) as e:
            print(f"Error writing to history.txt: {e}")

    def HistoryButton_clicked(self):
        try:
            with open("history.txt", "r", encoding="utf-8") as f:
                history_content = f.read()
            
            if not history_content:
                QMessageBox.information(self, "기록 보기", "기록이 없습니다.")
                return

            dialog = QDialog(self)
            dialog.setWindowTitle("기록 보기")
            dialog.setGeometry(300, 300, 400, 300) # x, y, width, height

            layout = QVBoxLayout()
            
            text_edit = QTextEdit()
            text_edit.setPlainText(history_content)
            text_edit.setReadOnly(True)
            layout.addWidget(text_edit)
            
            close_button = QPushButton("닫기")
            close_button.clicked.connect(dialog.accept)
            layout.addWidget(close_button)
            
            dialog.setLayout(layout)
            dialog.exec()

        except FileNotFoundError:
            QMessageBox.information(self, "기록 보기", "기록 파일(history.txt)을 찾을 수 없습니다.")
        except (IOError, OSError) as e:
            QMessageBox.warning(self, "오류", f"기록을 불러오는 중 오류가 발생했습니다: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
