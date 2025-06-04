def to_json(self, attrs=None):
    """
    Return a dictionary representation of the Student instance.
    If attrs is a list of strings, only those attributes are returned.
    """
    if (isinstance(attrs, list) and
            all(isinstance(attr, str) for attr in attrs)):
        return {
            k: getattr(self, k)
            for k in attrs
            if hasattr(self, k)
        }
    return self.__dict__
