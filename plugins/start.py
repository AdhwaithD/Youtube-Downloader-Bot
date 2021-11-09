from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("♻️ Updates ♻️", url="https://t.me/AD_BOTZ12")],
        [InlineKeyboardButton(
            "🌟 Report Bugs 🌟", url="https://t.me/Lucifer_Devil_AD")]
    ])
    welcomed = f"**🌹 ഹായ് 🌹 <b>{message.from_user.first_name}</b>\n/help കൂടുതൽ വിവരങ്ങൾക്ക്** [🔥](https://telegra.ph/file/ec3d6c6edd45e02c3c125.jpg\n\n)",
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
