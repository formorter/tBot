import logging


class BotLogger:
	"""
	Тупой логгер
	Выводит информацию о том, что бот запущен
	"""
	logger = logging.getLogger()
	logger.setLevel('INFO') 
	logging.basicConfig(level ='INFO')


	def main(self):
		self.logger.info(f'Бот запущен, приятного пользования')

log = BotLogger()
log.main()
