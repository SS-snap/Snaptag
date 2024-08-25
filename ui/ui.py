from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTextEdit, QVBoxLayout, QWidget, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Snap_tag")
        self.setGeometry(100, 100, 1200, 800)  # 调整为宽 1200, 高 800 的窗口尺寸

        # 设置窗口图标
        self.setWindowIcon(QIcon('./assets/app_icon.png'))  # 可根据实际路径设置窗口图标

        # 创建中心小部件
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # 设置平铺背景图片
        self.setStyleSheet("""
            QMainWindow {
                background-image: url('./assets/background.png');
                background-repeat: repeat;
            }
        """)

        # 创建主布局
        main_layout = QVBoxLayout(central_widget)

        # 添加顶部弹簧空间，让按钮布局更均匀
        main_layout.addSpacerItem(QSpacerItem(40, 100, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # 选择文件夹按钮
        self.select_folder_button = QPushButton("你的数据集 (data)", self)
        self.select_folder_button.setFixedSize(400, 100)  # 增大按钮尺寸
        self.select_folder_button.setFont(QFont("Arial", 22, QFont.Bold))  # 使用加粗字体
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
        main_layout.addWidget(self.select_folder_button, alignment=Qt.AlignCenter)  # 按钮居中

        # 添加按钮之间的弹簧空间
        main_layout.addSpacerItem(QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # 开始批处理按钮
        self.process_button = QPushButton("开始批处理 (Processing)", self)
        self.process_button.setEnabled(False)
        self.process_button.setFixedSize(400, 100)  # 增大按钮尺寸
        self.process_button.setFont(QFont("Arial", 22, QFont.Bold))  # 使用加粗字体
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
        main_layout.addWidget(self.process_button, alignment=Qt.AlignCenter)  # 按钮居中

        # 添加显示选择文件夹的标签
        self.folder_label = QLabel("Selected Folder: None", self)  # 创建标签
        self.folder_label.setFont(QFont("Arial", 14))
        self.folder_label.setStyleSheet("color: #333; margin-top: 10px;")  # 样式设置
        main_layout.addWidget(self.folder_label, alignment=Qt.AlignCenter)  # 标签居中

        # 添加结果显示区域
        self.result_box = QTextEdit(self)  # 创建一个 QTextEdit 用于显示结果
        self.result_box.setFixedSize(800, 300)  # 调整显示区域大小
        self.result_box.setFont(QFont("Arial", 14))
        self.result_box.setReadOnly(True)
        self.result_box.setStyleSheet("background-color: #f9f9f9; border: 1px solid #ccc;")
        main_layout.addWidget(self.result_box, alignment=Qt.AlignCenter)  # 将结果显示框添加到布局中

        # 添加底部弹簧空间
        main_layout.addSpacerItem(QSpacerItem(40, 100, QSizePolicy.Expanding, QSizePolicy.Minimum))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
