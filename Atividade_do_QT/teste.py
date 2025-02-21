import registro, sys
from registro import Ui_Form
 
if __name__=="__main__":
    app=QApplication(sys.argv)
    Form = QMainWindow()  
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())