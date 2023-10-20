# coding=utf-8

from typing import Iterable, Sequence

from .MyselfClass import DataEncryption

__all__ = ["SmtpData"]


class SmtpData:
    def __init__(
        self,
        data: bytes | bytearray | Iterable[int] | None = None,
        *,
        GSM: bytes | bytearray | Iterable[int] = bytes(64),
        GprsAPN: bytes | bytearray | Iterable[int] = bytes(64),
        GprsAccount: bytes | bytearray | Iterable[int] = bytes(64),
        GprsPassword: bytes | bytearray | Iterable[int] = bytes(64),
        SmtpServer: bytes | bytearray | Iterable[int] = bytes(64),
        SmtpPort: bytes | bytearray | Iterable[int] = bytes(64),
        SendEmail: bytes | bytearray | Iterable[int] = bytes(64),
        SendEmailPassword: bytes | bytearray | Iterable[int] = bytes(64),
        SmtpEmail1: bytes | bytearray | Iterable[int] = bytes(64),
        SmtpEmail2: bytes | bytearray | Iterable[int] = bytes(64),
        SmtpEmail3: bytes | bytearray | Iterable[int] = bytes(64),
        SmtpEmail4: bytes | bytearray | Iterable[int] = bytes(64),
    ) -> None:
        self._gsm: bytearray = bytearray(GSM).ljust(64, b"\0")
        self._gprs_apn: bytearray = bytearray(GprsAPN).ljust(64, b"\0")
        self._gprs_account: bytearray = bytearray(GprsAccount).ljust(64, b"\0")
        self._gprs_password: bytearray = bytearray(GprsPassword).ljust(64, b"\0")
        self._smtp_server: bytearray = bytearray(SmtpServer).ljust(64, b"\0")
        self._smtp_port: bytearray = bytearray(SmtpPort).ljust(64, b"\0")
        self._send_email: bytearray = bytearray(SendEmail).ljust(64, b"\0")
        self._send_email_password: bytearray = bytearray(SendEmailPassword).ljust(
            64, b"\0"
        )
        self._smtp_email1: bytearray = bytearray(SmtpEmail1).ljust(64, b"\0")
        self._smtp_email2: bytearray = bytearray(SmtpEmail2).ljust(64, b"\0")
        self._smtp_email3: bytearray = bytearray(SmtpEmail3).ljust(64, b"\0")
        self._smtp_email4: bytearray = bytearray(SmtpEmail4).ljust(64, b"\0")

        if data is not None:
            self.data = data

    @property
    def GSM(self) -> bytearray:
        return self._gsm

    @GSM.setter
    def GSM(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._gsm = bytearray(value).ljust(64, b"\0")

    @property
    def GprsAPN(self) -> bytearray:
        return self._gprs_apn

    @GprsAPN.setter
    def GprsAPN(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._gprs_apn = bytearray(value).ljust(64, b"\0")

    @property
    def GprsAccount(self) -> bytearray:
        return self._gprs_account

    @GprsAccount.setter
    def GprsAccount(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._gprs_account = bytearray(value).ljust(64, b"\0")

    @property
    def GprsPassword(self) -> bytearray:
        return self._gprs_password

    @GprsPassword.setter
    def GprsPassword(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._gprs_password = bytearray(value).ljust(64, b"\0")

    @property
    def SmtpServer(self) -> bytearray:
        return self._smtp_server

    @SmtpServer.setter
    def SmtpServer(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._smtp_server = bytearray(value).ljust(64, b"\0")

    @property
    def SmtpPort(self) -> bytearray:
        return self._smtp_port

    @SmtpPort.setter
    def SmtpPort(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._smtp_port = bytearray(value).ljust(64, b"\0")

    @property
    def SendEmail(self) -> bytearray:
        return self._send_email

    @SendEmail.setter
    def SendEmail(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._send_email = bytearray(value).ljust(64, b"\0")

    @property
    def SendEmailPassword(self) -> bytearray:
        return self._send_email_password

    @SendEmailPassword.setter
    def SendEmailPassword(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._send_email_password = bytearray(value).ljust(64, b"\0")

    @property
    def SmtpEmail1(self) -> bytearray:
        return self._smtp_email1

    @SmtpEmail1.setter
    def SmtpEmail1(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._smtp_email1 = bytearray(value).ljust(64, b"\0")

    @property
    def SmtpEmail2(self) -> bytearray:
        return self._smtp_email2

    @SmtpEmail2.setter
    def SmtpEmail2(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._smtp_email2 = bytearray(value).ljust(64, b"\0")

    @property
    def SmtpEmail3(self) -> bytearray:
        return self._smtp_email3

    @SmtpEmail3.setter
    def SmtpEmail3(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._smtp_email3 = bytearray(value).ljust(64, b"\0")

    @property
    def SmtpEmail4(self) -> bytearray:
        return self._smtp_email4

    @SmtpEmail4.setter
    def SmtpEmail4(self, value: bytes | bytearray | Iterable[int]) -> None:
        self._smtp_email4 = bytearray(value).ljust(64, b"\0")

    @property
    def data(self) -> bytearray:
        return (
            self._gsm
            + DataEncryption(self._gprs_apn)
            + DataEncryption(self._gprs_account)
            + DataEncryption(self._gprs_password)
            + DataEncryption(self._smtp_server)
            + DataEncryption(self._smtp_port)
            + DataEncryption(self._send_email)
            + DataEncryption(self._send_email_password)
            + DataEncryption(self._smtp_email1)
            + DataEncryption(self._smtp_email2)
            + DataEncryption(self._smtp_email3)
            + DataEncryption(self._smtp_email4)
        )

    @data.setter
    def data(self, data: bytes | bytearray | Sequence[int]) -> None:
        self._gsm = data[0:64]
        self._gprs_apn = DataEncryption(data[64:128])
        self._gprs_account = DataEncryption(data[128:192])
        self._gprs_password = DataEncryption(data[192:256])
        self._smtp_server = DataEncryption(data[256:320])
        self._smtp_port = DataEncryption(data[320:384])
        self._send_email = DataEncryption(data[384:448])
        self._send_email_password = DataEncryption(data[448:512])
        self._smtp_email1 = DataEncryption(data[512:576])
        self._smtp_email2 = DataEncryption(data[576:640])
        self._smtp_email3 = DataEncryption(data[640:704])
        self._smtp_email4 = DataEncryption(data[704:768])
