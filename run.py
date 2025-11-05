import threading
import asyncio
from raybm import SEA, start_streaming

async def main():
    room_id = "6706b1dc20084804ef575ccb"
    token = "75c96515b2b89f9a990c4c15796d4b883ab045193aafaa809043a3573afe249a"    
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