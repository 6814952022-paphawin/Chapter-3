# รายงานแบบฝึกหัด Socket API & Docker (Assignment 1 & 2)

**ข้อมูลผู้จัดทำ**
* ชื่อ-นามสกุล: นายปภาวิณ สืบวงษ์รุ่ง 
* รหัสนักศึกษา: 6814952022
* กลุ่ม/เซคชัน: sec 2

---

## 🛠️ แบบฝึกหัดที่ 1: ระบบ Chat ด้วย Docker (2 Clients & 1 Server)

### คำอธิบายการทำงาน
ระบบแชทนี้ประยุกต์ใช้ Socket API แบบ TCP ในการส่งข้อมูลระหว่าง Client 2 ตัว ผ่าน Server กลาง โดยรันอยู่ในรูปแบบของ Docker Multi-container และใช้ Docker Compose ในการจัดการ

### ขั้นตอนการเริ่มทำงาน (How to run)
1. เปิด Terminal และเข้าไปที่โฟลเดอร์แบบฝึกหัดที่ 1:
   ```bash
   cd exercise-1
2. สั่งรันคอนเทนเนอร์ทั้งหมดผ่าน Docker Compose:
  docker-compose up --build
3. การเข้าใช้งาน Client:
  เปิด Terminal ใหม่เพื่อเข้าคอนเทนเนอร์ Client 1:
    docker exec -it chat_client1 python client.py
  เปิด Terminal ใหม่เพื่อเข้าคอนเทนเนอร์ Client 2:
    docker exec -it chat_client2 python client.py
