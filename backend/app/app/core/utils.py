from typing_extensions import AsyncIterator


async def read_bytes(generator: AsyncIterator[bytes]) -> bytes:
    body = b""
    async for data in generator:
        body += data
    return body