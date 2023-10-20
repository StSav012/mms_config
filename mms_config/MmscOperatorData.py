# coding=utf-8
from contextlib import suppress

__all__ = ["MmscOperatorData"]


class MmscOperatorData:
    def __init__(self, info: str = "") -> None:
        self._name: str = ""
        self._apn: str = ""
        self._mmsc: str = ""
        self._ip: str = ""
        self._port: str = ""
        self._account: str = ""
        self._password: str = ""
        with suppress(ValueError):
            (
                self._name,
                self._apn,
                self._mmsc,
                self._ip,
                self._port,
                self._account,
                self._password,
            ) = info.split("$", maxsplit=6)

    @property
    def Name(self) -> str:
        return self._name

    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def APN(self) -> str:
        return self._apn

    @APN.setter
    def APN(self, value: str) -> None:
        self._apn = value

    @property
    def MMSC(self) -> str:
        return self._mmsc

    @MMSC.setter
    def MMSC(self, value: str) -> None:
        self._mmsc = value

    @property
    def IP(self) -> str:
        return self._ip

    @IP.setter
    def IP(self, value: str) -> None:
        self._ip = value

    @property
    def Port(self) -> str:
        return self._port

    @Port.setter
    def Port(self, value: str) -> None:
        self._port = value

    @property
    def User(self) -> str:
        return self._account

    @User.setter
    def User(self, value: str) -> None:
        self._account = value

    @property
    def Password(self) -> str:
        return self._password

    @Password.setter
    def Password(self, value: str) -> None:
        self._password = value
