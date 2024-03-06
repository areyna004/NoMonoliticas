import asyncio
import time

async def foo(delay, mensaje):
   while True:
      await asyncio.sleep(delay)
      print(f'{mensaje}')

def main():
   loop = asyncio.get_event_loop()
   loop.create_task(foo(1, "A"))  
   loop.create_task(foo(3, "B"))
   loop.create_task(foo(6, "C"))  
   loop.run_forever()

try:
   main()
except Exception as e:
   print('Error: ', e)
