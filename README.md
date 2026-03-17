# 🔐 Password Generator Application

A simple and secure **Password Generator** built using **Python** and **Tkinter**.  
This project generates strong passwords, shows their strength, allows copying, and saving them to a file. It also includes an executable version for direct use.

---

## 🚀 Features

- Generate strong passwords of any length  
- Choose to include:
  - Letters ✅
  - Numbers ✅
  - Symbols ✅
- Password strength indicator (Weak / Medium / Strong)  
- Copy password to clipboard  
- Save passwords to a file (`passwords.txt`) in the same folder  
- Clear saved passwords  
- Works as Python script **and** standalone EXE  

---

## 🖥️ Tech Stack

- Python 3.x  
- Tkinter (GUI)  
- PyInstaller (for EXE build)  
- Random module for password generation  
- OS module for file handling

## 📂 File Structure

```text
Password-Generator/
│
├── password_gui.py         # Main Python script
├── lock.ico                # App icon
├── README.md               # Project README
├── LICENSE                 # MIT License
├── .gitignore              # Ignore unnecessary files
├── dist/                   # Optional folder containing EXE
│   └── password_gui.exe
└── screenshots/
    └── app.png             # Screenshot of app

**▶️ How to Run**

Using Python:
Clone the repo:
git clone https://github.com/YourUsername/password-generator-app.git
cd password-generator-app
Run the Python script:
python password_gui.py
Using EXE:
Open the dist/ folder
Run password_gui.exe
Passwords will be saved in the same folder as the EXE

**🧠 How it Works**

Enter desired password length
Select options (letters, numbers, symbols)
Click Generate Password
Password strength is shown (Weak / Medium / Strong)
Copy or save passwords using the buttons
Saved passwords are stored in passwords.txt in the same folder

---

**🔮 Future Improvements**

Dark mode UI
Master password protection
Encrypt saved passwords
Add copy-to-clipboard history

**👨‍💻 Author**

Gayathri Chatlapalli
GitHub: https://github.com/Chatlapalli
LinkedIn: www.linkedin.com/in/chvsgayathri-0059161aa
Email: chvsgayathri@gmail.com

**📝 License**

This project is licensed under the MIT License - see the LICENSE file for details.
