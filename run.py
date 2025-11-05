import threading
import asyncio
import os
from raybm import SEA, start_streaming
from flask import Flask

# --- Flask healthcheck ---
app = Flask(__name__)

@app.route("/")
def health():
    return "Bot is alive!", 200

def run_flask():
    app.run(host="0.0.0.0", port=8080)

flask_thread = threading.Thread(target=run_flask)
flask_thread.daemon = True
flask_thread.start()
# -----------------------

async def main():
    # Read room_id and token from Railway environment variables
    room_id = os.getenv("ROOM_ID")
    token = os.getenv("BOT_TOKEN")
    
    if not room_id or not token:
        print("ERROR: ROOM_ID or BOT_TOKEN not set in environment variables!")
        return
    
    bot_instance = SEA()

    # Start the streaming thread
    streaming_thread = threading.Thread(target=start_streaming, args=(bot_instance,))
    streaming_thread.daemon = True
    streaming_thread.start()

    while True:
        try:
            await asyncio.sleep(5)
            await bot_instance.run(room_id, token)
        except Exception as e:
            print(f"Bot error: {e}. Restarting in 5 seconds...")
            await asyncio.sleep(5)

if __name__ == '__main__':
    asyncio.run(main())
