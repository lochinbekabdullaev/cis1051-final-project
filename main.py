import nextcord
from nextcord.ext import commands
import aiohttp
import random

bot = commands.Bot(command_prefix="!", intents=nextcord.Intents.all())


@bot.event
async def on_ready():
    print("Bot has connected to Discord")


@bot.event
async def on_message(message):
    quite_phrases = ["shareef no one asked", ":shushing_face:"]
    rand_quite_phrases = random.choice(quite_phrases)
    ignored_commands = ["!dice", "!weather"]

    if message.author == bot.user:
        return

    if any(message.content.startswith(command) for command in ignored_commands):
        await bot.process_commands(message)
        return

    if message.author.id == {INSERT USER'S DISCORD ID} and random.random() < 0.2:
        await message.channel.send(rand_quite_phrases)


@bot.command()
async def dice(ctx: commands.Context):
    rolled_dice = random.randint(1, 6)
    await ctx.send(f":game_die: {rolled_dice}")


@bot.command()
async def weather(ctx: commands.Context, *, city):
    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": '238f06413f374673b2715416241012',
        "q": city
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as res:
            data = await res.json()

            location = data["location"]["name"]
            temp_f = data["current"]["temp_f"]
            humidity = data["current"]["humidity"]
            wind_mph = data["current"]["wind_mph"]
            condition = data["current"]["condition"]["text"]
            image_url = "http:" + data["current"]["condition"]["icon"]

            embed = nextcord.Embed(title=f"Weather for {location}", description=f"The condition in `{location}` is ` "
                                                                                f"{condition}`")
            embed.add_field(name="Temperature", value=f"F: {temp_f}")
            embed.add_field(name="Humidity", value=f"{humidity}")
            embed.add_field(name="Wind Speeds", value=f"MPH: {wind_mph}")
            embed.set_thumbnail(url=image_url)

            await ctx.send(embed=embed)


bot.run(TYPE DISCORD TOKEN HERE)
