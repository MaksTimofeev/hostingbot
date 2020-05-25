import discord
import config
from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot
import random
from datetime import datetime
import obnova
from obnova import novost
import BotInfo
from BotInfo import infa
from BotInfo import version

admins =["624616513197965353"]

#Переменная префикса и основная и удаление хелпа
PREFIX = '.'
client = commands.Bot(command_prefix = PREFIX)
client.remove_command("help")

#Панель запуска и статус бота
@client.event
async def on_ready( ):
    print("Бот подключен!")
    await client.change_presence( status = discord.Status.dnd, activity = discord.Game("Мастерскую Python /(×_×)/") )
    
#Ивент на сообщения и запись
@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author==client.user:
    	return
    print("{0.guild}. {0.author} на {0.channel}: {0.content}".format(message))
    
#Ивент на ошибку
@client.event
async def on_commands_error( ):
    pass 

#Хелп
@client.command( pass_context = True )
async def хелп( ctx ):
    emb = discord.Embed( title = 'Мои команды, Сэр.', colour = discord.Color.orange() )
    emb.add_field( name = '{}чистка'.format(PREFIX), value = 'Очистка сообщений.')
    emb.add_field( name = '{}юзер'.format(PREFIX), value = 'Информация об участнике.')
    emb.add_field( name = '{}новости'.format(PREFIX), value = 'Новости бота.')
    emb.add_field( name = '{}бот_инфо'.format(PREFIX), value = 'Небольшая информация о боте.')
    emb.add_field( name = '{}бот_вер'.format(PREFIX), value = 'Версия бота.')
    await ctx.send ( embed = emb )

#Юзер
@client.command( pass_context = True )
async def юзер(ctx, member: discord.Member):
    emb = discord.Embed( title = f'Информацич об участнике { member }.', colour = discord.Color.green() )
    emb.add_field( name = 'Имя:', value = f'{ member };')
    emb.add_field( name = 'Ник:', value = f'{ member.nick };')
    emb.add_field( name = 'Роли', value = f'{ member.roles };')
    emb.add_field( name = 'Id:', value = f'{ member.id };')
    emb.add_field( name = 'Статус:', value = f'{ member.status };')
    await ctx.send( embed = emb )
    
#Очистка сообщений
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def чистка( ctx, amount : int ):
	await ctx.channel.purge( limit = amount )
	await ctx.send( f"Удалено { amount } сообщений." )
	
#Обновления
@client.command( pass_context = True )
async def новости(ctx):
    await ctx.send('{0}'.format(novost))

#Информация о боте
@client.command( pass_context = True )
async def бот_инфо( ctx ):
    await ctx.send("{0}".format(infa))
    
@client.command( pass_context = True )
async def бот_вер( ctx ):
    await ctx.send("{0}".format(version))
    
#Команда на сбор
@client.command( pass_context = True )
async def собрать( ctx, arg=None ):
    a = arg
    if a==None:
    	await ctx.send( f"@everyone, { ctx.author.name } объявил общий сбор!")
    else:
        await ctx.send( f"@everyone, { ctx.author.name } объявил общий сбор.\nПо поводу:\n" + a)
    
#Ошибки с чистка
@чистка.error
async def чистка_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send( f"{ ctx.author.name }, укажите кол-во сообщений!")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send( f"{ ctx.author.name }, у вас недостаточно прав для использования данной команды.")
        
#Ошибки с юзер
@юзер.error
async def юзер_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send( f"{ ctx.author.name }, укажите участника, о котором хотите узнать.")
        
#Запуск
client.run( config.TOKEN )