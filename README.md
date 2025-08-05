
# 🔐 QR Code Generator for Secrets & UPI Payments (India Only 🇮🇳)

Ever wanted to share a **secret** without saying it out loud? Or let someone pay you via UPI without spelling out your ID 5 times?  
This Python project makes it super simple (and kinda cool) to do both using QR codes.

---

## ✨ Features

🎯 **2-in-1 Tool:**
- ✅ Generate QR for **secret messages** (instead of typing them publicly).
- ✅ Generate **UPI Payment QR** codes to:
  - Just share your UPI ID.
  - OR set a fixed amount to avoid bargaining (😉).

🎨 **Interactive UX:**
- Fun greetings every time you run it (because why not?).
- Clean terminal prompts with emoji-powered vibes.

🖼️ **Save & Share:**
- Option to **save** QR code images for later.
- Works offline, fast, and easy.

---

## 💡 Use Cases

- 🔏 Share private links/messages with friends.
- 💸 Get paid instantly using UPI QR.
- 🛍️ Street vendors / freelancers who want fixed-amount UPI requests.
- 🤫 Classroom quizzes, party games, mystery notes — now in QR form!

---

## 🛠 How It Works

1. Clone or download this repo.
2. Run the script:
   ```bash
   python qr_generator.py
   ```
3. Choose:
   - `1` to generate **secret text QR**.
   - `2` to generate **UPI payment QR** (with or without amount limit).
4. QR is shown instantly. You can also choose to save it as an image.

---

## 📸 Screenshots

| Secret QR | UPI QR with Amount |
|-----------|--------------------|
| ![secret_qr](./sample_qrs/secret_qr.png) | ![upi_qr](./sample_qrs/upi_qr.png) |

> *(You can generate your own and replace these with actual screenshots from your run!)*

---

## 🧠 Behind the Scenes

- Built using the Python `qrcode` library.
- No internet required (except for UPI payments to work, obviously).
- Supports **Indian UPI only** (INR as default currency).

---

## 📦 Requirements

- Python 3.x
- qrcode:
  ```bash
  pip install qrcode[pil]
  ```

---

## 🚀 What's Next?

- [ ] Add GUI (using Tkinter or PyQt)
- [ ] Add UPI name & note customization
- [ ] Encrypt secret text before generating QR
- [ ] Build a simple Flask Web App version

---

## 🤝 Contribute?

Feel free to fork, star, suggest ideas or PR!  
Made for fun and learning. Let’s build together.

---

## 👨‍💻 Author

Made with love by [YourNameHere]  
For feedback, collabs, or just to say hi: [your_email@example.com]

---

## 📢 Note

This tool was designed with **Indian UPI system in mind**.  
International users might have to modify the code for their own payment gateways.

---

Happy Scanning! 🖤  
```

---

Let me know if you want a **cool badge section** (`[![Made With Python](...)]`) or want to convert this into a **Markdown with images and demo video embedded**. I can even generate a sample folder structure if you're planning to organize your GitHub repo like a pro.
