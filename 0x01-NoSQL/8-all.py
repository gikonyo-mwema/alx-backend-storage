def list_all(mongo_collection):
    """
    Lists all documents in the specified MongoDB collection

    Args:
        mongo_collection: A PyMongo collectioin object.

    Returns:
        A list of documents (empty list if no documents found).
    """
    return list(mongo_collection.find())
