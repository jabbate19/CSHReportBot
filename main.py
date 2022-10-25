import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

API_TOKEN = os.environ['API_TOKEN']
SOCKET_TOKEN = os.environ['SOCKET_TOKEN']
REPORT_CHANNEL = os.environ['REPORT_CHANNEL']

app = App(token=API_TOKEN)

@app.event("message")
def got_dm(client, event, logger):
    if event['channel_type'] == 'im':
        client.chat_postMessage(
            channel=REPORT_CHANNEL,
            text=event['text']
        )

if __name__ == "__main__":
    SocketModeHandler(app, SOCKET_TOKEN).start()

