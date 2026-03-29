# 🔍 network-reconnaissance-tool

A fast, multi-threaded port scanner built in Python for cybersecurity learning and lab environments.

---

## 🚀 Features

- ⚡ Multi-threaded scanning (fast performance)
- 🌐 Scan custom IP addresses and port ranges
- 🧠 Service detection (FTP, SSH, HTTP, etc.)
- 📡 Banner grabbing support
- 📁 Export results to CSV
- 💻 Command-line interface (CLI)

---

## 🛠️ Technologies Used

- Python 3
- Socket Programming
- ThreadPoolExecutor (Concurrency)
- Argparse (CLI handling)

---

## ▶️ Usage

### Basic Scan
```bash
python3 scanner.py -t 127.0.0.1 -p 1-1000

Scanning 192.168.56.101
Started at: 2026-03-29

[OPEN] Port 21 (FTP)
[OPEN] Port 22 (SSH)
[OPEN] Port 80 (HTTP)

Scan Complete

🧪 Lab Setup
- Kali Linux (Attacker Machine)
- Metasploitable 2 (Target Machine)
- VirtualBox (Host-Only Network)

⚠️ Disclaimer

This tool is for educational purposes only.

Only use on:
- Systems you own
- Authorized lab environments

Unauthorized scanning is illegal.

📌 Future Improvements
- Add colored output 🎨
- Improve service detection 🔍
- Build GUI version 🖥️
- Add vulnerability scanning integration

👨‍💻 Author

## James Lewis
Aspiring Cybersecurity Professional
