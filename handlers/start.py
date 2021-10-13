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



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b><b>Hoş Geldiniz {message.from_user.first_name}!</b>

<b>🎙️ Ezel Music Bot </b> Yeni Yöntemlerle</b> Olabildiğince Basit, Gruplarınızda Müzik <b>Oynatmak,</b> İçin Tasarlanmış Bir <b>Botum</b>.

<b>❓ Nasıl Kullanılır? </b>
Boun Komutlarının Tam Listesini Görmek İçin! » 🎛 <b>Komutlar</b> Düğmesine Veya /Help Düğmesine Basın <b>EzelMusicBot!</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ Beni Grubunuza Ekleyin ➕", url="t.me/ezelmusicbot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "🎛️ Komutlar", url="/play (Şarkı İsmi)"
                    ),
                    InlineKeyboardButton(
                        "👤 Sahibim ", url="https://t.me/theezelboss")
                    ],[
                    InlineKeyboardButton(
                        "📢 Kanalımız ", url="https://t.me/ezelizm"
                    ),
                    InlineKeyboardButton(
                        "👥 Support ", url="https://t.me/EzelAssistant"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🎼 Assistanım", url="https://t.me/EzelAssistant"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ <b>Bir YouTube Videosu Mu Aramak İstiyorsunuz? </b>",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👥 Support", url="https://t.me/ezelhome"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Evet", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ Hayır", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b><u>Komutlar!</u>
\n/play <song name> - İstediğiniz Şarkıyı Çalın
/dplay <song name> - Deezer Aracılığıyla İstediğiniz Şarkıyı Çalın
/splay <song name> - Jio Saavn Aracılığıyla İstediğiniz Şarkıyı Çalın
/playlist - Şimdi Çalma Listesini Göster
/current - Şimdi Çalan Göster
/song <song name> - İstediğiniz Şarkıları Hızlı Bir Şekilde İndirin
/search <query> - Youtube'daki Videoları Ayrıntılarla Arayın
/deezer <song name> - İstediğiniz Şarkıları Deezer İle Hızlıca İndirin
/saavn <song name> - İstediğiniz Şarkıları Jio Saavn Aracılığıyla Hızlıca İndirin
/video <song name> - İstediğiniz Videoları Hızlı Bir Şekilde İndirin
\n<u>Yalnızca Yöneticiler</u>
/player - Müzik Çalar Ayarları Panelini Aç
/pause - Şarkı Çalmayı Duraklatır
/resume - Şarkıyı Çalmaya Devam Et
/skip - Sonraki Şarkıyı Çal
/end - Müzik Çalmayı Durdur
/userbotjoin - Asistanı Sohbetinize Davet Edin
/admincache - Yönetici Listesini Yeniler
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👤 Sahibim", url="https://t.me/theezelboss"
                    )
                ]
            ]
        )
    )    
