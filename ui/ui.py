from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTextEdit, QVBoxLayout, QWidget, QSpacerItem, QSizePolicy, QHBoxLayout, QSlider
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QFontDatabase

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

        # 使用垂直布局来放置两个按钮，确保它们上下排列
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
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #388E3C;
            }
        """)
        button_layout.addWidget(self.select_folder_button)

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
            }
            QPushButton:hover {
                background-color: #1E88E5;
            }
            QPushButton:pressed {
                background-color: #1976D2;
            }
        """)
        button_layout.addWidget(self.process_button)

        # 添加按钮布局到主布局
        main_layout.addLayout(button_layout)

        font_id = QFontDatabase.addApplicationFont("./1.ttf")

        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]  # 获取字体族名称
        else:
            font_family = "Arial"

        # 添加滑块布局
        slider_layout = QVBoxLayout()

        # 滑块样式表（黑色风格和缩小的滑块）
        slider_style = """
        QSlider::groove:horizontal {
            border: 1px solid #bbb;
            background: #000;
            height: 6px;
            border-radius: 3px;
        }
        QSlider::handle:horizontal {
            background: #000;
            border: 1px solid #333;
            width: 14px;
            margin: -5px 0;
            border-radius: 7px;
        }
        QSlider::sub-page:horizontal {
            background: #555;
            border-radius: 3px;
        }
        QSlider::add-page:horizontal {
            background: #999;
            border-radius: 3px;
        }
        """

        # 滑块标签样式表（黑色文字）
        label_style = """
        QLabel {
            color: #000;
            font-size: 14px;
        }
        """

        self.top_k_slider = QSlider(Qt.Horizontal)
        self.top_k_slider.setRange(1, 100)
        self.top_k_slider.setValue(50)  # 默认值
        self.top_k_slider.setStyleSheet(slider_style)  # 应用样式
        self.top_k_slider.setTickPosition(QSlider.TicksAbove)  # 在滑块上方显示刻度
        self.top_k_slider.setTickInterval(10)
        self.top_k_label = QLabel(f"top_k: {self.top_k_slider.value()}")


        # 使用本地字体并加粗
        self.top_k_label.setFont(QFont("Arial", 16, QFont.Bold))

        slider_layout.addWidget(self.top_k_label)
        slider_layout.addWidget(self.top_k_slider)

        # 监听 top_k 滑块的变化，动态更新标签文本
        self.top_k_slider.valueChanged.connect(lambda: self.top_k_label.setText(f"top_k: {self.top_k_slider.value()}"))

        # 设置 top_p 滑块和标签
        self.top_p_slider = QSlider(Qt.Horizontal)
        self.top_p_slider.setRange(1, 100)  # 将1-100转换为0.01-1.0
        self.top_p_slider.setValue(90)  # 默认值0.9
        self.top_p_slider.setStyleSheet(slider_style)  # 应用样式
        self.top_p_slider.setTickPosition(QSlider.TicksAbove)  # 在滑块上方显示刻度
        self.top_p_slider.setTickInterval(10)
        self.top_p_label = QLabel(f"top_p: {self.top_p_slider.value() / 100}")


        # 使用本地字体并加粗
        self.top_p_label.setFont(QFont("Arial", 16, QFont.Bold))

        slider_layout.addWidget(self.top_p_label)
        slider_layout.addWidget(self.top_p_slider)

        # 监听 top_p 滑块的变化，动态更新标签文本
        self.top_p_slider.valueChanged.connect(
            lambda: self.top_p_label.setText(f"top_p: {self.top_p_slider.value() / 100}"))

        # 设置 temperature 滑块和标签
        self.temperature_slider = QSlider(Qt.Horizontal)
        self.temperature_slider.setRange(1, 100)  # 将1-100转换为0.01-1.0
        self.temperature_slider.setValue(70)  # 默认值0.7
        self.temperature_slider.setStyleSheet(slider_style)  # 应用样式
        self.temperature_slider.setTickPosition(QSlider.TicksAbove)  # 在滑块上方显示刻度
        self.temperature_slider.setTickInterval(10)
        self.temperature_label = QLabel(f"temperature （Imagination） : {self.temperature_slider.value() / 100}")
        self.temperature_label.setStyleSheet("color: black;")  # 设置字体颜色为红色

        # 使用本地字体并加粗
        self.temperature_label.setFont(QFont(font_family, 16, QFont.Bold))

        slider_layout.addWidget(self.temperature_label)
        slider_layout.addWidget(self.temperature_slider)

        # 监听 temperature 滑块的变化
        self.temperature_slider.valueChanged.connect(lambda: self.temperature_label.setText(f"temperature: {self.temperature_slider.value() / 100}"))

        # 在滑块上方增加空白，使它下移
        main_layout.addSpacerItem(QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed))  # 增加空白以移动滑块位置
        main_layout.addLayout(slider_layout)

        # 文件选择标签
        self.folder_label = QLabel("Selected Folder: None", self)
        self.folder_label.setFont(QFont("Arial", 14))
        self.folder_label.setStyleSheet("color: #333;")
        main_layout.addWidget(self.folder_label)

        # 输入和结果展示框的布局
        white_box_layout = QVBoxLayout()

        # 输入框
        self.question_input = QTextEdit(self)
        self.question_input.setPlaceholderText("引导模型打标或保持默认\n(Enter your question)")
        self.question_input.setFixedHeight(300)
        self.question_input.setFont(QFont("Arial", 16))
        white_box_layout.addWidget(self.question_input)

        # 结果展示框
        self.result_box = QTextEdit(self)
        self.result_box.setFixedHeight(150)
        self.result_box.setFont(QFont("Arial", 14))
        self.result_box.setReadOnly(True)
        white_box_layout.addWidget(self.result_box)

        main_layout.addLayout(white_box_layout)

    # 更新背景图片
    def update_background(self):
        pixmap = QPixmap('./assets/background.png')
        self.background_label.setPixmap(pixmap)

    # 处理窗口大小变化时的背景调整
    def resizeEvent(self, event):
        self.background_label.resize(self.size())
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
