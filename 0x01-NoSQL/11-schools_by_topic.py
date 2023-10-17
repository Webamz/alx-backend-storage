#!/usr/bin/env python3
"""
This module has a function schools_by_topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns lists of schools having a topic
    """
    return list(mongo_collection.find({"topics": topic}))
