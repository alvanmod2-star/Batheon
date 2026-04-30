import os
from pyrogram import Client, filters
from pyrogram.types import Message
import time

# أخذ المعلومات من منصة Render
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
SESSION = os.environ.get("SESSION")

if not all([API_ID, API_HASH, SESSION]):
    print("نقص بالمعلومات! تأكد من إضافة API_ID و API_HASH و SESSION في Render.")
    exit()

# تشغيل الحساب
app = Client(
    "MyBotSession",
    session_string=SESSION,
    api_id=int(API_ID),
    api_hash=API_HASH
)

# 1. أمر الفحص (.بينج)
@app.on_message(filters.command("بينج", prefixes=".") & filters.me)
async def ping_command(client: Client, message: Message):
    start_time = time.time()
    await message.edit_text("انتظر...")
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000)
    await message.edit_text(f"**بينج السورس:** `{ping_time} ms` ⚡️\n**السورس شغال حجي!** ✅")

# 2. أمر معرفة الايدي (.ايدي)
@app.on_message(filters.command("ايدي", prefixes=".") & filters.me)
async def id_command(client: Client, message: Message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        await message.edit_text(f"**ايدي الشخص:** `{user_id}`")
    else:
        await message.edit_text(f"**ايدي الشات:** `{message.chat.id}`")

# 3. أمر الرد السريع (.هلا)
@app.on_message(filters.command("هلا", prefixes=".") & filters.me)
async def hello_command(client: Client, message: Message):
    await message.edit_text("**هلا بيك حبيبي، السورس الخاص بيك جاهز وبخدمتك!** 🫡")

print("السورس اشتغل بنجاح! روح للتليجرام واكتب .بينج")
app.run()

