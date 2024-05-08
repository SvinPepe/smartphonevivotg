import pyrogram
from pyrogram import Client, filters

with open("config.txt", "r") as f:
    api_id = f.readline()
    api_hash = f.readline()
    app = Client("client", int(api_id), api_hash)

vivo = True


@app.on_message(filters.command("vivo"))
def vivo(client, message):
    global vivo
    vivo = not vivo


@app.on_message(filters.me)
def smatrphonevivo(client, msg):
    if vivo:
        if msg.text is not None:
            msg.edit_text(f"{msg.text}\nСмартфон vivo")
        else:
            msg.edit_text("Смартфон vivo")


app.run()
