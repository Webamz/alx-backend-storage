#!/usr/bin/env python3
""" A script that displays stats about nginx logs
"""
from pymongo import MongoClient
from typing import List


if __name__ == "__main__":
    client: MongoClient = MongoClient('mongodb://127.0.0.1:27017')
    db = client['logs']
    collection = db['nginx']

    total_logs: int = collection.count_documents({})
    print(f"{total_logs} logs")

    http_methods: List[str] = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_stats = {method: collection.count_documents(
        {"method": method}) for method in http_methods}

    print("Methods:")
    for method, count in method_stats.items():
        print(f"\tmethod {method}: {count}")

    status_count: int = collection.count_documents(
            {"method": "GET", "path": "/status"}
            )
    print(f"{status_count} status check")
