import discord
import os
import youtube_dl
from pydub import AudioSegment
from discord.ext import commands
from audio import speed_change
#from pysndfx import AudioEffectsChain
bot = commands.Bot(command_prefix = '!yee ')

@bot.command(name = 'reverb')
async def yt(ctx, url):
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
  newPath = "./" + video_title + ".mp3"
  os.rename(r"./song.mp3",newPath)
  sound = AudioSegment.from_file(newPath)
  newSound = speed_change(sound, 0.77)
  file_handle = newSound.export(newPath, format="mp3")
  await ctx.send(file=discord.File(newPath))
  os.remove(newPath)

@bot.command(name = 'ping')
## Responds with any message to show the bot is online and working
async def ping(ctx):
  await ctx.send("im gonna cuhm on u fr")
@bot.event
## Calls when login is sucessful, prints user info 
async def on_ready():
  print('Logged in as {0.user}'.format(bot))

bot.run(os.getenv('TOKEN'))