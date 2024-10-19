# Honeypot ด้วย Python (thai ver.)

โครงการนี้เป็นโปรเจกต์ Honeypot ที่เขียนด้วย Python ซึ่งสามารถทำงานได้บน Windows และ Linux โดยจะฟังการเชื่อมต่อเข้ามาทางพอร์ตที่กำหนดไว้ และบันทึก IP ที่พยายามเชื่อมต่อ พร้อมทั้งบล็อก IP ที่มีพฤติกรรมผิดปกติ

## คุณสมบัติการทำงาน

- ฟังการเชื่อมต่อบนพอร์ต 9999 (สามารถเปลี่ยนแปลงได้)
- บันทึก IP ที่เชื่อมต่อในไฟล์ `ip_addresses.txt`
- บล็อก IP หลังจากพยายามเชื่อมต่อเกิน 3 ครั้ง (สามารถปรับได้)
- บันทึก IP ที่ถูกบล็อกในไฟล์ `blocked_ips.txt`
- บันทึกการพยายามเชื่อมต่อทั้งหมดลงในไฟล์ `honeypot.log`
- หากไม่มีไฟล์ `honeypot.log`, `ip_addresses.txt`, หรือ `blocked_ips.txt` จะสร้างไฟล์ใหม่ให้อัตโนมัติ

## สิ่งที่ต้องการ

- Python 3.x
- รองรับทั้ง Linux และ Windows

## วิธีการใช้งาน

1. **ดาวน์โหลดโปรเจกต์**:
   - ดาวน์โหลดไฟล์ `honeypot.py` และบันทึกไว้ในโฟลเดอร์ที่คุณต้องการ

2. **ติดตั้ง Python**:
   - ตรวจสอบว่าคุณได้ติดตั้ง Python บนเครื่องของคุณแล้ว โดยใช้คำสั่งใน Terminal หรือ Command Prompt:
     ```bash
     python --version
     ```
   - หากยังไม่ได้ติดตั้ง Python สามารถดาวน์โหลดได้ที่ [python.org](https://www.python.org/downloads/)

3. **รันโปรแกรม**:
   - เปิด Terminal หรือ Command Prompt และไปยังโฟลเดอร์ที่คุณบันทึกไฟล์ `honeypot.py`
   - ใช้คำสั่งต่อไปนี้เพื่อรันโปรแกรม:
     ```bash
     python honeypot.py
     ```

4. **ตรวจสอบการทำงาน**:
   - เมื่อโปรแกรมรันอยู่ จะมีข้อความ "Honeypot is running on port 9999..." ปรากฏขึ้น
   - คุณสามารถลองเชื่อมต่อไปยัง Honeypot โดยใช้เครื่องมือเช่น `telnet` หรือ `netcat` (nc) จากเครื่องอื่น:
     ```bash
     telnet <IP address> 9999
     ```
     หรือ
     ```bash
     nc <IP address> 9999
     ```
   - เปลี่ยน `<IP address>` เป็น IP ของเครื่องที่รันโปรแกรม Honeypot

5. **ตรวจสอบไฟล์บันทึก**:
   - โปรแกรมจะบันทึก IP ที่เข้ามาเชื่อมต่อในไฟล์ `ip_addresses.txt`
   - หาก IP ถูกบล็อก โปรแกรมจะบันทึกข้อมูลลงในไฟล์ `blocked_ips.txt`
   - สามารถตรวจสอบไฟล์ `honeypot.log` เพื่อดูเหตุการณ์ที่เกิดขึ้น

6. **หยุดโปรแกรม**:
   - เมื่อคุณต้องการหยุดการทำงานของ Honeypot สามารถกด `Ctrl + C` ใน Terminal หรือ Command Prompt

# Honeypot in Python (eng ver.)

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

2. **Install Python**:
   - Make sure you have Python installed on your machine by using the following command in the Terminal or Command Prompt:
     ```bash
     python --version
     ```
   - If Python is not installed, you can download it from [python.org](https://www.python.org/downloads/).

3. **Run the Program**:
   - Open Terminal or Command Prompt and navigate to the folder where you saved the `honeypot.py` file.
   - Use the following command to run the program:
     ```bash
     python honeypot.py
     ```

4. **Check the Operation**:
   - When the program is running, you will see the message "Honeypot is running on port 9999..."
   - You can try connecting to the Honeypot using tools like `telnet` or `netcat` (nc) from another machine:
     ```bash
     telnet <IP address> 9999
     ```
     or
     ```bash
     nc <IP address> 9999
     ```
   - Replace `<IP address>` with the IP of the machine running the Honeypot.

5. **Check the Log Files**:
   - The program will log the IPs that connect to it in the `ip_addresses.txt` file.
   - If an IP gets blocked, the information will be recorded in the `blocked_ips.txt` file.
   - You can check the `honeypot.log` file to see the events that occurred.

6. **Stop the Program**:
   - When you want to stop the Honeypot from running, you can press `Ctrl + C` in the Terminal or Command Prompt.

