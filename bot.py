import discord
import random
import asyncio
from discord.ext import commands
from discord import Embed
sfw1 = "https://media.discordapp.net/attachments/721728322266071130/723700380902359120/image0.jpg" " https://media.discordapp.net/attachments/721728322266071130/723700392667381760/image0.jpg" " https://media.discordapp.net/attachments/721728322266071130/723701464458985483/image0.jpg" " https://media.discordapp.net/attachments/721728322266071130/723701613461635092/image0.jpg" " https://media.discordapp.net/attachments/721728322266071130/723701860216602714/image0.jpg"
sfw2 = "https://media.discordapp.net/attachments/721728322266071130/723704914643255356/image0.jpg" " https://media.discordapp.net/attachments/721728322266071130/723704922843119666/image0.jpg" " https://media.discordapp.net/attachments/721728322266071130/723704930036088862/image0.jpg" " https://media.discordapp.net/attachments/721728322266071130/723704942493302864/image0.jpg" " https://media.discordapp.net/attachments/721728322266071130/723704949266972783/image0.jpg"
sfw3 = "https://media.discordapp.net/attachments/721728322266071130/723711533271613440/image4.jpg" " https://media.discordapp.net/attachments/721728322266071130/723711532797788191/image3.jpg" " https://media.discordapp.net/attachments/721728322266071130/723711532558450764/image2.jpg" " https://media.discordapp.net/attachments/721728322266071130/723711532348735548/image1.jpg" " https://media.discordapp.net/attachments/721728322266071130/723711532076105818/image0.jpg"
sfw4 = "https://media.discordapp.net/attachments/721728322266071130/723713195004395581/image0.jpg" " https://media.discordapp.net/attachments/721728322266071130/723713195449253948/image1.jpg" " https://media.discordapp.net/attachments/721728322266071130/723713195868684288/image2.jpg" " https://media.discordapp.net/attachments/721728322266071130/723713196321669171/image3.jpg" " https://media.discordapp.net/attachments/721728322266071130/723713196531253288/image4.jpg"
sfw5 = "https://media.discordapp.net/attachments/721728322266071130/723714337922875464/image0.jpg" " https://media.discordapp.net/attachments/721728322266071130/723714338220933120/image1.jpg" " https://media.discordapp.net/attachments/721728322266071130/723714338531049472/image2.jpg" " https://media.discordapp.net/attachments/721728322266071130/723714338757673030/image3.jpg" " https://media.discordapp.net/attachments/721728322266071130/723714339080503316/image4.jpg"
sfw6 = "https://media.discordapp.net/attachments/723715512827117650/723715791811248239/image0.jpg" " https://media.discordapp.net/attachments/723715512827117650/723715792155181076/image1.jpg" " https://media.discordapp.net/attachments/723715512827117650/723715792385998929/image2.jpg" " https://media.discordapp.net/attachments/723715512827117650/723715792675536926/image3.jpg" " https://media.discordapp.net/attachments/723715512827117650/723715793036247050/image4.jpg"
sfw7 = "https://media.discordapp.net/attachments/723715512827117650/723717474968928286/image0.jpg" " https://media.discordapp.net/attachments/723715512827117650/723717475245490176/image1.jpg" " https://media.discordapp.net/attachments/723715512827117650/723717475568713805/image2.jpg" " https://media.discordapp.net/attachments/723715512827117650/723717475811721286/image3.jpg" " https://media.discordapp.net/attachments/723715512827117650/723717487589457960/image4.jpg"
sfw8 = "https://media.discordapp.net/attachments/723715512827117650/723719261297573978/image0.jpg" " https://media.discordapp.net/attachments/723715512827117650/723719261553426483/image1.jpg" " https://media.discordapp.net/attachments/723715512827117650/723719262153212024/image2.jpg" " https://media.discordapp.net/attachments/723715512827117650/723719262463721492/image3.jpg" " https://media.discordapp.net/attachments/723715512827117650/723719262862049360/image4.jpg"
sfw9 = "https://media.discordapp.net/attachments/723715512827117650/723719263214632980/image5.jpg" " https://media.discordapp.net/attachments/723722369469907006/723987427932504125/image0.jpg" " https://media.discordapp.net/attachments/723722369469907006/724297749935292478/image2.png" " https://media.discordapp.net/attachments/723722369469907006/724297749637365840/image1.jpg" " https://media.discordapp.net/attachments/723722369469907006/724297748374880256/image0.jpg"
sfw10 = "https://media.discordapp.net/attachments/723722369469907006/724343251884048394/image4.jpg" " https://media.discordapp.net/attachments/723722369469907006/724344498112692224/image0.jpg" " https://media.discordapp.net/attachments/723722369469907006/724343250780946432/image1.jpg" " https://media.discordapp.net/attachments/723722369469907006/724343251192250418/image2.jpg" " https://media.discordapp.net/attachments/723722369469907006/724343250403721306/image0.jpg"
sfw11 = "https://media.discordapp.net/attachments/723722369469907006/724345766398656624/image0.jpg" " https://media.discordapp.net/attachments/723722369469907006/724345766650576906/image1.jpg" " https://media.discordapp.net/attachments/723722369469907006/724343251615744030/image3.jpg" " https://media.discordapp.net/attachments/723722369469907006/724345967083520273/image0.jpg" " https://media.discordapp.net/attachments/723722369469907006/724345978886422538/image0.jpg"
sfw12 = "https://media.discordapp.net/attachments/723722369469907006/724347499288068126/image0.jpg" " https://media.discordapp.net/attachments/723722369469907006/724347499707629588/image1.jpg" " https://media.discordapp.net/attachments/723722369469907006/724347500009357372/image2.jpg" " https://media.discordapp.net/attachments/723722369469907006/724347500496158821/image3.jpg" " https://media.discordapp.net/attachments/723722369469907006/724347500898549880/image4.jpg"
sfw13 = "https://media.discordapp.net/attachments/723723371589664791/725152518434193468/image0.jpg" " https://media.discordapp.net/attachments/723723371589664791/725152519151419512/image1.jpg" " https://media.discordapp.net/attachments/723723371589664791/725152519470448711/image2.jpg" " https://media.discordapp.net/attachments/723723371589664791/725152519788953701/image3.jpg" " https://media.discordapp.net/attachments/723723371589664791/725152520070234162/image4.jpg"
client = commands.Bot(command_prefix = '?')

client.remove_command("help")
@client.event

async def on_ready():
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Fortnite Porn"))
     print('Bot is Online')




@client.command()
async def fnlibrary(ctx):
     await ctx.send("Are you sure you want to do this? type ?fnconfirm to see the whole Fortnite Porn library, navigate with all of the current pages: We currently have 2 pages, to navigate to page 2 type ?fnpg2 to go to the second page.")

@client.command()
async def fnconfirm(ctx):
     await ctx.send("Posting all current Fortnite Porn from Page 1 of the library.")
     await asyncio.sleep(3)
     await ctx.send(sfw1)
     await asyncio.sleep(3)
     await ctx.send("Posted all Fortnite Porn for Page 1, for Page 2 type ?fnpg2")

@client.command()
async def fnpg2(ctx):
    await ctx.send("Posting all Fortnite Porn from Page 2 of the library.")
    await asyncio.sleep(3)
    await ctx.send(sfw2)
    await asyncio.sleep(3)
    await ctx.send("Posted all Fortnite Porn from Page 2 of the library, for Page 3 type ?fnpg3")

@client.command()
async def fnpg3(ctx):
    await ctx.send("Posting all Fortnite Porn from Page 3 of the library.")
    await asyncio.sleep(3)
    await ctx.send(sfw3)
    await asyncio.sleep(3)
    await ctx.send("Posted all Fortnite Porn from Page 3 of the library, for Page 4 type ?fnpg4")
    
@client.command()
async def fnpg4(ctx):
    await ctx.send("Posting all Fortnite Porn from Page 4 of the library.")
    await asyncio.sleep(3)
    await ctx.send(sfw4)
    await asyncio.sleep(3)
    await ctx.send("Posted all Fortnite Porn from Page 4 of the library, for Page 5 type ?fnpg5")
@client.command()
async def fnpg5(ctx):
    await ctx.send("Posting all Fortnite Porn from Page 5 of the library.")
    await asyncio.sleep(3)
    await ctx.send(sfw5)
    await asyncio.sleep(3)
    await ctx.send("Posted all Fortnite Porn from Page 5 of the library, for Page 6 type ?fnpg6")
@client.command()
async def fnpg6(ctx):
    await ctx.send("Posting all Fortnite Porn from Page 6 of the library.")
    await asyncio.sleep(3)
    await ctx.send(sfw6)
    await asyncio.sleep(3)
    await ctx.send("Posted all Fortnite Porn from Page 6 of the library, for Page 7 type ?fnpg7")
@client.command()
async def fnpg7(ctx):
    await ctx.send("Posting all Fortnite Porn from Page 7 of the library.")
    await asyncio.sleep(3)
    await ctx.send(sfw7)
    await asyncio.sleep(3)
    await ctx.send("Posted all Fortnite Porn from Page 7 of the library, for Page 8 type ?fnpg8")
@client.command()
async def fnpg8(ctx):
    await ctx.send("Posting all Fortnite Porn from Page 8 of the library.")
    await asyncio.sleep(3)
    await ctx.send(sfw8)
    await asyncio.sleep(3)
    await ctx.send("Posted all Fortnite Porn from Page 8 of the library, for Page 9 type ?fnpg9")
@client.command()
async def fnpg9(ctx):
    await ctx.send("Posting all Fortnite Porn from Page 9 of the library.")
    await asyncio.sleep(3)
    await ctx.send(sfw9)
    await asyncio.sleep(3)
    await ctx.send("Posted all Fortnite Porn from Page 9 of the library, for Page 10 type ?fnpg10")
@client.command()
async def fnpg10(ctx):
    await ctx.send("Posting all Fortnite Porn from Page 10 of the library.")
    await asyncio.sleep(3)
    await ctx.send(sfw10)
    await asyncio.sleep(3)
    await ctx.send("Posted all Fortnite Porn from Page 10 of the library, for Page 11 type ?fnpg11")
@client.command()
async def fnpg11(ctx):
    await ctx.send("Posting all Fortnite Porn from Page 11 of the library.")
    await asyncio.sleep(3)
    await ctx.send(sfw11)
    await asyncio.sleep(3)
    await ctx.send("Posted all Fortnite Porn from Page 11 of the library, for Page 12 type ?fnpg12")
@client.command()
async def fnpg12(ctx):
    await ctx.send("Posting all Fortnite Porn from Page 12 of the library.")
    await asyncio.sleep(3)
    await ctx.send(sfw12)
    await asyncio.sleep(3)
    await ctx.send("Posted all Fortnite Porn from Page 12 of the library, for Page 13 type ?fnpg13")
@client.command()
async def fnpg13(ctx):
    await ctx.send("Posting all Fortnite Porn from Page 13 of the library.")
    await asyncio.sleep(3)
    await ctx.send(sfw13)
    await asyncio.sleep(3)
    await ctx.send("Posted all Fortnite Porn from Page 13 of the library, for Page 14 type ?fnpg14")
@client.command()
async def help(ctx):
     await ctx.send("Locating Commands..")
     await asyncio.sleep(1)
     await ctx.send("Loading Commands..")
     await asyncio.sleep(1)
     await ctx.send("?𝘩𝘦𝘭𝘱")
     await ctx.send("Helps you out with all of the commands.")
     await ctx.send("?𝘧𝘯𝘭𝘪𝘣𝘳𝘢𝘳𝘺")
     await ctx.send("Shows you all Fortnite Porn avalible.")
     await ctx.send("?𝘧𝘯𝘱𝘨(𝘯𝘶𝘮𝘣𝘦𝘳)")
     await ctx.send("This is here to navigate through the Fortnite Porn pages!")
     await ctx.send("These are all of the commands so far.")
client.run("NzIzNjgyMzgzNzA1OTMxODE3.Xvo31w.zsSKCgGTlpU5dcUmVbXdTFc7_6E")
