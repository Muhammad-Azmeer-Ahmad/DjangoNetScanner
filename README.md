# Django Net Scanner

🚀A **🌐web-based Nmap vulnerability scanner built with Django**, enabling users to scan and analyze open ports  🔓 and services on any target system. It offers a simple yet powerful 🖥️interface to perform network scans through the browser.🚀

---
## ⚠️ Important Note

This project is **currently not deployed online** 🌐 and is meant **only for educational purposes** 📘.  
It is designed to be **run locally on your own machine** 💻.

🛠️ **Feel free to:**
- 📥 Clone the repository  
- 🧑‍💻 Explore and modify the code  
- 🚀 Deploy it on your own server if you wish  
- 📈 Use it as a base for your learning or development journey

✅ Ideal for students, developers, and cybersecurity learners!

________________________________________________________________________________


## 🚀 Features

- **Network Scanning**: Perform real-time Nmap scans on IP addresses or domain names.
- **Port & Service Detection**: Detect open ports and identify services running on the target.
- **User-Friendly Interface**: Enter target information and view results in an intuitive web layout.
- **Customizable & Extendable**: Designed to be a starter project for learning and further development.

---

## 📦 Clone & Run Locally

To get started with this project locally:

### 📥Clone the repository:
```bash
git clone https://github.com/muhammadazmeerahmad/DjnagoNetScanner
cd DjangoNetScanner
```

## 🧪Create Virtual Environment:
```bash
python -m venv venv
```
### ⚙️ Activate it:
-**🪟Windows**:
```bash 
venv\Scripts\activate
```
-**🐧Linux/Mac**:
```bash
source venv/bin/activate
```

## 📦 Install Dependencies:
```bash
pip install -r requirements.txt
``` 

## 🟢 Run Server:
```bash
python manage.py runserver
```
Visit the web application in your browser:
🌐 http://127.0.0.1:8000


### 🗂️ Project Structure:
```bash
DjangoNetScanner/
│
├── manage.py                 # Django management script
├── requirements.txt          # Python package dependencies
│
├── setup/
│   └── setup_instructions.txt  # Optional setup notes
│
├── vulnscanner/              # Main Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── scanner/                  # App handling scan logic
│   ├── templates/
│   │   └── index.html        # Frontend HTML template
│   ├── views.py              # Scan logic (Nmap calls, rendering)
│   └── urls.py               # Routes for the scanner app
│
├── db.sqlite3                # Default Django database (for local use)
└── venv/                     # Python virtual environment
```

### 🛠️ Technologies Used:
- **🐍Python**
- **🌐Django**
- **🕵️‍♂️Nmap via python-nmap package**

### ⚠️ Requirements:
- **⚙️You must have Nmap installed on your system**
📥Download it here: https://nmap.org/download.html

