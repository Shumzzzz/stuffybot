import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import os

TOKEN = 'NjgwODE5MzgxNjcyMDgzNTM2.XlV4Nw.b78xGe23RsCzcPmFMu0THQ9RRNk'

bott = Bot(command_prefix='!') #инициализируем бота с префиксом '!'
@bott.command(pass_context=True) #разрешаем передавать агрументы
async def test(ctx, arg): #создаем асинхронную фунцию бота
    await ctx.send(arg) #отправляем обратно аргумент


@bott.event
async def on_ready():
    print('Logged in as')
    print(bott.user.name)
    print(bott.user.id)
    print('------')

@bott.command(pass_context=True)
async def rules(rule):
    await rule.channel.send('Правила сервера:\n• Не спамь.\n• Не размещайте личную информацию.\
\n• Не рекламируйте и не делитесь социальными ссылками.\n• Не размещайте ссылки, которые могут причинить вред другим.\
\n• Не выдавайте себя за администраторов или других пользователей.\n• Не просите денег или предметов.\n• Не публикуйте\
контент NSFW(Для этого есть отдельный канал!)\n\nОстальные условия в Discord Условия использования и Руководящие принципы сообщества также действуют там, где это применимо.Правила могут изменяться без ведома участников сервера!')

@bott.command(pass_context=True)
async def invitelink(link):
    await link.channel.send('Ссылка: https://discord.gg/sY7y3n6')

@bott.command(pass_context=True)
async def coinflip(coin):
    variable = [
        "Выпал орёл!",
        "Выпала решка!",]
    await coin.channel.send("{}".format(random.choice(variable)))

@bott.event
async def on_voice_state_update(before, after ):
    role = discord.utils.get(after.server.roles, name="NovicE")
    if not before.voice.voice_channel and after.voice.voice_channel:
        await bott.add_roles(after, role)
    elif before.voice.voice_channel and not after.voice.voice_channel:
        await bott.remove_roles(after, role)

@bott.event
async def on_member_join(rolee):
    role = discord.utils.get(rolee.guild.roles, name = "NovicE")
    await rolee.add_roles(role)
bott.run(TOKEN)
