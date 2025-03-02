import sys
from PySide6.QtCore import QTime, QTimer, Slot, Qt
from PySide6.QtWidgets import QApplication, QLCDNumber, QVBoxLayout, QWidget, QPushButton, QColorDialog
from PySide6.QtGui import QColor, QPalette

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Create main layout
        layout = QVBoxLayout()
        
        # Create LCD Display
        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(8)  # 6 digits and 2 colons
        self.lcd.setSegmentStyle(QLCDNumber.Filled)
        
        # Set initial color
        self.display_color = QColor(0, 255, 0)  # Default green color
        self.updateColor()
        
        # Create color button
        self.color_button = QPushButton('Change Color')
        self.color_button.clicked.connect(self.changeColor)
        
        # Add widgets to layout
        layout.addWidget(self.lcd)
        layout.addWidget(self.color_button)
        
        # Set the layout
        self.setLayout(layout)
        
        # Setup window properties
        self.setWindowTitle("Digital Clock")
        self.resize(1000, 300)
        self.setStyleSheet("background-color: black;")
        
        # Remove window frame
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        # Setup timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.displayTime)
        self.timer.start(1000)  # Update every second
        
        # Initial display
        self.displayTime()
        
    @Slot()
    def displayTime(self):
        current_time = QTime.currentTime()
        display_text = current_time.toString("hh:mm:ss")
        self.lcd.display(display_text)
        
    def changeColor(self):
        color = QColorDialog.getColor(self.display_color, self)
        if color.isValid():
            self.display_color = color
            self.updateColor()
            
    def updateColor(self):
        palette = self.lcd.palette()
        # Fixed: Changed WindowText to windowText
        palette.setColor(QPalette.WindowText, self.display_color)
        self.lcd.setPalette(palette)
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
            
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()
            
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPosition().toPoint() - self.dragPosition)
            event.accept()

def main():
    app = QApplication(sys.argv)
    
    # Create and show the clock
    clock = DigitalClock()
    clock.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
