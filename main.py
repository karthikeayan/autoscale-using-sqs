import boto3
from queuemodule import QueueDetails
from core import Core
from autoscale import Scale

if __name__ == "__main__":
    sqs = boto3.resource('sqs')
    autoscaling = boto3.client('autoscaling')
    
    queue = QueueDetails(sqs, 'https://queue.amazonaws.com/291890047404/test')
    message_count = queue.get_message_count()
    instance_count_desired = Core().calculate_instance_count(message_count)
    Scale(autoscaling, 'AutoScalingGroupName').set_desired_capacity(instance_count_desired)
