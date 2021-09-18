from helper.database import getid
ADMIN = int(os.environ.get("ADMIN", 1745047302))

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("Checking All Users From Database")
   ids = getid()
   tot = len(ids)
   await ms.edit(f"Starting Broadcast 😃 \n\n Sending Message To {tot} Users")
   for id in ids:
     try:
     	await message.reply_to_message.copy(id)
     except:
     	pass
