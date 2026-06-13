# Mini Project 7 — MQTT Pub/Sub Communication

Demonstrates MQTT publish/subscribe messaging using a public broker via Python and an interactive web dashboard.

## Features
- **Publisher** sends random numbers every 2 seconds to a topic
- **Subscriber** listens and prints received messages in real time
- Uses public MQTT brokers (e.g. `test.mosquitto.org` / `broker.hivemq.com`)

### Web Interface (`index.html`)
- Dark **glassmorphism** design with console interface
- **Live Connection Settings** — connect to any public WebSocket broker port
- **Live Publishing panel** — input custom topics and payloads to publish instantly
- **Live Console Feed** — real-time logging of system connection changes, publish events, and subscription receipts
- Status badge with glowing LED connection indicator

## How to Run

### Python CLI (Pub/Sub)
Open **two separate terminals**:

**Terminal 1 — Start Subscriber:**
```bash
pip install -r requirements.txt
python subscriber.py
```

**Terminal 2 — Start Publisher:**
```bash
python publisher.py
```

### Web Version
Open `index.html` in any browser — connect to `broker.hivemq.com` on port `8000` (WebSocket) and test publishing/subscribing interactively!

## Files
| File | Description |
|------|-------------|
| `publisher.py` | Publishes random numbers to MQTT topic |
| `subscriber.py` | Subscribes and prints incoming messages |
| `requirements.txt` | Python dependencies |
| `index.html` | Real-time MQTT subscriber/publisher dashboard |

## Concepts Used
- MQTT protocol (IoT communication)
- Publish/Subscribe architecture
- WebSockets communication (Paho MQTT JS client)
- Real-time logging & visual interface
