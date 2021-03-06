# 0. О программе

  Eagle-owl - приложение-бот для telegram, имитирует "Уханье"-"угуканье"-"подтверждение" филина.

# 1. Структура репозитория

    \eagle-owl - каталог, содержащий в себе основной код бота;  
    \ - корневой каталог, содержит в себе скрипт start.bat;  

# 2. Системные требования
   
	* ОС Windows 7 или выше;  
	* python 3.6 или выше;  
	* pyTelegramBotAPI 0.3.0 или выше.  

# 3. Установка программы

   Для установки программы необходимо установить python (если таковой не был установлен). Затем при помощи утилиты pip необходимо установить pyTelegramBotAPI( `pip install pyTelegramBotAPI` ).

# 4. Настройка программы

   Для нормальной работы программы необходимо:
    - ввести TOKEN бота (идентификационный знак программы);  
    - ввести адрес прокси (при необходимости);  

## 4.1 TOKEN-бота

   Для получения TOKEN-а telegram-бота необходимо:  
    1. Написать в мессанджере telegram боту BotFather команду `/newbot`.  
    2. Ввести имя бота (name).  
    3. Ввести пользовательское имя бота (логин) (username).  
    4. Имя бота (name) может быть любым, но пользовательское имя должно быть уникальным. Если введенное пользовательское имя уже имеется в telegram, BotFather предложит Вам написать другое пользовательское имя.  
    5. После получения TOKEN-а бота его необходимо вписать в файле \eagle-owl\config.py в поле TOKEN = '[ваш токен]' (без квадратных скобочек [], конечно).  

## 4.2 Настройка прокси

   Если необходимо обеспечить работу бота через прокси, то для этого необходимо ввести адрес прокси в формате `"https://xxx.xxx.xxx.xxx.:yyyy"`, где xxx.xxx.xxx.xxx - IP-адрес прокси-сервера, yyyy - порт прокси-сервера.  
    Или можно использовать формат `"https://login:pass@xxx.xxx.xxx.xxx:yyy"`, где login - имя пользователя для подклчения к прокси-серверу, pass - пароль для подключения к прокси-серверу, xxx.xxx.xxx.xxx - IP-адрес прокси-сервера, yyyy - порт прокси-сервера. Вместо https допускается также использовать протоколы socks5. Эти данные также необходимо ввести в файл \eagle-owl\config.py в поле PROXY = '[ваш прокси]' (без квадратных скобочек, конечно)

# 5. Инструкция по управлению

   Для запуска бота необходимо запустить скрипт start.bat.
   Для остановки работы бота необходимо ввести Ctrl-C или закрыть окно.  
   ВНИМАНИЕ! Если в переменной окружения PATH отсутствует каталог, содержащий python, то бот не запустится.
   Найдите бота в мессенджере telegram и отправьте ему сообщение или команду.
   Бот обладает следующими командами:
    1. /start - войти в режим "филина";  
    2. /stop - выйти из режима "филина";  
    3. /send_location - выдать координату 39.032487, 125.752385.

## 5.1 Режим "филина"

   При переходе в режим "филина" бот присылает анекдот про двух говорящих птиц. В режиме "филина" филин говорит раз в две минуты "Угу". Если вы попросите филина что-то подтвердить, то он ответит "Подтверждаю". После выхода из режима "филина" бот приводит цитату из "Сказа про Федота-стрельца".
