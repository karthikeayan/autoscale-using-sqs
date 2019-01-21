import logging
logger = logging.getLogger(__name__)

class Core:
    def __init__(self, instance_capacity):
        self.instance_capacity = instance_capacity

    def calculate_instance_count(self, message_count, instance_count_actual):
        if (message_count / instance_count_actual) > self.instance_capacity:
            logger.info("Calculated desired instance count: {}".format(message_count / self.instance_capacity))
            return int(message_count / self.instance_capacity)
        else:
            logger.info("Calculated desired instance count: {}".format(message_count / self.instance_capacity))
            return instance_count_actual