from datetime import datetime
from PyQt5.QtCore import qInfo, qWarning

class Logger:
    def __init__(self, name: str = ""):
        self.name = name
        if self.name is None or self.name == "":
            self.name = self.__caller_filename()

    @staticmethod
    def __caller_filename():
        import inspect
        stack = inspect.stack()
        caller_frame = stack[2]
        full_filepath = caller_frame.filename.replace("\\", "/")
        return full_filepath[full_filepath.rindex("pykrita/") + len("pykrita/"):]

    def __format(self, level: str, msg: str):
        import inspect
        stack = inspect.stack()
        caller_frame = stack[2]
        datestr = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        return f"[{level}][{self.name}:{caller_frame.lineno}] {datestr}: {msg}".encode("utf-8")

    def info(self, msg: str):
        qInfo(self.__format('INFO', msg))

    def warn(self, msg: str):
        qWarning(self.__format("WARN", msg))

    # call this will terminate krita!
    # def error(self, msg: str):
    #     qFatal(self.__format("FATAL", msg))