# Mini Project 7 — MQTT Pub/Sub Communication

Demonstrates MQTT publish/subscribe messaging using a public broker.

## Features
- **Publisher** sends random numbers every 2 seconds to a topic
- **Subscriber** listens and prints received messages in real time
- Uses the public MQTT broker `test.mosquitto.org`

## How to Run

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

The subscriber will display messages as they arrive from the publisher.

## Files
| File | Description |
|------|-------------|
| `publisher.py` | Publishes random numbers to MQTT topic |
| `subscriber.py` | Subscribes and prints incoming messages |
| `requirements.txt` | Python dependencies |

## Concepts Used
- MQTT protocol (IoT communication)
- Publish/Subscribe architecture
- Network programming
- Real-time messaging
