import discord
from discord.ext import tasks



class chatbot(discord.Client):
    @tasks.loop(seconds=1)
    async def every_hour_notice(self):
        fr = open('ttt.txt', 'r', encoding='UTF8')

        t = fr.readline()

        if (t != ""):
            await client.get_channel(809475704977752164).send(t)
            fr.close()
            with open('ttt.txt', 'w') as fw:
                fw.write("")
        else:
            fr.close()

    async def on_ready(self):

        print("READY")

        self.every_hour_notice.start()



if __name__ == "__main__":
    client = chatbot()
    client.run("ODEwMDA5NjQ3MzI2Mjk4MTMy.YCdaRQ.rLB2Qmq1SlmDmA9K2O6G032gp30")
