import asyncio
import discord
import json
import random

client = discord.Client()

tokendata = json.load(open('./assets/token.json'))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----------')

@client.async_event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter+=1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!insult'):
        outmsg = "    "
        theuser = message.server.get_member_named(str(message.mentions[0]))
        outmsg += theuser.mention
        t1 = ['lazy','stupid','insecure','idiotic','slimy','slutty','smelly','pompous','communist','dicknose','pig-eating','racist','elitist','white trash','drug-loving','butterface','tone deaf','ugly','creepy']
        t2 = ['douche','ass','turd','recturm','butt','cock','shit','crotch','bitch','turd','prick','slut','taint','fuck','dick','goner','shart','nut','sphincter']
        t3 = ['pilot','canoe','captain','pirate','hammer','knob','box','jockey','nazi','waffle','goblin','blossum','biscuit','clown','socket','monster','hound','dragon','balloon']
        outmsg += " is a "+random.choice(t1)+" "+random.choice(t2)+" "+random.choice(t3)+"."
        await client.send_message(message.channel, outmsg)

client.run(tokendata["token"])
