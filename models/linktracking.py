class LinkTracking:
    def __init__(self):
        self.message = ''
        self.error = False
        self.next = False
        self.page = ''

    def init(self):
        self.message = ''
        self.error = False
        self.next = False

    def __str__(self):
        return (
            f'error: {self.error}, page: {self.page}'
            f'message:{self.message}')
