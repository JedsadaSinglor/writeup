# Simple Keylogger in Python

โปรเจกต์นี้เป็น Keylogger ง่าย ๆ ที่เขียนด้วย Python เพื่อบันทึกการกดปุ่มบนคีย์บอร์ด โดยจะบันทึกข้อมูลลงในไฟล์ `keylog.txt` และหยุดการทำงานเมื่อกดปุ่ม Esc

## คุณสมบัติ

- บันทึกการกดปุ่มทั้งหมดในไฟล์ `keylog.txt`
- หยุดการทำงานเมื่อกดปุ่ม Esc
- ใช้งานง่ายและไม่ต้องการการติดตั้งซอฟต์แวร์เพิ่มเติม

## สิ่งที่ต้องการ

- Python 3.x
- ไลบรารี `pynput`

## วิธีการติดตั้ง

1. **ดาวน์โหลดโปรเจกต์**:
   ```bash
   git clone https://github.com/your-username/keylogger-project.git
   cd keylogger-project
