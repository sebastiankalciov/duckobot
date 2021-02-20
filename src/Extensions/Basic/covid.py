from io import BytesIO

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
        global populatie, tara
        global steag
        response = requests.get("https://corona.lmao.ninja/v2/countries")
        data = response.json()
        for i in range(0, len(data) - 1):
            if args[0].capitalize() in data[i].get('country'):
                tara = data[i].get('country')
                populatie = data[i].get('population')
                steag = data[i].get('countryInfo').get('flag')
                cazuriTotale = data[i].get('cases')
                cazuriToday = data[i].get('todayCases')
                deaths = data[i].get('deaths')
                deathsToday = data[i].get('todayDeaths')
                recovered = data[i].get('recovered')
                recoveredToday = data[i].get('todayRecovered')
                #tests = data[i].get('tests')


        df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv',
                         parse_dates=['Date'])
        countries = [f'{args[0].capitalize()}']
        df = df[df['Country'].isin(countries)]
        # Section 3 - Creating a Summary Column
        df['Cases'] = df[['Confirmed', 'Recovered']].sum(axis=1)
        df = df.pivot(index='Date', columns='Country', values='Cases')
        countries = list(df.columns)
        covid = df.reset_index('Date')
        covid.set_index(['Date'], inplace=True)
        covid.columns = countries
        # Section 5 - Calculating Rates per 100,000
        populations = {f'{args[0].capitalize()}': populatie}
        percapita = covid.copy()
        for country in list(percapita.columns):
            percapita[country] = percapita[country] / populations[country] * 100000
        colors = {f'{args[0].capitalize()}': '#d64036'}
        plt.rcParams['axes.labelcolor'] = 'white'
        plt.rcParams['xtick.color'] = 'white'
        plt.rcParams['ytick.color'] = 'white'
        # Section 7 - Creating the Visualization
        plot = covid.plot(figsize=(10, 4), color=list(colors.values()), linewidth=4, legend=False, alpha=.95) #figsize=(14, 8), color=list(colors.values()), linewidth=3, legend=False
        plot.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
        plot.set_rasterized(True)
        #plot.grid(color='#000000') #2f3136 #
        plot.set_xlabel('Data', alpha=.95)
        plot.set_ylabel('# numarul cazurilor', alpha=.95)
        #plot.set_title(f'{args[0].capitalize()}')
        plt.legend(['Cazuri'])
        plt.savefig('covid.png', transparent = True, dpi = 1000)
        canvas = plt.get_current_fig_manager().canvas
        canvas.draw()
        # aici se schimba din matplotlib in PIL
        pil_image = PIL.Image.frombytes('RGB', canvas.get_width_height(), canvas.tostring_rgb()).convert("RGBA")
        buffer = BytesIO()
        pil_image.save(buffer, format="PNG")
        buffer.seek(0)

        embed = discord.Embed(color=0x333438) # 0xe64141
        embed.set_author(name=f'Grafic SARS-Cov2 -> {args[0].capitalize()}', icon_url=steag)
        embed.add_field(name='🧪 Cazuri totale:', value=f'**{cazuriTotale}** [**`+{cazuriToday}`** astazi]')
        embed.add_field(name='☠ Decese:', value=f'**{deaths}** [**`+{deathsToday}`** astazi]')
        embed.add_field(name='🩹 Vindecati:', value=f'**{recovered}** [**`+{recoveredToday}`** astazi]')
        embed.set_image(
            url="attachment://covid.png" #
        )

        image = discord.File('./covid.png', filename="covid.png") #buffer
        await ctx.send(
            embed=embed,
            file=image
        )

def setup(bot):
    bot.add_cog(Covid(bot))
