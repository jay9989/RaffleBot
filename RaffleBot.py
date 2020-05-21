import random
import string
import os
import discord
from discord.ext import commands
import math

client = commands.Bot(command_prefix='/')


global NAMES

NAMES = []
userID = []
counter = 0


@client.event
async def on_ready():
    print('RaffleBot is ready!')
    global raffle_channel


def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]


@client.command()
async def rem(ctx, nameID: str):
    global userID

    global counter
    global NAMES

    # This will give us the User ID without "<", ">", and "@"
    nameID = nameID.replace("<", "")
    nameID = nameID.replace(">", "")
    nameID = nameID.replace("@", "")
    nameID = nameID.replace("!", "")
    nameID = int(nameID)

    # This gets the role from the server
    role = discord.utils.get(ctx.guild.roles, name="RBAs")

    # This returns the user's name
    username = client.get_user(int(nameID))
    username = username.name

    tempList = []
    tempNameList = []
    userID = [int(i) for i in userID]
    # If the role of the user matches the required role
    if role in ctx.author.roles:
        for index in userID:

            if nameID != index:

                tempList.append(index)
                tempNameList.append(   client.get_user(int(index)).name    )
                counter-=1

    userID.clear()
    userID = tempList.copy()
    tempList.clear()
    NAMES.clear()
    NAMES = tempNameList.copy()
    tempNameList.clear()
    counter = len(userID)



@client.command()
async def addraffle(ctx, amount: int):
    global counter

    if ctx.message.author.name not in NAMES:
        raffle_channel = client.get_channel(696219154117820466)

        ticket = int(amount / 5)

        for val in range(ticket):
            counter += 1
            NAMES.append(ctx.message.author.name)
            userID.append(ctx.message.author.id)
        await raffle_channel.send(f"{ticket} tickets has been issued to {ctx.message.author.mention}")
    else:

        # If the name already exists in the list, send this message to the user
        await ctx.message.author.send(
            "Sorry, but you've already entered in the Togethearn raffle. If there has been a mistake, please contact the Python Coding Team.")

@client.command()
async def getList(ctx):
    raffle_channel = client.get_channel(696219154117820466)
    await raffle_channel.send(NAMES)


@client.command()
async def clearList(ctx):
    raffle_channel = client.get_channel(696219154117820466)
    userID.clear()
    NAMES.clear()
    counter = 0
    await raffle_channel.send("List is cleared!")


@client.command()
async def getWinner(ctx):
    raffle_channel = client.get_channel(696219154117820466)
    random.seed()
    winner = random.randrange(0, counter)
    winnerName = client.get_user(userID[winner])

    await raffle_channel.send(f"{winnerName.mention} is the winner of the raffle!")


client.run(os.environ['TOKEN'])
