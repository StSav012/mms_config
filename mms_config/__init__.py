# coding=utf-8
def main() -> int:
    import sys
    from pathlib import Path

    from packaging.version import parse
    from qtpy import QT_VERSION
    from qtpy.QtCore import QLibraryInfo, QLocale, QTranslator, Qt
    from qtpy.QtWidgets import QApplication

    from .FormMain import FormMain

    app: QApplication = QApplication(sys.argv)
    if parse(QT_VERSION) < parse('6'):
        QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)

    languages: set[str] = set(QLocale().uiLanguages() + [QLocale().bcp47Name(), QLocale().name()])
    language: str
    translations_path: str = QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
    qtbase_translator: QTranslator = QTranslator()
    for language in languages:
        if qtbase_translator.load("qtbase_" + language, translations_path):
            QApplication.installTranslator(qtbase_translator)
            break
    my_translator: QTranslator = QTranslator()
    for language in languages:
        if my_translator.load(language, str(Path(__file__).parent / "i18n")):
            QApplication.installTranslator(my_translator)
            break
    w: FormMain = FormMain()
    w.show()
    return app.exec()
