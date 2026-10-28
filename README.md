# ⚡ PayPulse AI

> **Autonomous Real-Time Transaction Routing & Fraud Prevention Engine**  
> *Built for the Global PayPal Ecosystem.*



## ⚡ Problem Statement
Modern digital commerce processes millions of multi-channel transactions at millisecond speed, but traditional ecosystems flag fraud after the fact. This leads to high false-decline rates, cart abandonment, and lost revenue. **PayPulse AI** fixes this by processing transaction flows with sub-millisecond routing, predictive risk assessment, and smart micro-payment consolidation.



## 🚀 Key Features
* **Sub-Millisecond AI Risk Guard:** Predicts fraudulent transactions using ONNX Runtime optimized XGBoost & TensorFlow classification models.
* **Smart Micro-Payment Routing:** Dynamically assesses network strain, processing fees, and API speeds to route transactions through the highest-efficiency pathway.
* **Kafka & Redis Data Stream:** Ingests transaction streams via Apache Kafka with in-memory state tracking using Redis.
* **PayPal Integration:** Custom simulated webhooks leveraging PayPal Developer APIs for real-time checkout approvals and dispute triggers.



## 🛠 Tech Stack
* **Languages:** Python 3.11, TypeScript
* **Backend Framework & AI:** FastAPI, ONNX Runtime, XGBoost, TensorFlow, Apache Kafka, Redis
* **Frontend Dashboard:** Next.js (React), Tailwind CSS, Recharts
* **DevOps & Tools:** Git, VS Code



### 1. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
