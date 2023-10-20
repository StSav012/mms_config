# coding=utf-8
from contextlib import suppress
from pathlib import Path
from typing import ClassVar, Iterable

from qtpy.QtCore import (
    QXmlStreamReader,
    Qt,
    Signal,
    Slot,
)
from qtpy.QtWidgets import (
    QComboBox,
    QGridLayout,
    QLineEdit,
    QMessageBox,
    QSpinBox,
    QWidget,
)

from .EmailServerData import EmailServerData
from .GroupBox import FormGroupBox
from .OperatorBinaryFile import OperatorBinaryFile
from .SmtpCountryData import SmtpCountryData
from .SmtpData import SmtpData
from .SmtpOperatorData import SmtpOperatorData

__all__ = ["PageSmtp"]


class PageSmtp(QWidget):
    stateChanged: ClassVar[Signal] = Signal(bool)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.country_data: list[SmtpCountryData] = []
        self.email_server_data: list[EmailServerData] = []

        self.cbMode: QComboBox = QComboBox(self)
        self.cbCountry: QComboBox = QComboBox(self)
        self.cbOperator: QComboBox = QComboBox(self)
        self.spinPictureNum: QSpinBox = QSpinBox(self)
        self.tbGprsApn: QLineEdit = QLineEdit(self)
        self.tbGprsAccount: QLineEdit = QLineEdit(self)
        self.tbGprsPassword: QLineEdit = QLineEdit(self)
        self.cbEmailSSL: QComboBox = QComboBox(self)
        self.cbEmailType: QComboBox = QComboBox(self)
        self.tbEmailPassword: QLineEdit = QLineEdit(self)
        self.tbEmailAccount: QLineEdit = QLineEdit(self)
        self.tbEmailPort: QLineEdit = QLineEdit(self)
        self.tbEmailServer: QLineEdit = QLineEdit(self)
        self.tbEmail4: QLineEdit = QLineEdit(self)
        self.tbEmail3: QLineEdit = QLineEdit(self)
        self.tbEmail2: QLineEdit = QLineEdit(self)
        self.tbEmail1: QLineEdit = QLineEdit(self)

        self._setup_ui()

    def _setup_ui(self) -> None:
        group_general: FormGroupBox = FormGroupBox(self.tr("Settings"), self)
        group_general.addRow(self.tr("Mode:"), self.cbMode)
        group_general.addRow(self.tr("Country:"), self.cbCountry)
        group_general.addRow(self.tr("Operator:"), self.cbOperator)
        group_general.addRow(self.tr("Picture No./day:"), self.spinPictureNum)

        group_gprs: FormGroupBox = FormGroupBox(self.tr("GPRS"), self)
        group_gprs.addRow(self.tr("APN:"), self.tbGprsApn)
        group_gprs.addRow(self.tr("Account:"), self.tbGprsAccount)
        group_gprs.addRow(self.tr("Password:"), self.tbGprsPassword)

        group_server: FormGroupBox = FormGroupBox(self.tr("E-mail"), self)
        group_server.addRow(self.tr("SSL:"), self.cbEmailSSL)
        group_server.addRow(self.tr("Type:"), self.cbEmailType)
        group_server.addRow(self.tr("Server:"), self.tbEmailServer)
        group_server.addRow(self.tr("Account:"), self.tbEmailAccount)
        group_server.addRow(self.tr("Password:"), self.tbEmailPassword)
        group_server.addRow(self.tr("Port:"), self.tbEmailPort)

        group_email: FormGroupBox = FormGroupBox(self.tr("E-mail Recipients"), self)
        group_email.addRow(self.tr("1:"), self.tbEmail1)
        group_email.addRow(self.tr("2:"), self.tbEmail2)
        group_email.addRow(self.tr("3:"), self.tbEmail3)
        group_email.addRow(self.tr("4:"), self.tbEmail4)

        layout: QGridLayout = QGridLayout(self)
        layout.addWidget(group_general, 0, 0)
        layout.addWidget(group_gprs, 0, 1)
        layout.addWidget(group_server, 1, 0)
        layout.addWidget(group_email, 1, 1)

        self.cbMode.addItems([self.tr("Manual"), self.tr("Auto")])
        self.cbEmailType.addItems(
            [
                self.tr("Other"),
                self.tr("Gmail"),
                self.tr("Hotmail"),
            ]
        )
        self.cbEmailSSL.addItems(
            [
                self.tr("No SSL"),
                self.tr("SSL"),
                self.tr("STARTTLS"),
            ]
        )

        self.tbEmailAccount.setMaxLength(64)
        self.tbEmailPassword.setMaxLength(64)
        self.tbEmailServer.setMaxLength(64)
        self.tbEmailPort.setMaxLength(64)
        self.tbEmail1.setMaxLength(64)
        self.tbEmail2.setMaxLength(64)
        self.tbEmail3.setMaxLength(64)
        self.tbEmail4.setMaxLength(64)

        self.cbOperator.currentIndexChanged.connect(
            self.cbSmtpOperator_SelectedIndexChanged
        )
        self.cbMode.currentIndexChanged.connect(self.cbSmtpMode_SelectedIndexChanged)
        self.cbCountry.currentIndexChanged.connect(
            self.cbSmtpCountry_SelectedIndexChanged
        )
        self.cbEmailType.currentIndexChanged.connect(
            self.cbSmtpType_SelectedIndexChanged
        )

    def setEnabled(self, enabled: bool) -> None:
        if enabled != self.isEnabled():
            self.stateChanged.emit(enabled)
            super().setEnabled(enabled)

    def initialize(self) -> None:
        self.tbEmail1.clear()
        self.cbMode.setCurrentIndex(1)
        self.setEnabled(False)
        self.cbEmailType.setCurrentIndex(0)
        self.cbEmailSSL.setCurrentIndex(0)
        self.spinPictureNum.setValue(99)
        self.ReadSmtpXmlFile()
        self.ReadSmtpEmailServerXmlFile()
        self.display_default_country_operator()
        self.display_default_email_server()
        self.tbEmail2.setEnabled(False)
        self.tbEmail3.setEnabled(False)
        self.tbEmail4.setEnabled(False)

    @Slot(int)
    def cbSmtpOperator_SelectedIndexChanged(self, _: int) -> None:
        self.display_default_operator_info()

    @Slot(int)
    def cbSmtpMode_SelectedIndexChanged(self, index: int) -> None:
        if not index:
            self.cbCountry.clear()
            self.cbCountry.addItem(self.tr("Other"))
            self.cbCountry.setCurrentIndex(0)
            self.cbOperator.clear()
            self.cbOperator.addItem(self.tr("Other"))
            self.cbOperator.setCurrentIndex(0)
            self.tbGprsApn.setEnabled(True)
            self.tbGprsAccount.setEnabled(True)
            self.tbGprsPassword.setEnabled(True)
            self.tbEmailServer.setEnabled(True)
            self.tbEmailPort.setEnabled(True)
            self.tbEmailAccount.setEnabled(True)
            self.tbEmailPassword.setEnabled(True)
            self.tbGprsApn.clear()
            self.tbGprsAccount.clear()
            self.tbGprsPassword.clear()
            return

        self.tbGprsApn.setEnabled(False)
        self.tbGprsAccount.setEnabled(False)
        self.tbGprsPassword.setEnabled(False)
        self.cbCountry.setEnabled(True)
        self.cbOperator.setEnabled(True)

        if self.country_data:
            self.cbCountry.clear()
            self.cbCountry.addItems([item.CountryName for item in self.country_data])
            self.cbCountry.setCurrentIndex(0)

            smtp_country_data: SmtpCountryData = self.country_data[0]
            if smtp_country_data.count > 0:
                self.cbOperator.clear()
                self.cbOperator.addItems(smtp_country_data.get_operator_names())
                self.cbOperator.setCurrentIndex(0)

        self.display_default_operator_info()

    @Slot(int)
    def cbSmtpCountry_SelectedIndexChanged(self, index: int) -> None:
        operator_names: list[str] = self.country_data[index].get_operator_names()
        if operator_names:
            self.cbOperator.clear()
            self.cbOperator.addItems(operator_names)
            self.cbOperator.setCurrentIndex(0)

    @Slot(int)
    def cbSmtpType_SelectedIndexChanged(self, index: int) -> None:
        if not index:  # Type: “Other”
            self.cbEmailSSL.setEnabled(True)
            self.cbEmailSSL.setCurrentIndex(0)
            self.tbEmailServer.clear()
            self.tbEmailPort.clear()
            self.tbEmailServer.setEnabled(True)
            self.tbEmailPort.setEnabled(True)
            return

        self.cbEmailSSL.setEnabled(False)
        self.tbEmailServer.setEnabled(False)
        self.tbEmailPort.setEnabled(False)

        index -= 1  # skip the “Other”
        if index < len(self.email_server_data):
            data: EmailServerData = self.email_server_data[index]
            self.tbEmailServer.setText(data.Http)
            self.tbEmailPort.setText(data.Port)
            self.cbEmailSSL.setCurrentIndex(
                min(
                    0,
                    self.cbEmailSSL.findText(data.Kind, Qt.MatchFlag.MatchFixedString),
                )
            )

    def display_default_country_operator(self) -> None:
        if not self.country_data:
            return

        self.cbCountry.clear()
        for item in self.country_data:
            self.cbCountry.addItem(item.CountryName)
        self.cbCountry.setCurrentIndex(0)

        smtp_country_data: SmtpCountryData = self.country_data[0]
        if smtp_country_data.count > 0:
            self.cbOperator.clear()
            self.cbOperator.addItems(smtp_country_data.get_operator_names())
            self.cbOperator.setCurrentIndex(0)

    def display_default_email_server(self) -> None:
        if not self.email_server_data:
            return

        self.cbEmailType.clear()
        self.cbEmailType.addItem(self.tr("Other"))
        for item in self.email_server_data:
            self.cbEmailType.addItem(item.Name)
        self.cbEmailType.setCurrentIndex(0)

    def display_default_operator_info(self) -> None:
        num: int = self.cbCountry.currentIndex()
        num2: int = self.cbOperator.currentIndex()
        if len(self.country_data) > num >= 0 and num2 >= 0:
            data: SmtpOperatorData = self.country_data[num].get_operator_data(num2)
            self.tbGprsApn.setText(data.APN)
            self.tbGprsAccount.setText(data.Account)
            self.tbGprsPassword.setText(data.Password)
            self.tbEmailServer.setText(data.Server)
            self.tbEmailPort.setText(data.Port)
            self.tbEmailAccount.setText(data.Email)
            self.tbEmailPassword.setText(data.EmailPassword)

    def ReadSmtpXmlFile(self) -> None:
        xml_document: QXmlStreamReader = QXmlStreamReader()
        self.country_data.clear()
        db_path: Path = Path(__file__).parent / "SMTPDB.DB"
        try:
            if not db_path.exists():
                return
            xml_document.addData(db_path.read_text(encoding="utf-8"))
        except OSError as ex:
            QMessageBox.warning(self, self.tr("Error"), str(ex))
            return
        if xml_document.hasError():
            QMessageBox.warning(self, self.tr("Error"), xml_document.errorString())
            return

        if xml_document.readNextStartElement():
            if xml_document.name() == "Config" and xml_document.readNextStartElement():
                if xml_document.name() == "Item":
                    while xml_document.readNextStartElement():
                        if xml_document.name() != "Country":
                            xml_document.skipCurrentElement()
                            continue

                        country_data: SmtpCountryData = SmtpCountryData(
                            xml_document.attributes().at(0).value()
                        )
                        while xml_document.readNextStartElement():
                            if xml_document.name() != "Operator":
                                xml_document.skipCurrentElement()
                                continue
                            operator_data: SmtpOperatorData = SmtpOperatorData()
                            while xml_document.readNextStartElement():
                                name: str = xml_document.name()
                                if hasattr(operator_data, name):
                                    setattr(
                                        operator_data,
                                        name,
                                        xml_document.readElementText(),
                                    )
                            country_data.append(operator_data)
                        self.country_data.append(country_data)

        self.country_data.sort()

        self.SaveXmlFileToBinaryFile(Path.cwd())

    def ReadSmtpEmailServerXmlFile(self) -> None:
        xml_document: QXmlStreamReader = QXmlStreamReader()
        self.email_server_data.clear()
        try:
            if not Path("SMTPSERVER.DB").exists():
                return
            xml_document.addData(Path("SMTPSERVER.DB").read_text(encoding="utf-8"))
        except OSError as ex:
            QMessageBox.warning(self, self.tr("Error"), str(ex))
            return
        if xml_document.hasError():
            QMessageBox.warning(self, self.tr("Error"), xml_document.errorString())
            return

        if xml_document.readNextStartElement():
            if xml_document.name() == "Item":
                while xml_document.readNextStartElement():
                    if xml_document.name() != "SERVER":
                        xml_document.skipCurrentElement()
                        continue
                    item: EmailServerData | None = None
                    while xml_document.readNextStartElement():
                        item = EmailServerData()
                        if hasattr(item, xml_document.name()):
                            setattr(
                                item,
                                xml_document.name(),
                                xml_document.readElementText(),
                            )
                        xml_document.skipCurrentElement()
                    if item is not None:
                        self.email_server_data.append(item)

    def SaveXmlFileToBinaryFile(self, path: Path) -> None:
        data: SmtpCountryData
        if not self.country_data:
            return
        with suppress(Exception):
            with open(path / "SMTPOp.dat", "wb") as f_out:
                for data in self.country_data:
                    for i in range(data.count):
                        f_out.write(
                            OperatorBinaryFile(
                                data.CountryName,
                                data.get_operator_data(i),
                            ).GetSmtpData()
                        )

    @property
    def data(self) -> bytearray:
        array6: bytearray = bytearray(self.tbEmailPort.text().encode()).ljust(64, b"\0")
        array6[30] = self.cbEmailType.currentIndex()
        array6[31] = self.cbEmailSSL.currentIndex()
        return SmtpData(
            GSM=[
                self.cbMode.currentIndex(),
                int(self.isEnabled()),
                self.spinPictureNum.value(),
                *self.cbCountry.currentText().encode()[:16].ljust(16, b"\0"),
                *self.cbOperator.currentText().encode()[:16].ljust(16, b"\0"),
            ],
            GprsAPN=self.tbGprsApn.text().encode(),
            GprsAccount=self.tbGprsAccount.text().encode(),
            GprsPassword=self.tbGprsPassword.text().encode(),
            SmtpServer=self.tbEmailServer.text().encode(),
            SmtpPort=array6,
            SendEmail=self.tbEmailAccount.text().encode(),
            SendEmailPassword=self.tbEmailPassword.text().encode(),
            SmtpEmail1=self.tbEmail1.text().encode(),
            SmtpEmail2=self.tbEmail2.text().encode(),
            SmtpEmail3=self.tbEmail3.text().encode(),
            SmtpEmail4=self.tbEmail4.text().encode(),
        ).data

    @data.setter
    def data(self, data: SmtpData | bytes | bytearray | Iterable[int]) -> None:
        try:
            if not isinstance(data, SmtpData):
                data = SmtpData(data)
            gsm: bytearray = data.GSM
            self.setEnabled(bool(gsm[1]))
            self.cbMode.setCurrentIndex(gsm[0])
            self.spinPictureNum.setValue(gsm[2])
            self.tbGprsApn.setText(data.GprsAPN.decode())
            self.tbGprsAccount.setText(data.GprsAccount.decode())
            self.tbGprsPassword.setText(data.GprsPassword.decode())
            text: str = gsm[3 : 16 + 3].decode()
            value: str = gsm[19 : 16 + 19].decode()
            num: int = self.cbCountry.findText(text)
            if text != "Other" and 0 <= num < len(self.country_data):
                self.cbCountry.setCurrentIndex(num)
                operator_name: list[str] = self.country_data[num].get_operator_names()
                if operator_name and self.cbCountry.count() > 0:
                    self.cbOperator.clear()
                    self.cbOperator.addItems(operator_name)
                    if (num := self.cbOperator.findText(value)) != -1:
                        self.cbOperator.setCurrentIndex(num)
                    else:
                        self.cbOperator.setCurrentIndex(0)
            num2: int = data.SmtpPort[30]
            num3: int = data.SmtpPort[31]
            if 0 <= num2 < self.cbEmailType.count():
                self.cbEmailType.setCurrentIndex(num2)
            if 0 <= num3 <= self.cbEmailSSL.count():
                self.cbEmailSSL.setCurrentIndex(num3)
            self.tbEmailServer.setText(data.SmtpServer.decode())
            self.tbEmailPort.setText(data.SmtpPort.decode())
            self.tbEmailAccount.setText(data.SendEmail.decode())
            self.tbEmailPassword.setText(data.SendEmailPassword.decode())
            self.tbEmail1.setText(data.SmtpEmail1.decode())
            self.tbEmail2.setText(data.SmtpEmail2.decode())
            self.tbEmail3.setText(data.SmtpEmail3.decode())
            self.tbEmail4.setText(data.SmtpEmail4.decode())
        except Exception as ex:
            import traceback

            QMessageBox.warning(self, self.tr("Error"), str(ex))
            traceback.print_exception(ex)
