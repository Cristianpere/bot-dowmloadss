from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/byicewolf")],
        [InlineKeyboardButton(
            "Reporta cualquier cosa a mi owner 🤑", url="https://t.me/retiradoice")]
    ])
    welcomed = f"Hola pa <b>{message.from_user.first_name}</b>\n/help para más información"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
