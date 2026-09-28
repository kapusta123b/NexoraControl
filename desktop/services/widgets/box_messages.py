import logging
from typing import Literal

from PySide6.QtWidgets import QApplication, QMessageBox

MessageType = Literal["critical", "information", "warning", "question"]


class MessageBox:

    def show_message(
        self,
        message_type: MessageType = "information",
        title: str = "Message Box",
        text: str = "",
    ) -> None:
        try:
            message_func = getattr(QMessageBox, message_type)
            parent_window = QApplication.activeWindow()

            message_func(parent_window, title, text)

        except AttributeError as e:
            logging.exception(f"Invalid method name: {e}")
            return None
