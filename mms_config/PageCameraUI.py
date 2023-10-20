# coding=utf-8
from typing import Iterable

from qtpy.QtCore import (
    QDateTime,
    QLocale,
    QTime,
    QTimer,
    Slot,
)
from qtpy.QtWidgets import (
    QComboBox,
    QDateTimeEdit,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QWidget,
)

from .CameraData import CameraData
from .GroupBox import FormGroupBox, GridGroupBox
from .MyselfClass import GetSystemDateTime

__all__ = ["PageCamera"]


class PageCamera(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.timerDisplayDateTime: QTimer = QTimer(self)
        self.cbTimerLapseStatus: QComboBox = QComboBox(self)
        self.cbTimerStatus3: QComboBox = QComboBox(self)
        self.cbTimerStatus2: QComboBox = QComboBox(self)
        self.cbTimerStatus1: QComboBox = QComboBox(self)
        self.dtOpen2: QDateTimeEdit = QDateTimeEdit(self)
        self.dtOpen3: QDateTimeEdit = QDateTimeEdit(self)
        self.dtClose2: QDateTimeEdit = QDateTimeEdit(self)
        self.dtTimerLapse: QDateTimeEdit = QDateTimeEdit(self)
        self.dtClose3: QDateTimeEdit = QDateTimeEdit(self)
        self.dtClose1: QDateTimeEdit = QDateTimeEdit(self)
        self.dtOpen1: QDateTimeEdit = QDateTimeEdit(self)
        self.cbPassword: QComboBox = QComboBox(self)
        self.mtbPassword: QLineEdit = QLineEdit(self)
        self.cbDateFormat: QComboBox = QComboBox(self)
        self.cbTvMode: QComboBox = QComboBox(self)
        self.cbDistance: QComboBox = QComboBox(self)
        self.cbLanguage: QComboBox = QComboBox(self)
        self.cbMode: QComboBox = QComboBox(self)
        self.cbDateTime: QLabel = QLabel(self)
        self.tbID: QLineEdit = QLineEdit(self)
        self.cbISO: QComboBox = QComboBox(self)
        self.cbMulti: QComboBox = QComboBox(self)
        self.cbCameraResolution: QComboBox = QComboBox(self)
        self.cbDelay: QComboBox = QComboBox(self)
        self.cbVoice: QComboBox = QComboBox(self)
        self.cbVideoLength: QComboBox = QComboBox(self)
        self.cbVideoResolution: QComboBox = QComboBox(self)

        self._setup_ui()

    def _setup_ui(self) -> None:
        group_camera: FormGroupBox = FormGroupBox(self.tr("Camera"), self)
        group_camera.addRow(self.tr("ID:"), self.tbID)
        group_camera.addRow(self.tr("ISO:"), self.cbISO)
        group_camera.addRow(self.tr("Multi:"), self.cbMulti)
        group_camera.addRow(self.tr("Resolution:"), self.cbCameraResolution)
        group_camera.addRow(self.tr("Interval:"), self.cbDelay)

        group_video: FormGroupBox = FormGroupBox(self.tr("Video"), self)
        group_video.addRow(self.tr("Voice:"), self.cbVoice)
        group_video.addRow(self.tr("Video Length:"), self.cbVideoLength)
        group_video.addRow(self.tr("Resolution:"), self.cbVideoResolution)

        group_setup: FormGroupBox = FormGroupBox(self.tr("Setup"), self)
        group_setup.addRow(self.tr("Mode:"), self.cbMode)
        group_setup.addRow(self.tr("Language:"), self.cbLanguage)
        group_setup.addRow(self.tr("Motion Detection:"), self.cbDistance)
        group_setup.addRow(self.tr("TV Mode:"), self.cbTvMode)
        group_setup.addRow(self.tr("Date/Time:"), self.cbDateTime)
        group_setup.addRow(self.tr("Date Format:"), self.cbDateFormat)
        group_setup.addRow(self.tr("Password ON/OFF:"), self.cbPassword)
        group_setup.addRow(self.tr("Password:"), self.mtbPassword)

        group_timers: GridGroupBox = GridGroupBox(self.tr("Timers"), self)
        group_timers.addRow(
            (
                QLabel(self.tr("Timer"), self),
                QLabel(self.tr("Status"), self),
                QLabel(self.tr("Start Time"), self),
                QLabel(self.tr("End Time"), self),
            )
        )
        group_timers.addRow(
            (
                QLabel(self.tr("Timer 1:"), self),
                self.cbTimerStatus1,
                self.dtOpen1,
                self.dtClose1,
            )
        )
        group_timers.addRow(
            (
                QLabel(self.tr("Timer 2:"), self),
                self.cbTimerStatus2,
                self.dtOpen2,
                self.dtClose2,
            )
        )
        group_timers.addRow(
            (
                QLabel(self.tr("Timer 3:"), self),
                self.cbTimerStatus3,
                self.dtOpen3,
                self.dtClose3,
            )
        )
        group_timers.addRow(
            (
                QLabel(self.tr("Timer Lapse:"), self),
                self.cbTimerLapseStatus,
                self.dtTimerLapse,
            )
        )

        layout: QGridLayout = QGridLayout(self)
        layout.addWidget(group_camera, 0, 0)
        layout.addWidget(group_video, 1, 0)
        layout.addWidget(group_setup, 0, 1, 2, 1)
        layout.addWidget(group_timers, 2, 0, 1, 2)

        self.cbTimerLapseStatus.addItems([self.tr("OFF"), self.tr("ON")])
        self.cbTimerStatus1.addItems([self.tr("OFF"), self.tr("ON")])
        self.cbTimerStatus2.addItems([self.tr("OFF"), self.tr("ON")])
        self.cbTimerStatus3.addItems([self.tr("OFF"), self.tr("ON")])
        self.cbISO.addItems(
            [
                self.tr("Auto"),
                self.tr("100"),
                self.tr("200"),
                self.tr("400"),
            ]
        )
        self.cbMulti.addItems(
            [
                self.tr("Single"),
                self.tr("3 Pictures"),
                self.tr("6 Pictures"),
                self.tr("9 Pictures"),
            ]
        )
        self.cbCameraResolution.addItems(
            [
                self.tr("8M"),
                self.tr("5M"),
                self.tr("3M"),
            ]
        )
        self.cbDelay.addItems(
            [
                self.tr("1  Second"),
                self.tr("5  Seconds"),
                self.tr("10 Seconds"),
                self.tr("30 Seconds"),
                self.tr("1  Minutes"),
                self.tr("2  Minutes"),
                self.tr("5  Minutes"),
                self.tr("10 Minutes"),
                self.tr("30 Minutes"),
            ]
        )
        self.cbVoice.addItems([self.tr("OFF"), self.tr("ON")])
        self.cbPassword.addItems([self.tr("OFF"), self.tr("ON")])
        self.cbVideoLength.addItems(
            [
                self.tr("10S"),
                self.tr("30S"),
                self.tr("60S"),
                self.tr("90S"),
            ]
        )
        self.cbVideoResolution.addItems(
            [
                self.tr("720P"),
                self.tr("WVGA"),
                self.tr("QVGA"),
            ]
        )
        self.cbMode.addItems(
            [
                self.tr("Camera"),
                self.tr("Video"),
                self.tr("Camera&Video"),
            ]
        )
        self.cbDistance.addItems(
            [
                self.tr("High"),
                self.tr("Normal"),
                self.tr("Low"),
            ]
        )
        self.cbLanguage.addItems(
            [
                QLocale(language).nativeLanguageName()
                for language in [
                    QLocale.Language.English,
                    QLocale.Language.French,
                    QLocale.Language.German,
                    QLocale.Language.Spanish,
                    QLocale.Language.Russian,
                    QLocale.Language.Danish,
                    QLocale.Language.Dutch,
                    QLocale.Language.Polish,
                    QLocale.Language.Portuguese,
                    QLocale.Language.Swedish,
                    QLocale.Language.Italian,
                    QLocale.Language.Finnish,
                ]
            ]
        )
        self.cbDateFormat.addItems(["yy/MM/dd", "dd/MM/yy", "MM/dd/yy"])
        self.cbTvMode.addItems([self.tr("NTSC"), self.tr("PAL")])

        self.dtOpen1.setDisplayFormat("HH:mm:ss")
        self.dtOpen2.setDisplayFormat("HH:mm:ss")
        self.dtOpen3.setDisplayFormat("HH:mm:ss")
        self.dtClose1.setDisplayFormat("HH:mm:ss")
        self.dtClose2.setDisplayFormat("HH:mm:ss")
        self.dtClose3.setDisplayFormat("HH:mm:ss")
        self.dtTimerLapse.setDisplayFormat("HH:mm:ss")

        self.tbID.setMaxLength(6)
        self.tbID.setText("CAM000")

        self.mtbPassword.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.mtbPassword.setText("0000")

        self.timerDisplayDateTime.setInterval(1000)
        self.timerDisplayDateTime.start()
        self.timerDisplayDateTime.timeout.connect(self._on_timeout)

    def initialize(self) -> None:
        self.cbMode.setCurrentIndex(0)
        self.cbCameraResolution.setCurrentIndex(0)
        self.cbDelay.setCurrentIndex(0)
        self.cbMulti.setCurrentIndex(0)
        self.cbISO.setCurrentIndex(0)
        self.tbID.setText("CAM000")
        self.cbVideoResolution.setCurrentIndex(0)
        self.cbVideoLength.setCurrentIndex(0)
        self.cbVoice.setCurrentIndex(1)
        self.cbDateFormat.setCurrentIndex(1)
        self.cbDistance.setCurrentIndex(0)
        self.cbLanguage.setCurrentIndex(0)
        self.cbTvMode.setCurrentIndex(0)
        self.cbPassword.setCurrentIndex(0)
        self.cbTimerStatus1.setCurrentIndex(1)
        self.cbTimerStatus2.setCurrentIndex(0)
        self.cbTimerStatus3.setCurrentIndex(0)
        self.cbTimerLapseStatus.setCurrentIndex(0)
        self.dtOpen1.setDateTime(QDateTime(2013, 1, 1, 0, 0, 0))
        self.dtOpen2.setDateTime(QDateTime(2013, 1, 1, 0, 0, 0))
        self.dtOpen3.setDateTime(QDateTime(2013, 1, 1, 0, 0, 0))
        self.dtClose1.setDateTime(QDateTime(2013, 1, 1, 23, 59, 59))
        self.dtClose2.setDateTime(QDateTime(2013, 1, 1, 23, 59, 59))
        self.dtClose3.setDateTime(QDateTime(2013, 1, 1, 23, 59, 59))
        self.dtTimerLapse.setDateTime(QDateTime(2013, 1, 1, 1, 0, 0))
        self.mtbPassword.setText("0000")

    @Slot()
    def _on_timeout(self) -> None:
        self.cbDateTime.setText(
            QDateTime.currentDateTime().toString(
                " ".join(
                    (
                        self.cbDateFormat.currentText(),
                        "HH:mm:ss",
                    )
                )
            )
        )

    @property
    def data(self) -> bytearray:
        return CameraData(
            Mode=self.cbMode.currentIndex(),
            CameraResolution=self.cbCameraResolution.currentIndex(),
            Interval=self.cbDelay.currentIndex(),
            Multi=self.cbMulti.currentIndex(),
            ISO=self.cbISO.currentIndex(),
            CameraID=self.tbID.text().encode(),
            VideoResolution=self.cbVideoResolution.currentIndex(),
            VideoLength=self.cbVideoLength.currentIndex(),
            Voice=self.cbVoice.currentIndex(),
            DateTime=(GetSystemDateTime()),
            DateFormat=self.cbDateFormat.currentIndex(),
            Distance=self.cbDistance.currentIndex(),
            Language=self.cbLanguage.currentIndex(),
            Timer1=[
                self.cbTimerStatus1.currentIndex(),
                self.dtOpen1.time().hour(),
                self.dtOpen1.time().minute(),
                self.dtOpen1.time().second(),
                self.dtClose1.time().hour(),
                self.dtClose1.time().minute(),
                self.dtClose1.time().second(),
            ],
            Timer2=[
                self.cbTimerStatus2.currentIndex(),
                self.dtOpen2.time().hour(),
                self.dtOpen2.time().minute(),
                self.dtOpen2.time().second(),
                self.dtClose2.time().hour(),
                self.dtClose2.time().minute(),
                self.dtClose2.time().second(),
            ],
            Timer3=[
                self.cbTimerStatus3.currentIndex(),
                self.dtOpen3.time().hour(),
                self.dtOpen3.time().minute(),
                self.dtOpen3.time().second(),
                self.dtClose3.time().hour(),
                self.dtClose3.time().minute(),
                self.dtClose3.time().second(),
            ],
            TimerLapse=[
                self.cbTimerLapseStatus.currentIndex(),
                self.dtTimerLapse.time().hour(),
                self.dtTimerLapse.time().minute(),
                self.dtTimerLapse.time().second(),
            ],
            TVMode=self.cbTvMode.currentIndex(),
            PasswordSwitch=self.cbPassword.currentIndex(),
            PasswordInfor=map(
                lambda x: max(48, x),
                self.mtbPassword.text().encode(),
            ),
        ).data

    @data.setter
    def data(self, data: CameraData | bytes | bytearray | Iterable[int]) -> None:
        try:
            if not isinstance(data, CameraData):
                data = CameraData(data)
            self.cbMode.setCurrentIndex(data.Mode)
            self.cbCameraResolution.setCurrentIndex(data.CameraResolution)
            self.cbDelay.setCurrentIndex(data.Interval)
            self.cbMulti.setCurrentIndex(data.Multi)
            self.cbISO.setCurrentIndex(data.ISO)
            self.tbID.setText(data.CameraID.decode())
            if not data.CameraID:
                self.tbID.setText("CAM000")
            self.cbVideoResolution.setCurrentIndex(data.VideoResolution)
            self.cbVideoLength.setCurrentIndex(data.VideoLength)
            self.cbVoice.setCurrentIndex(data.Voice)
            self.cbDateFormat.setCurrentIndex(data.DateFormat)
            self.cbDistance.setCurrentIndex(data.Distance)
            self.cbLanguage.setCurrentIndex(data.Language)
            timer: bytearray = data.Timer1
            self.cbTimerStatus1.setCurrentIndex(timer[0])
            self.dtOpen1.setTime(QTime(timer[1], timer[2], timer[3]))
            self.dtClose1.setTime(QTime(timer[4], timer[5], timer[6]))
            timer2: bytearray = data.Timer2
            self.cbTimerStatus2.setCurrentIndex(timer2[0])
            self.dtOpen2.setTime(QTime(timer2[1], timer2[2], timer2[3]))
            self.dtClose2.setTime(QTime(timer2[4], timer2[5], timer2[6]))
            timer3: bytearray = data.Timer3
            self.cbTimerStatus3.setCurrentIndex(timer3[0])
            self.dtOpen3.setTime(QTime(timer3[1], timer3[2], timer3[3]))
            self.dtClose3.setTime(QTime(timer3[4], timer3[5], timer3[6]))
            timer_lapse: bytearray = data.TimerLapse
            self.cbTimerLapseStatus.setCurrentIndex(timer_lapse[0])
            self.dtTimerLapse.setTime(
                QTime(timer_lapse[1], timer_lapse[2], timer_lapse[3])
            )
            self.cbTvMode.setCurrentIndex(data.TVMode)
            self.cbPassword.setCurrentIndex(data.PasswordSwitch)
            self.mtbPassword.setText(data.PasswordInfor.decode())
        except Exception as ex:
            import traceback

            QMessageBox.warning(self, self.tr("Error"), str(ex))
            traceback.print_exception(ex)
