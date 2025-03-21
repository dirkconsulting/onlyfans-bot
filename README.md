# 🤖 OnlyFans Bot - Automated Chat & PPV Sales

This bot automates **OnlyFans** conversations, engages with subscribers, and sells PPV content using **Selenium + ChatGPT**.

## 🌟 Features:
✅ **AI-Powered Chat:** ChatGPT generates personalized messages.  
✅ **PPV Sales Automation:** Detects online users and offers PPV videos.  
✅ **User Database:** Stores purchase history, interests, and last 30 messages.  
✅ **Message Randomization:** Avoids repetitive messages for higher engagement.  
✅ **Selenium Automation:** Sends messages and interacts with OnlyFans UI.  

---

## 📂 Project Structure

| File | Description |
|------|------------|
| `bot.py` | Main bot script. Detects online users, chats with them, and offers PPV. |
| `onlyfans.py` | Manages OnlyFans login, message sending, and user detection using Selenium. |
| `chatgpt_api.py` | Calls ChatGPT API to generate realistic responses for chats. |
| `ppv.py` | Automates PPV sales, ensuring unique messages and personalized offers. |
| `database.py` | Stores user data, message templates, and PPV content in SQLite. |
| `config.py` | Stores API keys and credentials (DO NOT SHARE THIS FILE). |

---

## 🚀 How to Use

### **1️⃣ Install Dependencies**
```bash
sudo apt update && sudo apt install python3 python3-venv git -y
cd ~/onlyfans_bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
