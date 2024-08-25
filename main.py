import sys
import os
from PyQt5.QtWidgets import QApplication, QFileDialog
from ui.ui import MainWindow
from loadingmodel import load_model_and_tokenizer
from PIL import Image

class Application:
    def __init__(self):
        self.model, self.tokenizer = load_model_and_tokenizer()

    def process_image(self, image_path, question, top_k=50, top_p=0.9, temperature=0.7):
        image = Image.open(image_path).convert('RGB')
        msgs = [{'role': 'user', 'content': [image, question]}]

        result = self.model.chat(
            image=None,
            msgs=msgs,
            tokenizer=self.tokenizer,
            top_k=top_k,
            top_p=top_p,
            temperature=temperature
        )
        return result

    def process_images_in_folder(self, folder_path, output_folder, question, top_k=50, top_p=0.9, temperature=0.7):
        results = []
        for image_file in os.listdir(folder_path):
            if image_file.endswith(('.png', '.jpg', '.jpeg')):  # 支持的图像格式
                image_path = os.path.join(folder_path, image_file)
                result = self.process_image(image_path, question, top_k, top_p, temperature)

                image_name_prefix = os.path.splitext(image_file)[0]  # 获取图像文件名前缀
                output_file_path = os.path.join(output_folder, f"{image_name_prefix}.txt")

                with open(output_file_path, 'w') as output_file:
                    output_file.write(result)

                results.append(f"图像: {image_file}\n成功保存至: {output_file_path}\n")
        return "\n".join(results)

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    application = Application()

    selected_folder = None

    def on_folder_selected():
        nonlocal selected_folder
        selected_folder = QFileDialog.getExistingDirectory(window, "Select Folder")
        if selected_folder:
            window.folder_label.setText(f"Selected Folder: {selected_folder}")
            window.process_button.setEnabled(True)

    def on_process_clicked():
        if selected_folder:
            question = window.question_input.toPlainText().strip()
            if not question:
                question = 'What is in the image?'

            # 获取top_k, top_p 和 temperature的滑块值
            top_k = window.top_k_slider.value()
            top_p = window.top_p_slider.value() / 100.0  # 滑块的值是1-100，需要转换为0.01-1.0
            temperature = window.temperature_slider.value() / 100.0  # 滑块的值是1-100，需要转换为0.01-1.0

            results = application.process_images_in_folder(selected_folder, selected_folder, question, top_k, top_p, temperature)
            window.result_box.setText(results)

    window.select_folder_button.clicked.connect(on_folder_selected)
    window.process_button.clicked.connect(on_process_clicked)

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
