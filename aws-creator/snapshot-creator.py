import boto3
import click

session = boto3.Session()
session.resource('ec2')

def list_instances():
    ec2s = session.resource('ec2')
    for ec2 in ec2s.instances.all():
        if ec2.tags is not None:
            na = [name for name in ec2.tags if name['Key'] == "Name" and "ssi" in name['Value']]
            if len(na) > 0:
                print("EC2: " + str(na[0]['Value']) + " " + str(ec2.state))

                if ec2.state['Name'] == 'stopped':
                    ec2.start()
                    print("Starting... ")
                else:
                    ec2.stop()
                    print("Stopping... ")


if __name__ == "__main__":
    #print(sys.argv)
    list_instances()