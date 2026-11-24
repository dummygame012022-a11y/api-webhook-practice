import csv
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Order Webhook")
CSV_PATH = Path("orders.csv")


class Order(BaseModel):
    order: str | int
    item: str | None = None
    qty: int | None = Field(default=None, ge=1)


class WebhookResponse(BaseModel):
    status: str


@app.post("/webhook", response_model=WebhookResponse)
def webhook(data: Order):
    with CSV_PATH.open("a", newline="") as f:
        csv.writer(f).writerow([data.order, data.item, data.qty])
    return {"status": "ok"}
