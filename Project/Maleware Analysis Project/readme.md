# Malware Analysis Tool (thai ver.)

## รายละเอียดโปรเจกต์
เครื่องมือนี้ถูกสร้างขึ้นเพื่อวิเคราะห์ไฟล์ PE (Portable Executable) โดยไม่ต้องรันไฟล์มัลแวร์จริงๆ โปรแกรมจะให้ข้อมูลสำคัญเกี่ยวกับไฟล์ เช่น ขนาดไฟล์ วันที่สร้าง จุดเริ่มต้นการทำงาน และแฮช SHA-256 ของไฟล์ เพื่อช่วยในการวิเคราะห์ความปลอดภัยของไฟล์

## คุณสมบัติ
- ตรวจสอบขนาดของไฟล์
- แสดงวันที่สร้างไฟล์
- ระบุจุดเริ่มต้นการทำงานของโปรแกรม
- คำนวณแฮช SHA-256 ของไฟล์
- แสดงรายละเอียดเกี่ยวกับเซ็กชันในไฟล์

## การติดตั้ง
1. ติดตั้ง Python 3.x หากยังไม่ได้ติดตั้ง
2. ติดตั้งไลบรารีที่จำเป็น:
   ```bash
   pip install pefile

## วิธีการใช้งาน

1. **ดาวน์โหลดโปรแกรม**:
   - ดาวน์โหลดไฟล์ `malware_analysis.py` และบันทึกไว้ในโฟลเดอร์ที่คุณต้องการ

2. **ติดตั้งไลบรารีที่จำเป็น**:
   - คุณต้องติดตั้งไลบรารี `pefile` โดยใช้คำสั่ง pip:
     ```bash
     pip install pefile
     ```

3. **รันโปรแกรม**:
   - เปิด Terminal หรือ Command Prompt และไปยังโฟลเดอร์ที่คุณบันทึกไฟล์ `malware_analysis.py`
   - ใช้คำสั่งต่อไปนี้เพื่อรันโปรแกรม:
     ```bash
     python malware_analysis.py <file_path>
     ```
   - แทนที่ `<file_path>` ด้วยที่อยู่ของไฟล์ PE ที่คุณต้องการวิเคราะห์

4. **ตรวจสอบผลลัพธ์**:
   - โปรแกรมจะแสดงผลการวิเคราะห์เกี่ยวกับไฟล์ PE ที่คุณระบุ
   ```bash
      --- Analyzing the file: sample.exe --- File Size: 123456 bytes

   This shows how big the file is. Creation Date: 2024-10-19 12:34:56
   This is when the file was created. Entry Point: 0x00401234
   This is where the program starts running in memory. SHA-256 Hash: abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890
   This is a unique code for this file based on its content.
   Sections of the file:

   .text: 102400 bytes [!] This section may contain executable code.
   .data: 20480 bytes
   --- Analysis Complete ---
   ```

## Malware Analysis Tool (eng ver.)

This project is a tool for analyzing PE (Portable Executable) files, allowing you to check basic information and specific characteristics of potentially malicious files.

### Usage

1. **Download the Program**:
   - Download the `malware_analysis.py` file and save it in your desired folder.

2. **Install Required Library**:
   - You need to install the `pefile` library using pip:
     ```bash
     pip install pefile
     ```

3. **Run the Program**:
   - Open Terminal or Command Prompt and navigate to the folder where you saved the `malware_analysis.py` file.
   - Use the following command to run the program:
     ```bash
     python malware_analysis.py <file_path>
     ```
   - Replace `<file_path>` with the path to the PE file you want to analyze.

4. **Check the Output**:
   - The program will display the analysis results for the specified PE file.
   ```bash
      --- Analyzing the file: sample.exe --- File Size: 123456 bytes

   This shows how big the file is. Creation Date: 2024-10-19 12:34:56
   This is when the file was created. Entry Point: 0x00401234
   This is where the program starts running in memory. SHA-256 Hash: abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890
   This is a unique code for this file based on its content.
   Sections of the file:

   .text: 102400 bytes [!] This section may contain executable code.
   .data: 20480 bytes
   --- Analysis Complete ---
   ```
