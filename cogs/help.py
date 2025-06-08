import discord
from discord.ext import commands
from discord import app_commands
import settings

class help(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        client.tree.add_command(self.help_group, guild=settings.GUILDS_ID)

    help_group = app_commands.Group(name="league_help", description="Helpful info by league")


    @help_group.command(name="cfb", description="SimCFB introduction and help")
    async def cfb(self, interaction: discord.Interaction):
        embed = discord.Embed(colour=discord.Colour.dark_gold(),
                            description="The CFB can be daunting to jump into, so here are a few useful links for CFB to get you started. We encourage you to explore the dev diary subforum [here](https://www.simfba.com/forum/18-dev-diary/) for detailed explanations in all aspects of the sim and interface. Feel free to also ask for help in the https://discord.com/channels/586207409681334522/612270150137282560 or in https://discord.com/channels/586207409681334522/850218461480615936.",
                            title="Welcome to the SimCFB brought to you by SimFBA") 
        embed.add_field(name="Gameplanning", value="https://www.simfba.com/topic/6167-116-simcfb-simnfl-the-new-gameplan-page", inline=False)
        embed.add_field(name="Recruiting", value="https://www.simfba.com/topic/3107-57-interface-update-recruiting", inline=False)
        embed.add_field(name="Transfers", value="https://www.simfba.com/topic/6216-117-simfba-simbba-transfer-portal-pt-1-high-level-overview", inline=False)
        embed.add_field(name="", value="*Note: Some values and interface layouts may have been updated since these are older dev diaries, but the concepts should mostly stay the same.*", inline=False)
        embed.add_field(name="For a more in-depth explanation on how to participate in the SimCFB and SimNFL, please refer to this great guide created by Piercewise1:", value="https://docs.google.com/document/d/1Q8aRPUIooEIjIPLmTeXOOF6CnGPnxk3t8ThmNemyQ7M/edit", inline=False)
        embed.add_field(name="For a more in-depth guide on gameplanning in SimCFB and SimNFL, please refer to this great guide created by Sarge", value="https://www.simfba.com/topic/7425-cfbnfl-sarges-guide-to-gameplanning-the-seconding", inline=False)
 
        await interaction.response.send_message(embed=embed)

    @help_group.command(name="cbb", description="SimCBB introduction and help")
    async def cbb(self, interaction: discord.Interaction):
        embed = discord.Embed(colour=discord.Colour.dark_gold(),
                            description="The CBB can be daunting to jump into, so here are a few useful links for CBB to get you started. We encourage you to explore the dev diary subforum [here](https://www.simfba.com/forum/18-dev-diary/) for detailed explanations in all aspects of the sim and interface. Feel free to also ask for help in the https://discord.com/channels/586207409681334522/1026933570826158231 or in https://discord.com/channels/586207409681334522/850218461480615936.",
                            title="Welcome to the SimCBB brought to you by SimFBA") 
        embed.add_field(name="Gameplanning", value="https://www.simfba.com/topic/4886-94-simcbb-gameplan-update", inline=False)
        embed.add_field(name="Recruiting", value="https://www.simfba.com/topic/3794-72-simbba-interface-recruiting", inline=False)
        embed.add_field(name="Transfers", value="https://www.simfba.com/topic/6216-117-simfba-simbba-transfer-portal-pt-1-high-level-overview", inline=False)
        embed.add_field(name="", value="*Note: Some values and interface layouts may have been updated since these are older dev diaries, but the concepts should mostly stay the same.*", inline=False)
        
        await interaction.response.send_message(embed=embed)

    @help_group.command(name="nfl", description="SimNFL introduction and help")
    async def nfl(self, interaction: discord.Interaction):
        embed = discord.Embed(colour=discord.Colour.dark_gold(),
                            description="The SimNFL can be daunting to jump into, so here are a few useful links for NFL to get you started. We encourage you to explore the dev diary subforum [here](https://www.simfba.com/forum/18-dev-diary/) for detailed explanations in all aspects of the sim and interface. Feel free to also ask for help in the https://discord.com/channels/586207409681334522/914917788206891048 or in https://discord.com/channels/586207409681334522/850218461480615936.",
                            title="Welcome to the SimNFL brought to you by SimFBA")
        embed.add_field(name="Gameplanning", value="https://www.simfba.com/topic/6167-116-simcfb-simnfl-the-new-gameplan-page", inline=False)
        embed.add_field(name="Free Agency", value="https://www.simfba.com/topic/7521-129-simfba-simbba-offseason-free-agency-update", inline=False)
        embed.add_field(name="Drafting", value="https://www.simfba.com/topic/6144-113-simfba-the-draft-page", inline=False)
        embed.add_field(name="", value="*Note: Some values and interface layouts may have been updated since these are older dev diaries, but the concepts should mostly stay the same.*", inline=False)
        embed.add_field(name="For a more in-depth explanation on how to participate in the SimCFB and SimNFL, please refer to this great guide created by Piercewise1:", value="https://docs.google.com/document/d/1Q8aRPUIooEIjIPLmTeXOOF6CnGPnxk3t8ThmNemyQ7M/edit", inline=False)
        embed.add_field(name="For a more in-depth guide on gameplanning in SimCFB and SimNFL, please refer to this great guide created by Sarge", value="https://www.simfba.com/topic/7425-cfbnfl-sarges-guide-to-gameplanning-the-seconding", inline=False)

        await interaction.response.send_message(embed=embed)

    @help_group.command(name="nba", description="SimNBA introduction and help")
    async def nba(self, interaction: discord.Interaction):
        embed = discord.Embed(colour=discord.Colour.dark_gold(),
                            description="The NBA can be daunting to jump into, so here are a few useful links for NBA to get you started. We encourage you to explore the dev diary subforum [here](https://www.simfba.com/forum/18-dev-diary/) for detailed explanations in all aspects of the sim and interface. Feel free to also ask for help in the https://discord.com/channels/586207409681334522/1026933591919317133 or in https://discord.com/channels/586207409681334522/850218461480615936.",
                            title="Welcome to the SimNBA brought to you by SimFBA") 
        embed.add_field(name="Gameplanning", value="https://www.simfba.com/topic/4886-94-simcbb-gameplan-update", inline=False)
        embed.add_field(name="Free Agency", value="https://www.simfba.com/topic/7521-129-simfba-simbba-offseason-free-agency-update", inline=False)
        embed.add_field(name="Drafting", value="https://www.simfba.com/topic/5441-100-the-simnba-draft-page", inline=False)
        embed.add_field(name="", value="*Note: Some values and interface layouts may have been updated since these are older dev diaries, but the concepts should mostly stay the same.*", inline=False)
        
        await interaction.response.send_message(embed=embed)

async def setup(client: commands.Bot):
    await client.add_cog(help(client))
