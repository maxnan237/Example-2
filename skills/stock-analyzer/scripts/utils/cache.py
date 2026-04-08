"""
Cache manager for stock data.
Caches fetched data to reduce API calls during repeated analysis.
"""

import os
import json
import hashlib
import time
import pandas as pd


class CacheManager:
    """Simple file-based cache for stock data."""

    TTL = 3600  # Cache TTL in seconds (1 hour)

    def __init__(self, cache_dir):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)

    def _cache_path(self, key):
        hashed = hashlib.md5(key.encode()).hexdigest()
        return os.path.join(self.cache_dir, f"{hashed}.json")

    def get(self, key):
        """
        Retrieve cached data if it exists and is not expired.

        Returns:
            pandas DataFrame or None
        """
        path = self._cache_path(key)
        if not os.path.exists(path):
            return None

        try:
            with open(path, "r") as f:
                cached = json.load(f)

            if time.time() - cached.get("timestamp", 0) > self.TTL:
                os.remove(path)
                return None

            df = pd.DataFrame(cached["data"])
            if "Date" in df.columns:
                df["Date"] = pd.to_datetime(df["Date"])
                df.set_index("Date", inplace=True)
            return df
        except (json.JSONDecodeError, KeyError, ValueError):
            return None

    def set(self, key, df):
        """
        Cache a DataFrame.

        Args:
            key: Cache key
            df: pandas DataFrame to cache
        """
        path = self._cache_path(key)
        try:
            data = df.reset_index()
            # Convert datetime columns to strings
            for col in data.columns:
                if pd.api.types.is_datetime64_any_dtype(data[col]):
                    data[col] = data[col].astype(str)

            payload = {
                "timestamp": time.time(),
                "data": data.to_dict(orient="records"),
            }
            with open(path, "w") as f:
                json.dump(payload, f)
        except Exception:
            pass

    def clear(self):
        """Remove all cached data."""
        for f in os.listdir(self.cache_dir):
            path = os.path.join(self.cache_dir, f)
            if os.path.isfile(path) and f.endswith(".json"):
                os.remove(path)
