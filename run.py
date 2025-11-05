import threading
import asyncio
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
    room_id = "6706b1dc20084804ef575ccb"
    token = "75c96515b2b89f9a990c4c15796b4b883ab045193aafaa809043a3573afe249a"    
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
