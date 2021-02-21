from io import BytesIO # Importing required libraries.
import PIL
import discord
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import requests
from discord.ext import commands
import numpy as np

class Covid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def covid(self, ctx, *args):

        global population, country
        global flag
        response = requests.get("https://corona.lmao.ninja/v2/countries")
        data = response.json()

        try:
            for i in range(0, len(data) - 1): # For every country in that data
                if args[0].capitalize() in data[i].get('country'): # If requested country is there

                    country = data[i].get('country') # Get info
                    population = data[i].get('population')
                    flag = data[i].get('countryInfo').get('flag')
                    totalCases = data[i].get('cases')
                    todayCases = data[i].get('todayCases')
                    deaths = data[i].get('deaths')
                    deathsToday = data[i].get('todayDeaths')
                    recovered = data[i].get('recovered')
                    recoveredToday = data[i].get('todayRecovered')

        except Exception as e: # If there's no such country return with a response.

            embed = discord.Embed(color = 0xD63535, description = "> Please mention a valid country! ⚠️")
            return await ctx.send(embed = embed)

        df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv',
                         parse_dates=['Date'])

        countries = [f'{args[0].capitalize()}']

        df = df[df['Country'].isin(countries)]
        df['Cases'] = df[['Confirmed', 'Recovered']].sum(axis=1)
        df = df.pivot(index='Date', columns='Country', values='Cases')
        countries = list(df.columns)
        if countries == []:
            embed = discord.Embed(color = 0xD63535, description = "> Please mention a valid country! ⚠️")
            return await ctx.send(embed = embed)

        covid = df.reset_index('Date')
        covid.set_index(['Date'], inplace=True)
        covid.columns = countries

        percapita = covid.copy()

        for country in list(percapita.columns):
            percapita[country] = percapita[country] / population * 100000
            
        colors = {f'{args[0].capitalize()}': '#d64036'}
        plt.rcParams['axes.labelcolor'] = 'white'
        plt.rcParams['xtick.color'] = 'white'
        plt.rcParams['ytick.color'] = 'white'

        plot = covid.plot(figsize=(10, 4), color=list(colors.values()), linewidth=4, legend=False, alpha=.95)
        plot.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
        plot.set_rasterized(True)

        plot.set_xlabel('Data', alpha=.95)
        plot.set_ylabel('# number of cases', alpha=.95)

        plt.legend(['Cases'])
        plt.savefig('covid.png', transparent = True, dpi = 1000)

        canvas = plt.get_current_fig_manager().canvas
        canvas.draw()

        pil_image = PIL.Image.frombytes('RGB', canvas.get_width_height(), canvas.tostring_rgb()).convert("RGBA")
        buffer = BytesIO()
        pil_image.save(buffer, format="PNG")
        buffer.seek(0)

        embed = discord.Embed(color=0xD63535) # Creating the embed with the data.
        embed.set_author(name=f'Graph SARS-Cov2 -> {args[0].capitalize()}', icon_url=flag)
        embed.add_field(name='🧪 Total cases:', value=f'{totalCases} [**`+{todayCases}`** today]')
        embed.add_field(name='☠ Total deaths:', value=f'{deaths} [**`+{deathsToday}`** today]')
        embed.add_field(name='🩹 Healed:', value=f'{recovered} [**`+{recoveredToday}`** today]')

        embed.set_image(
            url="attachment://covid.png" #
        )

        image = discord.File('./covid.png', filename="covid.png") # Graph
        await ctx.send( # Sending the embed with the graph.
            embed=embed,
            file=image
        )

def setup(bot):
    bot.add_cog(Covid(bot))
