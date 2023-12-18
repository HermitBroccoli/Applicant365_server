import sys
from typing import TypedDict
from subprocess import run


class Colors(TypedDict):
		error: str
		success: str
		warning: str
		info: str
		highlight: str
		default: str
	
COLOR_BG: Colors = {
	"error": "\033[91m",       # Красный для ошибок
	"success": "\033[92m",     # Зелёный для успешных операций
	"warning": "\033[93m",     # Жёлтый для предупреждений
	"info": "\033[94m",        # Синий для информационных сообщений
	"highlight": "\033[95m",   # Пурпурный для выделения
	"default": "\033[0m"       # Сброс настроек цвета
}

def get_venv():
	if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
		# print(COLOR_BG['success'] + "Вы находитесь в виртуальном окружении." + COLOR_BG['default'])
		return True
	else:
		print(COLOR_BG['error'] + "Вы НЕ находитесь в виртуальном окружении" + COLOR_BG['default'])
		print(COLOR_BG['info'] + "Сейчас будет создана виртуальная среда!" + COLOR_BG['default'])
		if sys.platform.startswith('win'):
			run("py -m venv venv", shell=True)
			print(COLOR_BG['success'] + "Виртуальная среда успешно создана!" + COLOR_BG['default'])
		elif sys.platform.startswith('startswith'):
			run("python3 -m venv venv", shell=True)
			print(COLOR_BG['success'] + "Виртуальная среда успешно создана!" + "\nПоДождите какое-то время")
		