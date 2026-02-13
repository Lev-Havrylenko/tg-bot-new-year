import telebot
import random
from telebot import types
import os
TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

text = """ты у меня самая лучшая 🥇
ты самая красивая девушка в мире 😍
ты самая умная🤓
у тебя шикарные длинные волосы 😳
я обожаю твои волосы💓
у тебя самый красивые реснички 💞
твой носик самый красивый во всём мире 🥹
я тебя люблю сильнее всех на свете ❤️❤️❤️
с тобой хоть на край свет 🌍
я всегда рядом 💞
я всегда готов тебя поддержать 
я всегда рад тебе помогать❤️‍🩹
ты у меня самая прекрасная 😘
ты идеальна от стоп до макушки ❤️‍🔥❤️‍🔥❤️‍🔥
ты всегда умеешь поддержать 😚
ты моя опора 💪🏻
ты мой смысл жить 🧐
ты моя первая мысль с утра и последняя мысль ночью ☀️✨
с тобой все проблемы кажутся мелочами жизни 🤏
в твоих объятиях очень тепло 🫂
ты у меня самая милая   🥰 
ты у меня самая нежная  🩷
ты моя самая любимая кошечка 😽
в твоих объятиях я словно растворюсь 🫠
с тобой дни идут как минуты ⏳
у тебя самый красивый голос, я бы слушал его часами напролет 🗣️
ты самый интересный собеседник ❣️
у тебя очень красивый и вкусные ушки 😊
твоя шея как молоко 🥛
ты пахнешь вкуснее всех 🤤
ты у меня самая стильная 👠
ты у меня самая мудрая 🧠
я обожаю проводить с тобой время 🤗
ты у меня самая соблазнительная🥵
ты у меня самая сексуальная 😏
у тебя лучшая попа в мире 🍑(🥜)
у тебя самые лучшие сисюлики 🍒
ты всегда находишь нужные слова чтобы меня поддержать утешить ✊🏻
ты самая внимательная ‼️
ты лучшее что случалось в моей жизнь💖
я лучше тебя никого не встречал, сильнее тебя никого не любил ❤️‍🔥❤️‍🔥❤️‍🔥
воспоминание с тобой самые тёплые 💭
ты мой дом 🏠
я заработаю все деньги мира для тебя 💰
я всегда готов выслушать тебя ни смотря ни на что 👂
я за тебя горой 🏔️
я буду любить тебя всю жизнь 💟
я буду оберегать тебя от всех невзгод 🪬
ты готовишь лучше всех 🍜
ты самая заботливая 😌
ты невероятная 🥰
ты такая прикольная🤪
в твоих глазах я готов утонуть 👀
я очень тобой горжусь 🥹 
ты молодец 👏🏻 
ты умничка😚
у тебя всё всегда будет получатся 🤩
 ты очень добрая 😄
ты самая креативная 👩‍🎨
 ты у меня такая клёвая 😝
ты делаешь мою жизнь ярче 🌟
с тобой интересно даже простое молчание 😶 
я очень сильно тебя ценю 💝
я очень сильно тебя уважаю 💙
с тобой не страшны любые препятствия😌
мне очень нравится заботится о тебе 🧡
я очень хочу чтобы всю жизнь мы были вместе ❤️
с тобой очень спокойно спать (ну а иногда очень страшно 😁)
без тебя моя жизнь не имеет смысла😢
я хочу быть только с тобой🫵
кроме тебя мне никто не нужен ❌
я всегда буду любить тебя на 100 процентов 🔋"""
splt_text = text.split('\n')

all_photo = ["AgACAgIAAxkBAANFaUSnhSpFWdN9_5H_Px91RmWfVH8AAsYLaxtv3ChKgIJNgWTSP9kBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANEaUSnheQi34SMoxhGiYDFAAExbnA2AALEC2sbb9woSvG_rdhzLrCCAQADAgADeQADNgQ",
             "AgACAgIAAxkBAANGaUSnhap077ClEz2FUktwnlKce1sAArwLaxtv3ChKh17cQVz4c_ABAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANHaUSnhYR6WVX3MVJ95N489vufd8EAAr4Laxtv3ChKGXJR4u06Iw4BAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAMnaUSnhfCslrY_Akia7JzUlsQXViAAAqMLaxtv3ChKFmBOvebdvN4BAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAMoaUSnhSzDAz9a99lFQ-NYEhinFRUAAqQLaxtv3ChK_muu633AF20BAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAMpaUSnhZn1CDDD_oH-BIuSyrFh_0IAAqULaxtv3ChKzYcpgzLAtBYBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAMqaUSnhWij8y8sygGxoFEDJQuU3UwAAqYLaxtv3ChKX1bXyPsPJ5QBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAMraUSnhVVDHzU-P8HZd8B79xXd310AAqcLaxtv3ChKXk3Z2Xz_VP4BAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAMsaUSnhTqw06KN_mbjOv1TXrMLOfYAAqgLaxtv3ChKsuoBFSB341wBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAMtaUSnhUDF007vot-85ISIMhncCCAAAqkLaxtv3ChKfT2i3k2yvbABAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAMuaUSnhQ36fu_DKuvTY3ZXMgglf-YAAqoLaxtv3ChKcHoOav-w0DcBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAMvaUSnhWhzJ3obhsNU8ClzTqz7shYAAqsLaxtv3ChKBEL0cRs1ZT4BAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAMwaUSnhWPWV86CU4ZRWjgZrFg3qR0AAqwLaxtv3ChKTZ0x7xM8NgQBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAMxaUSnhc5U9InGMm5vsxSLZo6nbBsAAq0Laxtv3ChKWFmdZEaNq84BAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAMyaUSnhY3X6REuX163RrZcSxTn-ZIAAq4Laxtv3ChKiYBO1qsGbCgBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAMzaUSnhS9h6Ao5vaV-mmUCph3ljjAAAq8Laxtv3ChKMNsIH0uevPQBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAM0aUSnhV1GCybzvx45-eaoJGKEW5wAArALaxtv3ChKhYyw6oziV04BAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAM1aUSnhYhkXc7nGdILTB5AkMXFvY4AArELaxtv3ChKm2OxNoaqNDoBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAM2aUSnhRElHbhITl02QGb6jKzpd2sAArILaxtv3ChKeiKsAh1UN58BAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAM3aUSnheS9S6C8ldZrJZogy7cj3SkAArMLaxtv3ChK25fm0Ojq8vQBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAM4aUSnhexNghdesIME2o2ku6pwukgAArkLaxtv3ChKG4dth-Cc2aIBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAM5aUSnhcJd0b3jpeus2iXKuhcQ8DUAArsLaxtv3ChKDuAwI7cy2p8BAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAM6aUSnhbPDlpurUNdWon-53-ajbB4AAr0Laxtv3ChKl-0PD0ESX3QBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAM7aUSnhSsFq0ZTwj2eTacQYduCPu0AAr8Laxtv3ChK3f9_BoF0He4BAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAM8aUSnhSHPozO2Qo3dMgc4GfCmTBgAArQLaxtv3ChKV6VdJkgVL2ABAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAM9aUSnhQSMr7F2ULZd7i8IKNb-zf0AArULaxtv3ChKH5YNdQPTn04BAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAM-aUSnhcBfET-YzU2DnzsMmXcVwhQAArYLaxtv3ChKPrltBcXP3MMBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAAM_aUSnhf02qHJSV4lEjwv94vuN0qAAArcLaxtv3ChK67agu15miAoBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANAaUSnhXy2qFh8yU86nxhOHK9_5KoAAsALaxtv3ChK1Wr2EQzl--YBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANBaUSnhVhqcojglob-eSBY0wvbEwkAAsILaxtv3ChKqGXKxyPJba4BAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANCaUSnhbTvlnO8izqrzAdonwu6RD8AArgLaxtv3ChKNQoja_maw_UBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANDaUSnhQcQOFYsjvonpF89fUDjw_MAAroLaxtv3ChKA1IzpnRjdYMBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANFaUSnhSpFWdN9_5H_Px91RmWfVH8AAsYLaxtv3ChKgIJNgWTSP9kBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANEaUSnheQi34SMoxhGiYDFAAExbnA2AALEC2sbb9woSvG_rdhzLrCCAQADAgADeQADNgQ",
             "AgACAgIAAxkBAANGaUSnhap077ClEz2FUktwnlKce1sAArwLaxtv3ChKh17cQVz4c_ABAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANHaUSnhYR6WVX3MVJ95N489vufd8EAAr4Laxtv3ChKGXJR4u06Iw4BAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANIaUSnhVaA5mPH30DI-2SSKpMJJlgAAsgLaxtv3ChK99TGBD9D0jMBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANJaUSnhZc5tMQRAQ8CazbldYT2XrMAAsoLaxtv3ChKEeHxN-IYcQwBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANKaUSnhU9KJMbxxrvGX1WwpPkSrKUAAswLaxtv3ChKBQmAwyd4AAElAQADAgADeQADNgQ",
             "AgACAgIAAxkBAANLaUSnhZIYz02H8SVv0qQwrzdxeQgAAsELaxtv3ChKr3iKsTy0GvYBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANMaUSnhegmjD3IE2K7Dnu4VbXuY30AAsMLaxtv3ChKtx-K4zwFUPwBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANNaUSnhSWrxWP2GV19W4Hb_zXrZu4AAsULaxtv3ChK62FoyAx8nLoBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANOaUSnhV0XwytLizXcwRp7_o-gzzQAAscLaxtv3ChK3oLE23zEiz0BAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANPaUSnhSCIWwVezQ4JqnQ71Lg7BhwAAskLaxtv3ChK8TQ-eohiIyEBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANQaUSnhUJ5Qpklxmug8_P_FJ_hCJUAAssLaxtv3ChK9e5hzeGKjfIBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANRaUSnhXsbjtVGpv2bAy5m3eLZVikAAs0Laxtv3ChK4sOXUISMDHcBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANSaUSnhW7BWCHIFew8P04p1bWwZP0AAs4Laxtv3ChKV-Um8fb6jlkBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANTaUSnhUbA5bFE5hx1iM-IkzTjk2EAAs8Laxtv3ChK3Y-TY0x0sEsBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANUaUSnhWwRD7z3RbAlvaBjQtDPuL4AAtALaxtv3ChK86JVtmp260UBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANVaUSnhbkrrAXwGv95M8v8R4CcrhwAAtELaxtv3ChKkut1qaozVNIBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANWaUSnhQMnO0BI4zvNC7yB2Zv8bZgAAtILaxtv3ChK8d2ED9QAAXeQAQADAgADeQADNgQ",
             "AgACAgIAAxkBAANXaUSnhfHFwOzoYhc9EJxQm2LL2a0AAtMLaxtv3ChK0g_LS-WVJwYBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANYaUSnhbF0uCMlolNWPVTeeyZhQaEAAtQLaxtv3ChKbJ10ONe36dsBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANZaUSnhYO_c7M-JaEyg1e2kG1xEVkAAtULaxtv3ChKtvbuHlnoBmIBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANaaUSnha-FEXeA-W1mAQ5nnTMj6FcAAtYLaxtv3ChKTmRCx4Iqt5wBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANbaUSnhWN99kSb9l-Bw0rE1JPXL94AAtcLaxtv3ChK0CXoLEo1RS0BAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANcaUSnhU6IroScPxR4xxM0LyzpdG8AAtkLaxtv3ChKvz2JgKMj3asBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANdaUSnhWzfMTQwG2s0ZSOM2f2Xo9gAAtoLaxtv3ChKtbKt-mg1YyoBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANeaUSnhZ_WMDHa0SRHiw7ioZ7l0w0AAtwLaxtv3ChKvJCyP7GXfX4BAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANfaUSnhasMhhTUbL3TZ4aezwW0wdkAAtsLaxtv3ChKrAKGjxgIK7QBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANgaUSnhabcBSVDXi4QYZogGDHDbWIAAt4Laxtv3ChKHa8Ba9aa5QkBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANhaUSnhXzVpdH4AAFpBOEy4wKhQznoAALgC2sbb9woSr0znIPDwMegAQADAgADeQADNgQ",
             "AgACAgIAAxkBAANiaUSnhfzi21omj16eJgpCeSXctnYAAuILaxtv3ChKOJmdgBoI0sABAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANjaUSnhU2hwKw3tO3A3U1WAzEO9egAAuQLaxtv3ChKCw2OjkGl_S4BAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANkaUSnhc-QLFJTnUBM0puETMdsFDUAAuULaxtv3ChKaNuutYxUtWUBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANlaUSnhXsJ7c33wIZxClewielGdskAAucLaxtv3ChKaShJ26QlbvEBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANmaUSnhdUlNc0X38x22pEmSpbxt8gAAtgLaxtv3ChKyGBec1TCdJkBAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANnaUSnhY7JfLXLEX6t4SJ-uCWE4RAAAukLaxtv3ChKBVe5gb3KIv8BAAMCAAN5AAM2BA",
             "AgACAgIAAxkBAANoaUSnhbtxldFNA-gk2Imf_NwftB8AAuoLaxtv3ChKNfKXbkTsU7EBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAANpaUSnhR8ktp72j-2MUXDAwsUyJNYAAuELaxtv3ChK9NAFvvemEZEBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAANqaUSnhQu4GtwXYrofjLBRdzPWrRgAAuYLaxtv3ChKlC69KNWk8GMBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAANraUSnheO9J83xunLXb3jzYs5eAYAAAusLaxtv3ChKFvbqhBW3ZiEBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAANsaUSnhYmZIFI-K5QmHDzSZLjH4QsAAu0Laxtv3ChKR5Qr0ATcx40BAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAANtaUSnhbQtjlCgm8cursXX5f40t4kAAu4Laxtv3ChKfrD6fhfXCKkBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAANuaUSnhVP7UVsalESnoGmTNLoy6sIAAt0Laxtv3ChKt2VLwCuuxSABAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAANvaUSnhXKoNiv1v06Ziw1XrLODbSEAAvALaxtv3ChKD76n7RkgWT4BAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAANwaUSnhf45TANMbRKKCQABzWuiprLtAALyC2sbb9woShXCsymFfxT5AQADAgADeQADNgQ",
            "AgACAgIAAxkBAANxaUSnhcdyIj6yOpPCoNTgKUF1KcAAAvMLaxtv3ChK1tq_ai8ciLUBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAANyaUSnhfuQfyK_fNe1XfkoEYgGqJoAAvQLaxtv3ChK8gRKgnKGUEwBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAANzaUSnhTmgdc2FZ4o8gluxfT9BZjwAAugLaxtv3ChK_ATDlUWpb5wBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAN0aUSnhRto6uLgOf_wp07F25dw8fYAAu8Laxtv3ChKq2hRtp0JISsBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAN1aUSnhQgxqvIlkA9Ct4KwPq0Z1E4AAvULaxtv3ChKmPz97NICWMcBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAN2aUSnhaSBXMqy5DnGOdEcdU7uqSsAAvcLaxtv3ChKLsG0jmFwK7QBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAN3aUSnhe7J17HnzOwbZcWd3aBozX4AAvkLaxtv3ChKtta8CsxpsbgBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAN4aUSnhS_3OhTPAhfttvIQaWy7i4IAAvsLaxtv3ChKX5_Aqlp7TqIBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAN5aUSnhV9x9zPIp7icCgLdRI46V_0AAv0Laxtv3ChKWiODAa8aQugBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAN6aUSnhV8dmGynO4BH3NkI7kc54iIAAt8Laxtv3ChKSdyan1eY-1IBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAN7aUSnhUQ4EDkr7Oxpd72yvk7wxnoAAv8Laxtv3ChKB6OYxAR0buEBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAN8aUSnhWwh_2E2161T8uTxl2630lsAAuMLaxtv3ChKUYjBKHd6SDMBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAN9aUSnhVUR8srkZTGRfy8Q166yru0AAuwLaxtv3ChKhR1D538inrABAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAN-aUSnhcFGz_-3Ih3vUF2WyC-WSqAAAvELaxtv3ChKTH6fAmiS6pgBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAN_aUSnhb2tFnaD2IT8wW1xVGgqIV8AAvYLaxtv3ChK5bGqAwoCiG0BAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAOAaUSnhcTea0V72eImesuSkQdQirMAAv4Laxtv3ChKV5IVkArEtYcBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAOBaUSnhWAjtmlZ7YVCI_VFqiTakZAAAwxrG2_cKEpaETBm8SBcJwEAAwIAA3kAAzYE",
            "AgACAgIAAxkBAAOCaUSnhSJOxKFSSFqpE7dwsWDtN8oAAvgLaxtv3ChK2REIU7fwi84BAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAODaUSnheeyenZmflQZ283ClidizqQAAgEMaxtv3ChKV0KK3pdlK7oBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAOEaUSnhe30PYwYsFe24jhA8rz5W7AAAgIMaxtv3ChK_zgGnMuILbQBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAOFaUSnhQopfxeg_vq49F86ZjGMlyUAAvoLaxtv3ChKUb0ShpIzlz8BAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAOGaUSnhfqQfP81_YYmWj44rwdmYwcAAvwLaxtv3ChKpZINyxhxkf4BAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAOmaUSnjEEdFmXnmqO6mrlOX3_VX0QAAgMMaxtv3ChKBkyvisGTECEBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAOnaUSnjCRBksA3KUXHibN4_Gem3NcAAgQMaxtv3ChKKluWCBt95C8BAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAOoaUSnjNixTGQ1Mg2BGe8WumACBe8AAgUMaxtv3ChKm02B781-cBoBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAOpaUSnjJsg6349U-afSvDPs8eTCmYAAgYMaxtv3ChKvdKnSCkVl1QBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAPKaUSnjPXNmddbO448J3aJG7-y_FAAAikMaxtv3ChKOB5vSQAB6t33AQADAgADeQADNgQ",
            "AgACAgIAAxkBAAPLaUSnjNdEZ_nKinb92Gz-jmXCTAQAAisMaxtv3ChKSWcGoy2a_OABAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAPNaUSnjKj4PhGX61ZroSHqF8CMS3wAAjAMaxtv3ChKXfqqoEOsqpIBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAPMaUSnjC9H32PEf2Akn7WeMJqL8DEAAi0Maxtv3ChKOeYbCPv1EUkBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAPOaUSnjNWFahbyu-EvGq5fqgKCuMMAAjMMaxtv3ChKUQ7PvNeV470BAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAPPaUSnjKnH2SjJEyKEZF-dZbmH-eAAAjUMaxtv3ChKoEbzWIshCGsBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAPRaUSnjCtbhkXxv1d8bIp1Unt31GYAAiYMaxtv3ChKxKn7E4knvSEBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAPTaUSnjO-LQIpxrdb983RRa7gMi4MAAioMaxtv3ChK3JodlkKGYDQBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAPWaUSnjKdBjD2VJ6TxTpJCjbQqd6kAAi4Maxtv3ChKh0vYQxQor-sBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAPXaUSnjJOFS5bu5MOYDpygqIfdWc8AAi8Maxtv3ChK9rUGuyyNIJsBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAPYaUSnjKR6bSffDNcqQYeZtVhErMkAAjcMaxtv3ChKWAEhsyTPA54BAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAPZaUSnjM0oKWWUiah76LsYu5S0tEYAAjkMaxtv3ChKLuQ_oxsS5lcBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAPaaUSnjMi9z6hXES-1LHCUYUHhhmQAAjsMaxtv3ChK4o-5RzM14OMBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAPbaUSnjI15LO1yScWEbva1mZg1dFAAAj0Maxtv3ChKmVBq_XXFF0kBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAPcaUSnjCGgtCSW6avvCdr1s9V1zgIAAjEMaxtv3ChKDM2cHrmER6MBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAPdaUSnjCqrwhnBp2lIDLXzIUuJKMsAAjIMaxtv3ChKSHnfsLjlOv0BAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAPeaUSnjIKSSMqhDqqMWl1yU1fIzHsAAjQMaxtv3ChKkM0zFXNIbpkBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAPfaUSnjOdXgh2LZGaFalnQQtdIbEQAAjYMaxtv3ChKrub_L4oPdnwBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAPgaUSnjH-vYnksxJZKch1jIOBklgUAAjoMaxtv3ChK2KklR3k0guEBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAPhaUSnjIcC-YNE8Uf5O5gGPJrXCpIAAjwMaxtv3ChKCJMR17XdzDwBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAPiaUSnjKuh5Yd4xH46_BvmSln_ah4AAj4Maxtv3ChK-fBX2CbS-KoBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAPjaUSnjNkYCQGtSVhJOx4-zT2lGgUAAj8Maxtv3ChKS6Dc1Nn9IqMBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAPkaUSnjNddiSP85rSTdf0MPdTs2oEAAkAMaxtv3ChKauJkR8kJ9HkBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAPlaUSnjAEuG_o_zrZrhrXgG_JgtpUAAjgMaxtv3ChKbsPhbcvpGjsBAAMCAAN5AAM2BA",
            "AgACAgIAAxkBAAIElmmPi9vJGHz691_keXqfVRlTWzD3AAKTFWsbTbqBSAhWK3iugP98AQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEl2mPi9v_F0o7ItBzpTrgX9v20fW9AAKUFWsbTbqBSFhTc16cX_jbAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEmGmPi9vGN6HzoPZKeScGszv9dgaXAAKYFWsbTbqBSGiP8Qs7_VMMAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEmWmPi9sqOQNKCSDW3Of-9DUs0M6iAAKaFWsbTbqBSOm-A8yDBB4MAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEmmmPi9vUSDfJkK4XmQ7FQeJKHJn7AAKbFWsbTbqBSJjIga7si4QXAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEm2mPi9skaWMwGiC_vFzTk99lZ8q-AAKcFWsbTbqBSIeFLwRN27VVAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEnGmPi9ucZSsqvDgAAUNyUrgqZefiEwACnRVrG026gUji2jhLQO23agEAAwIAA3cAAzoE",
            "AgACAgIAAxkBAAIEnWmPi9vE11EkPvPn3Mp89pgTV2BbAAKVFWsbTbqBSBQ-0KlgkUEWAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEnmmPi9t7Kuzqf5if-pHRORsyxMQ7AAKWFWsbTbqBSBnwRYXnhTYmAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEn2mPi9uAzn8pJGy24OomF0lmMAbbAAKXFWsbTbqBSFC2DX8N2vepAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEb2mPi32qNTBLrLHvKbHhTiy9GDjvAAJvFWsbTbqBSEJO4x3vIbJ-AQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEcGmPi31iUkssSbw8F5d05JKmPoWUAAJoFWsbTbqBSA0FbKPwu_vQAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEcWmPi31YMJr3170wszjAhpT0n7W_AAJpFWsbTbqBSDVgZXRvIArVAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEcmmPi30hKyDmjIt9U3vAI5jY1MtsAAJqFWsbTbqBSGh3u3Bnt2OTAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEc2mPi30DDr4o_VY5swf8jfNT3R8kAAJrFWsbTbqBSNJOn80O3aZSAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEdGmPi33ud7-v9FShHee3bMbTlJ_oAAJsFWsbTbqBSJ-S9VwkA100AQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEbmmPi30XG6sY5-CfiJHQPEMbDRqPAAJnFWsbTbqBSNDGfHOx1s1CAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEdWmPi31fwJchr0a_pI8HpkD2MOOlAAJtFWsbTbqBSDhZf8Bs9EInAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEdmmPi33gjBE_-zoghbTiyoJzlW9_AAJwFWsbTbqBSKycZesFMCBcAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEd2mPi328A5xoBDTbFB2YljhEPySDAAJuFWsbTbqBSGUefIBP4VeKAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEeGmPi6SxdGwD73iwhmJSiBwoZh8AA3cVaxtNuoFIWdGINCndT0oBAAMCAAN3AAM6BA",
            "AgACAgIAAxkBAAIEeWmPi6R9NTTevOXfdl9VrpKVMfahAAJ7FWsbTbqBSFoAAdmFSM_oVwEAAwIAA3cAAzoE",
            "AgACAgIAAxkBAAIEemmPi6Sq_QABW0wmVIVCGqKxsUw4qQACfRVrG026gUhHvMWVgVdnTwEAAwIAA3cAAzoE",
            "AgACAgIAAxkBAAIEe2mPi6S6C0lmUAXf_u_IZVjE5SvdAAJxFWsbTbqBSEE6GyqKgr-RAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEfGmPi6SSb2KIc0BM6dd2nBVDC5UUAAJyFWsbTbqBSPKJ0TvaraGwAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEfGmPi6SSb2KIc0BM6dd2nBVDC5UUAAJyFWsbTbqBSPKJ0TvaraGwAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEfmmPi6TXpxhv1pyd_cYcN3qB4ksKAAKBFWsbTbqBSOVACQuD2EzgAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEf2mPi6QrlDkByHgadvyxYro8pctDAAKDFWsbTbqBSHYYMPG9xwABdwEAAwIAA3cAAzoE",
            "AgACAgIAAxkBAAIEgGmPi6TskWDmf5U1STU-RM3KfP_-AAJzFWsbTbqBSAAB3eBqyGXWygEAAwIAA3cAAzoE",
            "AgACAgIAAxkBAAIEgWmPi6Q76vzZco2poVfjOJjFJcHCAAJ0FWsbTbqBSEyH1qL778rWAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEgmmPi6v_xpgWHjcnm41BoY3xBQ9lAAJ2FWsbTbqBSIGC9PpQt1RqAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEg2mPi6vDQLB66sgGha3lWCNrM4DdAAJ4FWsbTbqBSKqPdajyV4KFAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEhGmPi6u06H8D2UdhAAEayoZkUghV1wACfBVrG026gUgrVhzp0kXnSwEAAwIAA3cAAzoE",
            "AgACAgIAAxkBAAIEhWmPi6vRfJkP9sCTtwIsJpp2o8-yAAJ-FWsbTbqBSJVeupTQySL5AQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEhmmPi6sD8v1uc1Uea-d2fHBC0MFBAAKAFWsbTbqBSHwNzEm9k_gDAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEh2mPi6uleSQGFxhxBPjpW3crvkAKAAKCFWsbTbqBSOJId_BeBDLBAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEiGmPi6sq_NhF6MkNly9wLsvTimdtAAKEFWsbTbqBSG3edKxyzQccAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEiWmPi6tGZ5-1BNxL7HvVBcCuWRC6AAKFFWsbTbqBSNiwRX4OqjetAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEimmPi6v_5qTrb-vFDQp1MZJxdvkoAAKGFWsbTbqBSFBQthg4A148AQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEi2mPi6syfoSaLVxIKCZrHce0m-2qAAKHFWsbTbqBSAHGM0qjIDxmAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEjGmPi7ygj2k7SOz2RkbAop5P97oEAAKIFWsbTbqBSH0uregBv_m1AQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEjWmPi7wdwmr2g56zKZya3mg-q5UkAAKJFWsbTbqBSCL6vo0vLRJ7AQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEjmmPi7w5fUcoWQlR27FAAkkYqA5WAAKKFWsbTbqBSCggjzlbqFZ2AQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEj2mPi7wAAbfbsS9CONtE7zQ8qcy3dAACixVrG026gUgTW4JM_9fRwgEAAwIAA3cAAzoE",
            "AgACAgIAAxkBAAIEkGmPi7xsCM1Nh5js11JeAAG2y_xYuwACjBVrG026gUiDrE7fZdTaHwEAAwIAA3cAAzoE",
            "AgACAgIAAxkBAAIEkWmPi7y-SoSVjDZRjtFGPi52chXkAAKNFWsbTbqBSFM5Ku5gZ1sJAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEkmmPi7wevCfKfAvXr7sgNip-mCGKAAKPFWsbTbqBSHCYP-CfAXCGAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIEk2mPi7xHogx7INc7iteIWzekPnrrAAKQFWsbTbqBSNO5JzovTjSqAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIElGmPi7ypEro55aj-md0bKNG4vdE4AAKRFWsbTbqBSDy8sBXVqSZOAQADAgADdwADOgQ",
            "AgACAgIAAxkBAAIElWmPi7zt6DJJgp7oI2k5ouvZRxWrAAKSFWsbTbqBSPIwNcXXb_d2AQADAgADdwADOgQ",
         ]
all_video = ["BAACAgIAAxkBAAIBaWlEr30nRDeBAAEViw1JBz2DGtMi7wAC6YoAAm_cKEq3ehbC62zyPDYE",
             "BAACAgIAAxkBAAIBamlEr30Z3tOXY__kvCrRak1tSkpzAAIrhwACYtIpSvVWvvqnrzIAATYE",
             "BAACAgIAAxkBAAIBbmlEsEN7DkPUV3kWNXY2HwnmZmNUAAIthwACYtIpSn0zc9yMA7AMNgQ",
             "BAACAgIAAxkBAAIBbWlEsEP_kqYaf56-vZIVmz-mFWzVAAIshwACYtIpSpLHoFm_3gsNNgQ",
             "BAACAgIAAxkBAAIBb2lEsEP6nEXM0cEgP97cXOTz-jxqAAIuhwACYtIpSp-9bp-1VaihNgQ",
             "BAACAgIAAxkBAAIBcGlEsENDvUKK-IHS5xLj0uRBIM-WAAIvhwACYtIpSoo7BDfg-s1eNgQ",
             "BAACAgIAAxkBAAIBcWlEsEPgQRY47CTJTbad4mDpMclHAAIwhwACYtIpShPS_lg2Tdw0NgQ",
             "BAACAgIAAxkBAAIBcmlEsEPhnzn23Q6GjRVjP47iuHBPAAI2hwACYtIpSv87jz5nOW4pNgQ",
             "BAACAgIAAxkBAAIBc2lEsEM_5abJCE89-TuAgqZrP6aOAAIxhwACYtIpSv2H3cPzsz7RNgQ",
             "BAACAgIAAxkBAAIBdGlEsEPQpaQVzxolS8z8KFSd2MmOAAIyhwACYtIpSmGZc_G_M4NrNgQ",
             "BAACAgIAAxkBAAIBdWlEsENuWaU3Bat6AXZS5o2A4We6AAI3hwACYtIpStlXE1VqFSkYNgQ",
             "BAACAgIAAxkBAAIBdmlEsEPi8aDWcN_vDRTng-DKjz1uAAIzhwACYtIpSiCypb_-AAGfLTYE",
             "BAACAgIAAxkBAAIBgmlEsHancRd0WO25bIT82IRjFKLeAAI1hwACYtIpStEPv9oOX2VCNgQ",
             "BAACAgIAAxkBAAIBgWlEsHamxz9y6-R33XAZnEXdG3gEAAI7hwACYtIpSiFyVErAHs22NgQ",
             "BAACAgIAAxkBAAIBg2lEsHbICivfUt3JKRa8w9jhEuHxAAI8hwACYtIpSmFwi9Y2OJG6NgQ",
             "BAACAgIAAxkBAAIBhGlEsHb_ZhrYhcsdCyvoy1wPi3eZAAI4hwACYtIpSvaguRSd5AABUDYE",
             "BAACAgIAAxkBAAIBhWlEsHYFOFCnuGNpm-pBgv7ACwkeAAI5hwACYtIpSsryJ2oSLYBrNgQ",
             "BAACAgIAAxkBAAIBYWlErfmkL-MmawH9BaWh6_7s5dMxAAIphwACYtIpSjcTch1zajJoNgQ",
             "BAACAgIAAxkBAAIFAmmPjupWIJJjC9OUvDp2bNtBvrGmAALnmAACTbqBSJdmjAoBV8dxOgQ",
             "BAACAgIAAxkBAAIFA2mPjupuqQAB2Kpo244bDeLyCxgcogAC6JgAAk26gUgWJcZ3pxX71zoE",
             "BAACAgIAAxkBAAIFBWmPjuqbCzEVUHgT7FhdZLh7dZlpAALwmAACTbqBSD6BT5CHVDnZOgQ",
             "BAACAgIAAxkBAAIFBmmPjuqjLLP1U6xL_h_comD6T9U5AALqmAACTbqBSLTjLUz1-az_OgQ",
             "BAACAgIAAxkBAAIFB2mPjuok0Ejw5P4E0BurQVWY0GcpAALxmAACTbqBSLq_GdONsff9OgQ",
             "BAACAgIAAxkBAAIFCGmPjuon8S3YKsj90_mjwU12pdYQAALsmAACTbqBSE1S5qltLoEAAToE",
             "BAACAgIAAxkBAAIFCWmPjurMZXlenB9ntnWXlico3R16AALtmAACTbqBSH-Qlp9-U3F8OgQ",
             "BAACAgIAAxkBAAIFCmmPjuqwSLUNNG91dccLzn5MTS1iAALumAACTbqBSPqNDzPvUZaTOgQ",
             "BAACAgIAAxkBAAIFBGmPjuqZ3AVOEDj_Z90mIs0qdLhgAALpmAACTbqBSOuj7yp0tG-TOgQ",
]

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Комплиментики💋")
    btn2 = types.KeyboardButton("Наши фоточки/видео😻")
    btn3 = types.KeyboardButton("С 4 месяцами!!❤️❤️❤️")
    btn4 = types.KeyboardButton("С 14 февраля!!❤️❤️❤️")
    markup.add(btn1)
    markup.add(btn2, btn3)
    markup.add(btn4)
    
    bot.send_message(message.chat.id, "<b>Этот бот создан для самой любимой и самой лучшей девушки на свете!\n С любовью от Левика🦁</b>", reply_markup=markup, parse_mode="HTML")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Комплиментики💋":
        msg = random.choice(splt_text)
        bot.send_message(message.chat.id, msg)
    elif message.text == "Наши фоточки/видео😻":
        choice = random.choice(['photo', 'video'])
        if choice == 'photo':
            rand = random.choice(all_photo).strip()
            bot.send_photo(message.chat.id, photo=rand)
        else:
            rand = random.choice(all_video).strip()
            bot.send_video(message.chat.id, video=rand)
    elif message.text == "С 4 месяцами!!❤️❤️❤️":
        bot.send_message(message.chat.id, """<tg-spoiler> моя олюсічка красотулічка, поздравляю нас с (правда ещё не наступившими) 4 месяцами. ты подумай, это целая треть года. мне не верится что мы уже так долго! ещё вчера я впервые увидел тебя на знакомстве с одногруппниками и шел в общагу с бабочками в животе. если бы мне тогда сказали, я бы не поверил что ты станешь моей девушкой. станешь самим близким и самым ценным человеком для меня. что ты - именно та, которую я искал всю свою жизнь. такую добрую, милую, красивую, умную, заботливую, внимательную, понимающую, нежную, соблазнительную, мудрую. с такой прекрасной улыбкой, шикарными длинными волосами, с невероятно красивыми глазами, с таким красивым носиком, с такими роскошными ресницами и бровями, идеальную от макушки до стоп.  я благодарен судьбе за то что она свела нас. ты мой лучик света и моя опора. без тебя я не я. меня очень радует что мы с тобой строим отношения. общаемся, ищем компромиссы. за прошлый месяц мы сделали много работы над нашими отношениями и стали ещё ближе. меня очень радует тот факт что ты готова идти на компромиссы и даже на уступки ради укрепления наших отношений. я вижу сколько сил ты вкладываешь в «нас». я это невероятно ценю. ещё я очень ценю твою готовность меня поддержать во всём. будь то мои начинание или мои переживание. именно поэтому я доверяю тебе на все 101%. я смотрю на тебя и понимаю что ты именно та. что с тобой я хочу видеть будущее, что для тебя я готов отдать всего себя и делать всё возможное, чтобы ты была счастлива. порой я бываю грустный, ранимый, огорченный, злой, но ты делаешь всё возможное чтобы найти корень моих эмоций и помочь мне. это многое значит для меня. я не боюсь тебе показывать свои эмоции. с тобой я такой какой есть, со своими изъянами и недостатками. знай, это всё потому что я очень сильно тебя люблю, потому что я доверяю тебе на все 100% и потому что я открыт с тобой так, как ни с кем другим. учитывая что ты читаешь это в новый год, хочу пожелать нам чтобы этот год стал лучшим в нашей жизни. чтобы наши мечты сбывались и цели достигались. я уверен в новом году мы будем вместе, может нам предстоит пройти какие-то трудности и невзгоды, но я уверен, мы преодолеем все преграды, потому что мы есть друг у друга
любимая моя, ты самый ценный и самый близкий человек что у меня есть, был и будет. я с тобой хоть на край света и для тебя я сверну горы, знай это. я люблю тебя больше всех на этом белом свете. ты мой самый милый и нежный котик ❤️❤️❤️💋💋💋🫂🫂🫂
поздравляю нас с 4 месяцами и с новым 2026 годом 🥳🎉🍾</tg-spoiler>""", parse_mode="HTML")
    elif message.text == "С 14 февраля!!❤️❤️❤️":
        bot.send_message(message.chat.id, """<tg-spoiler>любимая моя, поздравляю нас с 14 февраля и целых 163 днями!! 
первое что хочу сказать, это то что я безумно рад что ты моя девушка, правда. ты заставляешь меня двигаться и развиваться. ты моя опора и ты мой дом. я очень рад что у меня есть такая девушка как ты. ты мой лучик света в этой темной и холодной зиме. ты всегда меня поддержишь и выслушаешь. я очень ценю тебя за это. с тобой я чувствую себя в безопасности, знаю что последнее время я был опечален, но ты ни в коем случае не воспринимай на свой счет. сейчас я активно работаю над всеми своими проблемами чтобы они не затрагивали тебя. я безумно рад что ты у меня очень понимающая. хоть с нового года у нас было не все гладко и мы расстались даже на целых несколько часов, но любовь это в первую очередь про выбор и я вижу твой выбор, и благодарен тебе за то что выбор ты делаешь в пользу наших отношений. так же хочу сказать спасибо за то что ты всегда идёшь на контакт и мы с тобой всегда общаемся и приходим к определенным выводам и продолжаем работу над нашими отношениями. очень надеюсь что все продолжится в том же духе и оглядываясь назад мы восхищено смотрели на весь тут путь, который мы выложили кирпичик за кирпичиком. желаю нам с тобой только процветания как в наших отношениях, так и наших личностей. я невероятно счастлив что ты начала выбираться из тяжелого периода в своей жизни и начинаешь находить в себе силы жить, это на самом деле очень большой анализ самой себя, что дается далеко не каждому! 
я искренне верю что весь наш путь перемен идёт только на пользу. мы сейчас как раз в том периоде жизни когда мы начинаем обретать ответственность и перестаем быть детьми. очень надеюсь что тебе понравится выбор твоей новой специальности в новом вузе, ведь ты уже с большей осознанностью подходишь к этому вопросу. знай, какой бы выбор ты не сделала, я тебя всегда поддержу (хоть могу и подушнить, куда без этого 😁)
я тебя очень сильно люблю и хочу чтобы мы продолжали нашу работу над отношениями и все так же решали проблемы разговорами и компромиссами ❤️❤️❤️💋💋💋
знай, ты у меня самая лучшая, самая красивая, самая умная, самая веселая и самая интересная!!
(поздравление могло получить немного сумбурным, серьезным и непонятным, так что прости за это 😋)</tg-spoiler>""",parse_mode="HTML")


bot.polling(non_stop=True)
