import discord
import asyncio

async def SendEmbedMessage(chan, embed):
    tries = 5
    try:
        await chan.send(embed=embed)
    except (discord.Forbidden, discord.HTTPException) as e:
        print(f"AN UNEXPECTED ERROR HAS OCCURED ON FIRST ATTEMPT: {e}")
        for i in range(1, tries + 1):
            sleep_timer = 5 * i
            await asyncio.sleep(sleep_timer)
            print("Attempting to send message another time...")
            try:
                await chan.send(embed=embed)
                print("Message sent successfully on retry.")
                break
            except (discord.Forbidden, discord.HTTPException) as e2:
                if i < tries:
                    continue
                print(f"AN UNEXPECTED ERROR HAS OCCURED: {e2}")
    
async def SendMessage(chan, msg):
    tries = 5
    try:
        await chan.send(msg)
    except (discord.Forbidden, discord.HTTPException) as e:
        print(f"AN UNEXPECTED ERROR HAS OCCURED ON FIRST ATTEMPT: {e}")
        for i in range(1, tries + 1):
            sleep_timer = 5 * i
            await asyncio.sleep(sleep_timer)
            print("Attempting to send message another time...")
            try:
                await chan.send(msg)
                print("Message sent successfully on retry.")
                break
            except (discord.Forbidden, discord.HTTPException) as e2:
                if i < tries:
                    continue
                print(f"AN UNEXPECTED ERROR HAS OCCURED: {e2}")