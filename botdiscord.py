import discord
import bot_logic
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def all(ctx):
    await ctx.send('Wszystkie komendy:\n**$all** - Wyświetla wszystkie komendy\n**$hello** - Wita się\n**$bye** - Żegna się\n**$hehe #** - Pisze "he" # razy\n**$password #** - Generuje hasło o długości #\n**$h #** - Pisze "h " # razy\n**$coin** - Rzuca monetą\n**$emoji** - Generuje losową emotkę\n**$dice #** - Rzuca kostką o # ścianach')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem {bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'👋')

@bot.command()
async def hehe(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def password(ctx, pass_chars = 12):
    await ctx.send(bot_logic.gen_pass(pass_chars))

@bot.command()
async def h(ctx, count_h = random.randint(3,13)):
    await ctx.send("h " * count_h)

@bot.command()
async def coin(ctx):
    await ctx.send(bot_logic.coin())

@bot.command()
async def emoji(ctx):
    await ctx.send(bot_logic.gen_emoji())

@bot.command()
async def dice(ctx, dice_sides = 6):
    await ctx.send(bot_logic.kostka(dice_sides))

bot.run("tu idzie token")
