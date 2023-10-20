# coding=utf-8
from contextlib import suppress

__all__ = ["SmtpOperatorData"]


class SmtpOperatorData:
    def __init__(self, info: str = "") -> None:
        self._name: str = ""
        self._apn: str = ""
        self._account: str = ""
        self._password: str = ""
        self._server: str = ""
        self._port: str = ""
        self._email: str = ""
        self._email_password: str = ""
        # FIXME: "$" not allowed as `_password`
        with suppress(ValueError):
            (
                self._name,
                self._apn,
                self._account,
                self._password,
                self._server,
                self._port,
                self._email,
                self._email_password,
            ) = info.split("$", maxsplit=7)

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
    def Account(self) -> str:
        return self._account

    @Account.setter
    def Account(self, value: str) -> None:
        self._account = value

    @property
    def Password(self) -> str:
        return self._password

    @Password.setter
    def Password(self, value: str) -> None:
        self._password = value

    @property
    def Server(self) -> str:
        return self._server

    @Server.setter
    def Server(self, value: str) -> None:
        self._server = value

    @property
    def Port(self) -> str:
        return self._port

    @Port.setter
    def Port(self, value: str) -> None:
        self._port = value

    @property
    def Email(self) -> str:
        return self._email

    @Email.setter
    def Email(self, value: str) -> None:
        self._email = value

    @property
    def EmailPassword(self) -> str:
        return self._email_password

    @EmailPassword.setter
    def EmailPassword(self, value: str) -> None:
        self._email_password = value
