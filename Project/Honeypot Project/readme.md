# Honeypot ง่าย ๆ ใน Python (thai ver.)

โครงการนี้เป็นโปรเจกต์ Honeypot ง่าย ๆ ที่เขียนด้วย Python ซึ่งสามารถทำงานได้บน Windows และ Linux โดยจะฟังการเชื่อมต่อเข้ามาทางพอร์ตที่กำหนด และบันทึก IP ที่พยายามเชื่อมต่อ พร้อมทั้งบล็อก IP ที่มีพฤติกรรมผิดปกติ

## คุณสมบัติ

- ฟังการเชื่อมต่อบนพอร์ต 9999 (สามารถเปลี่ยนแปลงได้)
- บันทึก IP ที่เชื่อมต่อในไฟล์ `ip_addresses.txt`
- บล็อก IP หลังจากพยายามเชื่อมต่อเกิน 3 ครั้ง (สามารถปรับได้)
- บันทึก IP ที่ถูกบล็อกในไฟล์ `blocked_ips.txt`
- บันทึกการพยายามเชื่อมต่อทั้งหมดลงในไฟล์ `honeypot.log`
- หากไม่มีไฟล์ `honeypot.log`, `ip_addresses.txt`, หรือ `blocked_ips.txt` จะสร้างไฟล์ใหม่ให้อัตโนมัติ

## สิ่งที่ต้องการ

- Python 3.x
- รองรับทั้ง Linux และ Windows

## วิธีการรัน

1. **ดาวน์โหลดโปรเจกต์**:
   ```bash
   git clone https://github.com/your-username/honeypot-project.git
   cd honeypot-project



# Simple Honeypot in Python (eng ver.)

This is a simple honeypot written in Python designed to run on Windows and Linux. It listens on a specified port, logs connection attempts, and blocks IPs that attempt to connect more than a predefined number of times. This is ideal for learning purposes and for detecting unauthorized access attempts.

## Features

- Listens on port 9999 (can be changed) for incoming connections.
- Logs all incoming IP addresses to `ip_addresses.txt`.
- Blocks IPs after 3 unsuccessful attempts (configurable).
- Logs blocked IPs to `blocked_ips.txt`.
- Logs all connection attempts to `honeypot.log`.
- Automatically creates log files if they do not exist.

## Requirements

- Python 3.x
- Works on both Linux and Windows systems

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/honeypot-project.git
   cd honeypot-project
