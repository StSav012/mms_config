# coding=utf-8
from typing import Iterable

from qtpy.QtWidgets import QFormLayout, QGridLayout, QGroupBox, QWidget

__all__ = ["FormGroupBox", "GridGroupBox"]


class FormGroupBox(QGroupBox):
    def __init__(self, title: str, parent: QWidget | None = None) -> None:
        super().__init__(title, parent)

        self._layout: QFormLayout = QFormLayout(self)

    def addRow(self, label: str, widget: QWidget) -> None:
        self._layout.addRow(label, widget)


class GridGroupBox(QGroupBox):
    def __init__(self, title: str, parent: QWidget | None = None) -> None:
        super().__init__(title, parent)

        self._layout: QGridLayout = QGridLayout(self)

    def addRow(self, widgets: Iterable[QWidget]) -> None:
        row: int = self._layout.rowCount()
        for column, widget in enumerate(widgets):
            self._layout.addWidget(widget, row, column)

    def addColumn(self, widgets: Iterable[QWidget]) -> None:
        column: int = self._layout.columnCount()
        for row, widget in enumerate(widgets):
            self._layout.addWidget(widget, row, column)
