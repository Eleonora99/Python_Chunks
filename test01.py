import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox

def dialog():
    mbox = QMessageBox()

    mbox.setText("questo testa è l'area del testo")
    mbox.setDetailedText("invece queste è l'area del testo dettagliato !")
    mbox.setStandardButtons (QMessageBox.StandardButton.Ok|QMessageBox.StandardButton.Cancel) 
            
    mbox.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300,300)
    w.setWindowTitle("GUI4FUN - Eleonora")
    
    label = QLabel(w)
    label.setText("Eleonora 4 ever")
    label.move(100,130)
    label.show()

    btn = QPushButton(w)
    btn.setText('Conferma')
    btn.move(110,150)
    btn.show()
    btn.clicked.connect(dialog)

    
    w.show()
    sys.exit(app.exec())