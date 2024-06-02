# coding=utf-8
from typing import Any

from .SmtpOperatorData import SmtpOperatorData

__all__ = ["SmtpCountryData"]


class SmtpCountryData:
    def __init__(
        self,
        countryName: str = "",
        data: SmtpOperatorData | None = None,
    ) -> None:
        self._country_name: str = countryName
        self._data: list[SmtpOperatorData] = []
        if data is not None:
            self._data.append(data)

    @property
    def CountryName(self) -> str:
        return self._country_name

    @CountryName.setter
    def CountryName(self, value: str) -> None:
        self._country_name = value

    @property
    def count(self) -> int:
        return len(self._data)

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, SmtpCountryData):
            return NotImplemented
        return self._country_name < other.CountryName

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, SmtpCountryData):
            return NotImplemented
        return self._country_name == other.CountryName

    def append(self, data: SmtpOperatorData) -> None:
        self._data.append(data)

    def get_operator_names(self) -> list[str]:
        return [item.Name for item in self._data]

    def get_operator_data(self, index: int) -> SmtpOperatorData:
        try:
            return self._data[index]
        except LookupError:
            SmtpOperatorData("Nothing")

    def remove(self, data: SmtpOperatorData) -> bool:
        try:
            self._data.remove(data)
        except ValueError:
            return False
        else:
            return True
