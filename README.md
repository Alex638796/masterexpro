# 🎓 MasterExPro

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Pyrogram](https://img.shields.io/badge/Pyrogram-Async-orange)
![MongoDB](https://img.shields.io/badge/MongoDB-Motor%20Async-green?logo=mongodb)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 📋 Table of Contents

- [Commands](#-commands)
- [Environment Variables](#-environment-variables)
- [Deployment](#-deployment)
- [Tech Stack](#-tech-stack)

---

## 💬 Commands

| Command | Access | Use Case |
|---|---|---|
| `/start` | Everyone | Start the bot, see the welcome menu |
| `/app` | Everyone | Open the app/platform selection menu |
| `/upgrade` | Everyone | View premium plan / upgrade options |
| `/myplan` | Everyone | Check your current plan/access status |
| `/myfiles` | Everyone | List your saved/uploaded files |
| `/upload` | Everyone | Upload a `.txt` file (`Name: URL` per line) for batch processing |
| `/stop` | Everyone | Stop an ongoing extraction task |
| `/stop_upload` | Everyone | Cancel an in-progress `.txt` upload/processing job |
| `/saveapi` | Plan holders | Save a custom App/API entry (requires an active plan) |
| `/auth` | 🔒 Owner only | Grant a user premium/authorized access |
| `/authlist` | 🔒 Owner only | List all authorized/premium users |
| `/remove` | 🔒 Owner only | Remove a user's authorized access |
| `/removeallfiles` | 🔒 Owner only | Delete all stored files for a user |
| `/allbackupfiles` | 🔒 Owner only | Get a backup of all stored files |
| `/status` | 🔒 Owner only | View bot/database status and stats |
| `/broadcast` | 🔒 Owner only | Reply to a message with this to broadcast it to all known users |

---

## 🔑 Environment Variables

### Mandatory

| Variable | Purpose |
|---|---|
| `BOT_TOKEN` | Telegram Bot Token, from @BotFather |
| `API_ID` | Telegram API ID, from my.telegram.org |
| `API_HASH` | Telegram API Hash, from my.telegram.org |
| `DB_URL` | MongoDB connection string (e.g. from MongoDB Atlas) |

### Optional

| Variable | Default | Purpose |
|---|---|---|
| `ADMIN_ID` | — | Comma-separated admin/owner user IDs |
| `OWNER_ID` | — | Bot owner's Telegram user ID |
| `DB_NAME` | `master_extractor` | MongoDB database name |
| `AUTH_LOG` | `0` | Channel ID for auth/premium-grant logs |
| `CHANNEL` | `0` | Channel ID used for the force-subscribe check |
| `PREMIUM_LOGS` | `0` | Channel ID for premium-purchase logs |
| `CH_URL` | — | Your channel's invite link (shown on join buttons) |
| `OWNER` | — | Owner's Telegram profile link (shown to users) |
| `THUMB_URL` | *(placeholder image)* | Default thumbnail image URL |
| `BOT_TEXT` | `Master Extractor` | Bot display name |
| `BOT_USERNAME` | — | Bot username, without `@` |
| `HOST` | `https://api.masterapi.tech` | API host URL |
| `TXT_LOG`, `HIT_LOG`, `DRM_DUMP`, `CHANNEL_ID`, `CHANNEL_ID2` | `0` / empty | Reserved — not currently read by any module |

---

## 🚀 Deployment

This bot is polling-based (Pyrogram), so it doesn't strictly need a public URL — the included Flask server only exists to satisfy platforms that require a bound port for health checks. It supports **Render, Heroku, Koyeb, Railway, Google Cloud Run, Google Colab, VPS, and Termux**.

### One-Click Deploy

| Platform | Deploy |
|---|---|
| Render | [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Alex638796/masterexpro) |
| Heroku | [![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Alex638796/masterexpro) |
| Koyeb | [![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/Alex638796/masterexpro&branch=main&name=masterexpro) |
| Google Colab | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Alex638796/masterexpro/blob/main/colab_deploy.ipynb) |
| Google Cloud | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/Alex638796/masterexpro&cloudshell_tutorial=.cloudshell/GCLOUD.md) |

> ⚠️ None of these badges fully automate deployment — each opens that platform's setup screen where you still need to fill in environment variables manually (see the table above).

> ℹ️ **Railway**: also deployable — it auto-detects the app via Nixpacks (`Procfile` + Dockerfile), no extra config needed. No badge here since Railway requires a pre-registered template.

### Render / Heroku / Koyeb / Google Cloud Run

All four use the included `Dockerfile` (Render directly via `render.yaml`; Heroku via `heroku.yml`/`app.json`). For manual Cloud Run deployment via `gcloud` CLI, see `.cloudshell/GCLOUD.md`.

### Google Colab (temporary/testing)

Click the Colab badge above to open `colab_deploy.ipynb`, fill in the mandatory fields (`BOT_TOKEN`, `API_ID`, `API_HASH`, `DB_URL`), and run the single cell. It clones the repo, installs dependencies, and runs `python3 main.py`. The cell blocks and streams logs live; press ■ to stop.

> ⚠️ Colab sessions are temporary (disconnect on tab close, inactivity, or after Colab's free-tier time limit — up to ~12 hours). Use for quick testing only.

### VPS

```bash
git clone https://github.com/Alex638796/masterexpro.git
cd masterexpro
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -U yt-dlp
export BOT_TOKEN="your_bot_token"
export API_ID="your_api_id"
export API_HASH="your_api_hash"
export DB_URL="your_mongodb_connection_string"
python3 run.py
```

Or via Docker, using the included `Dockerfile`:

```bash
git clone https://github.com/Alex638796/masterexpro.git
cd masterexpro
sudo apt install docker.io -y
sudo docker build -t masterexpro .
sudo docker run -it --rm --env-file .env masterexpro
```

### Termux (Android)

```bash
pkg update && pkg upgrade -y
pkg install python git ffmpeg -y
git clone https://github.com/Alex638796/masterexpro.git
cd masterexpro
pip install -r requirements.txt
pip install -U yt-dlp
export BOT_TOKEN="your_bot_token"
export API_ID="your_api_id"
export API_HASH="your_api_hash"
export DB_URL="your_mongodb_connection_string"
python3 main.py
```

### Local PC (Windows/Linux/macOS)

```bash
git clone https://github.com/Alex638796/masterexpro.git
cd masterexpro
python3 -m venv venv
# Windows: venv\Scripts\activate | Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
pip install -U yt-dlp
# set BOT_TOKEN, API_ID, API_HASH, DB_URL as environment variables, or in a .env file
python3 main.py
```

---

## 🧰 Tech Stack

- **Pyrogram** — Telegram MTProto client (bot logic, polling)
- **Flask + Gunicorn** — lightweight health-check web server
- **Motor** — async MongoDB driver
- **aiohttp / requests / cloudscraper** — HTTP clients for extraction modules (including anti-bot bypass)
- **yt-dlp** — video/audio extraction and download
- **ffmpeg / aria2** — media processing and fast downloading
