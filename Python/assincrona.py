import asyncio

async def comprimento():
    print("Começando...")
    await asyncio.sleep(1)
    print("Olá, depois de 1 segundo!")

asyncio.run(comprimento())
