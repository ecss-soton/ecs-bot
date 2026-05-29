import discord
from discord import app_commands
from discord.ext import commands

from bot.config import SECRET_CHANNEL_ID


class Appreciation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="appreciate",
        description="Secretly nominate a committee member for a weekly shoutout!",
    )
    @app_commands.describe(
        nominee="Who are you nominating?",
        reason="What did they do to deserve it?",
    )
    async def appreciate(
        self,
        interaction: discord.Interaction,
        nominee: discord.Member,
        reason: str,
    ):
        await interaction.response.send_message(
            f"Your nomination for **{nominee.display_name}** has been "
            f"secretly submitted. Thank you!",
            ephemeral=True,
        )

        embed = discord.Embed(
            title="\U0001f338 New Weekly Appreciation Nomination",
            color=discord.Color.from_rgb(255, 182, 193),
        )
        embed.add_field(name="Nominee", value=nominee.mention, inline=False)
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.add_field(
            name="Submitted By", value=interaction.user.mention, inline=False
        )

        channel = self.bot.get_channel(SECRET_CHANNEL_ID)
        if channel:
            await channel.send(embed=embed)
        else:
            print(f"ERROR: Could not find channel {SECRET_CHANNEL_ID}")


async def setup(bot: commands.Bot):
    await bot.add_cog(Appreciation(bot))
