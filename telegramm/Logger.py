import logging


class BotLogger: 				# тупой логгер
    logger = logging.getLogger()
    logger.setLevel('INFO')
    logging.basicConfig(level='INFO')

    def info_logg(self, message):
        self.logger.info(f'{message}')
