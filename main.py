import boto3
import ConfigParser
import logging
from sqs_auto_scale.queuemodule import QueueDetails
from sqs_auto_scale.core import Core
from sqs_auto_scale.autoscale import Scale

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
    handlers=[
        logging.StreamHandler()
    ])
logger = logging.getLogger()

configParser = ConfigParser.RawConfigParser()
configParser.read('app.config')
configSection = 'sqs'

def lambda_handler(event, context):
    group_name = configParser.get(configSection, 'asg_name')
    queue_url = configParser.get(configSection, 'queue_url')
    message_per_instance = int(configParser.get(configSection, 'message_per_instance'))

    logger.info("Auto Scaling Group Name: {0}".format(group_name))
    logger.info("SQS Queue URL: {0}".format(queue_url))
    logger.info("Number of messages one EC2 instance can handle: {0}".format(message_per_instance))

    sqs = boto3.resource('sqs')
    autoscaling = boto3.client('autoscaling')
    
    queue = QueueDetails(sqs, queue_url)
    message_count = queue.get_message_count()
    instance_count_actual = Scale(autoscaling, group_name).get_instance_count()
    instance_count_desired = Core(message_per_instance).calculate_instance_count(message_count, instance_count_actual)
    Scale(autoscaling, group_name).set_desired_capacity(instance_count_desired)
    return True

if __name__ == '__main__':
    lambda_handler('x', 'y')