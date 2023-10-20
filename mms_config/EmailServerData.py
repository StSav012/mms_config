# coding=utf-8
from contextlib import suppress

__all__ = ["EmailServerData"]


class EmailServerData:
    def __init__(self, info: str = "") -> None:
        self._ServerName: str = ""
        self._HTTP: str = ""
        self._Port: str = ""
        self._MailKind: str = ""
        with suppress(ValueError):
            (
                self._ServerName,
                self._HTTP,
                self._Port,
                self._MailKind,
            ) = info.split("$", maxsplit=3)

    @property
    def Name(self) -> str:
        return self._ServerName

    @Name.setter
    def Name(self, value: str) -> None:
        self._ServerName = value

    @property
    def Http(self) -> str:
        return self._HTTP

    @Http.setter
    def Http(self, value: str) -> None:
        self._HTTP = value

    @property
    def Port(self) -> str:
        return self._Port

    @Port.setter
    def Port(self, value: str) -> None:
        self._Port = value

    @property
    def Kind(self) -> str:
        return self._MailKind

    @Kind.setter
    def Kind(self, value: str) -> None:
        self._MailKind = value
