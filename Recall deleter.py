import os
import shutil
import getpass
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QMessageBox, QProgressBar
from PyQt5.QtGui import QPixmap
from qfluentwidgets import FluentIcon, PrimaryPushButton

class DeleteRecall(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("RecallDeleter")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        # Create a QLabel to hold the image
        self.label = QLabel(self)

        # Load the image using QPixmap
        pixmap = QPixmap('title.png')  # Replace with your image path

        # Set the pixmap onto the label
        self.label.setPixmap(pixmap)
        layout.addWidget(self.label)

        self.delete_button = PrimaryPushButton(FluentIcon.DELETE, "Delete Microsoft Recall")
        self.delete_button.clicked.connect(self.delete_contents)
        layout.addWidget(self.delete_button)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(0)  # Set initial progress to 0%
        self.progress_bar.setMaximum(100)  # Set maximum progress to 100%
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

    def delete_contents(self):
        username = getpass.getuser()
        target_directory = f"C:\\Users\\{username}\\AppData\\Local\\CoreAIPlatform.00\\UKP"

        if os.path.exists(target_directory):
            confirmation = QMessageBox.question(self, "Confirmation", "Are you sure you want to delete Microsoft Recall?", QMessageBox.Yes | QMessageBox.No)
            if confirmation == QMessageBox.Yes:
                try:
                    total_files = 0

                    for dirpath, dirnames, filenames in os.walk(target_directory):
                        total_files += len(filenames)

                    if total_files == 0:
                        QMessageBox.information(self, "Info", "No files to delete in: " + target_directory)
                        return

                    # Update progress bar based on total files (assuming each file deletion has equal weight)
                    progress_step = 100 / total_files

                    for dirpath, dirnames, filenames in os.walk(target_directory):
                        for filename in filenames:
                            file_path = os.path.join(dirpath, filename)
                            if os.path.isfile(file_path) or os.path.islink(file_path):
                                os.unlink(file_path)  # Remove the file or link
                                self.progress_bar.setValue(self.progress_bar.value() + progress_step)
                            elif os.path.isdir(file_path):
                                shutil.rmtree(file_path)  # Remove the directory and all its contents
                                self.progress_bar.setValue(self.progress_bar.value() + progress_step)

                    QMessageBox.information(self, "Success", "All contents deleted in: " + target_directory + ", Including screenshots.")
                except Exception as e:
                    QMessageBox.critical(self, "Error", "Error occurred while deleting contents: " + str(e))
            else:
                QMessageBox.information(self, "Cancelled", "Operation cancelled by the user.")
        else:
            QMessageBox.information(self, "Error", "The directory does not exist: " + target_directory + ". You might not have a Copilot+ PC.")

if __name__ == "__main__":
    app = QApplication([])

    window = DeleteRecall()
    window.show()

    app.exec_()
