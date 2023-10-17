#!/usr/bin/env python3
"""
This module lists all documents
"""
import pymongo


def list_all(mongo_collection):
    """
    lists all documents in a collections
    """
    return list(mongo_collection.find())
