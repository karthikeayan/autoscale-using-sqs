import logging
logger = logging.getLogger(__name__)

class Scale:
    def __init__(self, client, autoscale_group):
        self.client = client
        self.autoscale_group = autoscale_group

    def set_desired_capacity(self, dc):
        self.client.set_desired_capacity(
            AutoScalingGroupName=self.autoscale_group,
            DesiredCapacity=dc,
            HonorCooldown=True
        )

    def get_instance_count(self):
        instances = self.client.describe_auto_scaling_groups(AutoScalingGroupNames=[self.autoscale_group])
        logger.info("Found current instance count: {}".format(len(instances['AutoScalingGroups'][0]['Instances'])))
        return len(instances['AutoScalingGroups'][0]['Instances'])