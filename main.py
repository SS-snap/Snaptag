import sys
import os
from PyQt5.QtWidgets import QApplication, QFileDialog
from ui.ui import MainWindow
from loadingmodel import load_model_and_tokenizer
from PIL import Image


class Application:
    def __init__(self):

        self.model, self.tokenizer = load_model_and_tokenizer()

    def process_image(self, image_path):

        image = Image.open(image_path).convert('RGB')
        question = 'What is in the image?'
        msgs = [{'role': 'user', 'content': [image, question]}]


        result = self.model.chat(
            image=None,
            msgs=msgs,
            tokenizer=self.tokenizer
        )
        return result

    def process_images_in_folder(self, folder_path, output_folder):

        results = []
        for image_file in os.listdir(folder_path):
            if image_file.endswith(('.png', '.jpg', '.jpeg')):  # 支持的图像格式
                image_path = os.path.join(folder_path, image_file)
                result = self.process_image(image_path)


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

            results = application.process_images_in_folder(selected_folder, selected_folder)
            window.result_box.setText(results)


    window.select_folder_button.clicked.connect(on_folder_selected)
    window.process_button.clicked.connect(on_process_clicked)

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
