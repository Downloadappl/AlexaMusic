import json
import random
from typing import List, Union
import time
from pyrogram import filters
import datetime
from AlexaMusic import app
from pyrogram import Client, filters


#######£££££££££££££££#######££££££££££#############££££££££££#########££££#
#######£££££££££££££££#######££££££££££#############££££££££££#########££££

SUDOERS = [5012406813]

OWNER_ID = 5012406813

def is_sudoer(_, __, message):

    return message.from_user.id in SUDOERS or message.from_user.id == OWNER_ID

def is_owner(_, __, message):

    return message.from_user.id == OWNER_ID


other_filters = filters.group &  ~filters.via_bot & ~filters.forwarded
other_filters2 = (
    filters.private &  ~filters.via_bot & ~filters.forwarded
)


def command(commands: Union[str, List[str]]):
    return filters.command(commands, "")


def load_bank_data():
    try:
        with open('bank_tom.json', 'r') as file:
            bank_data = json.load(file)
    except FileNotFoundError:
        bank_data = {}
    
    return bank_data


def save_bank_data(bank_data):
    with open('bank_tom.json', 'w') as file:
        json.dump(bank_data, file)


cooldown_time = 12 * 60 * 60  


def check_cooldown(user_id):
    cooldown_data = load_cooldown_data()
    current_time = int(time.time())
    if str(user_id) in cooldown_data:
        last_use_time = cooldown_data[str(user_id)]
        time_passed = current_time - last_use_time
        remaining_time = cooldown_time - time_passed

        if time_passed < cooldown_time:
            hours = remaining_time // 3600
            minutes = (remaining_time % 3600) // 60
            response = f"عذرًا، يجب الانتظار {hours} ساعة و {minutes} دقيقة قبل استخدام الكنز مرة أخرى"
            return False, response

    cooldown_data[str(user_id)] = current_time
    save_cooldown_data(cooldown_data)
    return True, None


def load_cooldown_data():
    try:
        with open('cooldown_data.json', 'r') as file:
            cooldown_data = json.load(file)
    except FileNotFoundError:
        cooldown_data = {}
    
    return cooldown_data


def save_cooldown_data(cooldown_data):
    with open('cooldown_data.json', 'w') as file:
        json.dump(cooldown_data, file)




def get_remaining_time(user_id):
    cooldown_data = load_cooldown_data()
    current_time = int(time.time())
    if str(user_id) in cooldown_data:
        last_use_time = cooldown_data[str(user_id)]
        remaining_time = 20 * 60 - (current_time - last_use_time)
        if remaining_time < 0:
            remaining_time = 0
        return remaining_time
    return 0



#######£££££££££££££££#######££££££££££#############££££££££££#########££££#
#######£££££££££££££££#######££££££££££#############££££££££££#########££££

LUCK_COOLDOWN = 1200  


last_luck_times = {}


def get_luck_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_luck_times:
        last_luck_time = last_luck_times[user_id]
        elapsed_time = current_time - last_luck_time
        remaining_time = LUCK_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time


def update_luck_time(user_id):
    last_luck_times[user_id] = int(time.time())
    

#######£££££££££££££££#######££££££££££#############££££££££££#########££££#
#######£££££££££££££££#######££££££££££#############££££££££££#########££££

TRANSFER_COOLDOWN = 1200  


last_transfer_times = {}

def get_transfer_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_transfer_times:
        last_transfer_time = last_transfer_times[user_id]
        elapsed_time = current_time - last_transfer_time
        remaining_time = TRANSFER_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time


def update_transfer_time(user_id):
    last_transfer_times[user_id] = int(time.time())



@app.on_message(command('تحويل'))
def transfer(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()

    if str(user_id) in bank_data['accounts']:
        remaining_time = get_transfer_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 2 and args[1].isdigit():
                amount = int(args[1])
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    client.send_message(message.chat.id, f'تم تحويل {amount} دولار بنجاح')
                    update_transfer_time(user_id)
                else:
                    client.send_message(message.chat.id, 'رصيدك الحالي غير كافي')
            else:
                client.send_message(message.chat.id, 'الرجاء استخدام الأمر بالشكل الصحيح: تحويل + المبلغ')
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            client.send_message(message.chat.id, f'عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى')
    else:
        client.send_message(message.chat.id, 'ليس لديك حساب بنكي')


#######£££££££££££££££#######££££££££££#############££££££££££#########££££#
#######£££££££££££££££#######££££££££££#############££££££££££#########££££



@app.on_message(command('استثمار'))
def invest(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()

    if str(user_id) in bank_data['accounts']:
        remaining_time = get_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 2 and args[1].isdigit():
                amount = int(args[1])
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    bank_data['accounts'][str(user_id)]['balance'] -= amount
                    save_bank_data(bank_data)
                    # قم بتنفيذ الاستثمار وحساب العائد المحتمل
                    return_amount = amount * random.randint(50, 100) / 100
                    bank_data['accounts'][str(user_id)]['balance'] += return_amount
                    save_bank_data(bank_data)
                    cooldown_data = load_cooldown_data()
                    cooldown_data[str(user_id)] = int(time.time())
                    save_cooldown_data(cooldown_data)
                    client.send_message(message.chat.id, f'تهانينا! لقد استثمرت {amount} دولار وحصلت على عائد بقيمة {return_amount} دولار')
                else:
                    client.send_message(message.chat.id, 'رصيدك الحالي غير كافي')
            else:
                client.send_message(message.chat.id, 'الرجاء استخدام الأمر بالشكل الصحيح: استثمار + المبلغ')
        else:
            remaining_minutes = int(remaining_time / 60)
            remaining_seconds = remaining_time % 60
            client.send_message(message.chat.id, f'عذرًا، يجب الانتظار {remaining_minutes} دقيقة و {remaining_seconds} ثانية بين كل عملية استثمار')
    else:
        client.send_message(message.chat.id, 'ليس لديك حساب بنكي')




#######£££££££££££££££#######££££££££££#############££££££££££#########££££#
#######£££££££££££££££#######££££££££££#############££££££££££#########££££




@app.on_message(command('حظ'))
def luck(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()

    if str(user_id) in bank_data['accounts']:
        remaining_time = get_luck_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 2 and args[1].isdigit():
                amount = int(args[1])
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    bank_data['accounts'][str(user_id)]['balance'] -= amount
                    save_bank_data(bank_data)
                    chance = random.randint(0, 1)
                    if chance == 1:
                        win_amount = amount * random.uniform(1, 3)
                        bank_data['accounts'][str(user_id)]['balance'] += win_amount
                        save_bank_data(bank_data)
                        client.send_message(message.chat.id, f'تهانينا! لقد ربحت {win_amount} دولار')
                    else:
                        client.send_message(message.chat.id, 'للأسف، لم تربح أي شيء')
                    update_luck_time(user_id)
                else:
                    client.send_message(message.chat.id, 'رصيدك الحالي غير كافي')
            else:
                client.send_message(message.chat.id, 'الرجاء استخدام الأمر بالشكل الصحيح: حظ + المبلغ')
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            client.send_message(message.chat.id, f'عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى')
    else:
        client.send_message(message.chat.id, 'ليس لديك حساب بنكي')

#######£££££££££££££££#######££££££££££#############££££££££££#########££££#
#######£££££££££££££££#######££££££££££#############££££££££££#########££££




@app.on_message(command("اضف") & filters.create(is_sudoer))
def add_money(client, message):
    reply_message = message.reply_to_message
    if reply_message is not None and reply_message.from_user is not None:
        user_id = reply_message.from_user.id
        args = message.text.split(" ")
        if len(args) == 2 and args[1].isdigit():
            amount = int(args[1])
            bank_data = load_bank_data()

            if 'accounts' not in bank_data:
                bank_data['accounts'] = {}

            if str(user_id) in bank_data['accounts']:
                bank_data['accounts'][str(user_id)]['balance'] += amount
            else:
                bank_data['accounts'][str(user_id)] = {'balance': amount}

            save_bank_data(bank_data)
            client.send_message(message.chat.id, f'تمت إضافة {amount} فلوس للمستخدم {user_id}')
        else:
            client.send_message(message.chat.id, 'الرجاء استخدام الأمر بالشكل الصحيح: اضف + المبلغ')
    else:
        client.send_message(message.chat.id, 'الرجاء الرد على شخص لإضافة الفلوس له')

#######£££££££££££££££#######££££££££££#############££££££££££#########££££#
#######£££££££££££££££#######££££££££££#############££££££££££#########££££




@app.on_message(command("حذف حسابه") & filters.create(is_sudoer))
def delete_account(client, message):
    reply_message = message.reply_to_message
    if reply_message is not None and reply_message.from_user is not None:
        user_id = reply_message.from_user.id
        bank_data = load_bank_data()

        if str(user_id) in bank_data['accounts']:
            del bank_data['accounts'][str(user_id)]
            save_bank_data(bank_data)
            client.send_message(message.chat.id, f'تم حذف حساب المستخدم {user_id}')
        else:
            client.send_message(message.chat.id, 'المستخدم المحدد لا يملك حساب بنكي')
    else:
        client.send_message(message.chat.id, 'الرجاء الرد على شخص لحذف حسابه')

#######£££££££££££££££#######££££££££££#############££££££££££#########££££#
#######£££££££££££££££#######££££££££££#############££££££££££#########££££



@app.on_message(command('حذف') & filters.create(is_sudoer))
def delete_specific_account(client, message):
    args = message.text.split(' ')
    if len(args) == 2 and args[1].isdigit():
        user_id = args[1]
        bank_data = load_bank_data()

        if str(user_id) in bank_data['accounts']:
            del bank_data['accounts'][str(user_id)]
            save_bank_data(bank_data)
            client.send_message(message.chat.id, f'تم حذف حساب المستخدم {user_id}')
        else:
            client.send_message(message.chat.id, 'المستخدم المحدد لا يملك حساب بنكي')
    else:
        client.send_message(message.chat.id, 'الرجاء استخدام الأمر بالشكل الصحيح: حذف_حساب + اليوزر')
#######£££££££££££££££#######££££££££££#############££££££££££#########££££#
#######£££££££££££££££#######££££££££££#############££££££££££#########££££



@app.on_message(command('تصفير البنك') & filters.create(is_sudoer))
def reset_bank(client, message):
    bank_data = {'accounts': {}}
    save_bank_data(bank_data)
    client.send_message(message.chat.id, 'تم مسح جميع حسابات البنك')
    
    
#######£££££££££££££££#######££££££££££#############££££££££££#########££££#
#######£££££££££££££££#######££££££££££#############££££££££££#########££££



@app.on_message(command('تفعبل البنك') & filters.create(is_sudoer))
def enable_bank_game(client, message):
    chat_id = message.chat.id
    bank_data = load_bank_data()

    if 'game_enabled' in bank_data:
        client.send_message(chat_id, 'لعبة البنك مفعلة بالفعل في المجموعة')
    else:
        bank_data['game_enabled'] = True
        save_bank_data(bank_data)
        client.send_message(chat_id, 'تم تفعيل لعبة البنك في المجموعة')



#######£££££££££££££££#######££££££££££#############££££££££££#########££££#
#######£££££££££££££££#######££££££££££#############££££££££££#########££££



@app.on_message(command('تعطبل البنك') & filters.create(is_sudoer))
def disable_bank_game(client, message):
    chat_id = message.chat.id
    bank_data = load_bank_data()

    if 'game_enabled' in bank_data:
        del bank_data['game_enabled']
        save_bank_data(bank_data)
        client.send_message(chat_id, 'تم تعطيل لعبة البنك في المجموعة')
    else:
        client.send_message(chat_id, 'لعبة البنك معطلة بالفعل في المجموعة')


#######£££££££££££££££#######££££££££££#############££££££££££#########££££#
#######£££££££££££££££#######££££££££££#############££££££££££#########££££



@app.on_message(command('انشاء حساب بنكي'))
def create_account(client, message):
    user_id = message.from_user.id
    username = message.from_user.username
    bank_data = load_bank_data()
    account_number = random.randint(100000000000000, 999999999999999)
    if 'accounts' not in bank_data:
        bank_data['accounts'] = {}
    
    if str(user_id) in bank_data['accounts']:
        client.send_message(message.chat.id, 'لديك بالفعل حساب بنكي')
    else:
        bank_data['accounts'][str(user_id)] = {
            'username': username,
            'balance': 50,
            'account_number': account_number,
            'thief': 0
        }
        save_bank_data(bank_data)
        client.send_message(message.chat.id, 'تم إنشاء حساب بنكي بنجاح اكتب حسابي لترى حسابك')

#######£££££££££££££££#######££££££££££#############££££££££££#########££££#
#######£££££££££££££££#######££££££££££#############££££££££££#########££££


@app.on_message(command('فلوسي'))
def check_balance(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    
    if str(user_id) in bank_data['accounts']:
        balance = bank_data['accounts'][str(user_id)]['balance']
        client.send_message(message.chat.id, f'رصيدك الحالي هو: {balance} دولار')
    else:
        client.send_message(message.chat.id, 'ليس لديك حساب بنكي')

#######£££££££££££££££#######££££££££££#############££££££££££#########££££#
#######£££££££££££££££#######££££££££££#############££££££££££#########££££




@app.on_message(command('فلوسه'))
def check_user_balance(client, message):
    reply = message.reply_to_message
    if reply:
        user_id = reply.from_user.id
        bank_data = load_bank_data()
        
        if str(user_id) in bank_data['accounts']:
            balance = bank_data['accounts'][str(user_id)]['balance']
            client.send_message(message.chat.id, f'رصيد {reply.from_user.username} هو: {balance} دولار')
        else:
            client.send_message(message.chat.id, f'المستخدم {reply.from_user.username} ليس لديه حساب بنكي')
    else:
        client.send_message(message.chat.id, 'الرجاء الرد على رسالة المستخدم للحصول على معلومات الحساب')

#######£££££££££££££££#######££££££££££#############££££££££££#########££££#
#######£££££££££££££££#######££££££££££#############££££££££££#########££££




@app.on_message(command('حسابي'))
def view_account(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    
    if str(user_id) in bank_data['accounts']:
        username = bank_data['accounts'][str(user_id)]['username']
        balance = bank_data['accounts'][str(user_id)]['balance']
        account_number = bank_data['accounts'][str(user_id)]['account_number']
        client.send_message(message.chat.id, f'حسابك البنكي:\nالمستخدم: {username}\nالرصيد: {balance} دولار\nرقم الحساب : {account_number}')
    else:
        client.send_message(message.chat.id, 'ليس لديك حساب بنكي')

#######£££££££££££££££#######££££££££££#############££££££££££#########££££#
#######£££££££££££££££#######££££££££££#############££££££££££#########££££



@app.on_message(command('حسابه'))
def view_user_account(client, message):
    reply = message.reply_to_message
    if reply:
        user_id = reply.from_user.id
        bank_data = load_bank_data()
        
        if str(user_id) in bank_data['accounts']:
            username = bank_data['accounts'][str(user_id)]['username']
            balance = bank_data['accounts'][str(user_id)]['balance']
            account_number = bank_data['accounts'][str(user_id)]['account_number']
            client.send_message(message.chat.id, f'حساب {reply.from_user.username} البنكي:\nالمستخدم: {username}\nالرصيد: {balance} دولار\nرقم حسابه : {account_number}')
        else:
            client.send_message(message.chat.id, f'المستخدم {reply.from_user.username} ليس لديه حساب بنكي')
    else:
        client.send_message(message.chat.id, 'الرجاء الرد على رسالة المستخدم لعرض حسابه البنكي')





#######£££££££££££££££#######££££££££££#############££££££££££#########££££#
#######£££££££££££££££#######££££££££££#############££££££££££#########££££




OPERATION_COOLDOWN = 1200  


last_operation_times = {}


def get_operation_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_operation_times:
        last_operation_time = last_operation_times[user_id]
        elapsed_time = current_time - last_operation_time
        remaining_time = OPERATION_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time
def update_operation_time(user_id):
    last_operation_times[user_id] = int(time.time())



@app.on_message(command(['', 'مضاربة', 'مضاربه', '']))
def multiply(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()

    if str(user_id) in bank_data['accounts']:
        remaining_time = get_operation_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 2 and args[1].isdigit():
                amount = int(args[1])
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    bank_data['accounts'][str(user_id)]['balance'] -= amount
                    save_bank_data(bank_data)
                    multiplier = random.randint(2, 5)
                    result_amount = amount * multiplier
                    bank_data['accounts'][str(user_id)]['balance'] += result_amount
                    save_bank_data(bank_data)
                    client.send_message(message.chat.id, f'تهانينا! لقد قمت بالمضاربه وحصلت على {result_amount} دولار')
                    update_operation_time(user_id)
                else:
                    client.send_message(message.chat.id, 'رصيدك الحالي غير كافي')
            else:
                client.send_message(message.chat.id, 'الرجاء استخدام الأمر بالشكل الصحيح: مضاربه + المبلغ')
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            client.send_message(message.chat.id, f'عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى')
    else:
        client.send_message(message.chat.id, 'ليس لديك حساب بنكي')



#######£££££££££££££££#######££££££££££#############££££££££££#########££££#
#######£££££££££££££££#######££££££££££#############££££££££££#########££££


OPERATION_COOLDOWN = 1200  


last_bribe_times = {}


def get_bribe_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_bribe_times:
        last_bribe_time = last_bribe_times[user_id]
        elapsed_time = current_time - last_bribe_time
        remaining_time = OPERATION_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time


def update_bribe_time(user_id):
    last_bribe_times[user_id] = int(time.time())



@app.on_message(command('رشوه'))
def bribe_command(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()

    if str(user_id) in bank_data['accounts']:
        remaining_time = get_bribe_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 1:
                amount = random.randint(300, 4000)
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    if message.reply_to_message is None:
                        client.send_message(message.chat.id, 'الرجاء الرد على رسالة لإرسال الرشوة')
                        return
                    receiver_id = message.reply_to_message.from_user.id
                    if receiver_id == user_id:
                        client.send_message(message.chat.id, 'لا يمكنك إرسال رشوة لنفسك')
                        return
                    bank_data['accounts'][str(user_id)]['balance'] -= amount
                    bank_data['accounts'][str(receiver_id)]['balance'] += amount
                    save_bank_data(bank_data)
                    client.send_message(message.chat.id, f'تمت عملية الرشوة بنجاح! قمت بتحويل {amount} دولار إلى المستلم')
                    update_bribe_time(user_id)
                else:
                    client.send_message(message.chat.id, 'رصيدك الحالي غير كافي')
            else:
                client.send_message(message.chat.id, 'الرجاء استخدام الأمر بالشكل الصحيح: رشوة')
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            client.send_message(message.chat.id, f'عذرًا، يجب الانتظار {minutes} دقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى')
    else:
        client.send_message(message.chat.id, 'ليس لديك حساب بنكي')





#######£££££££££££££££#######££££££££££#############££££££££££#########££££#
#######£££££££££££££££#######££££££££££#############££££££££££#########££££






OPERATION_COOLDOWN = 1200


last_wheel_times = {}


def get_wheel_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_wheel_times:
        last_wheel_time = last_wheel_times[user_id]
        elapsed_time = current_time - last_wheel_time
        remaining_time = OPERATION_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time


def update_wheel_time(user_id):
    last_wheel_times[user_id] = int(time.time())



@app.on_message(command("عجلة الحظ"))
def wheel_of_fortune(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()

    if str(user_id) in bank_data['accounts']:
        remaining_time = get_wheel_remaining_time(user_id)
        if remaining_time <= 0:
            win_amount = random.randint(100, 5000)
            bank_data['accounts'][str(user_id)]['balance'] += win_amount
            save_bank_data(bank_data)
            if win_amount > 0:
                client.send_message(message.chat.id, f'تهانينا! لقد فزت بمبلغ {win_amount} دولار في عجلة الحظ')
            else:
                client.send_message(message.chat.id, 'عذرًا، لم تفز بأي مبلغ في عجلة الحظ هذه المرة')
            update_wheel_time(user_id)
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            client.send_message(message.chat.id, f'عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى')
    else:
        client.send_message(message.chat.id, 'ليس لديك حساب بنكي')




#######£££££££££££££££#######££££££££££#############££££££££££#########££££#
#######£££££££££££££££#######££££££££££#############££££££££££#########££££


OPERATION_COOLDOWN = 1200  


last_tip_times = {}

def get_custom_tip_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_tip_times:
        last_tip_time = last_tip_times[user_id]
        elapsed_time = current_time - last_tip_time
        remaining_time = OPERATION_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time


def update_custom_tip_time(user_id):
    last_tip_times[user_id] = int(time.time())


@app.on_message(command('بخشيش'))
def custom_tip_command(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()

    if str(user_id) in bank_data['accounts']:
        remaining_time = get_custom_tip_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 2 and args[1].isdigit():
                amount = int(args[1])
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    if message.reply_to_message is None:
                        client.send_message(message.chat.id, 'الرجاء الرد على رسالة لإرسال البخشيش')
                        return
                    receiver_id = message.reply_to_message.from_user.id
                    if receiver_id == user_id:
                        client.send_message(message.chat.id, 'لا يمكنك إرسال البخشيش لنفسك')
                        return
                    bank_data['accounts'][str(user_id)]['balance'] -= amount
                    bank_data['accounts'][str(receiver_id)]['balance'] += amount
                    save_bank_data(bank_data)
                    client.send_message(message.chat.id, f'تمت عملية البخشيش بنجاح! قمت بتحويل {amount} دولار إلى المستلم')
                    update_custom_tip_time(user_id)
                else:
                    client.send_message(message.chat.id, 'رصيدك الحالي غير كافي')
            else:
                client.send_message(message.chat.id, 'الرجاء استخدام الأمر بالشكل الصحيح: بخشيش + المبلغ')
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            client.send_message(message.chat.id, f'عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى')
    else:
        client.send_message(message.chat.id, 'ليس لديك حساب بنكي')


#######£££££££££££££££#######££££££££££#############££££££££££#########££££#
#######£££££££££££££££#######££££££££££#############££££££££££#########££££









SALARY_COOLDOWN = 1200  


last_salary_times = {}


def get_salary_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_salary_times:
        last_salary_time = last_salary_times[user_id]
        elapsed_time = current_time - last_salary_time
        remaining_time = SALARY_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time


def update_salary_time(user_id):
    last_salary_times[user_id] = int(time.time())



@app.on_message(command('راتب'))
def salary(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()

    if str(user_id) in bank_data['accounts']:
        remaining_time = get_salary_remaining_time(user_id)
        if remaining_time <= 0:
            salary_amount = 3500
            bank_data['accounts'][str(user_id)]['balance'] += salary_amount
            save_bank_data(bank_data)
            client.send_message(message.chat.id, f'تم صرف راتبك الشهري بمبلغ {salary_amount} دولار')
            update_salary_time(user_id)
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            client.send_message(message.chat.id, f'عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى')
    else:
        client.send_message(message.chat.id, 'ليس لديك حساب بنكي')

#######£££££££££££££££#######££££££££££#############££££££££££#########££££#
#######£££££££££££££££#######££££££££££#############££££££££££#########££££








STEAL_COOLDOWN = 1200  
POLICE_COOLDOWN = 1200  

last_steal_times = {}
last_police_times = {}
last_protection_times = {}


def get_steal_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_steal_times:
        last_steal_time = last_steal_times[user_id]
        elapsed_time = current_time - last_steal_time
        remaining_time = STEAL_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time


def get_police_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_police_times:
        last_police_time = last_police_times[user_id]
        elapsed_time = current_time - last_police_time
        remaining_time = POLICE_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time


def get_protection_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_protection_times:
        last_protection_time = last_protection_times[user_id]
        elapsed_time = current_time - last_protection_time
        remaining_time = STEAL_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time


def update_steal_time(user_id):
    last_steal_times[user_id] = int(time.time())


def update_police_time(user_id):
    last_police_times[user_id] = int(time.time())


def update_protection_time(user_id):
    last_protection_times[user_id] = int(time.time())

@app.on_message(command("زرف"))
def steal_money(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()

    if str(user_id) in bank_data['accounts']:
        remaining_time = get_steal_remaining_time(user_id)
        if remaining_time > 0:
            client.send_message(message.chat.id, f'يجب عليك الانتظار لمدة {remaining_time} ثانية قبل استخدام الأمر مرة أخرى')
        else:
            target_id = message.reply_to_message.from_user.id
            if str(target_id) in bank_data['accounts']:
                if target_id == user_id:
                    client.send_message(message.chat.id, 'يغبي ميصير تزرف نفسك')
                else:
                    stolen_amount = random.randint(10, 50)
                    if stolen_amount <= bank_data['accounts'][str(target_id)]['balance']:
                        bank_data['accounts'][str(user_id)]['balance'] += stolen_amount
                        bank_data['accounts'][str(target_id)]['balance'] -= stolen_amount
                        bank_data['accounts'][str(user_id)]['thief'] += stolen_amount
                        save_bank_data(bank_data)
                        update_steal_time(user_id)
                        client.send_message(message.chat.id, f'تم زرف {stolen_amount} دولار من المستخدم')
                    else:
                        client.send_message(message.chat.id, 'ماتكدر تزرفه لان مفلس')
            else:
                client.send_message(message.chat.id, 'المستخدم المحدد لا يملك حساب بنكي')
    else:
        client.send_message(message.chat.id, 'ليس لديك حساب بنكي')

@app.on_message(command("شرطة"))
def police_user(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()

    if str(user_id) in bank_data['accounts']:
        remaining_time = get_police_remaining_time(user_id)
        if remaining_time > 0:
            client.send_message(message.chat.id, f'يجب عليك الانتظار لمدة {remaining_time} ثانية قبل استخدام الأمر مرة أخرى')
        else:
            target_id = message.reply_to_message.from_user.id
            if str(target_id) in bank_data['accounts']:
                if target_id == user_id:
                    client.send_message(message.chat.id, 'لا يمكنك استخدام الأمر على نفسك!')
                else:
                    stolen_amount = random.randint(10, 50)
                    if stolen_amount <= bank_data['accounts'][str(user_id)]['balance']:
                        bank_data['accounts'][str(user_id)]['balance'] -= stolen_amount
                        bank_data['accounts'][str(target_id)]['balance'] += stolen_amount
                        save_bank_data(bank_data)
                        update_police_time(user_id)
                        client.send_message(message.chat.id, f'تمت عملية القبض على المستخدم! تم خصم {stolen_amount} دولار من حسابك')
                    else:
                        client.send_message(message.chat.id, 'رصيدك الحالي غير كافي للقبض على المستخدم')
            else:
                client.send_message(message.chat.id, 'المستخدم المحدد لا يملك حساب بنكي')
    else:
        client.send_message(message.chat.id, 'ليس لديك حساب بنكي')

@app.on_message(command("حماية"))
def protect_money(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()

    if str(user_id) in bank_data['accounts']:
        remaining_time = get_protection_remaining_time(user_id)
        if remaining_time > 0:
            client.send_message(message.chat.id, f'يجب عليك الانتظار لمدة {remaining_time} ثانية قبل استخدام الأمر مرة أخرى')
        else:
            protection_amount = random.randint(10, 50)
            if protection_amount <= bank_data['accounts'][str(user_id)]['balance']:
                bank_data['accounts'][str(user_id)]['balance'] -= protection_amount
                save_bank_data(bank_data)
                update_protection_time(user_id)
                client.send_message(message.chat.id, f'تم تنفيذ عملية حماية الأموال بنجاح! تم خصم {protection_amount} دولار من حسابك')
            else:
                client.send_message(message.chat.id, 'رصيدك الحالي غير كافي لحماية الأموال')
    else:
        client.send_message(message.chat.id, 'ليس لديك حساب بنكي')









@app.on_message(command(["توب الحراميه", "توب الحرامية", "", "", ""]))
def top_thieves(client, message):
    bank_data = load_bank_data()
    sorted_accounts = sorted(bank_data['accounts'], key=lambda x: bank_data['accounts'][x]['thief'], reverse=True)
    top_thieves = sorted_accounts[:10]  
    response = "أعلى الحرامية في البنك:\n\n"
    
    for thief_id in top_thieves:
        thief_username = client.get_chat(int(thief_id)).username
        thief_balance = bank_data['accounts'][thief_id]['thief']
        response += f"@{thief_username}: {thief_balance} دولار\n"
    
    client.send_message(message.chat.id, response)

#######£££££££££££££££#######££££££££££#############££££££££££#########££££#
#######£££££££££££££££#######££££££££££#############££££££££££#########££££






@app.on_message(command("توب فلوس"))
def top_money(client, message):
    bank_data = load_bank_data()
    sorted_accounts = sorted(bank_data['accounts'], key=lambda x: bank_data['accounts'][x]['balance'], reverse=True)
    top_accounts = sorted_accounts[:10]  # احصل على أول 10 حسابات بالأموال الأعلى
    response = "أعلى الأموال في البنك:\n\n"
    
    for account_id in top_accounts:
        account_username = client.get_chat(account_id).username
        account_balance = bank_data['accounts'][account_id]['balance']
        response += f"@{account_username}: {account_balance} دولار\n"
    
    client.send_message(message.chat.id, response)





