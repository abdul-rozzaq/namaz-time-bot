![alt](https://i.imgur.com/ax1RtVI.png)


# 🚀 FastAPI + python-telegram-bot Starter Template

A modern and developer-friendly starter template to build **Telegram bots** using [FastAPI](https://fastapi.tiangolo.com/) and [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot).

---

## 📦 Features

- ⚡ **FastAPI** based async webhook handling
- 🤖 **python-telegram-bot** v20+ support
- 🧱 Well-organized folder structure
- 🔌 CLI commands to manage the server and webhooks
- 📁 `.env` based configuration
- 🧪 Ready for deployment (Uvicorn, Docker optional)

---

## 🗂️ Project Structure

```
src/
├── config/              # Settings, environment variables
│   └── settings.py
├── controllers/         # Telegram webhook controller
│   └── webhook.py
├── core/                # Lifespan handlers, utilities
│   └── lifespan.py
├── services/            # Main bot logic
│   ├── bot.py           # Bot application
│   └── cli.py           # CLI application
│   main.py              # FastAPI app instance
├── .env.example         # Example environment variables
├── run.py               # CLI runner (runserver, set-webhook, etc)
```

---

## ⚙️ Setup & Usage

### 1. Clone the repository

```bash
git clone https://github.com/abdul-rozzaq/fastapi-telegram-bot.git
cd fastapi-telegram-bot
```

### 2. Create environment file

```bash
cp .env.example .env
```

Fill in your `.env` file:

```env
BOT_TOKEN=your_bot_token
WEBHOOK_DOMAIN=https://yourdomain.com
```

### 3. Run local server

```bash
python run.py runserver
```

### 4. Set or delete webhook

```bash
# Set Telegram webhook
python run.py set-webhook

# Delete Telegram webhook
python run.py delete-webhook
```

---

## 📸 Screenshot

Here’s how the project looks inside VSCode:

![Project Screenshot](https://i.imgur.com/W7voTlK.png)

---

## 🧪 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [python-telegram-bot](https://docs.python-telegram-bot.org/)
- [Uvicorn](https://www.uvicorn.org/)
- Python 3.10+

---

## 📌 Why this template?

Telegram bot development usually starts with:
- Rewriting webhook logic
- Copy-pasting CLI tools
- Manually testing endpoint lifecycle

This template removes all the friction and lets you focus on **building features**.

---

## 🛠️ TODO (Contributions Welcome!)

- [ ] Add example handlers (start/help commands)
- [ ] Docker support
- [ ] Add logging
- [ ] Deployment guides (Railway, Render, etc)

---

## 🤝 Contributing

Pull requests, issues and ideas are welcome!  
If you find this useful, consider giving it a ⭐ star.

---

## 📜 License

MIT License.  
Free to use, modify, and share.

---

## 🙌 Made with ❤️ by a developer who loves bots.