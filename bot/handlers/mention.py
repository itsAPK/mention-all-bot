from ..utils import is_group_register
from ..models import session,Group,Message

async def admin_tag(bot,message):
    try:
        #session.query(Group).session.query(Group).filter(Group.group==message.chat.username).one()
        admin=bot.iter_participants(message.chat.username,filter='administrators')
        v=""
        async for u in admin:
            if u.user.is_bot ==False  :
                v+=u.user.mention()+','
        m=await bot.send_message(message.chat.id,v,reply_to_message_id =message.message_id)
        session.add(Message(group=message.chat.username,message_id=m.message_id))
        session.commit()
    except Exception:
        await bot.send_message(message.chat.id,"Your Group have no permission to use my commands please contact my owner @ronaldo_william")
        