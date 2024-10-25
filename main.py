import sys
import fitz  # PyMuPDF
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import os


class PDFImageExtractor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PDF Image Extractor")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Select a PDF file to extract images", self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.button = QPushButton("Choose PDF", self)
        self.button.clicked.connect(self.choose_pdf)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def choose_pdf(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open PDF File", "", "PDF Files (*.pdf)", options=options)
        if file_path:
            output_folder = QFileDialog.getExistingDirectory(self, "Select Output Folder")
            if output_folder:
                self.extract_images(file_path, output_folder)

    def extract_images(self, pdf_path, output_folder):
        pdf_document = fitz.open(pdf_path)
        img_count = 0
        output_folder = f"{output_folder}/export"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            images = page.get_images(full=True)

            for img_index, img in enumerate(images):
                xref = img[0]
                base_image = pdf_document.extract_image(xref)
                img_bytes = base_image["image"]
                img_ext = base_image["ext"]
                img_count += 1
                img_path = os.path.join(output_folder, f"image_page{page_num + 1}_{img_index + 1}.{img_ext}")
                with open(img_path, "wb") as img_file:
                    img_file.write(img_bytes)

        self.label.setText(f"Extracted {img_count} images to: {output_folder}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = PDFImageExtractor()
    ex.show()
    sys.exit(app.exec_())
