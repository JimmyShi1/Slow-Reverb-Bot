import discord
import os
import youtube_dl
from pydub import AudioSegment
from discord.ext import commands
from audio import speed_change
from dotenv import load_dotenv
#from pysndfx import AudioEffectsChain
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix = '!yee ')

@bot.command(name = 'play')
async def play(ctx, url):
  song_there = os.path.isfile("./song.mp3")
  try:
    if song_there:
      os.remove("./song.mp3")
  except PermissionError:
    await ctx.send("there is already something playing, you're getting cuhmed on")

  voice_channel = ctx.message.author.voice.channel
  channel = voice_channel.name
  vc = await voice_channel.connect()
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
    info_dict = ydl.extract_info(url, download=False)
    video_title = info_dict.get('title', None)
  sound = AudioSegment.from_file('./song.mp3')
  newSound = speed_change(sound, 0.77)
  file_handle = newSound.export('./song.mp3', format="mp3")
  vc.play(discord.FFmpegPCMAudio('./song.mp3'))
  await ctx.send("Now playing: " + video_title)
  

@bot.command(name = 'reverb')
#sends .mp3 file of youtube link in chat. Takes command [prefix] [url] [name = optional]
#if no name is given, the file defaults to the youtube name
async def yt(ctx, url, *args):
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
    info_dict = ydl.extract_info(url, download=False)
    video_title = info_dict.get('title', None)
  if args:
    newPath = "./" + ("{}".format(" ".join(args))) + ".mp3"
  else:
    newPath = "./" + video_title + ".mp3"
  os.rename("./song.mp3",newPath)
  sound = AudioSegment.from_file(newPath)
  newSound = speed_change(sound, 0.77)
  file_handle = newSound.export(newPath, format="mp3")
  await ctx.send(file=discord.File(newPath))
  os.remove(newPath)

@bot.command(name = 'ping')
## Responds with any message to show the bot is online and working
async def ping(ctx):
  await ctx.send("im gonna cuhm on u fr")
@bot.command(name = 'andrew')
async def andrew(ctx):
  await ctx.send("andrew feelsweir")
@bot.event
## Calls when login is sucessful, prints user info 
async def on_ready():
  print('Logged in as {0.user}'.format(bot))

bot.run(TOKEN)