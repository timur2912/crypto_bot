from string import Template
from googletrans import Translator

def translate_to_russian(english_text):
    try:
        translator = Translator()
        translated = translator.translate(english_text, src='en', dest='ru')
        return translated.text
    except:
        return english_text


def BuyFormaterVIP(data):
    t = Template(
"""➡ СИГНАЛ
📊 ПОКУПКА - $name - Плечо: $leverage

✔ Вход: $entry

⚡ Цели: $targets 

⛔ Стоп-лосс: $stop_loss 
""")

    s = t.substitute(entry=data['entry'],
                     targets=data['targets'],
                     stop_loss=data['stop_loss'],
                     name=data['name'],
                     leverage=data['leverage'],
                     )
    return s

def SellFormaterVIP(data):
    t = Template(
"""➡ Продажа
📊 ПОКУПКА - $name - Плечо: $leverage

✔ Вход: $entry

⚡ Цели: $targets 

⛔ Стоп-лосс: $stop_loss 
""")

    s = t.substitute(entry=data['entry'],
                     targets=data['targets'],
                     stop_loss=data['stop_loss'],
                     name=data['name'],
                     leverage=data['leverage'],
                     )
    return s

def TargetFormater(data):
    t = Template(
"""$name - Цель 2 достигнута ✔
✅ Заработок: $profit

⏰ Время: $period
""")

    s = t.substitute(profit=data['profit'],
                     period=translate_to_russian(data['period']),
                     name=data['name'],
                     )
    return s

def LossFormater(data):
    t = Template(
"""❌ $name - Стоп-Лосс 
Потеря: $loss
""")

    s = t.substitute(loss=data['loss'],
                     name=data['name'],
                     )
    return s

def AllTargetsFormater(data):
    t = Template(
"""🚫💵 $name Все цели достигнуты!!
✅ Заработок: $profit
⏰ Время: $period
""")

    s = t.substitute(profit=data['profit'],
                     period=translate_to_russian(data['period']),
                     name=data['name'],
                     )
    return s

def BuyFormater(data):
    t = Template(
"""➡ СИГНАЛ
📊 ПОКУПКА - $name - Плечо: $leverage

✔ Вход: $entry

⚡ Цели: $targets 

⛔ Стоп-лосс: $stop_loss 
""")

    s = t.substitute(entry=data['entry'],
                     targets=data['targets'],
                     stop_loss=data['stop_loss'],
                     name=data['name'],
                     leverage=data['leverage'],
                     )
    return s

def SellFormater(data):
    t = Template(
"""🔐 Новый сигнал $name доступен.
 👑 Сигнал доступен только с ВИП статусом.
""")

    s = t.substitute(name=data['name'],

                     )
    return s