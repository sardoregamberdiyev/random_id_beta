import random
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


def inline_btn(btn_type=None, ctg=None, tip=None, bts=None):
    if btn_type == "callru":
        btn = [
            [InlineKeyboardButton("Для связи👨🏻‍💻", url="https://t.me/Welkin_Manager")]
        ]

    return InlineKeyboardMarkup(btn)


def btns(tip=None):
    bts = []
    # if tip == "contact":
    #     bts.append([KeyboardButton("📞 Raqamni yuborish",
    #                                request_contact=True)])

    # if tip == "region":
    #     bts = [[KeyboardButton("Tashkent"), KeyboardButton("Farg'ona")],
    #            [KeyboardButton("Andijon"), KeyboardButton("Jizzax")],
    #            [KeyboardButton("Sirdaryo"), KeyboardButton("Surxondaryo")],
    #            [KeyboardButton("Samarqand"), KeyboardButton("Buxoro")],
    #            [KeyboardButton("Namangan"), KeyboardButton("Navoiy")],
    #            [KeyboardButton("Xorazm"), KeyboardButton("Qashqadaryo")],
    #            [KeyboardButton("Orqaga 🔙")]
    #            ]

    if tip == "langru":
        bts = [
            [KeyboardButton("🇺🇿 Uzbek tili")],
            [KeyboardButton("🇷🇺 Руский язык")],
            [KeyboardButton("🇺🇸 English")],
        ]

    elif tip == "connectionru":
        bts = [
            [KeyboardButton("Связь📲")],
            [KeyboardButton("Назад 🔙"),KeyboardButton("Следующий🔜")],
        ]

    elif tip == "my_id_ru":
        bts = [
            [KeyboardButton("Получить идентификатор 🎲"), KeyboardButton("Я не получил удостоверение личности ❌")],
            [KeyboardButton("Связь 📲"), KeyboardButton("Назад🔙")],
        ]
    return ReplyKeyboardMarkup(bts, resize_keyboard=True)


def message_handler(update, context):
    msg = update.message.text

    # Tillar
    if msg == "🇺🇿 Uzbek tili":
        update.message.reply_text(f"ID olishdan oldin biz bilan bog'laning biz sizni qaysi maktabda ish faoliyat olib"
                                  "borishingizni bilishimiz va bazaga qo'shishimiz kerak, "
                                  "bog'lanishingiz mumkin 👇🏻", reply_markup=btns("connection"))

    elif msg == "🇷🇺 Руский язык":
        update.message.reply_text(f"Пожалуйста, свяжитесь с нами перед получением удостоверения личности"
                                  "нам нужно знать, что вы идете и добавляете в базу данных, "
                                  "вы можете связаться👇🏻", reply_markup=btns("connectionru"))

    elif msg == "🇺🇸 English":
        update.message.reply_text(f"Please contact us before getting ID"
                                  "we need to know what you are going to add to the database "
                                  "you can contact👇🏻", reply_markup=btns("connection"))

    # ID olish uchun bog'lanish
    if msg == "Связь📲":
        update.message.reply_text("Связаться с администратором UniCard👨🏻‍💻",
                                  reply_markup=inline_btn("callru"), parse_mode="HTML")

    # Contact
    elif msg == "Следующий🔜":
        update.message.reply_photo(photo=open("photo_2023-03-24_14-01-03.jpg", "rb"),
                                   caption="После того, как вам дадут случайный ID 👆🏻 \nНа сайте <b>Tasdiqlash ko'dni "
                                           "kiriting"
                                           "</b> введите в пустое поле.",
                                   reply_markup=btns("my_id_ru"), parse_mode="HTML")

    # ID olish
    elif msg == "Получить идентификатор 🎲":
        user_id = update.message.from_user.id
        random_id = random.randint(100000, 999999)
        context.user_data['id'] = random_id
        update.message.reply_text(f"UniCard, для однократного рандома \n\nВаш идентификационный номер: <b>{random_id}</b>",
                                  parse_mode="HTML")

    elif msg == "Я не получил удостоверение личности ❌":
        chat_id = update.message.chat_id
        context.bot.send_document(chat_id=chat_id, document=open("YordamPDF.pdf", "rb"), filename='YordamPDF.pdf',
                                  caption="<b>Unicard</b> о проекте и правильной системе управления "
                                          "Электронная концепция использования PDF.", parse_mode="HTML")

    elif msg == "Связь 📲":
        update.message.reply_text("Если у вас возникли проблемы с использованием и получением вашего "
                                  "идентификационного номера.\nМы вы можете связаться 👇🏻",
                                  reply_markup=inline_btn("callru"), parse_mode="HTML")

    # orqaga qaytish
    elif msg == "Назад🔙":
        update.message.reply_text("Прежде чем вы получите свой случайный идентификационный номер, вы должны связаться "
                                  "с администратором UniCard и\n вам необходимо заполнить информацию👇🏻",
                                  reply_markup=btns("connectionru"))

    elif msg == "Назад 🔙":
        update.message.reply_text("Если вы ошиблись в выборе языка, подайте заявку на другом языке👇🏻",
                                  reply_markup=btns("langru"))

