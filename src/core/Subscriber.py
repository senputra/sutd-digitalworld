class Subscriber:
    """ An implementation for a subscriber class

    :param name: A string, The subscriber's name
    """
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))
