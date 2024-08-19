import telebot
import threading
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Ciao! Mi hanno detto che ti chiami pimpi... guarda un po' che coincidenza io sono il pimpi finder e sarò il tuo aiutante in questa nuova avventura. Digita '/info' per avere maggiori informazioni su di me!")

user_data = {}
hints = {
    0: {'type': 'text', 'content': 'Indizio 1: Questo è un testo.'},
    1: {'type': 'image', 'content': 'https://example.com/image1.jpg'},
    2: {'type': 'video', 'content': 'https://example.com/video1.mp4'},
    3: {'type': 'audio', 'content': 'https://example.com/audio1.mp3'},
    4: {'type': 'text', 'content': 'Indizio 1: Questo è un testo.'},
    5: {'type': 'text', 'content': 'Indizio 1: Questo è un testo.'},
    6: {'type': 'text', 'content': 'Indizio 1: Questo è un testo.'},
    7: {'type': 'text', 'content': 'Indizio 1: Questo è un testo.'},
    8: {'type': 'text', 'content': 'Indizio 1: Questo è un testo.'},
    9: {'type': 'text', 'content': 'Indizio 1: Questo è un testo.'},
    10: {'type': 'text', 'content': 'Indizio 1: Questo è un testo.'},
    11: {'type': 'text', 'content': 'Indizio 1: Questo è un testo.'},
    12: {'type': 'text', 'content': 'Indizio 1: Questo è un testo.'},
    13: {'type': 'text', 'content': 'Indizio 1: Questo è un testo.'},
    14: {'type': 'text', 'content': 'Indizio 1: Questo è un testo.'},
    15: {'type': 'text', 'content': 'Indizio 1: Questo è un testo.'},
    16: {'type': 'text', 'content': 'Indizio 1: Questo è un testo.'},
    17: {'type': 'text', 'content': 'Indizio 1: Questo è un testo.'},
    18: {'type': 'text', 'content': 'Indizio 1: Questo è un testo.'},
    19: {'type': 'text', 'content': 'Indizio 1: Questo è un testo.'}    
}
secret_words = {"Lucca": 0,
                "Indizio": 1,
                "Indizio": 2,
                "Indizio": 3,
                "Indizio": 4,
                "Indizio": 5,
                "Indizio": 6,
                "Indizio": 7,
                "Indizio": 8,
                "Indizio": 9,
                "Indizio": 10,
                "Indizio": 11,
                "Indizio": 12,
                "Indizio": 13,
                "Indizio": 14,
                "Indizio": 15,
                "Indizio": 16,
                "Indizio": 17,
                "Indizio": 18,
                "Indizio": 19}

def generate_keyboard(user_id):
    markup = InlineKeyboardMarkup()
    buttons = []

    # Aggiungi i pulsanti per gli indizi
    for i in range(20):
        # Se l'indizio è sbloccato, mostra il testo dell'indizio; altrimenti, mostra un lucchetto
        if i in user_data.get(user_id, {}).get('unlocked', []):
            button_text = f"🌼 Clue {i + 1}"
        else:
            button_text = "🔒 Locked"

        button = InlineKeyboardButton(button_text, callback_data=f"hint_{i}")
        buttons.append(button)

    markup.add(*buttons)
    return markup


@bot.message_handler(commands=['hunt'])
def hunt(message):
    user_id = message.from_user.id

    # Invia il menu con gli indizi
    bot.send_message(message.chat.id, "NON CI CREDO HAI SCOPERTO LA PAROLA MAGICA MA CHE BRAVA!")
    time.sleep(5)
    bot.send_message(message.chat.id, "Probabilmente fino ad ora non avrai ben capito di cosa stiamo parlando, o forse si... diciamo che la parola segreta ci ha un po' smascherati")
    time.sleep(6)
    bot.send_message(message.chat.id, "Va bene Ste allora che dici possiamo iniziare?")
    time.sleep(7)
    bot.send_message(message.chat.id, "Non saprei, facciamo decidere lei, per favore pimpi, puoi dare un bacino a ste se pensi di essere pronta?")
    time.sleep(10)
    bot.send_message(message.chat.id, "Oh cazzo ragazzi che imbarazzo...prendete una stanza la prossima volta")
    time.sleep(4)
    bot.send_message(message.chat.id, "Ecco a te la tua home con tutti i tuoi indizi...\nDovrai sbloccarli però ihih.\n Da ora in poi puoi accedervi usando /home, BUONA FORTUNA E TANTI AUGURI MUAH", reply_markup=generate_keyboard(user_id))  

@bot.message_handler(commands=['home'])
def home(message):
    user_id = message.from_user.id

    # Inizializza lo stato dell'utente se non esiste
    if user_id not in user_data:
        user_data[user_id] = {'unlocked': []}

    # Invia il menu con gli indizi
    bot.send_message(message.chat.id, "Ecco tutti i tuoi indizi pimpi:", reply_markup=generate_keyboard(user_id))
    

@bot.message_handler(commands=['unlock'])
def unlock_hint(message):
    user_id = message.from_user.id
    input_word = message.text[len('/unlock '):].strip()

    if input_word in secret_words:
        hint_id = secret_words[input_word]
        # Sblocca il prossimo indizio (questo è solo un esempio, gestisci lo sblocco come preferisci)
        if hint_id not in user_data[user_id].get('unlocked', []):
            user_data[user_id]['unlocked'].append(hint_id)
            # Invia il nuovo stato del menu
            bot.send_message(message.chat.id, "Hai sbloccato un nuovo indizio, ma che brava!", reply_markup=generate_keyboard(user_id))
    else:
        bot.send_message(message.chat.id, "Parola chiave errata. Usa il comando /unlock parola_segreta per sbloccare un indizio (stupidina).")


def handle_hint(user_id, hint_id, chat_id):
    hint = hints.get(hint_id)
    if hint:
        if hint['type'] == 'text':
            bot.send_message(chat_id, hint['content'])
        elif hint['type'] == 'image':
            bot.send_photo(chat_id, hint['content'])
        elif hint['type'] == 'video':
            bot.send_video(chat_id, hint['content'])
        elif hint['type'] == 'audio':
            bot.send_audio(chat_id, hint['content'])


# Gestisci le risposte dei pulsanti
@bot.callback_query_handler(func=lambda call: call.data.startswith("hint_"))
def handle_callback(call):
    user_id = call.from_user.id
    hint_id = int(call.data.split('_')[1])
    
    if hint_id in user_data.get(user_id, {}).get('unlocked', []):
        handle_hint(user_id, hint_id, call.message.chat.id)
    else:
        bot.send_message(call.message.chat.id, "Questo indizio è ancora bloccato. Completa la caccia per sbloccarlo.")


@bot.message_handler(commands=['info'])
def infos(message):
    bot.reply_to(message, "Vedo che sei molto curiosa (ste mi aveva avvertito ma non credevo così tanto...) e bene ti racconterò di me.\n Sono pimpi finder e sarò la tua guida durante il corso di questa caccia. Stefano mi ha detto che è il tuo compleanno oggi vero? Allora inizerò facendoti i miei più sentiti auguri cara pimpi, quando sei pronta per iniziare il viaggio digita la parola segreta.")
    def send_buttons():
        # Funzione da eseguire dopo un ritardo
        time.sleep(9)
        markup = InlineKeyboardMarkup()
        button_yes = InlineKeyboardButton("Sì", callback_data="yes")
        button_no = InlineKeyboardButton("No", callback_data="no")
        markup.add(button_yes, button_no)
        bot.send_message(message.chat.id, "Ti vedo un po' confusa, non ricordi la parola segreta? Sicura di essere pimpi?", reply_markup=markup)

    # Avvia un thread per inviare il secondo messaggio dopo il ritardo
    threading.Thread(target=send_buttons).start()


# Gestisci le risposte dei pulsanti
@bot.callback_query_handler(func=lambda call: call.data in ["yes", "no"])
def handle_callback(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "Ottimo! Allora procediamo! Forse stefanuccio non ti ha detto la parola segreta... chiedila a lui no?")
    elif call.data == "no":
        bot.send_message(call.message.chat.id, "Oh no! Forse c'è stato un malinteso, mi dispiace chiunque tu sia...")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()