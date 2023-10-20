# coding=utf-8
from typing import Self

from .MmscOperatorData import MmscOperatorData

__all__ = ["MmscCountryData"]


class MmscCountryData:
    def __init__(
        self,
        countryName: str = "",
        operatorName: MmscOperatorData | None = None,
    ) -> None:
        self._CountryName: str = countryName
        self._Operator: list[MmscOperatorData] = []
        if operatorName is not None:
            self._Operator.append(operatorName)

    @property
    def CountryName(self) -> str:
        return self._CountryName

    @CountryName.setter
    def CountryName(self, value: str) -> None:
        self._CountryName = value

    @property
    def Count(self) -> int:
        return len(self._Operator)

    def __lt__(self, other: Self) -> bool:
        return self._CountryName < other.CountryName

    def __eq__(self, other: Self) -> bool:
        return self._CountryName == other.CountryName

    def Add(self, data: MmscOperatorData) -> None:
        self._Operator.append(data)

    def GetOperatorNames(self) -> list[str]:
        return [item.Name for item in self._Operator]

    def GetOperatorData(self, index: int) -> MmscOperatorData:
        try:
            return self._Operator[index]
        except LookupError:
            MmscOperatorData("Nothing")

    def Remove(self, data: MmscOperatorData) -> bool:
        try:
            self._Operator.remove(data)
        except ValueError:
            return False
        else:
            return True
