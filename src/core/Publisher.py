class Publisher:
    def __init__(self, events):
        # maps event names to subscribers
        # str -> dict
        self.events = {event: dict()
                       for event in events}
    def get_subscribers(self, event):
        return self.events[event]
    def attatch(self, event, who, callback=None):
        if callback == None:
            callback = getattr(who, 'update')
        self.get_subscribers(event)[who] = callback
    def detach(self, event, who):
        del self.get_subscribers(event)[who]
    def notify(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)
