from ..markup import start_markup
from ..config import Config
from ..models import Group,Message,session
from ..utils import is_group_register


async def StartHandler(bot,message):
    data=f"Hello 👋  My Name is Mention Master and i am a bot, My owner is @ronaldo_william \n@all - to tag all members \n/set_all - Everyone Can use @all command \n/set_admin_only - Only admins can use @all command \n/delete_all - This option for delete all mentioned messages \n@admin - to tag admins only"
    if message.chat.id in Config.ADMIN_ID:
        await bot.send_message(message.chat.id,data,reply_markup=start_markup())
    else:
        await bot.send_message(message.chat.id,data)
        
        
async def set_all_handler(bot,message):
    """a=""
    m=bot.iter_chat_members(message.chat.username)
    async for i in m:
        a+=i.user.mention()+','
    await message.reply_text(a)

    #for i in admin:
        #await bot.reply_text(i.user.mention())"""
    if is_group_register(message.chat.username) is False:
        try:
            admins=[]
            admin=bot.iter_chat_members(message.chat.username,filter='administrators')
            async for u in admin:
                if u.status=='creator' or u.status=='administrators'and u.user.is_bot ==False  :
                    admins.append(u.user.id)
            if message.from_user.id in admins:
                session.query(Group).filter(Group.group==message.chat.username).update({Group.tag_all:True})
                session.commit()
                m= await bot.send_message(message.chat.id,"Sucessfully Set")
                session.add(Message(group=message.chat.username,message_id=m.message_id))
                session.commit()
            else:
                await message.reply(message.chat.id,"You're not Admin")  
                session.add(Message(group=message.chat.username,message_id=m.message_id))
                session.commit()      
        except Exception as e:
            print(e)
            await bot.send_message(message.chat.id,"Your Group have no permission to use my commands please contact my owner @ronaldo_william")

async def set_admin_only_handler(bot,message):
    if is_group_register(message.chat.username) is False:
        try:
            admins=[]
            admin=bot.iter_chat_members(message.chat.username,filter='administrators')
            async for u in admin:
                if u.status=='creator' or u.status=='administrators'and u.user.is_bot ==False  :
                    admins.append(u.user.id)
            if message.from_user.id in admins:
                session.query(Group).filter(Group.group==message.chat.username).update({Group.tag_all:False})
                session.commit()
                m=await bot.send_message(message.chat.id,"Sucessfully Set")
                print(m)
                session.add(Message(group=message.chat.username,message_id=m.message_id))
                session.commit()
            else:
                await message.reply(message.chat.id,"You're not Admin")  
                session.add(Message(group=message.chat.username,message_id=m.message_id))
                session.commit()      
        except Exception as e:
            print(e)
            await bot.send_message(message.chat.id,"Your Group have no permission to use my commands please contact my owner @ronaldo_william")

async def delete_message(bot,message):
    if is_group_register(message.chat.username) is False:
        try:
            admin=bot.iter_chat_members(message.chat.username,filter='administrators')
            admins=[]
            async for u in admin:
                if u.status=='creator' or u.status=='administrators'and u.user.is_bot ==False  :
                    admins.append(u.user.id)
            if message.from_user.id in admins:
                z=session.query(Message).filter(Message.group==message.chat.username).all()
                for i in z:
                    await bot.delete_messages(message.chat.id,i.message_id)
                    session.query(Message).filter(Message.group==message.chat.username,Message.message_id==i.message_id).delete()
                    session.commit()
                await message.reply("Sucessfully deleted..")
            else:

                    m=await bot.send_message(message.chat.id,"You're not Admin")
                    session.add(Message(group=message.chat.username,message_id=m.id))
                    session.commit()
        except Exception as e:
            print(e)
            await bot.send_message(message.chat.id,"Your Group have no permission to use my commands please contact my owner @ronaldo_william")
