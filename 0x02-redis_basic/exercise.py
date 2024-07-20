#!/usr/bin/env python3
""" Cache Class """
import redis
import uuid
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, None]:
        """
        Retrieve data from Redis using the provided key.
        If fn is provided, apply the conversion functionto the data.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """
        Retrieve data as a UTF-8 string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieve data as an integer.
        """
        return self.get(key, fn=int)

    # Define the count_calls decorator
    def count_calls(method: Callable) -> Callable:
        @wraps(method)  # Use wraps to preserve original function info
        def wrapper(self, *args, **kwargs):
            method_name = method.__qualname__  # Get qualified method name
            count_key = f"calls:{method_name}"  # Create a key for counting
            self._redis.incr(count_key)  # Increment the count
            return method(self, *args, **kwargs)  # Call the original

        return wrapper

    # Apply the decorator to Cache.store
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis and return the generated key.
        """
        key = str(uuid.uuid4())  # Generate a random key
        self._redis.set(key, data)
        return key
