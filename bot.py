import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {client.latency * 1000}')


@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['As I see it, yes.',
                 'Ask again later.',
                 'Better not tell you now',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Don’t count on it.',
				 'It is certain.',
                 'It is decidedly so.',
                 'Most likely.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Outlook good.',
                 'Reply hazy, try again.',
                 'Signs point to yes.',
                 'Very doubtful.',
                 'Without a doubt.',
                 'Yes.',
                 'Yes – definitely.',
                 'You may rely on it.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def clear(ctx , amount=1000):
	await ctx.channel.purge(limit = amount)

@client.command()
async def kick(ctx , member : discord.member , * , reason=None):
	await member.kick(reason = reason)

@client.command()
async def ban(ctx , member : discord.member , * , reason=None):
	await member.ban(reason = reason)

client.run('Nzg3MjI1NjY0MTU4OTU3NTY4.X9R3CA.4FSVh015VIKJEjcXkQEiTW5w8nI')
