import logging
logger = logging.getLogger(__name__)

class QueueDetails:
    def __init__(self, client, queue_url):
        self.client = client
        self.queue_url = queue_url
        self.queue = self.client.Queue(self.queue_url)

    def get_message_count(self):
        self.attributes = self.queue.attributes
        self.message_count = int(self.attributes['ApproximateNumberOfMessages']) + \
            int(self.attributes['ApproximateNumberOfMessagesNotVisible'])

        logger.info('Messages in the Queue: {}'.format(self.message_count))
        return self.message_count
