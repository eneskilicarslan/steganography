import funcs
from gui import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog
# Example usage
# input_image = 'sample.png'

# # message = funcs.string_to_binary_string('AI will take over the world!')
# print("Message:", message)
# Embed text into the image


# output_image = funcs.embed_text(input_image, message, funcs.prime_numbers)

# Extract the hidden text from the modified image
# hidden_message = funcs.extract_text(output_image, funcs.prime_numbers)

# print("Hidden Message:", hidden_message)
# funcs.compare_images(input_image, output_image)


app = QApplication(sys.argv)
Dialog = QDialog()
ui = Ui_MainWindow()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())
