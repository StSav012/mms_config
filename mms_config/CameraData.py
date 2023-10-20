# coding=utf-8

from typing import Iterable

__all__ = ["CameraData"]


class CameraData:
    def __init__(
        self,
        data: bytes | bytearray | Iterable[int] | None = None,
        *,
        Mode: int = 0,
        CameraResolution: int = 0,
        Interval: int = 0,
        Multi: int = 0,
        ISO: int = 0,
        CameraID: bytes | bytearray | Iterable[int] = bytes(11),
        VideoResolution: int = 0,
        VideoLength: int = 0,
        Voice: int = 0,
        DateTime: bytes | bytearray | Iterable[int] = bytes(6),
        DateFormat: int = 0,
        Distance: int = 0,
        Language: int = 0,
        Timer1: bytes | bytearray | Iterable[int] = bytes(7),
        Timer2: bytes | bytearray | Iterable[int] = bytes(7),
        Timer3: bytes | bytearray | Iterable[int] = bytes(7),
        TimerLapse: bytes | bytearray | Iterable[int] = bytes(12),
        TVMode: int = 0,
        PasswordSwitch: int = 0,
        PasswordInfor: bytes | bytearray | Iterable[int] = bytes(4),
    ) -> None:
        self._mode: int = Mode
        self._camera_resolution: int = CameraResolution
        self._interval: int = Interval
        self._multi: int = Multi
        self._iso: int = ISO
        self._camera_id: bytearray = bytearray(CameraID)[:11].ljust(11, b"\0")
        self._video_resolution: int = VideoResolution
        self._video_length: int = VideoLength
        self._voice: int = Voice
        self._date_time: bytearray = bytearray(DateTime)[:6].ljust(6, b"\0")
        self._time_struct: int = DateFormat
        self._distance: int = Distance
        self._language: int = Language
        self._timer1: bytearray = bytearray(Timer1)[:7].ljust(7, b"\0")
        self._timer2: bytearray = bytearray(Timer2)[:7].ljust(7, b"\0")
        self._timer3: bytearray = bytearray(Timer3)[:7].ljust(7, b"\0")
        self._timer_lapse: bytearray = bytearray(TimerLapse)[:12].ljust(12, b"\0")
        self._tv_mode: int = TVMode
        self._password_switch: int = PasswordSwitch
        self._password_infor: bytearray = bytearray(PasswordInfor)[:4].ljust(4, b"\0")

        if data is not None:
            self.data = data

    @property
    def Mode(self) -> int:
        return self._mode

    @Mode.setter
    def Mode(self, value: int) -> None:
        self._mode = value

    @property
    def CameraResolution(self) -> int:
        return self._camera_resolution

    @CameraResolution.setter
    def CameraResolution(self, value: int) -> None:
        self._camera_resolution = value

    @property
    def Interval(self) -> int:
        return self._interval

    @Interval.setter
    def Interval(self, value: int) -> None:
        self._interval = value

    @property
    def Multi(self) -> int:
        return self._multi

    @Multi.setter
    def Multi(self, value: int) -> None:
        self._multi = value

    @property
    def ISO(self) -> int:
        return self._iso

    @ISO.setter
    def ISO(self, value: int) -> None:
        self._iso = value

    @property
    def CameraID(self) -> bytearray:
        return self._camera_id

    @CameraID.setter
    def CameraID(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._camera_id = bytearray(value).ljust(11, b"\0")[:11]

    @property
    def VideoResolution(self) -> int:
        return self._video_resolution

    @VideoResolution.setter
    def VideoResolution(self, value: int) -> None:
        self._video_resolution = value

    @property
    def VideoLength(self) -> int:
        return self._video_length

    @VideoLength.setter
    def VideoLength(self, value: int) -> None:
        self._video_length = value

    @property
    def Voice(self) -> int:
        return self._voice

    @Voice.setter
    def Voice(self, value: int) -> None:
        self._voice = value

    @property
    def DateTime(self) -> bytearray:
        return self._date_time

    @DateTime.setter
    def DateTime(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._date_time = bytearray(value).ljust(6, b"\0")[:6]

    @property
    def Timer1(self) -> bytearray:
        return self._timer1

    @Timer1.setter
    def Timer1(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._timer1 = bytearray(value).ljust(7, b"\0")[:7]

    @property
    def Timer2(self) -> bytearray:
        return self._timer2

    @Timer2.setter
    def Timer2(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._timer2 = bytearray(value).ljust(7, b"\0")[:7]

    @property
    def Timer3(self) -> bytearray:
        return self._timer3

    @Timer3.setter
    def Timer3(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._timer3 = bytearray(value).ljust(7, b"\0")[:7]

    @property
    def TimerLapse(self) -> bytearray:
        return self._timer_lapse

    @TimerLapse.setter
    def TimerLapse(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._timer_lapse = bytearray(value).ljust(12, b"\0")[:12]

    @property
    def DateFormat(self) -> int:
        return self._time_struct

    @DateFormat.setter
    def DateFormat(self, value: int) -> None:
        self._time_struct = value

    @property
    def Distance(self) -> int:
        return self._distance

    @Distance.setter
    def Distance(self, value: int) -> None:
        self._distance = value

    @property
    def Language(self) -> int:
        return self._language

    @Language.setter
    def Language(self, value: int) -> None:
        self._language = value

    @property
    def TVMode(self) -> int:
        return self._tv_mode

    @TVMode.setter
    def TVMode(self, value: int) -> None:
        self._tv_mode = value

    @property
    def PasswordSwitch(self) -> int:
        return self._password_switch

    @PasswordSwitch.setter
    def PasswordSwitch(self, value: int) -> None:
        self._password_switch = value

    @property
    def PasswordInfor(self) -> bytearray:
        return self._password_infor

    @PasswordInfor.setter
    def PasswordInfor(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._password_infor = bytearray(value).ljust(4, b"\0")[:4]

    @property
    def data(self) -> bytearray:
        array: bytearray = bytearray(80)
        array[0] = self._mode
        array[1] = self._camera_resolution
        array[2] = self._interval
        array[3] = self._multi
        array[4] = self._iso
        array[5:16] = self._camera_id
        array[16] = self._video_resolution
        array[17] = self._video_length
        array[18] = self._voice
        array[32:38] = self._date_time
        array[38] = self._time_struct
        array[39] = self._distance
        array[40] = self._language
        array[41:48] = self._timer1
        array[48:55] = self._timer2
        array[55:62] = self._timer3
        array[62:74] = self._timer_lapse
        array[74] = self._tv_mode
        array[75] = self._password_switch
        array[76:80] = self._password_infor
        return array

    @data.setter
    def data(self, data: bytes | bytearray | Iterable[int]) -> None:
        self._mode = data[0]
        self._camera_resolution = data[1]
        self._interval = data[2]
        self._multi = data[3]
        self._iso = data[4]
        self._camera_id = data[5:16]
        self._video_resolution = data[16]
        self._video_length = data[17]
        self._voice = data[18]
        self._date_time = data[32:38]
        self._time_struct = data[38]
        self._distance = data[39]
        self._language = data[40]
        self._timer1 = data[41:48]
        self._timer2 = data[48:55]
        self._timer3 = data[55:62]
        self._timer_lapse = data[62:74]
        self._tv_mode = data[74]
        self._password_switch = data[75]
        self._password_infor = data[76:80]
