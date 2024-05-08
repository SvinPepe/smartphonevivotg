import pyrogram
from pyrogram import Client, filters

print(pyrogram.__version__)
app = Client("client", 1, "0")
vivo = True


@app.on_message(filters.me)
def smatrphonevivo(client, msg):

    if vivo:
        msg.edit_text(f"{msg.text}\nСмартфон vivo")


@app.on_message(filters.me & filters.command("stop", prefixes='/'))
def stopvivo(client, msg):
    global vivo
    vivo = False


@app.on_message(filters.me & filters.command("start", prefixes='/'))
def startvivo(client, msg):
    global vivo
    vivo = True


app.run()
