from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"**🌹ഹായ്🌹  ഞാനൊരു youtube വീഡിയോ And audio ഡൗൺലോഡർ Bot ആണ് എനിക്കൊരു വീഡിയോയുടെ URL സെന്റ് ചെയ്താൽ ഓഡിയോ വേണോ അതോ വീഡിയോ ആണോ വേണ്ടത് ഓപ്ഷൻ വരും അതിലൊന്ന് തിരഞ്ഞെടുത്താൽ നിങ്ങൾ അയച്ച വീഡിയോ അല്ലെങ്കിൽ ഓഡിയോ ഡൗൺലോഡ് ചെയ്യാവുന്നതാണ്🔥🔥🔥എന്തായാലും ഇവിടെവരെ വന്നതല്ലേ എന്റെ സപ്പോർട്ട് ഗ്രൂപ്പിലും കൂടി ജോയിൻ ചെയ്യാവോ = @AD_BOTZ 🥺** [😌](https://telegra.ph/file/41912bdd880a331c4d8bc.jpg),\n\n"
    await message.reply_text(helptxt)

