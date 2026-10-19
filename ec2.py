import boto3
client = boto3.client('ec2')
response = client.run_instances(
    ImageId='ami-0bdc7d025135d7b49',
    InstanceType = 't2.micro',
    MinCount = 1,
    MaxCount = 1


)
