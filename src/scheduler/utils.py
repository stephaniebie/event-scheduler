def parse_object(item, attribute: str | None):
    """
    Parses the attribute of the object.

    Parameters
    ----------
    item
        The object to be parsed if an attribute exists
    attribute: str | None
        The particular attribute of the object to be parsed

    Returns
    -------
    The object itself or an attribute of the object
    """
    if attribute is None:
        return item
    return vars(item).get(attribute, None)
