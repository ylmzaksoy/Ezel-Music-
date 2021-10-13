# ZauteMusic (Telegram bot project )
# Copyright (C) 2021  ZauteKm 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.




from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["userbotjoin"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Öncelikle Beni Grubun Yöneticisi Olarak Ekleyin.</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "@EzelMusicBot"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"Emrettiğiniz Gibi Buraya Geldim.")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Yardımcı Zaten Sohbetinizde</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Taşkın Hata bekleyin 🛑 \n Kullanıcı {user.first_name} Userbot İçin Katılma İsteklerini Nedeniyle Ağır Şekilde Gruba Katılmak Emin Kullanıcı Grubunda Yasaklı Olmadığından Emin Olun Sorun Olamazdı! "
            "\n\nVeya @EzelMusicBot'u Grubunuza manuel olarak ekleyin ve tekrar deneyin</b>",
        )
        return
    await message.reply_text(
            "<b>Asistan Botum Sohbetinize Katıldı.</b>",
        )
    
@USER.on_message(filters.group & filters.command(["userbotleave"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>Kullanıcı Grubunuzdan Ayrılamadı! Sel Beklemesi Olabilir."
            "\n\nVeya Beni Grubunuzdan Elle Atabilirsiniz</b>",
        )
        return
