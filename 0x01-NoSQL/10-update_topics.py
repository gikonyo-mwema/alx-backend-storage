#!/usr/bin/env python3
""" Updates """


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of all school documents with the specified name.

    Args:
        mongo_collection: A PyMongo collection object.
        name (str): The school name to update.
        topics (list of str): The list of topics approached in the school.

    Return:
        None
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
