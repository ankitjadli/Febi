import discord
import asyncio
from discord.ext import commands

TOKEN = 'NTI3NDgzMDczNzI2NjQ0MjMz.DwX2dA.FyUnETLQ6EoFpYv_DxdZDFH31kI'

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='with Ankit'))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def ping():
	await client.say('Pong!')

@client.command(pass_context=True)
async def help(ctx):
 	author = ctx.message.author

 	embed = discord.Embed(
 		colour = discord.Colour.blue()
 	)

 	embed.set_author(name='Commands for using Febi :')
 	embed.add_field(name='!yo', value='Replies yo', inline=True)
 	embed.add_field(name='!wadap', value='Replies wadap MF', inline=True)
 	embed.add_field(name='!curse', value='Replies with a Curse word', inline=True)
 	embed.add_field(name='!emote', value='Replies with a Emote', inline=True)

 	await client.send_message(author, embed=embed)

client.run(TOKEN)    