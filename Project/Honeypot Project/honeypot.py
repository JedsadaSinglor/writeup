import socket
import logging
import os
import time

# ชื่อไฟล์ต่าง ๆ ที่ใช้ในโปรแกรม
log_file = "honeypot.log"
blocked_ips_file = "blocked_ips.txt"
ip_log_file = "ip_addresses.txt"

# ตรวจสอบว่ามีไฟล์อยู่แล้วหรือไม่ ถ้าไม่ให้สร้างไฟล์ใหม่
if not os.path.exists(log_file):
    with open(log_file, 'w') as f:
        pass  # สร้างไฟล์เปล่า
if not os.path.exists(blocked_ips_file):
    with open(blocked_ips_file, 'w') as f:
        pass  # สร้างไฟล์เปล่า
if not os.path.exists(ip_log_file):
    with open(ip_log_file, 'w') as f:
        pass  # สร้างไฟล์เปล่า

# ตั้งค่าการบันทึก log
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

# กำหนดเกณฑ์การบล็อก IP
MAX_ATTEMPTS = 3
BLOCK_TIME = 60  # บล็อก 60 วินาที
connection_attempts = {}

# ฟังก์ชันในการบันทึก IP
def log_ip(ip_address):
    with open(ip_log_file, 'a') as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {ip_address}\n")

# ฟังก์ชันในการบล็อก IP
def block_ip(ip_address):
    with open(blocked_ips_file, 'a') as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - BLOCKED - {ip_address}\n")
    connection_attempts[ip_address] = time.time()

# ฟังก์ชันตรวจสอบว่า IP ถูกบล็อกหรือไม่
def is_blocked(ip_address):
    if ip_address in connection_attempts:
        if time.time() - connection_attempts[ip_address] < BLOCK_TIME:
            return True
    return False

# ตั้งค่า Honeypot
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 9999))  # Bind กับ IP ทุกตัวที่เข้ามายัง port 9999
server_socket.listen(5)  # จำกัดการเชื่อมต่อสูงสุด 5 คิว

print("Honeypot is running on port 9999...")

while True:
    client_socket, client_address = server_socket.accept()
    ip_address = client_address[0]
    
    if is_blocked(ip_address):
        print(f"Connection attempt from blocked IP: {ip_address}")
        logging.info(f"Blocked IP tried to connect: {ip_address}")
        client_socket.close()
        continue
    
    print(f"Connection established from {ip_address}")
    logging.info(f"Connection established from {ip_address}")
    log_ip(ip_address)

    # นับจำนวนครั้งที่ IP เข้ามาเชื่อมต่อ
    if ip_address not in connection_attempts:
        connection_attempts[ip_address] = 1
    else:
        connection_attempts[ip_address] += 1

    if connection_attempts[ip_address] > MAX_ATTEMPTS:
        print(f"Blocking IP: {ip_address}")
        logging.info(f"Blocking IP: {ip_address}")
        block_ip(ip_address)
    
    client_socket.sendall(b"Hello! You have reached the honeypot!\n")
    client_socket.close()
