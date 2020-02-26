import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random

TOKEN = 'NjgwODE5MzgxNjcyMDgzNTM2.XlbCbw.VEQHUs-XKZMvKnjM159TK3MMQX0'

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
async def invlink(link):
    await link.channel.send('Ссылка: https://discord.gg/p4MrpbT')

@bott.command(pass_context=True)
async def coin(coin):
    variable = [
        "Выпал орёл!",
        "Выпала решка!",]
    await coin.channel.send("{}".format(random.choice(variable)))


@bott.event
async def on_member_join(rolee):
    role = discord.utils.get(rolee.guild.roles, name = "NovicE")
    await rolee.add_roles(role)

@bott.command(pass_context=True)
async def ping(pingg):
    await pingg.channel.send('Pong!')

@bott.command()
@commands.has_any_role('Silencer', 'AdministratoR','Administration Supervisor','Curator','Co-ManageR','ManageR','Co-OwneR','OwneR')
async def mute(ctx, member: discord.Member = None):
    role = discord.utils.get(ctx.guild.roles, name = 'Muted')
    if not member:
        await ctx.send('Вы не указали пользователя')
        return
    await member.add_roles(role)
    await ctx.send(str(member) + " Был замучен.")

@bott.command()
@commands.has_any_role('Silencer', 'AdministratoR','Administration Supervisor','Curator','Co-ManageR','ManageR','Co-OwneR','OwneR')
async def unmute(ctx, member: discord.Member = None):
    role = discord.utils.get(ctx.guild.roles, name = 'Muted')
    if not member:
        await ctx.send('Вы не указали пользователя')
        return
    await member.remove_roles(role)
    await ctx.send(str(member) + " Снова может говорить!")


@bott.command(pass_contesxt=True)
async def commands(comm):
    await comm.channel.send('Список комманд:\n• !coin - Бросить монетку.\n• !rules - Правила сервера.\n• !invlink - Ссылка для приглашения друзей.\n• !help - для вызова этого списка.')

bott.run(TOKEN)
