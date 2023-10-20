# coding=utf-8
from .MmscOperatorData import MmscOperatorData
from .SmtpOperatorData import SmtpOperatorData


class OperatorBinaryFile:
    def __init__(
        self,
        CountryName: str = "",
        data: MmscOperatorData | SmtpOperatorData | None = None,
    ) -> None:
        self._Country: str = CountryName
        self._Operator: str = ""
        self._APN: str = ""
        self._Account: str = ""
        self._Password: str = ""
        self._MMSC: str = ""
        self._GatewayIP: str = ""
        self._GatewayPort: str = ""
        self._Reserver: str = ""

        match data:
            case None:
                pass
            case MmscOperatorData():
                self._Operator = data.Name
                self._APN = data.APN
                self._Account = data.User
                self._Password = data.Password
                self._MMSC = data.MMSC
                self._GatewayIP = data.IP
                self._GatewayPort = data.Port
            case SmtpOperatorData():
                self._Operator = data.Name
                self._APN = data.APN
                self._Account = data.Account
                self._Password = data.Password
            case _:
                raise TypeError("Invalid data type")

    def GetMmsData(self) -> bytes:
        return (
            self._Country.encode()[:16].ljust(16, b"\0")
            + self._Operator.encode()[:16].ljust(16, b"\0")
            + self._APN.encode()[:48].ljust(48, b"\0")
            + self._Account.encode()[:48].ljust(48, b"\0")
            + self._Password.encode()[:48].ljust(48, b"\0")
            + self._MMSC.encode()[:48].ljust(48, b"\0")
            + self._GatewayIP.encode()[:16].ljust(16, b"\0")
            + self._GatewayPort.encode()[:8].ljust(8, b"\0")
        )

    def GetSmtpData(self) -> bytes:
        return (
            self._Country.encode()[:16].ljust(16, b"\0")
            + self._Operator.encode()[:16].ljust(16, b"\0")
            + self._APN.encode()[:48].ljust(48, b"\0")
            + self._Account.encode()[:48].ljust(48, b"\0")
            + self._Password.encode()[:48].ljust(48, b"\0")
        )
