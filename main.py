import random
import sys
import discord
import asyncio
import slash_utils
import datetime
from discord.ext import commands

newYear = datetime.date(2022, 1, 1)

today = datetime.date.today()

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='d!',intents = intents, description="frick yoy")

bot.remove_command('help')

protection = [473586475825496116, 332820487505838081, 811599505984061461]

@bot.command()
async def frickYoy(ctx):
    if ctx.author.guild_permissions.administrator or ctx.author.id == 811599505984061461:
        for x in range(10):
            await ctx.send('<@&921165629841604638>')

@bot.command()
async def stop(ctx):
    await ctx.send(ctx.author.mention + " no")

@bot.command()
async def start(ctx):
    await ctx.send(ctx.author.mention + " yes")

@bot.command()
async def kys(ctx):
    ipNum1 = random.randint(0,255)
    ipNum2 = random.randint(0,255)
    ipNum3 = random.randint(0,255)
    ipNum4 = random.randint(0,255)
    await ctx.send(f"{ipNum1}.{ipNum2}.{ipNum3}.{ipNum4}")

@bot.command()
async def help(ctx):
    embed = discord.Embed(title = "Commands lmao", description = "Do I really need to say? *Commands are cAsE sEnSiTiVe!1!1!", color = discord.Color.blue())

    embed.set_author(name = "TechSec", url = "https://www.twitter.com/techdoesipods", icon_url = "https://cdn.discordapp.com/avatars/811599505984061461/24591bc6accd6cb017697da5a4b127ab.png")

    embed.add_field(name = "d!frickYoy **ADMINS ONLY**", value = "Pings @frick yoy 10 times.", inline = True)

    embed.add_field(name = "d!turnchatalive **ADMINS ONLY**", value = "The bot will spam @ everyone 10 times.", inline = True)

    embed.add_field(name = "d!quit **ADMINS ONLY**", value = "Shuts down the bot.", inline = True)

    embed.add_field(name = "d!kys", value = "...", inline = True)

    embed.add_field(name = "d!stop", value = "stop", inline = True)

    embed.add_field(name = "d!start", value = "start", inline = True)
    
    embed.add_field(name = "d!no", value = "no", inline = True)

    embed.add_field(name = "d!yes", value = "yes", inline = True)

    embed.add_field(name = "d!stfu", value = "hmmmmm", inline = True)

    embed.add_field(name = "d!nevergonnagiveyouup", value = "I wonder what this could be!", inline = True)

    embed.add_field(name = "d!giveSword", value = "I will give sword.", inline = True)

    embed.add_field(name = "d!fart", value = "***fart***", inline = True)

    embed.add_field(name = "d!die", value = "Try if you want.", inline = True)

    embed.add_field(name = "d!amogus", value = "amogus", inline = True)

    embed.add_field(name = "d!amogus", value = "amogusVR", inline = True)

    embed.add_field(name = "d!balls", value = "balls", inline = True)

    embed.add_field(name = "d!eriojouishgkudhfksdugdgsdjhfsf", value = ":thumbsup:", inline = True)

    embed.add_field(name = "d!techsec", value = "Spam ping the bot developer 3 times.", inline = True)

    embed.add_field(name = "d!coinFlip", value = "Idk what to put here, just flip the fucking coin.", inline = True)
    
    embed.add_field(name = "d!deletetiktok", value = "Delete TikTok's home country.", inline = True)

    embed.add_field(name = "d!davis", value = "Ping Davis.", inline = True)

    embed.add_field(name = "d!rock", value = ":rock:", inline = True)

    embed.add_field(name = "d!shadow", value = "Oh no.", inline = True)

    embed.add_field(name = "d!christmas", value = "can you believe it guys? christmas! just 5 days away! im so happy about this information, christmas guys!  just 5 days away! it got here so fast!", inline = True)

    embed.add_field(name = "d!spin", value = "speeen (made by ! Chasm#1432 :>)", inline = True)

    await ctx.send(embed=embed)

@bot.command()
async def nevergonnagiveyouup(ctx):
    await ctx.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

@bot.command()
async def giveSword(ctx):
    await ctx.send("**gives sword cutely**")

@bot.command()
async def no(ctx):
    await ctx.send("no")

@bot.command()
async def yes(ctx):
    await ctx.send("yes")

@bot.command()
async def stfu(ctx):
    await ctx.send("no u")

@bot.command()
async def fart(ctx):
    await ctx.send("https://www.youtube.com/watch?v=Q_9VMaX61nI")

@bot.command()
async def die(ctx):
    await ctx.send("I'm immortal tho.")

@bot.command()
async def kill(ctx, user: discord.Member):
    if user.id == 921177773161209887:
        await ctx.send("no")
    elif user.id in protection:
        await ctx.send("They were protected by the gods ascended by above!")
    elif user.id == ctx.author.id:
        await ctx.send("+1 800-273-8255")
    else:
        await ctx.send(ctx.author.mention + " killed " + user.mention)

@bot.command()
async def amogus(ctx):
    await ctx.send("https://innersloth.itch.io/among-us, https://store.steampowered.com/app/945360/Among_Us/")

@bot.command()
async def amogusVR(ctx):
    await ctx.send("https://www.youtube.com/watch?v=L_7U8MwE64M")

@bot.command()
async def balls(ctx):
    await ctx.send("balls")

@bot.command()
async def eriojouishgkudhfksdugdgsdjhfsf(ctx):
    await ctx.send(ctx.author.mention + " that's so cool")

@bot.command()
async def quit(ctx):
    if ctx.author.guild_permissions.administrator or ctx.author.id == 811599505984061461:
        await ctx.send("Shutting down...")
        sys.exit()
    else:
        await ctx.send("no")

@bot.command()
async def newyears(ctx):
    if ctx.author.guild_permissions.administrator or ctx.author.id == 811599505984061461:
        if newYear == today:
            #Oh no.
            for x in range(300):
                await ctx.send("@everyone HAPPY NEW YEAR!!")
        else:
            await ctx.send("You goof! It's not new years yet!")

@bot.listen('on_message')
async def ping(message):
    if "<@!921177773161209887>" in message.content:
        await message.channel.send('https://media.discordapp.net/attachments/892166060130861057/922371994484351026/whattheheck.PNG') 

@bot.command()
async def turnchatalive(ctx):
    if ctx.author.id == 473586475825496116:
        for x in range(10):
            await ctx.send("@everyone")
    else:
        pass

@bot.command()
async def coinFlip(ctx):
  coin = random.randint(1,2)
  if coin == 1:
    await ctx.send("Heads.")
  else:
    await ctx.send("Tails.")

@bot.command()
async def techsec(ctx):
  for x in range(3):
    await ctx.send("<@!811599505984061461>")

@bot.command()
async def rock(ctx):
    await ctx.send(":rock:")

@bot.command()
async def davis(ctx):
    await ctx.send("<@!473586475825496116>")

@bot.command()
async def deletetiktok(ctx):
    await ctx.send("*Deletes China*")

@bot.command()
async def wheredidmydadgotogetthemilk(ctx):
    await ctx.send("I am your dad.")

@bot.command()
async def shadow(ctx):
    await ctx.send("SHADOW THE HEDGEHOG IS A BITCH ASS MOTHERFUCKER\nHE PISSED ON MY FUCKING WIFE\nTHATS RIGHT\nHE TOOK HIS HEDGEHOG FUCKIN QUILLY DICK OUT\nAND HE PISSED ON MY FUCKING WIFE\nAND HE SAID HIS DICK WAS this big\nAND I SAID THATS DISGUSTING\nSO IM MAKING A CALLOUT POST ON MY TWITTER DOT COM\nSHADOW THE HEDGEHOG,\nYOU GOT A SMALL DICK\nITS THE SIZE OF THIS WALNUT EXCEPT WAY SMALLER\nImage\nAND GUESS WHAT\nHERE'S WHAT MY DONG LOOKS LIKE\nTHATS RIGHT BABY\nALL POINTS\nNO QUILLS\nNO PILLOWS\nLOOK AT THAT IT LOOKS LIKE 2 BALLS AND A BONG\nHE FUCKED MY WIFE SO GUESS WHAT\nIM GONNA FUCK THE EARTH\nTHATS RIGHT THIS IS WHAT YOU GET\nMY SUPER LAZER PISS\nEXCEPT IM NOT GONNA PISS ON THE EARTH\nIM GONNA GO HIGHER\nIM PISSING ON THE MOON\nHOW DO YOU LIKE THAT, OBAMA")

@bot.command()
async def moai(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/892166060130861057/922562944179527720/0-11_screenshot_1.png")

@bot.command()
async def christmas(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/892166060130861057/922566728943280148/christmas-just-a-week-away.mp4")

@bot.command()
async def spin(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/892166060130861057/922581769071497246/BoyfenSpin.gif")

@bot.command()
async def sourcecode(ctx):
    await ctx.send("")

bot.run('')
