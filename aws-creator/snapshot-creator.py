import boto3

if __name__ == "__main__":
    session = boto3.Session()
    session.resource('ec2')
    ec2s = session.resource('ec2')

    for ec2 in ec2s.instances.all():
        print(ec2)