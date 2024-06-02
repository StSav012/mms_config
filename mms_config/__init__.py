# coding=utf-8
def main() -> int:
    import sys

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
    qtbase_translator: QTranslator = QTranslator()
    for language in languages:
        if qtbase_translator.load(
                'qtbase_' + language,
                QLibraryInfo.location(QLibraryInfo.LibraryPath.TranslationsPath),
        ):
            if QApplication.installTranslator(qtbase_translator):
                break
    my_translator: QTranslator = QTranslator()
    for language in languages:
        if my_translator.load(language, 'i18n'):
            if QApplication.installTranslator(my_translator):
                break
    w: FormMain = FormMain()
    w.show()
    return app.exec()
