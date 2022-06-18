import os
os.system("pip3 install amino.fix")
import aminofix
from random import choice
from keep_alive import keep_alive
clint=aminofix.Client()
x=open("sp.txt").read()
p = x.split(  '\n'  )
#________
link = "http://aminoapps.com/p/t7z8hz"
s = "AnsiMSI6IG51bGwsICIwIjogMiwgIjMiOiAwLCAiMiI6ICIzYjlhMzc5Mi02YjAxLTRmMjktOTU4NC0yNWRlYzAxYTgxMTUiLCAiNSI6IDE2NTU1OTE4MjQsICI0IjogIjQ2LjI0OC4yMDYuMTE5IiwgIjYiOiAxMDB9SpWaRUEOkTfwnSY8YAnHuGvISBk"
#________
keep_alive()
clint.login_sid(s)
print("login")
o=clint.get_from_code(link)
j=o.objectId
com=o.path[1:o.path.index(  '/' )]
clint.join_community(com)
subclint=aminofix.SubClient(comId=com,profile=clint.profile)
subclint.join_chat(j)
subclint.send_message(chatId=j,message='👀')
@clint.event('on_group_member_join')
def on_group_member_join(data: aminofix.objects.Event):
	author = data.message.author.nickname
	ttf = data.message.createdTime
	msg = f"""
 [BC]{author} منور/ة 

[BC] نرجو منك قرائة القوانين لتجنب المشاكل

[C]http://aminoapps.com/p/vyphmwf
"""
	subclint.send_message(chatId=j,message=msg)


@clint.event('on_group_member_leave')
def on_group_member_leave(data: aminofix.objects.Event):
 author = data.message.author.nickname
 msgG = f"""[BC] {author} الله معك 
[BC] اتمنى لك وقتاً ممتعاً """
 
 subclint.send_message(chatId=j, message=msgG)
@clint.event('on_text_message')
def on_text_message(data: aminofix.objects.Event):
    mention = data.message.mentionUserIds
    content = data.message.content
    msgId = data.message.messageId
    chatId = data.message.chatId
    author = data.message.author
    nm = data.message.author.nickname
    ttf = data.message.createdTime
    print(content)
    
    if content=="بوت":
    	hh = """[BC] انا بوت مساعده القروبات
[C] حالياً انا تحت التطوير 

[C] اكتب   [ حظ ] لكي تعرف كم انت محظوظ
[C] اكتب  [ اسمي ] لكي اكتب لك اسمك

[C] و انا لدي نظام خاص احذف الرسائل الغير اخلاقيه (تحت الطوير)"""
    	subclint.send_message(chatId=j,message=hh)

    if content=="عون":
    	hh = """ كلخرا لا تدوخني"""   
    	subclint.send_message(chatId=j,message=hh)
    if content=="حظ":
    	from random import choice
    	g=choice('0123456789')
    	
    	uiu = f"""من بين 1 الي 10
    	حصلت على -[ {g} ]-"""
    	subclint.send_message(chatId=j,message=uiu)

    if content=="اسمي":
    	subclint.send_message(chatId=j,message=nm)
    if content in p:
    	gt = f"عيب لا تسب {nm}"
    	subclint.delete_message(chatId=j,messageId=msgId)
    	subclint.send_message(chatId=j,message=gt)