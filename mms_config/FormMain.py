# coding=utf-8
from pathlib import Path
from typing import Iterable

from qtpy.QtCore import Slot
from qtpy.QtWidgets import (
    QCheckBox,
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QMessageBox,
    QPushButton,
    QTabBar,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from .PageCameraUI import PageCamera
from .PageMmsUI import PageMms
from .PageSmtpUI import PageSmtp


class FormMain(QDialog):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.tabs: QTabWidget = QTabWidget(self)
        self.tab_camera: PageCamera = PageCamera(self)
        self.tab_mms: PageMms = PageMms(self)
        self.tab_smtp: PageSmtp = PageSmtp(self)

        self.check_mms: QCheckBox = QCheckBox(self)
        self.check_smtp: QCheckBox = QCheckBox(self)

        self.buttons: QDialogButtonBox = QDialogButtonBox(self)
        self.button_load: QPushButton = QPushButton(self.tr("Load"), self)
        self.button_save: QPushButton = QPushButton(self.tr("Save"), self)
        self.button_reset: QPushButton = QPushButton(self.tr("Default"), self)
        self.button_about: QPushButton = QPushButton(self.tr("About"), self)

        self._setup_ui()
        self.initialize()

    def _setup_ui(self) -> None:
        self.setWindowTitle(self.tr("Camera Parameters"))

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.tabs)
        self.layout().addWidget(self.buttons, 0)

        self.buttons.addButton(
            self.button_load,
            QDialogButtonBox.ButtonRole.ActionRole,
        )
        self.buttons.addButton(
            self.button_save,
            QDialogButtonBox.ButtonRole.ApplyRole,
        )
        self.buttons.addButton(
            self.button_reset,
            QDialogButtonBox.ButtonRole.ResetRole,
        )
        self.buttons.addButton(
            self.button_about,
            QDialogButtonBox.ButtonRole.HelpRole,
        )

        self.tabs.addTab(self.tab_camera, self.tr("Menu"))
        self.tabs.addTab(self.tab_mms, self.tr("MMS"))
        self.tabs.addTab(self.tab_smtp, self.tr("SMTP"))

        self.tabs.tabBar().setTabButton(
            self.tabs.indexOf(self.tab_mms),
            QTabBar.ButtonPosition.LeftSide,
            self.check_mms,
        )
        self.tabs.tabBar().setTabButton(
            self.tabs.indexOf(self.tab_smtp),
            QTabBar.ButtonPosition.LeftSide,
            self.check_smtp,
        )

        self.tab_mms.stateChanged.connect(self._on_tab_mms_state_changed)
        self.tab_smtp.stateChanged.connect(self._on_tab_smtp_state_changed)
        self.check_mms.toggled.connect(self._on_check_mms_toggled)
        self.check_smtp.toggled.connect(self._on_check_smtp_toggled)

        self.button_load.clicked.connect(self._on_button_load_clicked)
        self.button_save.clicked.connect(self._on_button_save_clicked)
        self.button_reset.clicked.connect(self._on_button_reset_clicked)
        self.button_about.clicked.connect(self._on_button_about_clicked)

    def initialize(self) -> None:
        self.tab_camera.initialize()
        self.tab_mms.initialize()
        self.tab_smtp.initialize()

    def SaveToFile(
        self,
        filename: str,
        data: bytes | bytearray | Iterable[int],
    ) -> None:
        save_file_dialog: QFileDialog = QFileDialog(self)
        save_file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        save_file_dialog.setNameFilters(("Dat file(*.DAT)", "All Files(*.*)"))
        save_file_dialog.setHistory([filename])
        save_file_dialog.selectFile(filename)
        if save_file_dialog.exec() == QFileDialog.DialogCode.Accepted:
            for selected_file in save_file_dialog.selectedFiles():
                try:
                    Path(selected_file).open("wb").write(bytes(data))
                except Exception as ex:
                    QMessageBox.warning(self, self.tr("Error"), str(ex))

    @Slot(bool)
    def _on_tab_mms_state_changed(self, on: bool) -> None:
        self.check_mms.setChecked(on)

    @Slot(bool)
    def _on_tab_smtp_state_changed(self, on: bool) -> None:
        self.check_smtp.setChecked(on)

    @Slot(bool)
    def _on_check_mms_toggled(self, on: bool) -> None:
        self.tab_mms.setEnabled(on)

    @Slot(bool)
    def _on_check_smtp_toggled(self, on: bool) -> None:
        self.tab_smtp.setEnabled(on)

    @Slot()
    def _on_button_load_clicked(self) -> None:
        open_file_dialog: QFileDialog = QFileDialog(self)
        open_file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
        open_file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        open_file_dialog.setNameFilters(("Dat file(*.DAT)", "All Files(*.*)"))
        if open_file_dialog.exec() != QFileDialog.DialogCode.Accepted:
            return
        for selected_file in open_file_dialog.selectedFiles():
            try:
                array: bytes = Path(selected_file).open("rb").read()
            except Exception as ex:
                QMessageBox.warning(self, self.tr("Error"), str(ex))
            else:
                if len(array) != 1808:
                    QMessageBox.warning(
                        self,
                        self.tr("Error"),
                        self.tr("File has been damaged!"),
                    )
                    return
                self.tab_camera.data = array[0:80]
                self.tab_mms.data = array[80 : 960 + 80]
                self.tab_smtp.data = array[1040 : 1040 + 768]

    @Slot()
    def _on_button_save_clicked(self) -> None:
        self.SaveToFile(
            "Parameter.dat",
            self.tab_camera.data + self.tab_mms.data + self.tab_smtp.data,
        )

    @Slot()
    def _on_button_reset_clicked(self) -> None:
        match self.tabs.currentWidget():
            case self.tab_camera:
                self.tab_camera.initialize()
            case self.tab_mms:
                self.tab_mms.initialize()
            case self.tab_smtp:
                self.tab_smtp.initialize()

    @Slot()
    def _on_button_about_clicked(self) -> None:
        QMessageBox.about(
            self,
            self.tr("About"),
            self.tr(
                "A replica of MMS CONFIG 2.5.0.0 by Suntek International Co., ltd."
            ),
        )
        QMessageBox.aboutQt(self)
