import logging


class BotLogger: 				# тупой логгер
    logger = logging.getLogger()
    logger.setLevel('INFO')
    logging.basicConfig(level='INFO')

    def main(self, message):
        self.logger.info(f'{message}')
