
greetings = '''Царь позвал к себе Иванушку-дурака и говорит:
– Если завтра не принесешь двух говорящих птиц – голову срублю.
Иван принес филина и воробья. Царь говорит:
– Ну, пусть что-нибудь скажут.
Иван спрашивает:
– Воробей, почем раньше водка в магазине была?
Воробей:
– Чирик.
Иван филину:
– А ты, филин, подтверди.
Филин:
– Подтверждаю.'''

farawell = '''Ну а чтоб не одичали,
  Вот вам личный мой баян.
  Правда, он – моя вина!
   - Не играет ни рожна,
  Но какая-никакая,
  А культура вам нужна!'''

#состояние бота 0 - неопределенное
# 1 - запущен
# 2 - остановлен

bot_state = 0

def start():
	return greetings


def stop():
	return farawell