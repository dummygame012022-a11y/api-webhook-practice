# API and Webhook Practice

Two small Python scripts that show how to work with APIs.

## 1. github_repos.py (calling an API)
Sends a GET request to the GitHub API and prints each repo name with its language.

    python github_repos.py

## 2. webhook.py (receiving data)
A small Flask server with one address, /webhook.
- Accepts JSON sent with POST
- Returns an error (400) if the "order" field is missing
- Saves good orders to orders.csv

Run it:

    python webhook.py

Test it from a second terminal:

    curl -s -X POST http://127.0.0.1:8091/webhook -H "Content-Type: application/json" -d '{"order": 102, "item": "Bread", "qty": 3}'

## Skills shown
Python, requests, Flask, JSON, REST API, webhooks, CSV, input checking.
