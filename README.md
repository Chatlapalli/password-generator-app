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

---

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

---

## 📸 Screenshot

![App Screenshot](screenshots/app.png)

---

## ▶️ How to Run

### Using Python:

1. Clone the repo:

2. Run the Python script:


---

### Using EXE:

1. Open the `dist/` folder  
2. Run `password_gui.exe`  
3. Passwords will be saved in the **same folder as the EXE**  

---

## 🧠 How it Works

1. Enter desired password length  
2. Select options (letters, numbers, symbols)  
3. Click **Generate Password**  
4. Password strength is shown (Weak / Medium / Strong)  
5. Copy or save passwords using the buttons  
6. Saved passwords are stored in `passwords.txt` in the same folder  

---

## 🔮 Future Improvements

- Dark mode UI  
- Master password protection  
- Encrypt saved passwords  
- Add copy-to-clipboard history  

---

## 👨‍💻 Author

**Gayathri Chatlapalli**  
- GitHub: [https://github.com/Chatlapalli](https://github.com/Chatlapalli)  
- LinkedIn: [https://www.linkedin.com/in/chvsgayathri-0059161aa](https://www.linkedin.com/in/chvsgayathri-0059161aa)  
- Email: chvsgayathri@gmail.com  

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
