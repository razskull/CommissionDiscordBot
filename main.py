import discord
from discord.ext import commands
from discord import app_commands

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        try:
            guild = discord.Object(id='GUILD_ID_HERE')
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')
        except Exception as e:
            print(f'Error syncing comands: {e}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.lower().startswith('commission'):
            total = 0
            g = 0
            c = 0

            con1 = message.content.lower().split(" ")
            if len(con1) < 2:
                await message.channel.send("Not enough arguments! Please give a role") # send the necessary feedback
                return # end this function
            elif len(con1) > 2:
                await message.channel.send("Too many arguments! Please only give a role")
                return
            role = str(con1[-1])
            messages = [message async for message in message.channel.history(limit=100)]
            for i in messages:
                if i.content.lower().startswith('gem'):
                    con = i.content.lower().split(" ") 
                    if len(con) < 2:
                        await message.channel.send("Not enough arguments! Please give a number") # send the necessary feedback
                        return # end this function
                    elif len(con) > 2:
                        await message.channel.send("Too many arguments! Please only give a number")
                        return
                    g = g + int(con[-1])
                elif i.content.lower().startswith('chain'):
                    con2 = i.content.lower().split(" ") 
                    if len(con2) < 2:
                        await message.channel.send("Not enough arguments! Please give a number") # send the necessary feedback
                        return # end this function
                    elif len(con2) > 2:
                        await message.channel.send("Too many arguments! Please only give a number")
                        return
                    c = c + int(con2[-1])

                if(role == "jewel"):
                    total = 0.10 * g + 0.30 * c
                elif(role == "shift"):
                    total = 0.20 * g + 0.40 * c
                elif(role == "manager"):
                    total = 0.30 * g + 0.50 * c
                
            await message.channel.send(total)



intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix=';', intents=intents)

GUILD_ID = discord.Object(id='GUILD_ID_HERE')

client.run('DISCORD_TOKEN')
