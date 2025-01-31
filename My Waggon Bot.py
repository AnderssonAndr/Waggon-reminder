
import telebot
import random
import datetime
import time
import threading
from telebot.types import BotCommand
bot = telebot.TeleBot("7198639050:AAEtTCvj-3krpuHIds7OP8QPVOw0hHgjk2I")
bot.set_my_commands([
    BotCommand("start", "Начать общение с ботом"),
    BotCommand("habit", "Получить полезный совет")])
list_of_habits = ["Дай телу хорошую физическую нагрузку всего\n"
                  "по 1 минуте 4-5 раз в день - и ты снизишь\n"
                  "риск смерти от всех причин на 30-40%!!!",
                  "Питайся НЕ по часам, а дождавшись реального\n"
                  "аппетита - не думай, что ты умнее природы",
                  "Выделяй достаточное для тебя время для сна",
                  "Находи время пообщаться с приятными тебе \n "
                  "людьми"]
@bot.message_handler(commands=["start"])
def start_message(message):
    bot.reply_to(message, text="Привет)), я буду время от времени \n"
                               " напоминать о полезных привычках. \n"
                               "Или можешь нажать в menu  /habit в \n"
                               "свободную минуту, чтобы вспомнить \n"
                               "что-то полезное для здоровья сам/сама")
    reminder_thread = threading.Thread(target=reminder,
                                       args=(message.chat.id,))
    reminder_thread.start()
@bot.message_handler(commands=["habit"])
def habits(message):
    random_habit = random.choice(list_of_habits)
    bot.send_message(message.chat.id, random_habit)
def reminder(chat_id):
    while True:
        now = datetime.datetime.now()
        now = now.strftime("%H:%M")
       #for i in range(11,22):
            #if now == f"{i}:00" or now == f"{i}:30":
        if now.endswith(":00") or now.endswith(":30"):
            random_habit = random.choice(list_of_habits)
            bot.send_message(chat_id, random_habit)
            time.sleep(60*3)
bot.polling(none_stop=True)






