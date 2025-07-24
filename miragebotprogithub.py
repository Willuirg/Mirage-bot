guild_configs = {}  # Exemplo simples, reinicia ao desligar o bot
import random
import asyncio
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot (command_prefix=';',intents=intents)  

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot is ready!")


@bot.command()
async def ping(ctx):
    latencia = round(bot.latency * 1000)  # milissegundos
    await ctx.reply(f"Pong! Latência: {latencia}ms")

@bot.command()
async def hello(ctx):
    await ctx.reply("Oie, tudo bem?" \
    " Sou o bot do Wil, estou aqui para te ajudar!" )


@bot.command()
async def somar(ctx:commands.Context, num1=None, num2=None):
    if num1 is None and num2 is None:
        await ctx.reply("Por favor, informe dois números para somar. Exemplo: `;somar 2 3`")
        return
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        await ctx.reply("Por favor, informe apenas números inteiros. Exemplo: `;somar 2 3`")
        return
    resultado = num1 + num2
    await ctx.reply(f"A soma de {num1} e {num2} é: {resultado}")
    if num1 == 0 and num2 == 0:
        await ctx.reply("Somar com 0? Não faz sentido, né? 😅")


@bot.command()
async def soma(ctx:commands.Context, num1=None, num2=None):
    resultadodetexto = num1 + num2
    await ctx.reply(f"A soma de textos(troll hihi) é: {resultadodetexto}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("Você esqueceu de informar um argumento necessário. Por favor, verifique o comando e tente novamente.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.reply("Comando não encontrado. Verifique se você digitou o comando corretamente.")
    else:
        await ctx.reply(f"Ocorreu um erro: {str(error)}")

# @bot.event
# async def on_member_ban(guild, user):
#     canal_ban = bot.get_channel(1385784437568045169)
#     await canal_ban.send(f"{user.mention} foi de arrasta pra cima, PÁ ACESSO NEGADO🚫")

# @bot.event
# async def on_member_join(member: discord.Member):
#     canal_join = bot.get_channel(1385781774063501354)
#     await canal_join.send (f"Bem-vindo(a) {member.mention} ao servidor! Espero que se divirta aqui! Se precisar de ajuda, é só chamar o Pac ou qualquer outro membro da equipe! 😊")



@bot.command()
async def avatar(ctx: commands.Context, membro: discord.Member = None):
    user = membro or ctx.author
    embed = discord.Embed(title=f"Avatar de {user.name}", color=discord.Color.blue())
    embed.set_image(url=user.avatar.url if user.avatar else user.default_avatar.url)
    await ctx.reply(embed=embed)

@bot.tree.command(description="Mostra o avatar do usuário ou o seu, se não informar ninguém.")
async def avatar(interaction: discord.Interaction, user: discord.User = None):
    user = user or interaction.user
    embed = discord.Embed(title=f"Avatar de {user.name}", color=discord.Color.blue())
    embed.set_image(url=user.avatar.url if user.avatar else user.default_avatar.url)
    await interaction.response.send_message(embed=embed)


@bot.tree.command(description="Mostra o avatar do usuário ou o seu, de forma privada.")
async def avatar_in_secret(interaction: discord.Interaction, user: discord.User = None):
    user = user or interaction.user
    embed = discord.Embed(title=f"Avatar de {user.name}", color=discord.Color.blue())
    embed.set_image(url=user.avatar.url if user.avatar else user.default_avatar.url)
    await interaction.response.send_message(embed=embed, ephemeral=True)

@bot.command()
async def mercador(ctx: commands.Context):
    quotes = [
      "Got some rare things on sale, stranger! 😎",
      "What are ya buyin'?",
      "What are ya sellin'?",
      "Ahhh... I'll buy it at a high price!",
      "Hehehe... Thank you!",
      "Not enough cash, stranger.",
      "Come back anytime.",
      "Stranger, stranger! Now that's a weapon!",
      "Is that all, stranger?",
      "Hehehehehe...",
      "Heh heh heh... Thank you!",
      "Ahh, I'll buy it at a high price.",
      "I'll pay a high price for that!",
      "Got a selection of good things on sale, stranger!",
      "Hehehe... Welcome!",
    ]

    quote = random.choice(quotes)
    await ctx.reply(quote)

@bot.tree.command(description="Mostra os comandos disponíveis.")
async def help(interaction: discord.Interaction):
    embed =  discord.Embed(title="Comandos Disponíveis", color=discord.Color.blue())
    embed.add_field(name = ";ping", value = "Responde com 'Pong!(futuramente terá a latência do bot)")
    embed.add_field(name=";hello", value = "Responde o seu olá com uma saudação amigável.")
    embed.add_field(name=";somar <num1> <num2>",value = 'Soma dois numeros INTEIROS. Exemplo: `;somar 2 3`')
    embed.add_field(name=";soma <texto1> <texto2>", value = "Soma dois textos (trollagem). Exemplo: `;soma Olá Mundo`")
    embed.add_field(name=";avatar", value = "Mostra o seu avatar ou de outro usuário, basta marcar ele na mensagem.(que foto linda!)")
    embed.add_field(name="/avatar", value= "Mesma coisa do ;avatar. mas em slash command.")
    embed.add_field(name="/avatar_in_secret", value= "Mostra o seu avatar ou do usuário que você escolher, mas em segredo(só eu e você hihi)")
    embed.add_field(name="tem mais segredos do wil, mas só eu sei", value = "Tem nada aq não kkkkk")
    embed.add_field(name=";mercador", value="Hehehe... Welcome!")
    await interaction.response.send_message(embed=embed,ephemeral = True)

@bot.command()
async def Help(ctx: commands.Context):
    embed = discord.Embed(title="Comandos Disponíveis", color=discord.Color.blue())
    embed.add_field(name=";ping", value="Responde com 'Pong!(futuramente terá a latência do bot)")
    embed.add_field(name=";hello", value="Responde o seu olá com uma saudação amigável.")
    embed.add_field(name=";somar <num1> <num2>", value='Soma dois numeros INTEIROS. Exemplo: `;somar 2 3`')
    embed.add_field(name=";soma <texto1> <texto2>", value="Soma dois textos (trollagem). Exemplo: `;soma Olá Mundo`")
    embed.add_field(name=";avatar", value="Mostra o seu avatar.(que foto linda!)")
    embed.add_field(name="/avatar", value="Mesma coisa do ;avatar. mas em slash command.")
    embed.add_field(name="/avatar_in_secret", value="Mostra o seu avatar ou do usuário que você escolher, mas em segredo(só eu e você hihi)")
    embed.add_field(name=";mercador", value="Hehehe... Welcome!")
    embed.add_field(name="/kwisatz", value="Kwisatz Haderach! (Duna, eu te explico como que é meu caro!!)")
    embed.add_field(name="tem mais segredos do wil, mas só eu sei", value = "Tem nada aq não kkkkk")
    await ctx.reply(embed=embed)

# @bot.event
# async def on_message(message: discord.Message):
#     if message.author.bot:
#         return

#     if message.content.startswith("Mercador") or message.content.startswith("mercador"):
#         quotes = [
#             "Got some rare things on sale, stranger! 😎",
#             "What are ya buyin'?",
#             "What are ya sellin'?",
#             "Ahhh... I'll buy it at a high price!",
#             "Hehehe... Thank you!",
#             "Not enough cash, stranger.",
#             "Come back anytime.",
#             "Stranger, stranger! Now that's a weapon!",
#             "Is that all, stranger?",
#             "Hehehehehe...",
#             "Heh heh heh... Thank you!",
#             "Ahh, I'll buy it at a high price.",
#             "I'll pay a high price for that!",
#             "Got a selection of good things on sale, stranger!",
#             "Hehehe... Welcome!",
#         ]
#         quote = random.choice(quotes)
#         await message.channel.send(quote)    


@bot.tree.command(description = "Kwisatz Haderach!")
async def kwisatz(interaction : discord.Interaction):
    embed = discord.Embed(title="Kwisatz Haderach", description="O Kwisatz Haderach é um conceito do universo de Duna, criado por Frank Herbert. Ele se refere a um ser humano que possui habilidades mentais e físicas extraordinárias, capaz de acessar memórias ancestrais e prever o futuro. O Kwisatz Haderach é visto como uma figura messiânica, destinada a trazer mudanças significativas para o universo.", color=discord.Color.gold())
    embed.set_image(url="https://images-ext-1.discordapp.net/external/fPNVtlMKJuxV7sQb2GybP93DnM6HYGnd4ItFK2Q-pYA/%3F_nc_cat%3D109%26ccb%3D1-7%26_nc_sid%3D127cfc%26_nc_ohc%3DMTD_3ThbnzwQ7kNvwE3eNVT%26_nc_oc%3DAdkNzJGsFMymawD0Mb_3NDxCUCOlSl_RIp4SEaIL1tflFklxHcD-Q2OFMDccTO95hnPl9C8jN1bRqjyJYXDmGrN6%26_nc_zt%3D23%26_nc_ht%3Dscontent.fplu17-1.fna%26_nc_gid%3DqSwwv5grgrHtwy-vZK5PrQ%26oh%3D00_AfNOIZI8NxXUeLVAJfvIB2rPWoD5FEewDndyVHisyeeVAA%26oe%3D6860EA92/https/scontent.fplu17-1.fna.fbcdn.net/v/t39.30808-6/480238488_8767540540019250_5450124264791095945_n.jpg?format=webp&width=562&height=649")
    await interaction.response.send_message(embed=embed)



@bot.tree.command (description = "Segredos do wil!")
async def segredos (interaction : discord.Interaction):
    embed = discord.Embed(title = "Segredinhos do wil (o lendario que me criou)",color = discord.Color.purple())
    embed.add_field(name = "Segredo 1", value = "O Wil adora jogar Brawl Stars, um dia chama ele pra jogar com você!")
    embed.add_field(name = "Segredo 2", value = "Ele tem serios problemas com preguiça (pra escrever esse comando, ele demorou cerca de 34 minutos e 23 segundos! com todas as correções de erro deu em um total de 56 minutos e 26 segundos!)")
    embed.add_field(name = "Segredo 3", value = "Você que está lendo isso, é um grande sem oque fazer, por que você está lendo isso ainda? kkkkkkk")
    embed.add_field(name = "Dica", value = "tente falar sobre filosofia com ele, ele adora e vai te explicar oque for com o maior prazer do mundo!")
    embed.add_field(name = "Aliás, uma foto dele ai, btw", value = "https://media.discordapp.net/attachments/1307000023220748329/1384661638505828503/image.png?ex=685bcfe4&is=685a7e64&hm=113b3c905e2872de496649fa3df6caf787f949990effb9ba4f260d9ec55e6e31&=&format=webp&quality=lossless&width=685&height=649")
    embed.set_image(url="https://media.discordapp.net/attachments/1307000023220748329/1384661638505828503/image.png?ex=685bcfe4&is=685a7e64&hm=113b3c905e2872de496649fa3df6caf787f949990effb9ba4f260d9ec55e6e31&=&format=webp&quality=lossless&width=685&height=649")
    embed.set_footer(text="Esses segredos foram criados pelo Wil, então não me culpe por nada, ok? Se você não gostou, é só falar com ele! (ou não, kkkkk)")
    await interaction.response.send_message(embed=embed, ephemeral=True)

@bot.command()
async def queima(ctx: commands.Context):
    if ctx.author.guild_permissions.administrator:
        await ctx.channel.purge(limit=500)
        await ctx.send("Chat limpo com sucesso!", delete_after=5)
    else:
        await ctx.reply("Você não tem permissão para usar esse comando.", delete_after=5)

@bot.command()
async def limpar(ctx: commands.Context, quantidade: int = 10):
    if ctx.author.guild_permissions.administrator:
        await ctx.channel.purge(limit=quantidade)
        await ctx.send(f"{quantidade} mensagens apagadas com sucesso!", delete_after=5)
    else:
        await ctx.reply("Você não tem permissão para usar esse comando.", delete_after=5)




@bot.tree.command(description= "Spama o chat KKKKKKKKKKKKK")
async def spam(interaction: discord.Interaction, quantidade: int =10):
    if interaction.user.id == 771430165611544597:
        for i in range(quantidade):
            await interaction.channel.send("Spamado com sucesso! KKKKKKKKKKKK")
            await asyncio.sleep(0.5)  # Pequeno delay para evitar rate limit
    else:
        await interaction.response.send_message("Apenas o Wil pode usar esse comando!", ephemeral=True)



@bot.tree.command(description="Configura o canal onde não pode mandar mensagem")
async def set_lock_channel(interaction: discord.Interaction, canal: discord.TextChannel):
    guild_id = interaction.guild.id
    guild_configs[guild_id] = {"lock_channel": canal.id}
    await interaction.response.send_message(f"Canal bloqueado configurado: {canal.mention}", ephemeral=True)


@bot.tree.command(description="Bloqueia o canal configurado")
async def lock(interaction: discord.Interaction):
    guild_id = interaction.guild.id
    config = guild_configs.get(guild_id)
    if not config or "lock_channel" not in config:
        await interaction.response.send_message("Nenhum canal configurado para lock.", ephemeral=True)
        return
    canal = interaction.guild.get_channel(config["lock_channel"])
    overwrite = canal.overwrites_for(interaction.guild.default_role)
    overwrite.send_messages = False
    await canal.set_permissions(interaction.guild.default_role, overwrite=overwrite)
    await interaction.response.send_message(f"Canal {canal.mention} bloqueado!", ephemeral=True)


@bot.tree.command(description="Desbloqueia o canal configurado")
async def unlock(interaction: discord.Interaction):
    guild_id = interaction.guild.id
    config = guild_configs.get(guild_id)
    if not config or "lock_channel" not in config:
        await interaction.response.send_message("Nenhum canal configurado para unlock.", ephemeral=True)
        return
    canal = interaction.guild.get_channel(config["lock_channel"])
    overwrite = canal.overwrites_for(interaction.guild.default_role)
    overwrite.send_messages = True
    await canal.set_permissions(interaction.guild.default_role, overwrite=overwrite)
    await interaction.response.send_message(f"Canal {canal.mention} desbloqueado!", ephemeral=True)


@bot.command()
async def definir_canal(ctx: commands.Context, canal: discord.TextChannel):
    guild_id = ctx.guild.id
    guild_configs[guild_id] = {"lock_channel": canal.id}
    await ctx.reply(f"Canal bloqueado configurado: {canal.mention}")

@bot.command()
async def lock_canal(ctx: commands.Context):
    guild_id = ctx.guild.id
    config = guild_configs.get(guild_id)
    if not config or "lock_channel" not in config:
        await ctx.reply("Nenhum canal configurado para lock.")
        return
    canal = ctx.guild.get_channel(config["lock_channel"])
    overwrite = canal.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await canal.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.reply(f"Canal {canal.mention} bloqueado!")

@bot.command()
async def unlock_canal(ctx: commands.Context):
    guild_id = ctx.guild.id
    config = guild_configs.get(guild_id)
    if not config or "lock_channel" not in config:
        await ctx.reply("Nenhum canal configurado para unlock.")
        return
    canal = ctx.guild.get_channel(config["lock_channel"])
    overwrite = canal.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await canal.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.reply(f"Canal {canal.mention} desbloqueado!")



@bot.command()
async def ban(ctx: commands.Context, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.ban_members:
        await member.ban(reason=reason)
        await ctx.reply(f"{member.mention} foi banido do servidor! Motivo: {reason if reason else 'Nenhum motivo especificado.'}")
    else:
        await ctx.reply("Você não tem permissão para banir membros.")


@bot.command()
async def mute(ctx: commands.Context, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.mute_members:
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not mute_role:
            mute_role = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(mute_role, send_messages=False, speak=False)
        await member.add_roles(mute_role, reason=reason)
        await ctx.reply(f"{member.mention} foi silenciado! Motivo: {reason if reason else 'Nenhum motivo especificado.'}")
    else:
        await ctx.reply("Você não tem permissão para silenciar membros.")


@bot.command()
async def castigo(ctx: commands.Context, member: discord.Member, *, reason=None, ):
    if ctx.author.guild_permissions.manage_messages:
        await member.timeout(discord.utils.utcnow() + discord.utils.timedelta(minutes=10), reason=reason)
        await ctx.reply(f"{member.mention} foi colocado em timeout por 10 minutos! Motivo: {reason if reason else 'Nenhum motivo especificado.'}")
    else:
        await ctx.reply("Você não tem permissão para aplicar castigos.")
