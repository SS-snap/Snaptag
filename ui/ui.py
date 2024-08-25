from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTextEdit, QVBoxLayout, QWidget, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Snap_tag")
        self.setGeometry(100, 100, 1200, 800)


        self.setWindowIcon(QIcon('./assets/app_icon.png'))


        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)


        main_layout = QVBoxLayout(central_widget)


        self.background_label = QLabel(self)
        self.background_label.setScaledContents(True)
        self.update_background()
        self.background_label.lower()

        main_layout.addSpacerItem(QSpacerItem(40, 100, QSizePolicy.Expanding, QSizePolicy.Minimum))

       
        self.select_folder_button = QPushButton("你的数据集 (data)", self)
        self.select_folder_button.setFixedSize(400, 100)
        self.select_folder_button.setFont(QFont("Arial", 22, QFont.Bold))
        self.select_folder_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 30px;
                border-radius: 15px;
                padding: 15px;
                border: none;
                box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.2);
            }
            QPushButton:hover {
                background-color: #45a049;
                box-shadow: 5px 5px 12px rgba(0, 0, 0, 0.3);
            }
            QPushButton:pressed {
                background-color: #388E3C;
                box-shadow: inset 2px 2px 4px rgba(0, 0, 0, 0.2);
            }
        """)
        main_layout.addWidget(self.select_folder_button, alignment=Qt.AlignCenter)

        main_layout.addSpacerItem(QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))


        self.process_button = QPushButton("开始批处理 (Processing)", self)
        self.process_button.setEnabled(False)
        self.process_button.setFixedSize(400, 100)
        self.process_button.setFont(QFont("Arial", 22, QFont.Bold))
        self.process_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                font-size: 30px;
                border-radius: 15px;
                padding: 15px;
                border: none;
                box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.2);
            }
            QPushButton:hover {
                background-color: #1E88E5;
                box-shadow: 5px 5px 12px rgba(0, 0, 0, 0.3);
            }
            QPushButton:pressed {
                background-color: #1976D2;
                box-shadow: inset 2px 2px 4px rgba(0, 0, 0, 0.2);
            }
        """)
        main_layout.addWidget(self.process_button, alignment=Qt.AlignCenter)


        self.folder_label = QLabel("Selected Folder: None", self)
        self.folder_label.setFont(QFont("Arial", 14))
        self.folder_label.setStyleSheet("color: #333; margin-top: 10px;")
        main_layout.addWidget(self.folder_label, alignment=Qt.AlignCenter)


        self.result_box = QTextEdit(self)
        self.result_box.setFixedSize(800, 300)
        self.result_box.setFont(QFont("Arial", 14))
        self.result_box.setReadOnly(True)
        self.result_box.setStyleSheet("background-color: #f9f9f9; border: 1px solid #ccc;")
        main_layout.addWidget(self.result_box, alignment=Qt.AlignCenter)


        main_layout.addSpacerItem(QSpacerItem(40, 100, QSizePolicy.Expanding, QSizePolicy.Minimum))

    def update_background(self):

        pixmap = QPixmap('./assets/background.png')
        self.background_label.setPixmap(pixmap)

    def resizeEvent(self, event):

        self.background_label.resize(self.size())
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
