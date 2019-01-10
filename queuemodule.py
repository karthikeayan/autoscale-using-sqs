class QueueDetails:
    def __init__(self, client, queue_url):
        self.client = client
        self.queue_url = queue_url
        self.queue = self.client.Queue(self.queue_url)

    def get_message_count(self):
        self.attributes = self.queue.attributes
        self.message_count = int(self.attributes['ApproximateNumberOfMessages']) + \
            int(self.attributes['ApproximateNumberOfMessagesNotVisible'])

        return self.message_count