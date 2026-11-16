# Make: Webhook -> Google Sheets -> Telegram

Practice automation: when an order arrives by webhook, it is saved in a Google Sheet and an alert is sent to Telegram.

## Flow

1. **Webhook** (Make) receives order data as JSON.
2. **Google Sheets: Add a Row** saves the order.
3. **Telegram: Send a Text Message** sends an alert, for example "New order B002: 2 x Milk, P160".

## Sheet columns

order_id, date_time, customer, item, qty, price, total, status

- date_time uses Make's clock formatted for Asia/Manila.
- total = qty x price.
- status starts as New.

## Sample order sent to the webhook

    {"order_id": "B002", "customer": "Dan", "item": "Milk", "qty": 2, "price": 80}

## Result

- Telegram alert: New order B002: 2 x Milk, P160
- Sheet row: B002, Dan, Milk, 2, 80, 160, New

## Notes

- The webhook URL and the bot token are secret. They are not saved in this repo.
- Check that the webhook URL variable is not empty before sending, or blank rows and alerts are created.
- In a real client job, the client owns the Google Sheet, Make account, and Telegram bot.
