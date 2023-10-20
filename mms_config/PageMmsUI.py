# coding=utf-8
from contextlib import suppress
from pathlib import Path
from typing import ClassVar, Iterable

from qtpy.QtCore import (
    QXmlStreamReader,
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

from .GroupBox import FormGroupBox
from .MmsData import MmsData
from .MmscCountryData import MmscCountryData
from .MmscOperatorData import MmscOperatorData
from .OperatorBinaryFile import OperatorBinaryFile

__all__ = ["PageMms"]


class PageMms(QWidget):
    stateChanged: ClassVar[Signal] = Signal(bool)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.country_data: list[MmscCountryData] = []

        self.cbMode: QComboBox = QComboBox(self)
        self.cbCountry: QComboBox = QComboBox(self)
        self.cbOperator: QComboBox = QComboBox(self)
        self.spinPictureNum: QSpinBox = QSpinBox(self)
        self.tbGprsApn: QLineEdit = QLineEdit(self)
        self.tbGprsAccount: QLineEdit = QLineEdit(self)
        self.tbGprsPassword: QLineEdit = QLineEdit(self)
        self.tbMmsc: QLineEdit = QLineEdit(self)
        self.tbMmscIp: QLineEdit = QLineEdit(self)
        self.tbMmscPort: QLineEdit = QLineEdit(self)
        self.tbPhone1: QLineEdit = QLineEdit(self)
        self.tbPhone2: QLineEdit = QLineEdit(self)
        self.tbPhone3: QLineEdit = QLineEdit(self)
        self.tbPhone4: QLineEdit = QLineEdit(self)
        self.tbEmail1: QLineEdit = QLineEdit(self)
        self.tbEmail2: QLineEdit = QLineEdit(self)
        self.tbEmail3: QLineEdit = QLineEdit(self)
        self.tbEmail4: QLineEdit = QLineEdit(self)

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

        group_server: FormGroupBox = FormGroupBox(self.tr("Server"), self)
        group_server.addRow(self.tr("MMSC:"), self.tbMmsc)
        group_server.addRow(self.tr("IP:"), self.tbMmscIp)
        group_server.addRow(self.tr("Port:"), self.tbMmscPort)

        group_phone: FormGroupBox = FormGroupBox(self.tr("Phone"), self)
        group_phone.addRow(self.tr("1:"), self.tbPhone1)
        group_phone.addRow(self.tr("2:"), self.tbPhone2)
        group_phone.addRow(self.tr("3:"), self.tbPhone3)
        group_phone.addRow(self.tr("4:"), self.tbPhone4)

        group_email: FormGroupBox = FormGroupBox(self.tr("E-mail"), self)
        group_email.addRow(self.tr("1:"), self.tbEmail1)
        group_email.addRow(self.tr("2:"), self.tbEmail2)
        group_email.addRow(self.tr("3:"), self.tbEmail3)
        group_email.addRow(self.tr("4:"), self.tbEmail4)

        layout: QGridLayout = QGridLayout(self)
        layout.addWidget(group_general, 0, 0)
        layout.addWidget(group_gprs, 1, 0)
        layout.addWidget(group_server, 2, 0)
        layout.addWidget(group_phone, 0, 1)
        layout.addWidget(group_email, 1, 1, 2, 1)

        self.cbMode.addItems([self.tr("Manual"), self.tr("Auto")])

        self.tbGprsApn.setMaxLength(64)
        self.tbGprsAccount.setMaxLength(64)
        self.tbGprsPassword.setMaxLength(64)
        self.tbMmsc.setMaxLength(64)
        self.tbMmscIp.setMaxLength(64)
        self.tbMmscPort.setMaxLength(64)
        self.tbPhone1.setMaxLength(64)
        self.tbPhone2.setMaxLength(64)
        self.tbPhone3.setMaxLength(64)
        self.tbPhone4.setMaxLength(64)

        self.cbOperator.currentIndexChanged.connect(
            self.cbMmsOperator_SelectedIndexChanged
        )
        self.cbMode.currentIndexChanged.connect(self.cbMmsMode_SelectedIndexChanged)
        self.cbCountry.currentIndexChanged.connect(
            self.cbMmsCountry_SelectedIndexChanged
        )

    def setEnabled(self, enabled: bool) -> None:
        if enabled != self.isEnabled():
            self.stateChanged.emit(enabled)
            super().setEnabled(enabled)

    def initialize(self) -> None:
        self.cbMode.setCurrentIndex(1)
        self.setEnabled(False)
        self.tbPhone1.clear()
        self.tbEmail1.clear()
        self.ReadMmsXmlFile()
        self.display_default_country_operator()
        self.spinPictureNum.setValue(99)

    @Slot(int)
    def cbMmsOperator_SelectedIndexChanged(self, _: int) -> None:
        self.display_default_operator_info()

    @Slot(int)
    def cbMmsMode_SelectedIndexChanged(self, index: int) -> None:
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
            self.tbMmsc.setEnabled(True)
            self.tbMmscIp.setEnabled(True)
            self.tbMmscPort.setEnabled(True)
            self.tbGprsApn.clear()
            self.tbGprsAccount.clear()
            self.tbGprsPassword.clear()
            return

        self.tbMmsc.setEnabled(False)
        self.tbMmscIp.setEnabled(False)
        self.tbMmscPort.setEnabled(False)
        self.tbGprsApn.clear()
        self.tbGprsAccount.clear()
        self.tbGprsPassword.clear()
        self.tbMmsc.clear()
        self.tbMmscIp.clear()
        self.tbMmscPort.clear()

        if self.country_data:
            self.cbCountry.clear()
            self.cbCountry.addItems([item.CountryName for item in self.country_data])
            self.cbCountry.setCurrentIndex(0)

            mmsc_country_data: MmscCountryData = self.country_data[0]
            if mmsc_country_data.Count > 0:
                self.cbOperator.clear()
                self.cbOperator.addItems(mmsc_country_data.GetOperatorNames())
                self.cbOperator.setCurrentIndex(0)

        self.display_default_operator_info()

    @Slot(int)
    def cbMmsCountry_SelectedIndexChanged(self, index: int) -> None:
        operator_names: list[str] = self.country_data[index].GetOperatorNames()
        if operator_names:
            self.cbOperator.clear()
            self.cbOperator.addItems(operator_names)
            self.cbOperator.setCurrentIndex(0)

    def display_default_country_operator(self) -> None:
        if not self.country_data:
            return

        self.cbCountry.clear()
        for item in self.country_data:
            self.cbCountry.addItem(item.CountryName)
        self.cbCountry.setCurrentIndex(0)

        mmsc_country_data: MmscCountryData = self.country_data[0]
        if mmsc_country_data.Count > 0:
            self.cbOperator.clear()
            self.cbOperator.addItems(mmsc_country_data.GetOperatorNames())
            self.cbOperator.setCurrentIndex(0)

    def display_default_operator_info(self) -> None:
        num: int = self.cbCountry.currentIndex()
        num2: int = self.cbOperator.currentIndex()
        if len(self.country_data) > num >= 0 and num2 >= 0:
            data: MmscOperatorData = self.country_data[num].GetOperatorData(num2)
            self.tbGprsApn.setText(data.APN)
            self.tbGprsAccount.setText(data.User)
            self.tbGprsPassword.setText(data.Password)
            self.tbMmsc.setText(data.MMSC)
            self.tbMmscIp.setText(data.IP)
            self.tbMmscPort.setText(data.Port)

    def ReadMmsXmlFile(self) -> None:
        xml_document: QXmlStreamReader = QXmlStreamReader()
        self.country_data.clear()
        db_path: Path = Path(__file__).parent / "MMSDB.DB"
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

                        country_data: MmscCountryData = MmscCountryData(
                            xml_document.attributes().at(0).value()
                        )
                        while xml_document.readNextStartElement():
                            if xml_document.name() != "Operator":
                                xml_document.skipCurrentElement()
                                continue
                            operator_data: MmscOperatorData = MmscOperatorData()
                            while xml_document.readNextStartElement():
                                name: str = xml_document.name()
                                if hasattr(operator_data, name):
                                    setattr(
                                        operator_data,
                                        name,
                                        xml_document.readElementText(),
                                    )
                            country_data.Add(operator_data)
                        self.country_data.append(country_data)

        self.country_data.sort()

        self.SaveXmlFileToBinaryFile(Path.cwd())

    def SaveXmlFileToBinaryFile(self, path: Path) -> None:
        data: MmscCountryData
        if not self.country_data:
            return
        with suppress(Exception):
            with open(path / "MMSOp.dat", "wb") as f_out:
                for data in self.country_data:
                    for i in range(data.Count):
                        f_out.write(
                            OperatorBinaryFile(
                                data.CountryName,
                                data.GetOperatorData(i),
                            ).GetMmsData()
                        )

    @property
    def data(self) -> bytearray:
        return MmsData(
            GSM=[
                self.cbMode.currentIndex(),
                int(self.isEnabled()),
                self.spinPictureNum.value(),
                *self.cbCountry.currentText().encode()[:16].ljust(16, b"\0"),
                *self.cbOperator.currentText().encode()[:16].ljust(16, b"\0"),
            ],
            APN=self.tbGprsApn.text().encode(),
            Account=self.tbGprsAccount.text().encode(),
            MMSC=self.tbMmsc.text().encode(),
            Password=self.tbGprsPassword.text().encode(),
            IP=self.tbMmscIp.text().encode(),
            Port=self.tbMmscPort.text().encode(),
            Phone1=self.tbPhone1.text().encode(),
            Phone2=self.tbPhone2.text().encode(),
            Phone3=self.tbPhone3.text().encode(),
            Phone4=self.tbPhone4.text().encode(),
            Email1=self.tbEmail1.text().encode(),
            Email2=self.tbEmail2.text().encode(),
            Email3=self.tbEmail3.text().encode(),
            Email4=self.tbEmail4.text().encode(),
        ).data

    @data.setter
    def data(self, data: MmsData | bytes | bytearray | Iterable[int]) -> None:
        try:
            if not isinstance(data, MmsData):
                data = MmsData(data)
            gsm: bytearray = data.GSM
            self.setEnabled(bool(gsm[1]))
            self.cbMode.setCurrentIndex(gsm[0])
            self.spinPictureNum.setValue(gsm[2])
            self.tbGprsApn.setText(data.APN.decode())
            self.tbGprsAccount.setText(data.Account.decode())
            self.tbGprsPassword.setText(data.Password.decode())
            self.tbMmsc.setText(data.MMSC.decode())
            self.tbMmscIp.setText(data.IP.decode())
            self.tbMmscPort.setText(data.Port.decode())
            text: str = gsm[3 : 16 + 3].decode()
            value: str = gsm[19 : 16 + 19].decode()
            num: int = self.cbCountry.findText(text)
            if text != "Other" and 0 <= num < len(self.country_data):
                self.cbCountry.setCurrentIndex(num)
                operator_name: list[str] = self.country_data[num].GetOperatorNames()
                if operator_name and self.cbCountry.count() > 0:
                    self.cbOperator.clear()
                    self.cbOperator.addItems(operator_name)
                    if (num := self.cbOperator.findText(value)) != -1:
                        self.cbOperator.setCurrentIndex(num)
                    else:
                        self.cbOperator.setCurrentIndex(0)
            self.tbPhone1.setText(data.Phone1.decode())
            self.tbPhone2.setText(data.Phone2.decode())
            self.tbPhone3.setText(data.Phone3.decode())
            self.tbPhone4.setText(data.Phone4.decode())
            self.tbEmail1.setText(data.Email1.decode())
            self.tbEmail2.setText(data.Email2.decode())
            self.tbEmail3.setText(data.Email3.decode())
            self.tbEmail4.setText(data.Email4.decode())
        except Exception as ex:
            import traceback

            QMessageBox.warning(self, self.tr("Error"), str(ex))
            traceback.print_exception(ex)
