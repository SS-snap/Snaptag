import sys
import os
from PyQt5.QtWidgets import QApplication, QFileDialog
from ui.ui import MainWindow
from loadingmodel import load_model_and_tokenizer
from PIL import Image


class Application:
    def __init__(self):
        # 加载模型
        self.model, self.tokenizer = load_model_and_tokenizer()

    def process_image(self, image_path):
        # 处理单张图像并生成推理结果
        image = Image.open(image_path).convert('RGB')
        question = 'What is in the image?'
        msgs = [{'role': 'user', 'content': [image, question]}]

        # 使用加载的模型进行推理
        result = self.model.chat(
            image=None,
            msgs=msgs,
            tokenizer=self.tokenizer
        )
        return result

    def process_images_in_folder(self, folder_path, output_folder):
        # 遍历文件夹中的所有图像文件并处理，保存结果到指定文件夹
        results = []
        for image_file in os.listdir(folder_path):
            if image_file.endswith(('.png', '.jpg', '.jpeg')):  # 支持的图像格式
                image_path = os.path.join(folder_path, image_file)
                result = self.process_image(image_path)

                # 生成结果文件的路径
                image_name_prefix = os.path.splitext(image_file)[0]  # 获取图像文件名前缀
                output_file_path = os.path.join(output_folder, f"{image_name_prefix}.txt")

                # 将结果写入 .txt 文件
                with open(output_file_path, 'w') as output_file:
                    output_file.write(result)

                results.append(f"图像: {image_file}\n成功保存至: {output_file_path}\n")
        return "\n".join(results)


def main():
    app = QApplication(sys.argv)

    # 创建 UI 窗口
    window = MainWindow()

    # 创建应用逻辑类
    application = Application()

    selected_folder = None

    # 当选择文件夹时，启用“开始批处理”按钮
    def on_folder_selected():
        nonlocal selected_folder
        selected_folder = QFileDialog.getExistingDirectory(window, "Select Folder")
        if selected_folder:
            window.folder_label.setText(f"Selected Folder: {selected_folder}")
            window.process_button.setEnabled(True)  # 选择文件夹后启用批处理按钮

    # 当点击“开始批处理”按钮时，开始处理文件夹中的所有图像
    def on_process_clicked():
        if selected_folder:
            # 批处理图像并保存结果
            results = application.process_images_in_folder(selected_folder, selected_folder)
            window.result_box.setText(results)

    # 将选择文件夹和处理绑定到按钮点击事件
    window.select_folder_button.clicked.connect(on_folder_selected)
    window.process_button.clicked.connect(on_process_clicked)

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
