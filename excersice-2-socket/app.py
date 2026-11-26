from flask import Flask, request, render_template_string
import socket

app = Flask(__name__)

page_html = """
<!doctype html>
<html lang="th">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Socket Message Studio</title>
  <style>
    :root { color-scheme: light; --ink: #182333; --muted: #718096; --line: #e4eaf2; --blue: #4169e1; }
    * { box-sizing: border-box; }
    body {
      min-height: 100vh; margin: 0; padding: 32px 18px; display: grid; place-items: center;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif; color: var(--ink);
      background: radial-gradient(ellipse at 15% 5%, #dce9ff 0, transparent 38%),
                  radial-gradient(ellipse at 90% 90%, #e5e2ff 0, transparent 34%), #f5f7fb;
    }
    .shell { width: min(100%, 720px); }
    .topline { display: flex; align-items: center; gap: 11px; margin: 0 0 18px 6px; color: #526174; font-size: 13px; font-weight: 700; letter-spacing: .09em; text-transform: uppercase; }
    .mark { width: 34px; height: 34px; display: grid; place-items: center; border-radius: 11px; color: white; background: linear-gradient(145deg, #6587f6, #7959d8); box-shadow: 0 5px 14px #526bd64a; font-size: 17px; }
    .card { overflow: hidden; border: 1px solid #ffffff; border-radius: 24px; background: #ffffffed; box-shadow: 0 24px 70px #30456c1c, 0 2px 8px #30456c0a; }
    .hero { padding: 38px 42px 28px; }
    .eyebrow { margin: 0 0 10px; color: var(--blue); font-size: 12px; font-weight: 800; letter-spacing: .12em; text-transform: uppercase; }
    h1 { margin: 0; font-size: clamp(27px, 5vw, 38px); line-height: 1.15; letter-spacing: -.04em; }
    .intro { max-width: 520px; margin: 13px 0 0; color: var(--muted); font-size: 15px; line-height: 1.7; }
    form { padding: 0 42px 34px; }
    label { display: block; margin-bottom: 10px; font-size: 13px; font-weight: 700; }
    textarea { display: block; width: 100%; min-height: 150px; resize: vertical; padding: 15px 16px; border: 1px solid var(--line); border-radius: 14px; outline: none; background: #fbfcfe; color: var(--ink); font: inherit; line-height: 1.6; transition: border .2s, box-shadow .2s, background .2s; }
    textarea:focus { border-color: #829cf3; background: white; box-shadow: 0 0 0 4px #4169e11c; }
    textarea::placeholder { color: #a2adbc; }
    .actions { display: flex; align-items: center; justify-content: space-between; gap: 16px; margin-top: 16px; }
    .hint { color: #8a96a6; font-size: 12px; }
    button { display: inline-flex; align-items: center; justify-content: center; gap: 9px; min-height: 46px; padding: 0 20px; border: 0; border-radius: 12px; color: white; background: linear-gradient(135deg, #5278ee, #6758d5); box-shadow: 0 8px 18px #5e69dc38; font: inherit; font-size: 14px; font-weight: 700; cursor: pointer; transition: transform .15s, box-shadow .15s; }
    button:hover { transform: translateY(-1px); box-shadow: 0 11px 22px #5e69dc4a; }
    button:active { transform: translateY(0); }
    .result { margin: 0 42px 34px; padding: 20px; border: 1px solid #e2e9f4; border-radius: 16px; background: #f8faff; }
    .result-title { margin: 0 0 14px; font-size: 14px; }
    .result-title span { color: #32936b; }
    .result-label { margin: 13px 0 5px; color: #8490a0; font-size: 11px; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; }
    .result p { margin: 0; overflow-wrap: anywhere; white-space: pre-wrap; line-height: 1.6; }
    .footer { padding: 16px 42px; border-top: 1px solid #edf0f5; color: #98a2af; font-size: 11px; }
    @media (max-width: 540px) { body { padding: 20px 12px; } .hero { padding: 30px 24px 22px; } form { padding: 0 24px 26px; } .result { margin: 0 24px 26px; } .footer { padding: 15px 24px; } .actions { align-items: flex-start; flex-direction: column; } button { width: 100%; } }
  </style>
</head>
<body>
  <main class="shell">
    <div class="topline"><span class="mark">↗</span> Socket Message Studio</div>
    <section class="card">
      <header class="hero">
        <p class="eyebrow">Simple · Fast · Connected</p>
        <h1>ส่งข้อความถึง<br>Socket Server</h1>
        <p class="intro">พิมพ์ข้อความของคุณ แล้วส่งไปยังเซิร์ฟเวอร์เพื่อดูการตอบกลับได้ทันที</p>
      </header>
      <form method="post">
        <label for="message">ข้อความของคุณ</label>
        <textarea id="message" name="message" placeholder="ลองพิมพ์ข้อความที่นี่..." required>{{ message }}</textarea>
        <div class="actions">
          <span class="hint">ข้อความจะถูกส่งผ่าน TCP socket</span>
          <button type="submit">ส่งข้อความ <span aria-hidden="true">→</span></button>
        </div>
      </form>
      {% if response is not none %}
      <section class="result" aria-live="polite">
        <h2 class="result-title"><span>●</span> รับการตอบกลับแล้ว</h2>
        <div class="result-label">ข้อความที่ส่ง</div>
        <p>{{ message }}</p>
        <div class="result-label">Socket server ตอบกลับ</div>
        <p>{{ response }}</p>
      </section>
      {% endif %}
      <footer class="footer">Flask interface <span aria-hidden="true">·</span> TCP connection</footer>
    </section>
  </main>
</body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    response = None
    if request.method == 'POST':
        message = request.form.get('message', '')
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect(('socket_server', 12345))
            client_socket.sendall(message.encode())
            response = client_socket.recv(1024).decode()
        finally:
            client_socket.close()

    return render_template_string(page_html, message=message, response=response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
