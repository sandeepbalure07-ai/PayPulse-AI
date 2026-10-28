from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI(title="PayPulse AI Engine")

class Transaction(BaseModel):
    transaction_id: str
    amount: float
    currency: str
    merchant_id: str
    user_score: float

@app.get("/")
def health_check():
    return {"status": "online", "engine": "PayPulse AI Sub-Millisecond Router"}

@app.post("/api/v1/assess-risk")
async def assess_risk(tx: Transaction):
    start_time = time.perf_counter()
    
    # Sub-millisecond risk engine logic & pathway determination
    is_fraud = tx.amount > 10000 or tx.user_score < 0.2
    risk_score = 0.95 if is_fraud else 0.03
    recommended_pathway = "STEP_UP_AUTH" if is_fraud else "PAYPAL_DIRECT_FAST"
    
    latency_ms = (time.perf_counter() - start_time) * 1000
    
    return {
        "transaction_id": tx.transaction_id,
        "risk_score": risk_score,
        "flagged": is_fraud,
        "routing_pathway": recommended_pathway,
        "latency_ms": round(latency_ms, 3)
    }

@app.post("/api/v1/paypal-webhook")
async def paypal_webhook_listener(payload: dict):
    event_type = payload.get("event_type", "CHECKOUT.ORDER.APPROVED")
    return {"status": "success", "processed_event": event_type}