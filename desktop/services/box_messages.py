from PySide6.QtWidgets import QApplication, QMessageBox

class MessageBox:

    def __init__(self):
        self.message_types = {
            "critical": QMessageBox.critical,
            "information": QMessageBox.information,
            "warning": QMessageBox.warning,
            "question": QMessageBox.question,
        }

    
    def show_message(self, message_type: str, title: str, text: str):
        message = self.message_types.get(message_type)

        if callable(message):
            parent_window = QApplication.activeWindow()

            result = message(parent_window, title, text)
            return result
        
