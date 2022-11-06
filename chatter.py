from contextvars import Token
import discord
import os
from neuralintents import GenericAssistant
import nltk
# nltk.download('omw-1.4')


Token='Keep your Token Here!'
# client = discord.Client()
client = discord.Client(intents=discord.Intents.default())

chatbot=GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()
print("The Bot is running super FAST & is Online!")

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author==client.user:
        return
    

    if message.content.startswith('IARE'):
        await message.channel.send("IARE is an engineering college located in Dundigal,Hyderabad,500043")

    if message.content.startswith('placements'):
        await message.channel.send("https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/notification/2022-23/Deltax.pdf")

    if message.content.startswith('academic calender'):
        await message.channel.send("https://www.iare.ac.in/sites/default/files/AcademicCalendar2021/B.TECH_I_AND_II_SEMESTERS_ACADEMIC_CALENDAR_2021-2022_REVISED.pdf")

    if message.content.startswith('programs'):
        await message.channel.send('B.TECH \n M.TECH \n MBA')
    if message.content.startswith('feedback'):
        await message.channel.send('Write your feedback-https://forms.gle/SUnTbpveWrMQvsEVA')

    if message.content.startswith('bulletin board'):
        await message.channel.send("https://samvidha.iare.ac.in/index#bulletin")

    if message.content.startswith('help'):
        await message.channel.send("This bot support various queries.use '/' before the query and try.")    

    if message.content.startswith('/'):
        response= chatbot.request(message.content[0:])
        await message.channel.send(response)

client.run(Token)
