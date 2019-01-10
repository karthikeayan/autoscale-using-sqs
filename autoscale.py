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