from logic import *

def main():
    application = QApplication([])
    window = Logic()
    window.setWindowTitle("Voting")
    window.show()
    application.exec()


if __name__ == '__main__':
    main()