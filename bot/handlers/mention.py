from ..utils import is_group_register
from ..models import session,Group,Message
import time
import textwrap
from itertools import zip_longest  as izip
from telebot.util import split_string

#from telethon.errors.rpcerrorlist import MessageTooLongError

async def admin_tag(bot,message):
    if is_group_register(message.chat.username) is True:
        try:
            #session.query(Group).session.query(Group).filter(Group.group==message.chat.username).one()
            admin=bot.iter_chat_members(message.chat.username,filter='administrators')
            v=""
            async for u in admin:
                if u.user.is_bot ==False  :
                    v+=u.user.mention()+','
            m=await bot.send_message(message.chat.id,v,reply_to_message_id =message.message_id)
            session.add(Message(group=message.chat.username,message_id=m.message_id))
            session.commit()
        except Exception as e:
            print(e)
            await bot.send_message(message.chat.id,"Your Group have no permission to use my commands please contact my owner @ronaldo_william")


async def all_tag(bot,message):
    if is_group_register(message.chat.username) is True:
        try:
            z=session.query(Group).filter(Group.group==message.chat.username).one()
            if z.tag_all==True:
                all_users=[]
                all_users=bot.iter_chat_members(message.chat.username)
                v=[]
                async for u in all_users:
                
                        if u.user.first_name is None:
                                pass
                        else:
                                v.append(u.user.mention()+"\t")
#todo : clean code
                a=chunck(v)
                for k in a:
                    f=""
                    for s in k:
                        f+=s
                    m=await bot.send_message(message.chat.id,f,reply_to_message_id=message.message_id,parse_mode='html')
                    session.add(Message(group=message.chat.username,message_id=m.message_id))
                    session.commit()
                    time.sleep(2)
            else:
                admins=[]
                admin=bot.iter_chat_members(message.chat.username,filter='administrators')
                async for u in admin:
                    if u.user.is_bot ==False  :
                        admins.append(u.user.id)
                if message.from_user.id in admins:
                    all_users=[]
                    all_users=bot.iter_chat_members(message.chat.username)
                    v=[]
                    async for u in all_users:
                        if u.user.is_bot ==False  :
                            if u.user.first_name==None:
                                pass
                            else:
                                v.append(u.user.mention()+", ")
                    print(len(v))
                    import re
                    q="".join(v)
                    #for x in re.finditer('.{,5}',q):
                    m=await bot.send_message(message.chat.id,v,reply_to_message_id=message.message_id,parse_mode='html')
                    session.add(Message(group=message.chat.username,message_id=m.message_id))
                    session.commit()
                    time.sleep(2)
                else:
                    await bot.delete_messages(message.chat.id,message.message_id)
        
        except Exception as e:
            print(e)
            await bot.send_message(message.chat.id,"Your Group have no permission to use my commands please contact my owner @ronaldo_william")
            
def chunck(s):
    l=[r for r in s]
    for i in range(0,len(l),5):
        yield l[i:i+5]
        
    