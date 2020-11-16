import time
import os

def configure_aws():
    print("*** configure the AWS ***")
    os.system("aws configure")
    input("\t\t Press Enter to Continue")


def key_pair():
    key = input("Create a new key name: ")
    os.system("aws ec2 create-key-pair --key-name {}".format(key))
    input("\n\n Press Enter to Continue")


def ec2():
    while True:
        os.system("clear")
        print("\n\n")
        print("""
        press 1: To describe EC2 instance
        press 2: To launch EC2 instance
        press 3: To start EC2 instance
        press 4: To stop EC2 instance
        press 5: To terminate EC2 instance
        press 6: Return to menu
        """)

        i = int(input("Enter your choice: "))
        print(i)
        
        if i == 1:
            describe_ec2()
        elif i == 2:
            launch_ec2()
        elif i == 3:
            start_ec2()
        elif i == 4:
            stop_ec2()
        elif i == 5:
            terminate_ec2()
        elif i == 6:
            return
        else:
            print("\n Your Option is Invalid, Press Enter to Continue")


def s3():
    while True:
        os.system("clear")
        print("\n\n")
        print("""
        press 1: To create s3 bucket
        press 2: To update the content in s3 bucket
        press 3: To delete s3 bucket
        press 4: To delete object from the bucket
        press 5: Return to menu
        """)
        
        i = int(input("Enter your choice: "))
        print(i)
        if i == 1:
            s3bucket()
        elif i == 2:
            s3content()
        elif i == 3:
            s3delete()
        elif i == 4:
            s3deleteobj()
        elif i == 5:
            return
        else:
            input("\n Your Option is Invalid, Press Enter to Continue")


def ebs():
    while True:
        os.system("clear")
        print("\n\n")
        print("""
        Press 1: To Create EBS storage
        Press 2: To describe EBS
    	Press 3: To attach EBS
    	Press 4: To detach EBS
    	Press 5: To Delete the EBS
    	Press 6: Create a SnapShot of EBS
 	Press 7: Return to menu
    	""")

        i = int(input("Enter ur choice : "))
        print(i)
        if i == 1:
            create_ebs()
        elif i == 2:
            describe_ebs()
        elif i == 3:
    	    attach_ebs()
        elif i == 4:
    	    detach_ebs()
        elif i == 5:
    	    delete_ebs()
        elif i == 6:
    	    create_snapshot()
        elif i == 7:
    	    return
        else:
            input("\n Your Option is Invalid, Press Enter to Continue")


def sg():
    while True:
        os.system("clear")
        print("\n\n")
        print("""
    	Press 1: To create Security group
    	Press 2: To describe Security group
    	Press 3: To add ingress to security group
    	Press 4: To update egress to security group
    	Press 5: To delete security group
    	Press 6: Return to menu
    	Press 7: To exit
    	""")

        
        i = int(input("Enter ur choice : "))
        print(i)
        if i == 1:
            create_sg()
        elif i == 2:
    	    describe_sg()
        elif i == 3:
    	    ingress()
        elif i == 4:
    	    egress()
        elif i == 5:
    	    delete_sg()
        elif i == 6:
            return
        elif i == 7:
            exit()
        else:
            input("\n Your Option is Invalid, Press Enter to Continue")

# EC2


def launch_ec2():
    ami = input("Enter the AMI ID: ")
    ins = input("Enter instance type: ")
    noi = int(input("Enter the number of instance you want to launch: "))
    sub = input("Enter the subnet ID: ")
    sg = input(" Enter the security group: ")
    key = input("Enter your key name: ")
    os.system("aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group-ids {} --key-name {}".format(ami , ins , noi , sub , sg , key))
    input("\n\n Press Enter to continue")


def describe_ec2():
    os.system("aws ec2 describe-instances")
    input("\n\n Press Enter to Continue")


def start_ec2():
    a = input("Enter your AMI ID: ")
    os.system("aws ec2 start-instances --instance-ids {}".format(a))
    input("\n\n Press Enter to Continue")


def stop_ec2():
    a = input("Enter your AMI ID: ")
    os.system("aws ec2 stop-instances --instance-ids {}".format(a))
    input("\n\n Press Enter to Continue")

def terminate_ec2():
    a = input("Enter your AMI ID: ")
    os.system("aws ec2 terminate-instances --instance-ids {}".format(a))
    input("\n\n Press Enter to Continue")


# EBS


def describe_ebs():
    os.system("aws ec2 describe-volumes")
    input("\n\n Press Enter to Continue")

def create_ebs():
    vt = input("Enter the volume type: ")
    si = input("Enter the volume size: ")
    az = input("Enter the availability zone: ")
    os.system('aws ec2 create-volume --volume-type {} --size {} --availability-zone {}'.format(vt , si , az))
    input("\n\n Press Enter to Continue")


def attach_ebs():
    ids = input("Enter the instance ID: ")
    vol = input("Enter the volume ID: ")
    dn = input("Enter the device name: ")
    os.system('aws ec2 attach-volume --instance-id {} --volume-id {} --device {}'.format(ids , vol , dn))
    input("\n\n Press Enter to Continue")


def detach_ebs():
    vol = input('Enter the volume ID: ')
    os.system('aws ec2 detach-volume --volume-id {}'.format(vol))
    input("\n\n Press Enter To continue")

def delete_ebs():
    vol = input('Enter the volume ID: ')
    os.system('aws ec2 delete-volume --volume-id {}'.format(vol))
    input("\n\n Press Enter To continue")


def create_snapshot():
    vol = input("Enter Volume_ID: ")
    des = input("Enter The Description of This Snapshot: \n")
    os.system(f"aws ec2 create-snapshot --volume-id {vol} --description '{des}'")
    input("\n\n  Press Enter To continue")

# SECURITY GROUP 


def describe_sg():
    i = input('Enter security group ID: ')
    os.system('aws ec2 describe-security-groups --group-ids {}'.format(i))
    input("\n\n Press Enter To continue")

def create_sg():
    sgn = input('Enter security_group_name: ')
    des = input('Add description: ')
    vpc = input("Enter vcp_id: ")
    os.system('aws ec2 create-security-group --group-name {} --description "{}" --vpc-id {}'.format(sgn , des , vpc))
    input("\n\nPress Enter To continue")

def delete_sg():
    sgn = input('Enter the security group ID: ')
    os.system('aws ec2 delete-security-group --group-id {}'.format(sgn))
    input("\n\n Press Enter To continue")


def ingress():
    sg = input('Enter the security group ID: ')
    sn = input('Enter the security group name: ')
    p = input('Enter the protocol: ')
    pn = int(input('Enter the port number: '))
    cidr = input('Enter the cidr block: ')
    os.system('aws ec2 authorize-security-group-ingress --group-id {} --group-name {} --protocol {} --port {} --cidr {}'.format(sg , sn , p , pn , cidr))
    input("\n\nPress Enter To continue")

def egress():
    sg = input('Enter the security group ID: ')
    p = input('Enter the protocol: ')
    pn = int(input('Enter the  port number: '))
    cidr = input('Enter cidr block: ')
    os.system('aws ec2 authorize-security-group-egress --group-id {}  --protocol {} --port {} --cidr {}'.format(sg , p , pn , cidr))
    input("\n\n Press Enter To continue")

# S3


def s3bucket():
    bn = input('Enter the  unique bucket name: ')
    reg = input('Enter region: ')
    os.system('aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}'.format(bn , reg))
    input("\n\n Press Enter To continue")

def s3delete():
    bn = input('Enter the bucket name: ')
    reg = input('Enter the region: ')
    os.system('aws s3api delete-bucket --bucket {} --region {}'.format(bn , reg))
    input("\n\n Press Enter To continue")

def s3content():
    loc = input('Enter the local location: ')
    bn = input('Enter the bucket name: ')
    print("\n\n Upload process initiated ..... \n\n")
    os.system('aws s3 sync "{}" s3://{}'.format(loc , bn))
    time.sleep(10)
    input("\n\n Press Enter To continue")

def s3deleteobj():
    bn = input('Enter the bucket name: ')
    key = input('Enter key or pic: ')
    os.system('aws s3api delete-object --bucket {} --key {}'.format(bn , key))
    input("\n\n Press Enter To continue")


# CLOUD FRONT


def cloudfront():
	n = input('Enter bucket name: ')
	os.system('aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com'.format(n))
	input("\n \nTask Completed, Press Enter To continue")
