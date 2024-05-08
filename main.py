import pyrogram
from pyrogram import Client, filters

print(pyrogram.__version__)
app = Client("client", 1, "0")


@app.on_message(filters.me)
def smatrphonevivo(client, msg):
    msg.edit_text(f"{msg.text}\nСмартфон vivo")


app.run()
