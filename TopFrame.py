import random
from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout, QPushButton, QGraphicsDropShadowEffect
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt


class TopFrame(QFrame):
    color_emojis = [
        ("#FF0000", "🟥 Red"), ("#FF7F00", "🟧 Orange"), ("#FFFF00", "🟨 Yellow"),
        ("#00FF00", "🟩 Green"), ("#0000FF", "🟦 Blue"), ("#800080", "🟪 Purple"),
        ("#A52A2A", "🟫 Brown"), ("#000000", "⬛ Black"), ("#FFFFFF", "⬜ White"),
    ]

    def __init__(self, main_window=None, parent=None):
        super().__init__(parent)
        self.main_window = main_window

        self.setFixedHeight(100)
        self.setStyleSheet("background-color: black;")

        self.title_label = QLabel("TOOLS AUTO \n DOWNLOAD", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        font = QFont("Droid Serif", 26, QFont.Bold)
        font.setItalic(True)
        self.title_label.setFont(font)
        self.set_title_glow("#E0240B")

        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        self.setLayout(layout)

        # Buttons creation
        self.left_button_4 = QPushButton("4", self)
        self.apply_button_style(self.left_button_4, "gold")
        self.left_button_4.setFixedSize(40, 40)

        self.left_button_5 = QPushButton("5", self)
        self.apply_button_style(self.left_button_5, "gold")
        self.left_button_5.setFixedSize(40, 40)

        self.left_button_6 = QPushButton("6", self)
        self.apply_button_style(self.left_button_6, "gold")
        self.left_button_6.setFixedSize(40, 40)

        self.right_button_1 = QPushButton("1", self)
        self.apply_button_style(self.right_button_1, "orange")
        self.right_button_1.setFixedSize(40, 40)

        self.right_button_2 = QPushButton("2", self)
        self.apply_button_style(self.right_button_2, "orange")
        self.right_button_2.setFixedSize(40, 40)

        self.right_button_3 = QPushButton("3", self)
        self.apply_button_style(self.right_button_3, "orange")
        self.right_button_3.setFixedSize(40, 40)

        # Connect buttons to slots
        self.left_button_4.clicked.connect(self.on_button_4_clicked)
        self.left_button_5.clicked.connect(self.on_button_5_clicked)
        self.left_button_6.clicked.connect(self.on_button_6_clicked)
        self.right_button_1.clicked.connect(self.on_button_1_clicked)
        self.right_button_2.clicked.connect(self.on_button_2_clicked)
        self.right_button_3.clicked.connect(self.on_button_3_clicked)

    def resizeEvent(self, event):
        spacing, btn_size = 10, 40

        self.left_button_4.move(spacing + 0 * (btn_size + spacing), (self.height() - btn_size) // 2)
        self.left_button_5.move(spacing + 1 * (btn_size + spacing), (self.height() - btn_size) // 2)
        self.left_button_6.move(spacing + 2 * (btn_size + spacing), (self.height() - btn_size) // 2)

        start_x = self.width() - (btn_size + spacing) * 3 - spacing
        self.right_button_1.move(start_x + 0 * (btn_size + spacing), (self.height() - btn_size) // 2)
        self.right_button_2.move(start_x + 1 * (btn_size + spacing), (self.height() - btn_size) // 2)
        self.right_button_3.move(start_x + 2 * (btn_size + spacing), (self.height() - btn_size) // 2)

    def set_title_glow(self, color="#8D7907"):
        glow = QGraphicsDropShadowEffect(self)
        glow.setBlurRadius(25)
        glow.setOffset(0)
        glow.setColor(QColor(color))
        self.title_label.setGraphicsEffect(glow)
        self.title_label.setStyleSheet(f"color: {color};")

    def apply_button_style(self, button, name_color="gold"):
        button.setStyleSheet(f"""
            QPushButton {{
                background-color: black;
                color: {name_color};
                border: 2px solid {name_color};
                border-radius: 20px;
                padding: 7px 15px;
                font-weight: bold;
                font-size: 14px;
            }}
            QPushButton:hover {{
                background-color: #111111;
            }}
        """)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setColor(QColor(name_color))
        shadow.setOffset(0, 0)
        button.setGraphicsEffect(shadow)

    def on_button_4_clicked(self):
        color, name = random.choice(self.color_emojis)
        print(f"Button 4 clicked: changing glow to {name}")
        self.set_title_glow(color)

    def on_button_5_clicked(self):
        print("Button 5 clicked: changing TopFrame background randomly")
        color, name = random.choice(self.color_emojis)
        self.setStyleSheet(f"background-color: {color};")

    def on_button_6_clicked(self):
        color, name = random.choice(self.color_emojis)
        print(f"Button 6 clicked: changing MainWindow background to {name}")
        if self.main_window:
            self.main_window.change_background_color_and_title(color, name)

    def on_button_1_clicked(self):
        print("Button 1 clicked: toggling stay-on-top")
        if self.main_window:
            current_flag = self.main_window.windowFlags()
            if current_flag & Qt.WindowStaysOnTopHint:
                print("→ Switching to normal window mode")
                self.main_window.setWindowFlag(Qt.WindowStaysOnTopHint, False)
            else:
                print("→ Switching to always-on-top mode")
                self.main_window.setWindowFlag(Qt.WindowStaysOnTopHint, True)
            self.main_window.show()

    def on_button_2_clicked(self):
        print("Button 2 clicked: minimizing window")
        if self.main_window:
            self.main_window.showMinimized()

    def on_button_3_clicked(self):
        print("Button 3 clicked: exiting application")
        if self.main_window:
            self.main_window.close()
