---
title: KPilot
emoji: 🚀
colorFrom: indigo
colorTo: indigo
sdk: streamlit
sdk_version: 1.44.1
app_file: app.py
pinned: false
license: mit
---

![KPilot Banner](https://huggingface.co/spaces/GeetaAIVisionary/KPilot/resolve/main/Geeta-KPilot.png)

# 🚀 KPilot – Your Kafka Copilot

Ask questions about Kafka CLI, tuning, and configurations – trained on real Kafka cheat sheets and docs!

**KPilot** is a lightweight AI assistant built using:

- 🧠 **LangChain** – loads and embeds Kafka documentation
- 💬 **OpenAI GPT** – answers questions conversationally
- 🔍 **FAISS** – vector search for accurate matches
- 🖥️ **Streamlit** – clean and interactive UI

---

## 🔎 Sample Questions

- What’s the command to describe a Kafka topic?
- What is the difference between producer and consumer `acks`?
- How do I increase partitions for an existing topic?
- How does `retention.ms` affect topic behavior?

---

## 🛠️ How It Works

1. Upload Kafka docs (PDF or markdown)
2. Documents are chunked and embedded with `OpenAIEmbeddings`
3. Indexed into FAISS for semantic search
4. LangChain + Streamlit runs a chat interface over your docs

---

## 👩‍💻 About the Creator

Built by [Geeta Kudumula](https://www.linkedin.com/in/geeta-kudumula-7963b990/), a Senior AI & Kafka Architect  
👉 GitHub: [GeetaAIVisionary](https://github.com/GeetaAIVisionary)

