import threading
import asyncio
import os
from raybm import SEA, start_streaming

async def main():
    room_id = os.getenv("ROOM_ID")
    token = os.getenv("TOKEN")

    if not token:
        raise ValueError("TOKEN missing — Add it in Railway Variables!")
    if not room_id:
        raise ValueError("ROOM_ID missing — Add it in Railway Variables!")

    bot_instance = SEA()

    # Start audio streaming thread
    streaming_thread = threading.Thread(target=start_streaming, args=(bot_instance,))
    streaming_thread.daemon = True
    streaming_thread.start()

    while True:
        try:
            await bot_instance.run(room_id, token)
        except Exception as e:
            print(f"[Bot Error] {e}\nRestarting in 5 seconds…")
            await asyncio.sleep(5)

if __name__ == '__main__':
    asyncio.run(main())
