import random
import string
import os
import discord
from discord.ext import commands


ref = ["j.moomoo.com", "share.firstrade.com", "act.webull.com", "dough.com/referrals?referral=", "join.robinhood.com", "discord.gg"]
toggle = False

client = commands.Bot(command_prefix='/')

@client.event
async def on_ready():
    print('Bot is ready!')
    global channel

@client.event
async def on_message(message):
    await client.process_commands(message)
    if toggle == False:
        channel = client.get_channel(700563877959696384)
        text_channel = client.get_channel(696103801693798501)
        for x in range(0, len(ref)):
            if ref[x] in message.content:
                await message.delete()
                print(message.author)
                await message.author.send("Hello! We've noticed you sent a referral link and while we appreciate you trying to help others, referral links are not allowed here other than the ones in the channel. We hold two raffles per month where we ourselves promote a raffle winner's own links across our entire server and all our social platforms. The raffles allow us to keep up the many services and resources we work hard to provide to our community such as our website, forum, educational content, and one-on-one sessions. Raffle winners are also awarded private one-on-one sessions and access to our premium curriculum. If you have any questions, don't hesitate to message an Admin or Captain! Thank you for being a part of Togethearn!")
                await channel.send(f"{message.author.mention} has tried to send a referall link {text_channel.mention}")

@client.command()
async def enable(ctx):
    global toggle
    toggle = not toggle
    if toggle == False:
        await ctx.message.channel.send("Referral Destroyer is now on.")
    else:
        await ctx.message.channel.send("Referral Destroyer is now off.")

client.run(os.environ['TOKEN'])
