# coding=utf-8
import sys

from qtpy.QtWidgets import QApplication

from .FormMain import FormMain

app: QApplication = QApplication(sys.argv)
w: FormMain = FormMain()
w.show()
sys.exit(app.exec())
