def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the specified MOngoDB collection.

    Args:
        mongo_collection: A PyMongo collection object.
        **kwargs: Keyword arguments representing the document attributes.

    Returns:
        The new_id of the inserted document.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
