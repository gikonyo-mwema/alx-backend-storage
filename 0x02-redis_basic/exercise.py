#!/usr/bin/python3
""" Cache Class """
import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class using Redis
    """

    def __init__(self) -> None:
        """
        Initialize the cache class with Redis client instance.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis and return generated key.
        """
        key = str(uuid.uuid4())  # Generate a random key
        self._redis.set(key, data)
        return key
