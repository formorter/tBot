from loader import dp
from .all_updates import AllUpdatesChek
from .throttling import ThrottlingMiddleware

if __name__ == "middlewares":
    dp.middleware.setup(AllUpdatesChek())
    dp.middleware.setup(ThrottlingMiddleware())
