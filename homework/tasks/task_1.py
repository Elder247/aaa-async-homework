import asyncio
from asyncio import Task
from typing import Callable, Coroutine, Any


async def await_my_func(f: Callable[..., Coroutine] | Task | Coroutine) -> Any:
    # На вход приходит одна из стадий жизненного цикла корутины, необходимо вернуть результат
    # её выполнения.

    if isinstance(f, Callable):
        task = asyncio.create_task(f())
        return await task
    elif isinstance(f, Task):
        return await f
    elif isinstance(f, Coroutine):
        task = asyncio.create_task(f)
        return await task
    else:
        raise ValueError('invalid argument')
