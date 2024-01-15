from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.gzip import GZipMiddleware
from fastapi_utils.tasks import repeat_every

import uvicorn

from configs.config import CONFIG
from helpers.connection_checker import overload_checker


@repeat_every(seconds=5)
def do_check_overload():
    overload_checker.check_overload()


@asynccontextmanager
async def lifespan(app):
    print('Welcome to shop-dev app')
    await do_check_overload()
    yield
    print('Existed app')


app = FastAPI(lifespan=lifespan)


# noinspection PyTypeChecker
app.add_middleware(GZipMiddleware, minimum_size=1000)
# TODO: [Section 1][Section 2] Improve security by adding middlewares (like morgan, helmet in Nodejs)


@app.get('/')
async def root():
    data = {'message': 'Hello World'}

    return JSONResponse(
        content=data,
    )


def main():
    uvicorn.run(app, host=CONFIG['app']['host'], port=CONFIG['app']['port'])


if __name__ == '__main__':
    main()
