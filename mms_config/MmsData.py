# coding=utf-8

from typing import Iterable, Sequence

from .MyselfClass import DataEncryption

__all__ = ["MmsData"]


class MmsData:
    def __init__(
        self,
        data: bytes | bytearray | Iterable[int] | None = None,
        *,
        GSM: bytes | bytearray | Iterable[int] = bytes(64),
        APN: bytes | bytearray | Iterable[int] = bytes(64),
        Account: bytes | bytearray | Iterable[int] = bytes(64),
        Password: bytes | bytearray | Iterable[int] = bytes(64),
        MMSC: bytes | bytearray | Iterable[int] = bytes(64),
        IP: bytes | bytearray | Iterable[int] = bytes(64),
        Port: bytes | bytearray | Iterable[int] = bytes(64),
        Phone1: bytes | bytearray | Iterable[int] = bytes(64),
        Phone2: bytes | bytearray | Iterable[int] = bytes(64),
        Phone3: bytes | bytearray | Iterable[int] = bytes(64),
        Phone4: bytes | bytearray | Iterable[int] = bytes(64),
        Email1: bytes | bytearray | Iterable[int] = bytes(64),
        Email2: bytes | bytearray | Iterable[int] = bytes(64),
        Email3: bytes | bytearray | Iterable[int] = bytes(64),
        Email4: bytes | bytearray | Iterable[int] = bytes(64),
    ) -> None:
        self._gsm: bytearray = bytearray(GSM)[:64].ljust(64, b"\0")
        self._apn: bytearray = bytearray(APN)[:64].ljust(64, b"\0")
        self._account: bytearray = bytearray(Account)[:64].ljust(64, b"\0")
        self._password: bytearray = bytearray(Password)[:64].ljust(64, b"\0")
        self._mmsc: bytearray = bytearray(MMSC)[:64].ljust(64, b"\0")
        self._ip: bytearray = bytearray(IP)[:64].ljust(64, b"\0")
        self._port: bytearray = bytearray(Port)[:64].ljust(64, b"\0")
        self._phone1: bytearray = bytearray(Phone1)[:64].ljust(64, b"\0")
        self._phone2: bytearray = bytearray(Phone2)[:64].ljust(64, b"\0")
        self._phone3: bytearray = bytearray(Phone3)[:64].ljust(64, b"\0")
        self._phone4: bytearray = bytearray(Phone4)[:64].ljust(64, b"\0")
        self._email1: bytearray = bytearray(Email1)[:64].ljust(64, b"\0")
        self._email2: bytearray = bytearray(Email2)[:64].ljust(64, b"\0")
        self._email3: bytearray = bytearray(Email3)[:64].ljust(64, b"\0")
        self._email4: bytearray = bytearray(Email4)[:64].ljust(64, b"\0")

        if data is not None:
            self.data = data

    @property
    def GSM(self) -> bytearray:
        return self._gsm

    @GSM.setter
    def GSM(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._gsm = bytearray(value).ljust(64, b"\0")

    @property
    def Account(self) -> bytearray:
        return self._account

    @Account.setter
    def Account(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._account = bytearray(value).ljust(64, b"\0")

    @property
    def APN(self) -> bytearray:
        return self._apn

    @APN.setter
    def APN(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._apn = bytearray(value).ljust(64, b"\0")

    @property
    def Password(self) -> bytearray:
        return self._password

    @Password.setter
    def Password(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._password = bytearray(value).ljust(64, b"\0")

    @property
    def MMSC(self) -> bytearray:
        return self._mmsc

    @MMSC.setter
    def MMSC(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._mmsc = bytearray(value).ljust(64, b"\0")

    @property
    def IP(self) -> bytearray:
        return self._ip

    @IP.setter
    def IP(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._ip = bytearray(value).ljust(64, b"\0")

    @property
    def Port(self) -> bytearray:
        return self._port

    @Port.setter
    def Port(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._port = bytearray(value).ljust(64, b"\0")

    @property
    def Phone1(self) -> bytearray:
        return self._phone1

    @Phone1.setter
    def Phone1(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._phone1 = bytearray(value).ljust(64, b"\0")

    @property
    def Phone2(self) -> bytearray:
        return self._phone2

    @Phone2.setter
    def Phone2(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._phone2 = bytearray(value).ljust(64, b"\0")

    @property
    def Phone3(self) -> bytearray:
        return self._phone3

    @Phone3.setter
    def Phone3(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._phone3 = bytearray(value).ljust(64, b"\0")

    @property
    def Phone4(self) -> bytearray:
        return self._phone4

    @Phone4.setter
    def Phone4(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._phone4 = bytearray(value).ljust(64, b"\0")

    @property
    def Email1(self) -> bytearray:
        return self._email1

    @Email1.setter
    def Email1(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._email1 = bytearray(value).ljust(64, b"\0")

    @property
    def Email2(self) -> bytearray:
        return self._email2

    @Email2.setter
    def Email2(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._email2 = bytearray(value).ljust(64, b"\0")

    @property
    def Email3(self) -> bytearray:
        return self._email3

    @Email3.setter
    def Email3(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._email3 = bytearray(value).ljust(64, b"\0")

    @property
    def Email4(self) -> bytearray:
        return self._email4

    @Email4.setter
    def Email4(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._email4 = bytearray(value).ljust(64, b"\0")

    @property
    def data(self) -> bytearray:
        return (
            self._gsm
            + DataEncryption(self._apn)
            + DataEncryption(self._account)
            + DataEncryption(self._password)
            + DataEncryption(self._mmsc)
            + DataEncryption(self._ip)
            + DataEncryption(self._port)
            + DataEncryption(self._phone1)
            + DataEncryption(self._phone2)
            + DataEncryption(self._phone3)
            + DataEncryption(self._phone4)
            + DataEncryption(self._email1)
            + DataEncryption(self._email2)
            + DataEncryption(self._email3)
            + DataEncryption(self._email4)
        )

    @data.setter
    def data(self, data: bytes | bytearray | Sequence[int]) -> None:
        self._gsm = data[0:64]
        self._apn = DataEncryption(data[64:128])
        self._account = DataEncryption(data[128:192])
        self._password = DataEncryption(data[192:256])
        self._mmsc = DataEncryption(data[256:320])
        self._ip = DataEncryption(data[320:384])
        self._port = DataEncryption(data[384:448])
        self._phone1 = DataEncryption(data[448:512])
        self._phone2 = DataEncryption(data[512:576])
        self._phone3 = DataEncryption(data[576:640])
        self._phone4 = DataEncryption(data[640:704])
        self._email1 = DataEncryption(data[704:768])
        self._email2 = DataEncryption(data[768:832])
        self._email3 = DataEncryption(data[832:896])
        self._email4 = DataEncryption(data[896:960])
