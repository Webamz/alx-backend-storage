#!/usr/bin/env python3
"""
This module has a function to change school topic
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    updates rows
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
