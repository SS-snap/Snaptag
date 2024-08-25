from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTextEdit, QVBoxLayout, QWidget, QSpacerItem, QSizePolicy, QHBoxLayout
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Snap_tag")
        self.setGeometry(100, 100, 1200, 800)

        self.setWindowIcon(QIcon('./assets/app_icon.png'))


        # 背景标签
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())  # 设置背景标签大小和窗口一致
        self.background_label.setScaledContents(True)
        self.update_background()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        # 顶部空白空间（减少空白以上移按钮）
        main_layout.addSpacerItem(QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed))

        # 使用水平布局来放置按钮，确保它们在同一行并上移
        button_layout = QVBoxLayout()

        # 数据集选择按钮
        self.select_folder_button = QPushButton("选择数据集 (Select Dataset)", self)
        self.select_folder_button.setFixedSize(300, 60)
        self.select_folder_button.setFont(QFont("Arial", 16, QFont.Bold))
        self.select_folder_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                padding: 10px;
                border: none;
                font-size: 18px;
                /* 已移除 box-shadow */
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #388E3C;
            }
        """)
        button_layout.addWidget(self.select_folder_button)

        # 减少按钮之间的间距
        button_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum))

        # 开始批处理按钮
        self.process_button = QPushButton("开始批处理 (Start Processing)", self)
        self.process_button.setEnabled(False)
        self.process_button.setFixedSize(300, 60)
        self.process_button.setFont(QFont("Arial", 16, QFont.Bold))
        self.process_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border-radius: 10px;
                padding: 10px;
                border: none;
                font-size: 18px;
                /* 已移除 box-shadow */
            }
            QPushButton:hover {
                background-color: #1E88E5;
            }
            QPushButton:pressed {
                background-color: #1976D2;
            }
        """)
        button_layout.addWidget(self.process_button)

        # 将按钮布局添加到主布局
        main_layout.addLayout(button_layout)

        self.folder_label = QLabel("Selected Folder: None", self)  # 定义 folder_label
        self.folder_label.setFont(QFont("Arial", 14))
        self.folder_label.setStyleSheet("color: #333;")
        main_layout.addWidget(self.folder_label)

        # 再次减少按钮与下方内容之间的间距
        main_layout.addSpacerItem(QSpacerItem(40, 60, QSizePolicy.Minimum, QSizePolicy.Fixed))

        # 使用水平布局放置两个白色框
        white_box_layout = QVBoxLayout()

        # 输入框
        self.question_input = QTextEdit(self)
        self.question_input.setPlaceholderText("引导模型打标或保持默认\n(Enter your question)")
        self.question_input.setFixedHeight(300)
        self.question_input.setFont(QFont("Arial", 16))
        self.question_input.setStyleSheet("""
            QTextEdit {
                background-color: rgba(926, 126, 137, 0.5);  # 50% 不透明度
                border: 2px solid #ccc;
                border-radius: 10px;
                padding: 15px;
                font-size: 18px;
                background: transparent;
            }
        """)
        white_box_layout.addWidget(self.question_input)

        # 结果展示框
        self.result_box = QTextEdit(self)
        self.result_box.setFixedHeight(150)
        self.result_box.setFont(QFont("Arial", 14))
        self.result_box.setReadOnly(True)
        self.result_box.setStyleSheet("""
            QTextEdit {
                background-color: rgba(926, 126, 137, 0.5);  # 50% 不透明度
                border: 1px solid #ccc;
                padding: 15px;
                border-radius: 10px;
                background: transparent;
            }
        """)

        white_box_layout.addWidget(self.result_box)

        # 将两个白色框布局添加到底部
        main_layout.addLayout(white_box_layout)

        # 增加底部空白空间
        main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

    # 更新背景图片
    def update_background(self):
        pixmap = QPixmap('./assets/background.png')
        self.background_label.setPixmap(pixmap)

    # 处理窗口大小变化时的背景调整
    def resizeEvent(self, event):
        self.background_label.resize(self.size())  # 调整背景图片大小
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
