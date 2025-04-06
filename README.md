# Nmap Django Web Scanner

## Overview

**Nmap Django Web Scanner** is a web-based application built using Django and Nmap to perform network scanning for open ports on a given target. This project is designed to allow users to scan IP addresses or hostnames for open ports and get a detailed report on the results directly through a web interface.

## Features

- **Network Scanning**: Perform Nmap scans on remote targets.
- **Port Detection**: Detect open ports and services running on the target machine.
- **Django Interface**: A user-friendly web interface for entering target IP addresses or hostnames.
- **Real-Time Feedback**: View live results for scanned targets.

## Installation

Follow these steps to set up the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/muhammadazmeerahmad/nmap-django-scanner.git

# Nmap Django Scanner - Project Setup Instructions

This guide explains how to set up and run this project on your local machine after cloning it from GitHub.

## Clone the Project from GitHub
git clone https://github.com/muhammadazmeerahmad/nmap-django-scanner.git

cd nmap-django-scanner

## Create Virtual Environment
python -m venv venv

### Activate Virtual Environment
- For Windows:
venv\Scripts\activate

- For Linux/Mac:
source venv/bin/activate

## Install All Dependencies
pip install -r requirements.txt

## Run Django Server
python manage.py runserver

## Access Web Application
Open your browser and go to:
http://127.0.0.1:8000/scan/

## Project Structure
nmap-django-scanner/
│
├── manage.py
├── requirements.txt
├── setup/
│   └── setup_instructions.txt
│
├── vulnscanner/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── scanner/
│   ├── templates/
│   │   └── index.html
│   ├── views.py
│   └── urls.py
│
├── db.sqlite3
└── venv/

## Technologies Used
- Python
- Django
- Nmap (python-nmap library)

## Note:
- Before running the project make sure Nmap is installed on your machine.
- Install it from → https://nmap.org/download.html

## Author
Muhammad Azmeer Ahmad

GitHub Profile: https://github.com/muhammadazmeerahmad
