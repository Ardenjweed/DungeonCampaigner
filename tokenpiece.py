from PySide6.QtWidgets import QDialog, QLineEdit, QDialogButtonBox, QLabel, QTextEdit, QGridLayout
from PySide6.QtCore import Qt

class Token:
    def __init__(self):
        self.profile = None
        self.name = ""
        self.initiative = 0
        self.health = 0
        self.ac = 0
        self.weapon = None
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.create_token()

    def create_token(self):
        dialog = QDialog()
        dialog.setWindowTitle("Token Sheet")
        dialog.setMinimumWidth(400)

        main_layout = QGridLayout()
        
        # Row 0: Profile Picture Section
        pfp_label = QLabel("Profile Picture:")
        main_layout.addWidget(pfp_label, 0, 0, 1, 2)  

        # Profile Picture (QTextEdit as placeholder)
        pfp = QTextEdit()
        pfp.setFixedSize(200, 200) 
        main_layout.addWidget(pfp, 1, 0, 2, 2)  

        # Row 1: Name and Description Field
        name_label = QLabel("Name:")
        main_layout.addWidget(name_label, 1, 2)  
        name = QLineEdit()
        main_layout.addWidget(name, 1, 3)  

        description_label = QLabel("Description:")
        main_layout.addWidget(description_label, 2, 2)  
        description = QLineEdit()
        main_layout.addWidget(description, 2, 3)  


        # Row 3: Health and Initiative
        hp_label = QLabel("Health Points:")
        main_layout.addWidget(hp_label, 3, 0)
        hp_line = QLineEdit()
        main_layout.addWidget(hp_line, 3, 1)

        initiative_label = QLabel("Initiative:")
        main_layout.addWidget(initiative_label, 3, 2)
        initiative_line = QLineEdit()
        main_layout.addWidget(initiative_line, 3, 3)

        # Button row (row 4)
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        main_layout.addWidget(button_box, 4, 0, 1, 4, alignment=Qt.AlignCenter)

        dialog.setLayout(main_layout)
        dialog.exec()

def accept():
    print("accept")