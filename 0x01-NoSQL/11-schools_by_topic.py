def schools_by_topic(mongo_collection, topic):
    """
    Retrieves a list of schools with the specified topic.

    Args:
        mongo_collection: A PyMongo collection object.
        topic (str): The topic to search for.

    Returns:
        A list of school documents matching the topic.
    """
    return list(mongo_collection.find({"topics": topic}))
