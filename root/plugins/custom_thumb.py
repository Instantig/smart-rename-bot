'''
RenameBot
Thanks to Spechide Unkle as always fot the concept  ♥️
This file is a part of mrvishal2k2 rename repo 
Dont kang !!!
© Mrvishal2k2
'''

import  os, logging
from pyrogram import Client,filters
from root.config import Config
from root.utils import *


log = logging.getLogger(__name__)

@Client.on_message(filters.photo)
async def save_photo(c,m):
    v = await m.reply_text("**Sᴀᴠɪɴɢ Tʜᴜᴍʙɴᴀɪʟ ᴍᴇʀɪ ɪᴀᴀɴ** 💋",True)
    if m.media_group_id is not None:
        download_location = Config.DOWNLOAD_LOCATION + "/thumb/" + str(m.from_user.id) + "/" + str(m.media_group_id) + "/"
        os.makedirs(download_location, exist_ok=True)
        await df_thumb(m.from_user.id, m.id)
        await c.download_media(
            message=m,
            file_name=download_location
        )
    else:
        download_location = Config.DOWNLOAD_LOCATION + "/thumb/" + str(m.from_user.id) + ".jpg"
        await df_thumb(m.from_user.id, m.id)
        await c.download_media(
            message=m,
            file_name=download_location
        ) 
        try:
           await v.edit_text("**🧞‍♀ Tʜᴜᴍʙɴᴀɪʟ Sᴀᴠᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ ✔**")
        except Exception as e:
          log.error(f"#Error {e}")

@Client.on_message(filters.command(["deletethumb"]))
async def delete_thumbnail(c,m):
    download_location = Config.DOWNLOAD_LOCATION + "/thumb/" + str(m.from_user.id)
    try:
        os.remove(download_location + ".jpg")
        await del_thumb(m.from_user.id)
    except Exception as e:
        log.error(f"Error in removing thumb {e}")
        pass
    await m.reply_text("💔 **Tʜᴜᴍʙɴᴀɪʟ ʀᴇᴍᴏᴠᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ 😒**",quote=True)

@Client.on_message(filters.command(["showthumb"]))
async def show_thumbnail(c,m):
    thumb_image_path = Config.DOWNLOAD_LOCATION + "/thumb/" + str(m.from_user.id) + ".jpg"
    msgg = await m.reply_text("👀 **Cʜᴇᴄᴋɪɴɢ Tʜᴜᴍʙɴᴀɪʟ**...⌛",quote=True)

    if not os.path.exists(thumb_image_path):
        mes = await thumb(m.from_user.id)
        if mes is not None:
            msgg = await c.get_messages(m.chat.id, mes.msg_id)
            await msgg.download(file_name=thumb_image_path)
            thumb_image_path = thumb_image_path
        else:
            thumb_image_path = None

    if thumb_image_path is None:
        try:
            await msgg.edit_text("👻 **Nᴏ Tʜᴜᴍʙɴᴀɪʟ Fᴏᴜɴᴅ**!!")
        except:
              pass               
    else:
        try:
           await msgg.delete()

        except:
            pass

        await m.reply_photo(
        photo=thumb_image_path,
        caption="**Tʜɪs Yᴏᴜʀ Tʜᴜᴍʙɴᴀɪʟ sᴏʀ** 😎\n🗑 **Yᴏᴜ Cᴀɴ ᴅᴇʟᴇᴛᴇ ᴛʜɪs ʙʏ ᴜsɪɴɢ **\n/deletethumb **Command**",
        quote=True
    )

