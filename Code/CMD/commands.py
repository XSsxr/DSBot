import asyncio
import random
from discord.ext import commands
from Code.MSG.messages import DeleteMSGTiming
from Code.CONF.config_variables import data

#Roll CMD
class RollCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, *args):
        await ctx.message.delete(delay=DeleteMSGTiming)
        msg = await ctx.send("0")
        ran1, ran2 = 1, 100

        if args:
            try:
                if "-" in " ".join(args):
                    parts = " ".join(args).split("-")
                    ran1 = int(parts[0].strip())
                    ran2 = int(parts[1].strip())
                elif len(args) == 2:
                    ran1 = int(args[0])
                    ran2 = int(args[1])
            except (ValueError, IndexError):
                await msg.edit(content=data["EF"])
                return

        for _ in range(5):
            await asyncio.sleep(0.2)
            await msg.edit(content=f"{random.randint(ran1, ran2)}")

        final = random.randint(ran1, ran2)
        await msg.edit(content=f"{final}")
        await msg.delete(delay=DeleteMSGTiming)
#Roll CMD_ND


#Delete messages CMD
class DeleteMessages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dl(self, ctx, number:int):
        allowed_roles = [1479683391640174612,1423857083715158118]

        if not any(role.id in allowed_roles for role in ctx.author.roles):
            await ctx.send(data["NERTE"], delete_after=5)
            return

        if number > 20:
            confirm_msg = await ctx.send(data["AUSYWTD"].format(number=number))
            await confirm_msg.add_reaction("✅")
            await confirm_msg.add_reaction("❌")

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in ["✅", "❌"] and reaction.message.id == confirm_msg.id
            try:
                reaction,user = await self.bot.wait_for("reaction_add",timeout=30.0,check=check)
            except asyncio.TimeoutError:
                await ctx.send(data["WTE"], delete_after=5)
                await ctx.channel.purge(limit=3)
                return

            if str(reaction.emoji) == "✅":
                await ctx.channel.purge(limit=number+1)
            else:
                await ctx.send(data["DC"], delete_after=5)
                await ctx.channel.purge(limit=3)
        else:
            await ctx.channel.purge(limit=number+1)
#Delete messages CMD_ND