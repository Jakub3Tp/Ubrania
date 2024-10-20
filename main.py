import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.sizeS.toggled.connect(self.button_clicked)
        self.ui.sizeM.toggled.connect(self.button_clicked)
        self.ui.sizeL.toggled.connect(self.button_clicked)
        self.ui.sizeXL.toggled.connect(self.button_clicked)

        self.ui.kurierButton.toggled.connect(self.button_clicked)
        self.ui.paczkomatButton.toggled.connect(self.button_clicked)
        self.ui.odbiorosobistyButton.toggled.connect(self.button_clicked)

        self.show()

    def button_clicked(self):
        size = ""
        deliveryMethod = ""

        if self.ui.sizeS.isChecked():
            size = "S"
        elif self.ui.sizeM.isChecked():
            size = "M"
        elif self.ui.sizeL.isChecked():
            size = "L"
        elif self.ui.sizeXL.isChecked():
            size = "XL"

        if self.ui.kurierButton.isChecked():
            deliveryMethod = "Kurier"
        elif self.ui.paczkomatButton.isChecked():
            deliveryMethod = "Paczkomat"
        elif self.ui.odbiorosobistyButton.isChecked():
            deliveryMethod = "Odbiór osobisty"

        self.ui.resultLabel.setText(f'Rozmiar: {size}, Metoda dostawy: {deliveryMethod}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())