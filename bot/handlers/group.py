from ..models import Group,session
from ..config import Config

async def add_group(bot,message):
    if message.chat.id in Config.ADMIN_ID:
        msg=await bot.ask(message.chat.id,"Send bot username")
        session.add(Group(group=msg.text.replace('@','')))
        session.commit()
        print(msg.text.replace('@',''))
        await bot.send_message(message.chat.id,"Group added Sucessfully")
        
async def remove_group(bot,message):
    if message.chat.id in Config.ADMIN_ID:
        msg=await bot.ask(message.chat.id,"Send bot username")
        session.query(Group).filter(Group.group==msg.message.replace('@','')).delete()
        session.commit()
        print(msg.text.replace('@',''))
        await bot.send_message(message.chat.id,"Group removed Sucessfully")