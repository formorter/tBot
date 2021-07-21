from .all_updates import AllUpdatesChek
from loader import dp

if __name__ == "middlewares":
    dp.middleware.setup(AllUpdatesChek())