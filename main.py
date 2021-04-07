import discord
import os
import youtube_dl
#from pydub import AudioSegment
from discord.ext import commands
#from audio import speed_change
from pysndfx import AudioEffectsChain

bot = commands.Bot(command_prefix = '!yee ')

@bot.command(name = 'url')
async def yt(ctx, url):
  song_there = os.path.isfile('./song.mp3')
  try:
    if song_there:
      os.remove('./song.mp3')
  except PermissionError:
    await ctx.send("dude im going to cuhm on u")
  ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': './song.mp3',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
  fx = (
    AudioEffectsChain()
    .reverb()
    .speed(0.77)
  )
  fx('./song.mp3', './song.mp3')
  await ctx.send(file=discord.File('./song.mp3'))

@bot.command(name = 'ping')
async def ping(ctx):
  await ctx.send("im gonna cuhm on u fr")
@bot.event
## Calls when login is sucessful, prints user info 
async def on_ready():
  print('Logged in as {0.user}'.format(bot))

bot.run(os.getenv('TOKEN'))