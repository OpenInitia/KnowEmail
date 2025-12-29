import sys
from src.gui import EmailValidatorApp
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from lib.validators import is_valid_email_syntax, has_mx_record, verify_email_smtp

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = EmailValidatorApp()
    window.show()
    sys.exit(app.exec_())