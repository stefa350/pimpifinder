import telebot
import threading
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup, KeyboardButton
import time
import os

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

user_data = {}

hints = {
    0: [{'type': 'text', 'content': "E bene si la parola era proprio piripicchia, piccola piripicchia. Il prossimo però sarà un po' più difficile, ti darò un indizio con un'immagine, ecco a te:"},
        {'type': 'text', 'content': "_Il prossimo indizio troverai\n in una città dove non sei stata mai,\n patria dei comics e  dei souvenir da dimenticare,\n il suo nome è simile ad uno di cui non mi devo preoccupare... _"},
        {'type': 'image', 'content': 'https://raw.githubusercontent.com/stefa350/pimpifinder/main/PimpiFinder/lucca_mug1.jpg'},
        {'type': 'image', 'content': 'https://raw.githubusercontent.com/stefa350/pimpifinder/main/PimpiFinder/lucca_mug2.jpg'}
        ],
    1: [{'type': 'text', 'content': 'Okay ci stai prendendo la mano vedo, nella prossima troverai una piccola sorpresina, ma non ti cullare perchè il difficile sta per arrivare.'},
        {'type': 'text', 'content': 'Stavolta niente indovinello per te, vai soltanto a prendere una maglia per me, e cerca benee'}
        ],
    2: [{'type': 'text', 'content': "E bene si, hai trovato una sorpresina, ma cosa c'è lì? Una paperina? Forse è una figlia di Germi, o forse una delle tante..."},
        {'type': 'text', 'content': "Mi sa che Germi ha fatto più scappatelle di quanto pensassimo, visto che di figlie ne ha circa 50... ma tranquilla non devi trovarle tutte, per avere la prossima parola chiedi a stefanuccio quante ne devi trovare."},
        {'type': 'animation', 'content': "https://raw.githubusercontent.com/stefa350/pimpifinder/main/PimpiFinder/sillygoose.gif"}
        ],
    3: [ {'type':'text', 'content': "Va bene dai basta con le paperine ora, mi sa che ti sei sforzata abbastanza, forse hai bisogno di una pausa"},
         {'type':'text', 'content': "Oh? Come? Ste mi ha chiesto di poter prendere la parola per lasciarmi riposare un po', meno male che c'è lui, sei proprio fortunata... ci vediamo dopo pimpi!"},
         {'type':'text', 'content': "_Ciao pimpii sono stefanuccio, ti ricordi ancora di me? Se la risposta è no basta che guardi accanto a te e magari ti ricordi chi sono..._"},
         {'type':'text', 'content': "_Comunque, questo regalino te lo aspettavi lo so, e visto che il pimpi finder è in pausa ne approfitto per dartelo_"},
         {'type':'text', 'content': "_Considerlo come un regalino da vedere coi miei occhi, quindi non per forza con un messaggio nel testo o cose varie... o forse si_"},
         {'type':'text', 'content': "_Diciamo che troverai un po' un mix di cose, sia canzoni che mi fanno semplicemente pensare a te perchè magari le sentiamo assieme, sia canzoni il cui testo mi fa pensare a te (ci sono delle sorpresine alla fine).\n Ecco a te:_"},
         {'type':'text', 'content': "https://open.spotify.com/playlist/5QkWw9Oz01GiHp21ihTafK?si=1d79d3c20f3e4a70&pt=59f735a04480a6721b7fff1b93db5c96"},
         {'type':'text', 'content': "(La prossima parola segreta è il titolo della playlist)"}
        ],
    4: [{'type': 'text', 'content': "Che c'è? Sono ancora stanco... Lascio la parola a qualcuno che forse conosci"},
        {'type': 'video', 'content': 'https://github.com/stefa350/pimpifinder/raw/main/PimpiFinder/video1.mp4?v=1'}
        ],
    5: {'type': 'text', 'content': 'Spero tu sia stata contenta di non aver trovato una bolletta pimpi, la prossima è più vicina di quanto pensi, per trovarla dovrai appendertici per far rispondere chi è a casa'},
    6: [{'type':'audio', 'content': 'https://raw.githubusercontent.com/stefa350/pimpifinder/main/PimpiFinder/citofono.mp3'},
        {'type': 'text', 'content': 'Oooo chi è che suona'},
        {'type': 'text', 'content': "Ah sei tu pimpi, ero distratto scusami, per il prossimo indizio niente parole, solo numeri "},
        {'type': 'text', 'content': '37.727142,15.196627'}
        ],
    7: [{'type': 'text', 'content': 'Scusa gli inglesismi... non era il caso di scrivere TUTTA BAGNATA su un muro 💦💦'},
        {'type': 'text', 'content': 'Va bene okay sei stata brava fino ad ora, userò un aiuto da casa allora'},
        {'type': 'video', 'content': 'https://github.com/stefa350/pimpifinder/raw/main/PimpiFinder/video2.mp4?v=1'}
        ],
    8: [{'type': 'text', 'content': "Che brava pulcee, hai visto che aiutante che ho trovato? Va bene, andiamo avanti?"},
        {'type': 'text', 'content':'_Il prossimo indizio potrai trovare in un luogo di feste,\n con una cuccia fatta apposta per una piccola peste_'}
        ],
    9: [ {'type': 'video', 'content': 'https://github.com/stefa350/pimpifinder/raw/main/PimpiFinder/video3.mp4?v=1'},
       ],

    10:[
        {'type': 'text', 'content': "ihih okay matimati abbiamo quasi finito... diciamo, ecco il continuo dell'indovinello di prima"},
        {'type': 'text', 'content':'_Il prossimo indizio potrai trovare in un luogo di feste,\n con una cuccia fatta apposta per una piccola peste,\n lì la tua parolina potrai trovare in un posticino nascostino,\n dove era stato messo un regalino per un bambino (non il tuo fidanzato, un altro ihih)_'}
        ],

    11: [ {'type': 'text', 'content': "Visto che sei una bambina pure tu ho voluto mettere un regalino anche per te ihih"},
          {'type': 'text', 'content': "Okay okay ci siamo, adesso questa è semplice, il posto in cui devi andare è la casetta dell'ultima parola segreta."}
        ],
    12: [{'type': 'audio', 'content': 'https://raw.githubusercontent.com/stefa350/pimpifinder/main/PimpiFinder/saddino.mp3'},
         {'type':'text', 'content': "Questa sei tu quando ti dico che non posso farmi piccolo piccolo per poter stare sempre con te in una tua tasca"},
         {'type': 'text', 'content': "Questo è l'ultimo matimati, ce l'hai fattaa."}, 
         {'type': 'text', 'content': "Per l'ultimo messaggio lascio la parola a Ste se per te va bene"},
         {'type': 'text', 'content': "Ciao piccola pulcee sono stefanuccio (lo so che sono accanto a te adesso ma questo messaggio l'ho scritto tempo fa stupidina),\n L'ultimo posto dove devi andare è il posticino che ci lega di più in questa casetta, ci abbiamo passato uno dei nostri primi mesiversari a guardare le stelle e a fare anche altro..."},
         {'type': 'text', 'content': "Non è proprio questo il motivo per cui è uno dei posti più belli della casa, ma il motivo è che per me è un po' come se fosse il nostro posticino, è romantico ed appartato, un punto di 'fuga' dal caos per stare insieme a guardare le stelle.\n Hai capito di cosa parlo?"}
        ]
}
secret_words = {"piripicchia": 0,
                "Lucca": 1,
                "calzine paperine": 2,
                "quack50": 3,
                "pulce d'acqua dolce":4,
                "non sono una bolletta": 5,
                "M.Conti,S.D'Urso": 6,
                "WET": 7,
                "frontino": 8,
                "apritisesamo": 9,
                "brat": 10,
                "saphisaphi": 11,
                "cricetino topino": 12
}

# Funzione per inizializzare i dati utente se non esistono
def init_user_data(user_id):
    if user_id not in user_data:
        user_data[user_id] = {'unlocked': []}

def generate_keyboard(user_id):
    markup = InlineKeyboardMarkup()
    buttons = []
    emojis = ["🌼", "🐞", "💛", "🪿", "🌈", "🌲", "🎺", "💦", "🐾", "✨", "🟢", "⭐", "🐁"]

    # Aggiungi i pulsanti per gli indizi
    for i in range(13):
        # Se l'indizio è sbloccato, mostra il testo dell'indizio; altrimenti, mostra un lucchetto
        if i in user_data.get(user_id, {}).get('unlocked', []):
            emoji = emojis[i % len(emojis)]  
            button_text = f"{emoji} Clue {i + 1}"
        else:
            button_text = "🔒 Locked"

        button = InlineKeyboardButton(button_text, callback_data=f"hint_{i}")
        buttons.append(button)

    markup.add(*buttons)
    return markup


@bot.message_handler(commands=['start'])
def send_welcome(message):
    
    bot.reply_to(message, "Ciao! Mi hanno detto che ti chiami pimpi... guarda un po' che coincidenza io sono il pimpi finder e sarò il tuo aiutante in questa nuova avventura. Digita '/info' per avere maggiori informazioni su di me!")

@bot.message_handler(commands=['hunt'])
def hunt(message):
    user_id = message.from_user.id
    init_user_data(user_id)
    # Invia il menu con gli indizi

    bot.send_message(message.chat.id, "NON CI CREDO HAI SCOPERTO LA PAROLA SEGRETA MA CHE BRAVA!")
    time.sleep(3)
    bot.send_message(message.chat.id, "Probabilmente fino ad ora non avrai ben capito di cosa stiamo parlando, o forse si... diciamo che la parola segreta ci ha un po' smascherati")
    time.sleep(5)
    bot.send_message(message.chat.id, "Va bene Ste allora che dici possiamo iniziare?")
    time.sleep(7)
    bot.send_message(message.chat.id, "Non saprei, facciamo decidere lei, per favore pimpi, puoi dare un bacino a ste se pensi di essere pronta?")
    time.sleep(8)

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    unlock_button = KeyboardButton('🔓 Unlock')
    home_button = KeyboardButton('🏠 Home')
    markup.add(home_button, unlock_button)

    bot.send_message(message.chat.id, "Oh cazzo ragazzi che imbarazzo...prendete una stanza la prossima volta", reply_markup=markup)
    time.sleep(4)
    bot.send_message(message.chat.id, "Ecco a te la tua home con tutti i tuoi indizi...\nDovrai sbloccarli però ihih.\n Da ora in poi puoi accedervi cliccando 🏠 e potrai sbloccare nuovi indizi cliccando su 🔓 e digitando poi la parola segreta.\n BUONA FORTUNA E TANTI AUGURI MUAH", reply_markup=generate_keyboard(user_id)) 

    
    time.sleep(15)
    bot.send_message(message.chat.id, "Va bene dai il primo te lo do io, se no che aiutante sarei?")
    time.sleep(2)
    bot.send_message(message.chat.id, """_Il tuo primo indizio,\nsi nasconde in un posto un po' fittizio,\nnon è un luogo davvero reale,\nma è un posto in cui ti puoi sfogare,\ncerca lì dove le categorie si vanno a mescolare,\ntra mappe di chimica e merde da fare._""", parse_mode='Markdown')

@bot.message_handler(commands=['home'])
def home(message):
    user_id = message.from_user.id
    init_user_data(user_id)
    bot.send_message(message.chat.id, "Ecco tutti i tuoi indizi pimpi:", reply_markup=generate_keyboard(user_id))

@bot.message_handler(func=lambda message: message.text in ['🏠 Home', '🔓 Unlock'])
def handle_command(message):
    if message.text == '🏠 Home':
        user_id = message.from_user.id
        init_user_data(user_id)
        bot.send_message(message.chat.id, "Ecco tutti i tuoi indizi pimpi:", reply_markup=generate_keyboard(user_id))
    elif message.text == '🔓 Unlock':
        start_unlock_hint(message)
  

@bot.message_handler(commands=['unlock'])
def start_unlock_hint(message):
    user_id = message.from_user.id
    init_user_data(user_id)
    msg = bot.send_message(message.chat.id, "Inserisci la parola segreta per sbloccare un indizio per favore:")
    bot.register_next_step_handler(msg, check_secret_word)

def check_secret_word(message):
    user_id = message.from_user.id
    input_word = message.text.strip()

    if input_word in secret_words:
        hint_id = secret_words[input_word]
        # Sblocca il prossimo indizio (questo è solo un esempio, gestisci lo sblocco come preferisci)
        if hint_id not in user_data[user_id].get('unlocked', []):
            user_data[user_id]['unlocked'].append(hint_id)
            bot.send_message(message.chat.id, "Hai sbloccato un nuovo indizio, ma che brava!", reply_markup=generate_keyboard(user_id))
        else:
            bot.send_message(message.chat.id, "Questo indizio è già sbloccato.")
    else:
        bot.send_message(message.chat.id, "Parola chiave sbagliata, ritenta pimpi. Usa il comando /unlock parola_segreta per sbloccare un indizio (stupidina).")


def handle_hint(user_id, hint_id, chat_id):
    hint = hints.get(hint_id)
    
    if not hint:
        bot.send_message(chat_id, "Ops, sembra che ci sia un problema con questo indizio.")
        return
    
    if isinstance(hint,list):
        for item in hint:
            if item['type'] == 'text':
                time.sleep(3)
                bot.send_message(chat_id, item['content'], parse_mode='Markdown')
            elif item['type'] == 'image':
                time.sleep(5)
                bot.send_photo(chat_id, item['content'])
            elif item['type'] == 'video':
                time.sleep(3)
                bot.send_video(chat_id, item['content'])
            elif item['type'] == 'audio':
                bot.send_audio(chat_id, item['content'])
            elif item['type'] == 'animation':
                bot.send_animation(chat_id, item['content'])

       

    else:
        if hint['type'] == 'text':
            time.sleep(3)
            bot.send_message(chat_id, hint['content'], parse_mode='Markdown')
        elif hint['type'] == 'image':
            bot.send_photo(chat_id, hint['content'])
        elif hint['type'] == 'video':
            time.sleep(3)
            bot.send_video(chat_id, hint['content'])
        elif hint['type'] == 'audio':
            bot.send_audio(chat_id, hint['content'])
        

@bot.callback_query_handler(func=lambda call: call.data == "back_home")
def back_to_home(call):
    user_id = call.from_user.id
    bot.send_message(call.message.chat.id, "Sei tornata alla home:", reply_markup=generate_keyboard(user_id))


# Gestisci le risposte dei pulsanti
@bot.callback_query_handler(func=lambda call: call.data.startswith("hint_"))
def handle_callback(call):
    user_id = call.from_user.id
    hint_id = int(call.data.split('_')[1])
    print(user_data)
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

bot.infinity_polling()