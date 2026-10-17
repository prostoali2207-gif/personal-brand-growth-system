from render import render, phone

def split(title, body, img, w=400, h=820, crop=0, tag=""):
    t = f'<span class="tag">{tag}</span>' if tag else ""
    return f'<div class="split"><div class="txt">{t}<h2>{title}</h2><div class="body">{body}</div></div>{phone(img, w, h, crop)}</div>'

def statement(text, sub=""):
    s = f'<div class="sub" style="margin-top:44px">{sub}</div>' if sub else ""
    return f'<div class="quote"><span class="bar"></span>{text}{s}</div>'

def cta(title, sub):
    return {"html": f'<h2>{title}</h2><div class="sub">{sub}</div><div class="cta">Написать в директ →</div>', "center": True}

C = {}

# 1. ZAINAB — лендинг частного специалиста
C["01-landing-specialist"] = [
    {"html": '<h1>Сайт частного специалиста должен сразу ответить на <span class="acc">3 вопроса</span></h1><div class="sub">Разбор на примере лендинга преподавателя языков</div>' + phone("ls-hero.png", 470, 690)},
    {"html": split('Вопрос 1.<br>Чем ты мне <span class="acc">поможешь?</span>', "Не «курсы английского», а результат человеческими словами: не учить язык, а говорить на нём.", "ls-hero.png", tag="первый экран")},
    {"html": split('Вопрос 2.<br>Это точно <span class="acc">для меня?</span>', "Взрослым — для работы и переезда. Детям — для школы и экзаменов. Человек находит себя за секунду.", "ls-audience.png", crop=0, tag="для кого")},
    {"html": split('Вопрос 3.<br>Почему тебе <span class="acc">можно верить?</span>', "Образование, опыт и живые отзывы учеников и родителей — без глянца и без «лучший преподаватель города».", "ls-teacher.png", crop=0, tag="доверие")},
    {"html": split('И одна понятная <span class="acc">кнопка</span>', "«Записаться на пробный урок». Не пять способов связи, а один шаг, который легко сделать.", "ls-hero.png", tag="действие")},
    {"html": statement('Частный специалист продаёт не услугу, а себя.', 'Сайт должен звучать как человек, а не как каталог.'), "dark": True},
    (cta('Нужен лендинг для вашего дела?', 'Делаю лендинги для малого бизнеса и специалистов в ОАЭ — с заявками прямо в WhatsApp.')),
]

# 2. FleetDesk — клиент сам заполняет анкету
C["02-self-registration"] = [
    {"html": '<h1>Анкету заполняет <span class="acc">сам клиент</span> — с телефона</h1><div class="sub">Как устроена регистрация клиента в системе для автопроката</div>' + phone("client-register-redesign-step-2-mobile.png", 470, 720, 0)},
    {"html": split('Шаг 1.<br>Личные <span class="acc">данные</span>', "Имя как в документе, телефон, дата рождения, гражданство. Менеджер ничего не перепечатывает.", "client-register-redesign-step-1-mobile.png", crop=20)},
    {"html": split('Шаг 2.<br>Резидент или <span class="acc">турист?</span>', "От одного ответа зависит, какие документы попросит система дальше.", "client-register-redesign-step-2-mobile.png", crop=40)},
    {"html": split('Шаг 3.<br><span class="acc">Документы</span>', "Резиденту — Emirates ID и права. Туристу — паспорт и права. Можно догрузить позже — но до выдачи машины их могут попросить.", "client-register-fixed-step-3-resident-mobile.png", crop=40)},
    {"html": split('Шаг 4.<br>Проверка перед <span class="acc">отправкой</span>', "Клиент видит всё, что ввёл, и может исправить. Менеджер получает уже готовую карточку.", "client-register-fixed-step-4-resident-mobile.png", crop=40)},
    {"html": statement('Лучшая форма — та, где каждый заполняет своё.', 'Клиент — свои данные. Менеджер — только проверяет.'), "dark": True},
    (cta('Тот же принцип — для любого бизнеса', 'Клиника, сервис, агентство недвижимости: анкету заполняет клиент, а вы получаете готовые данные. Напишите — разберём ваш процесс.')),
]

# 3. Дубль оплаты
table_dup = '''<div class="table"><div class="row h"><span>Дата</span><span>Статья</span><span>Сумма</span></div>
<div class="row"><span>14.10</span><span>Оплата клиента</span><span>3 000</span></div>
<div class="row bad"><span>14.10</span><span>Оплата клиента</span><span>3 000</span></div></div>
<div class="cap" style="text-align:left;margin-top:18px">Пример для наглядности</div>'''
C["03-double-payment"] = [
    {"html": '<h1>Одна оплата записалась в учёт <span class="acc">дважды</span></h1><div class="sub">Обычная ситуация, а потом касса «не сходится» и все ищут, кто ошибся.</div>' + table_dup},
    {"html": '<span class="tag">как это бывает</span><h2>Нажал «Отправить». Ничего не произошло. <span class="acc">Нажал ещё раз.</span></h2><div class="body">Интернет подвис на секунду — а в таблице уже две одинаковые строки. Деньги пришли один раз, в учёте — два.</div>', "center": True},
    {"html": '<span class="tag">что я сделал</span><h2>У каждой операции — свой <span class="acc">номер</span></h2><div class="body">Пришла та же операция с тем же номером — система не создаёт новую строку, а возвращает уже записанную.</div><div class="card"><div class="r"><span>Оплата клиента · 3 000</span><span class="pill">записано</span></div><div class="mono">операция №A7F3</div></div><div class="card" style="margin-top:24px"><div class="r"><span>Повтор той же отправки</span><span class="pill">уже есть — без дубля</span></div><div class="mono">операция №A7F3</div></div>'},
    {"html": '<span class="tag">и ещё</span><h2>Совпали дата, счёт, сумма и комментарий — <span class="acc">предупреждение</span></h2><div class="body">Система не пишет молча, а показывает: «такая операция уже есть в строке №…».</div><div class="card"><div class="r"><span>14.10 · Оплата клиента · 3 000</span><span class="pill w">внимание</span></div><div>Такая операция уже есть в строке 52. Это отдельный платёж?</div></div>'},
    {"html": '<span class="tag">а если правда две оплаты?</span><h2>Записывается — <span class="acc">с пояснением</span></h2><div class="body">Настоящая вторая оплата не блокируется. Нужно просто указать, что это отдельный платёж.</div>', "center": True},
    {"html": statement('Ошибки в учёте почти всегда не про людей.', 'А про систему, которая позволяет ошибиться.'), "dark": True},
    (cta('Где у вас всё держится на «не забыть»?', 'Автоматизирую учёт, заявки и рутину для малого бизнеса — в тех программах, которыми вы уже пользуетесь.')),
]

# 4. Сначала покажем деталь
C["04-show-before-buy"] = [
    {"html": '<h1>Заказывать запчасть из другой страны <span class="acc">страшно</span></h1><div class="sub">Заплатишь — а придёт не то. Как сайт снимает этот страх.</div>' + phone("ap-trust.png", 470, 690, 0)},
    {"html": split('Сначала <span class="acc">показываем</span> деталь', "Перед покупкой клиенту отправляют фото и видео: состояние, маркировку, заметные особенности.", "ap-trust.png", crop=0, tag="шаг 1")},
    {"html": '<span class="tag">шаг 2</span><h2>Клиент <span class="acc">подтверждает</span> — и только потом выкуп</h2><div class="body">Решение принимает человек, который видел деталь своими глазами. Никаких «доверьтесь нам».</div>', "center": True},
    {"html": split('А название детали знать <span class="acc">не обязательно</span>', "Фото, номер или описание — любое одно. Менеджер начнёт подбор с того, что есть.", "ap-gap.png", crop=0, tag="заявка")},
    {"html": statement('Хороший сайт не уговаривает.', 'Он снимает страх, из-за которого человек не пишет.'), "dark": True},
    (cta('Чего боится ваш клиент?', 'Сделаю сайт, который отвечает на этот страх — для любого бизнеса: сервис, клиника, недвижимость, товары.')),
]

# 5. Предложение
C["05-offer"] = [
    {"html": '<span class="tag">предложение</span><h1>Лендинг, который приводит заявки <span class="acc">в WhatsApp</span></h1><div class="price">7 дней</div><div class="sub">От ваших материалов до готовой страницы.</div>'},
    {"html": '<h2>Что входит</h2><div class="list">' + "".join(f'<div class="li"><span class="num">{i}</span><span>{t}</span></div>' for i, t in enumerate([
        "Страница под ваш бизнес: кто вы, что предлагаете, почему вам можно верить",
        "Удобно на телефоне — оттуда приходит большинство клиентов",
        "Кнопка WhatsApp и форма заявки прямо вам в WhatsApp",
        "Тексты пишу я — от вас информация, логотип и фото",
        "2 круга правок и помощь с доменом"], 1)) + '</div>'},
    {"html": '<h2>Как работаем</h2><div class="list">' + "".join(f'<div class="li"><span class="num">{i}</span><span>{t}</span></div>' for i, t in enumerate([
        "Пишете в директ или WhatsApp: чем занимается бизнес",
        "Присылаете материалы: логотип, фото, контакты",
        "Через 7 дней — готовый лендинг, вносим правки",
        "Подключаем домен — и принимаете заявки"], 1)) + '</div>'},
    {"html": '<h2>Примеры работ</h2><div class="thumbs"><div>' + phone("ls-hero.png", 400, 760) + '<div class="cap">Преподаватель языков</div></div><div>' + phone("ap-hero.png", 400, 760) + '<div class="cap">Автозапчасти</div></div></div>'},
    {"html": '<span class="tag">цена</span><div class="price">2 500 AED</div><div class="sub">Английский, русский или арабский — за доплату.<br>Поддержка и мелкие правки — 200 AED в месяц, по желанию.</div><div class="cta">Написать в директ →</div>'},
]

if __name__ == "__main__":
    import sys
    only = sys.argv[1:] or list(C)
    for k in only:
        print(render(k, C[k]))
