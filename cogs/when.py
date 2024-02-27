import discord
from discord.ext import commands
from discord import app_commands

class when(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="when", description="Have trouble knowing when the next season will begin?")
    async def when(self, interaction: discord.Integration):
        embed = discord.Embed(colour=discord.Colour.dark_gold(),
                            description="The question that will always hit the discord",
                            title="When will the 2024 Season Start?")
        embed.add_field(name=f"When will gameplan page be available?", value="Probably in the new year.", inline=False)
        embed.add_field(name=f"When will the SimNFL Draft Start?", value="Probably after valentine's day.", inline=False)
        embed.add_field(name=f"When will spring games be here?", value="Probably after the SimNFL Draft.", inline=False)
        embed.add_field(name=f"When can I schedule my OOC opponents?", value="Probably in the new year.", inline=False)
        embed.add_field(name=f"When will the Free Agency Sync be ran?", value="Tuesdays.", inline=False)
        embed.add_field(name=f"When will the Crooting Sync be ran?", value="Wednesday mornings, all leagues.", inline=False)
        embed.add_field(name=f"When are games ran?", value="Wednesday evenings.", inline=False)
        embed.add_field(name=f"When are polls due?", value="Saturday at 11:59PM.", inline=False)
        embed.add_field(name=f"When stream?", value="Don't know.", inline=False)
        embed.add_field(name=f"When croots?", value="Don't know.", inline=False)
        embed.add_field(name=f"When juco?", value="You'd rather have the transfer portal.", inline=False)
        embed.add_field(name=f"When transfer?", value="Don't know.", inline=False)
        embed.add_field(name=f"When Guam?", value="Depends on when the B1G wants to increase their footprint even further across the pacific.", inline=False)
        embed.add_field(name=f"When will can I get jerseys for my favorite SimCFB player?", value="Visit your college bookstore for custom jerseys.", inline=False)
        embed.add_field(name=f"When college hockey?", value="Anyone here is welcome to begin development.", inline=False)
        embed.add_field(name=f"When college baseball?", value="See college hockey.", inline=False)
        embed.add_field(name=f"When volleyball?", value="See college hockey.", inline=False)
        embed.add_field(name=f"When World Cup?", value="Probably in a couple of seasons for basketball.", inline=False)
        embed.add_field(name=f"When boat game?", value="O_o", inline=False)

        await interaction.response.send_message(embed=embed)

async def setup(client: commands.Bot):
    await client.add_cog(when(client))