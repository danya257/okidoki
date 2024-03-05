import asyncio
# Функция-обработчик для кнопок "Подтвердить" и "Отменить"
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, Updater

from orders.models import Order


def send_telegram_message(message, chat_id):
    bot = Bot(token='6934370508:AAGhbvS5bGgDv5TCQT1KtgACRZCxS1bD6f4')

    button_confirm = InlineKeyboardButton(text="Подтвердить ✅", callback_data="confirm")
    button_cancel = InlineKeyboardButton(text="Отменить ❌", callback_data="cancel")
    production_time = [5, 10, 15]

    keyboard = [[button_confirm, button_cancel]]
    for production_time in production_time:
        button = InlineKeyboardButton(text=f"{production_time} мин", callback_data=f"time_{production_time}")
        keyboard.append([button])

    reply_markup = InlineKeyboardMarkup(keyboard)

    return bot.send_message(chat_id=chat_id, text=message, reply_markup=reply_markup)


# Функция-обработчик для кнопок "Подтвердить" и "Отменить"
def button_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_id = '144141209'
    bot = context.bot

    order_id = query.message.text.split()[3].replace('.', '')
    order = Order.objects.get(id=order_id)

    if query.data == 'confirm':
        order.confirmed = True
        order.cancelled = False
        order.save()

        time_buttons = [
            ["15 мин.", "15"], ["20 мин.", "20"], ["30 мин.", "30"],
            ["45 мин.", "45"], ["60 мин", "60"],
            ["1ч.15 мин.", "75"], ["1ч. 30 мин.", "90"]
        ]
        time_buttons_markup = [
            [InlineKeyboardButton(btn[0], callback_data=btn[1]) for btn in time_buttons]
        ]

        new_markup = InlineKeyboardMarkup(time_buttons_markup)
        query.edit_message_reply_markup(reply_markup=new_markup)

    elif query.data in ['15', '20', '30', '45', '60', '75', '90']:
        order_time = int(query.data)
        # Сохраняем значение времени в базе данных
        order.production_time = order_time
        order.save()


# Создаем обновление Telegram бота
updater = Updater(token='6934370508:AAGhbvS5bGgDv5TCQT1KtgACRZCxS1bD6f4', use_context=True)
dispatcher = updater.dispatcher

# Добавляем обработчик для callback запросов
dispatcher.add_handler(CallbackQueryHandler(button_callback))

# Запускаем бота
updater.start_polling()