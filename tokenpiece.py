from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLineEdit, QDialogButtonBox, QSizePolicy, QLabel, QSpacerItem, QTextEdit

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

        main_layout = QVBoxLayout()

        #PFP Label
        row1_layout = QHBoxLayout()
        pfp_label = QLabel("Profile Picture:")
        row1_layout.addWidget(pfp_label)
        main_layout.addLayout(row1_layout)

        #PFP & Name/Description
        row2_layout = QHBoxLayout()
        pfp = QTextEdit() #placeholder for importing image
        row2_layout.addWidget(pfp)

        name_label = QLabel("Name:")
        name = QLineEdit()
        row2_layout.addWidget(name_label)
        row2_layout.addWidget(name)
        main_layout.addLayout(row2_layout)


        # Health/Initiative row
        row3_layout = QHBoxLayout()
        hp_label = QLabel("Health Points:")
        hp_line = QLineEdit()
        row3_layout.addWidget(hp_label)
        row3_layout.addWidget(hp_line)

        initiative_label = QLabel("Initiative:")
        initiative_line = QLineEdit()
        row3_layout.addWidget(initiative_label)
        row3_layout.addWidget(initiative_line)
        main_layout.addLayout(row3_layout)

        # Button box setup
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        
        # Center the buttons using a horizontal layout with spacers
        button_layout = QHBoxLayout()
        button_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        button_layout.addWidget(button_box)
        button_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        
        main_layout.addLayout(button_layout)
        dialog.setLayout(main_layout)
        dialog.exec()

def accept():
    print("accept")