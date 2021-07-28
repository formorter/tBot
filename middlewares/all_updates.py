import logging

from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types


class AllUpdatesChek(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        logging.info("____________[Тут новый апдейт]____________")
        logging.info("1. Pre Process Update")
        #logging.info("Следующая точка: Process Update")
        data['middleware_data'] = "Это пойдёт до on_post_process_update"

    async def on_process_update(self, update: types.Update, data: dict):
        logging.info(f"2.Process Update{data=}")
        # logging.info("Следующая точка: Pre Process Message ")

    async def on_pre_process_message(self, message: types.Message, data: dict):
        logging.info(f"3. Pre Process Message, {data=}")
        # logging.info("Следующая точка: Filters")
        data['middleware_data'] = 'Это пройдет в on_process_message'

    """тут фильтры"""

    async def on_process_message(self, message: types.Message, data: dict):
        logging.info(f"5. Process Message")
        # logging.info("Следующая точка: Handler")
        data["middleware_data"] = 'Это попадет в Handler'

    """"хендлер"""

    async def on_post_process_message(self, message: types.Message, data_from_handler: list, data: dict):
        logging.info(f"7. Post Process Message {data=}, {data_from_handler=}")
        # logging.info("Следующая точка Post Process Update")

    async def on_post_process_update(self, update: types.Update, data_from_handler: list, data: dict):
        logging.info(f"8. Post Process Update {data=}, {data_from_handler=}")
        logging.info("_____________[Конец апдейта]_____________")

