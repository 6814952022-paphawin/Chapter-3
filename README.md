# รายงานแบบฝึกหัด Socket API & Docker (Assignment 1 & 2)

**ข้อมูลผู้จัดทำ**
* ชื่อ-นามสกุล: นายปภาวิณ สืบวงษ์รุ่ง 
* รหัสนักศึกษา: 6814952022
* กลุ่ม/เซคชัน: sec 2

---

## 🛠️ แบบฝึกหัดที่ 1: ระบบ Chat ด้วย Docker (2 Clients & 1 Server)

### คำอธิบายการทำงาน
ระบบแชทนี้ประยุกต์ใช้ Socket API แบบ TCP ในการส่งข้อมูลระหว่าง Client 2 ตัว ผ่าน Server กลาง โดยรันอยู่ในรูปแบบของ Docker Multi-container และใช้ Docker Compose ในการจัดการ

### ขั้นตอนการเริ่มทำงาน (How to Run)

**1. เปิด Terminal และเข้าไปยังโฟลเดอร์แบบฝึกหัดที่ 1**

```bash
cd exercise-1
```

**2. สั่งรันคอนเทนเนอร์ทั้งหมดผ่าน Docker Compose**

```bash
docker-compose up --build
```

**3. การเข้าใช้งาน Client**

เปิด Terminal ใหม่เพื่อเข้าใช้งาน Client 1:

```bash
docker exec -it chat_client1 python client.py
```

เปิด Terminal อีกหน้าต่างหนึ่งเพื่อเข้าใช้งาน Client 2:

```bash
docker exec -it chat_client2 python client.py
```

Chapter 1 chat-app
<img width="1270" height="576" alt="สกรีนช็อต 2026-11-26 092825" src="https://github.com/user-attachments/assets/317ab482-5e31-4453-acbf-a7a7175691e4" />
<img width="1273" height="579" alt="สกรีนช็อต 2026-11-26 092843" src="https://github.com/user-attachments/assets/419ad009-537f-429b-b87c-eb17ed91b825" />

Chapter 2 socket
<img width="1918" height="993" alt="สกรีนช็อต 2026-11-26 101212" src="https://github.com/user-attachments/assets/a9279da1-b3c8-4f0b-87b3-a055813a6d58" />


