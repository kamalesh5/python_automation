import os
import subprocess
import pandas
import time
from sklearn.linear_model import LinearRegression
from AWS import awsauto

os.system("tput setaf 6")
print("\t\t\t *********************")
print("\t\t\t WELCOME TO MY CONSOLE")
print("\t\t\t *********************")
os.system("tput setaf 7")

while True:
    choice = int(input(""" Select the technologies you want to configure:

    Press 1: To configure YUM
    Press 2: To configure HTTPD Webserver
    Press 3: To configure Docker
    Press 4: To use AWS
    Press 5: To configure Hadoop
    Press 6: To create partition
    Press 7: To Create LVM
    Press 8: Population Prediction 
    Press 9: Exit

    ENTER YOUR CHOICE: """))

    if choice == 1:
        
        def yum():

            os.system("tput setaf 3")
            print("\t\t\t YUM CONFIGURATION ")
            print("\t\t\t ***************** ")
            os.system("tput setaf 7")
            subprocess.getstatusoutput("echo '[dvd1] \nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream \ngpgcheck=0 \n\n[dvd2] \nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS \ngpgcheck=0' > myyum.repo | mv myyum.repo  /etc/yum.repos.d/")
            print("myyum.repo is the configured repository")
            os.system("yum repolist")
            input("press Enter to continue")
            os.system("clear")
        yum()

    elif choice == 2:

        os.system("tput setaf 3")
        print("\t\t\t HTTPD CONFIGURATION ")
        print("\t\t\t ******************* ")
        os.system("tput setaf 7")


        hchoice = int(input("""what do you want from HTTPD: ?

        Press 1: To Install HTTPD Webserver
        Press 2: To Start HTTPD
        Press 3: To see HTTPD Status
        Press 4: To stop HTTPD
        Press 5: To uninstall HTTPD
        Press 6: Exit

        Enter your choice: """))

        if hchoice == 1:
            os.system("yum install httpd")
            print("HTTPD successfully Installed")
            input("Press Enter to continue")

        elif hchoice == 2:
            os.system("systemctl start httpd")
            print("HTTPD started successfully")
            input("Press Enter to continue")

        elif hchoice == 3:
            os.system("systemctl status httpd")
            input("Press Enter to continue")

        elif hchoice == 4:
            os.system("systemctl stop httpd")
            print("HTTPD stopped successfully")
            input("Press Enter to continue")

        elif hchoice == 5:
            os.system("yum remove httpd")
            print("HTTPD uninstalled successfully")
            input("Press Enter to continue")
            os.system("clear")

        elif hchoice == 6:
            break

        else:
            print("Invalid input! Please try again")


    elif choice == 3:

        os.system("tput setaf 3")
        print("\t\t\t DOCKER CONFIGURATION ")
        print("\t\t\t ******************** ")
        os.system("tput setaf 7")

        dchoice = int(input(""" What do you want from Docker?

        Press 1: To Install Docker
        Press 2: To Start Docker service
        Press 3: To see the Docker Status
        Press 4: To download Docker image from Docker hub
        Press 5: To see list of Docker images available in your OS
        Press 6: To Install Docker Image
        Press 7: To boot OS 
        Press 8: To Terminate Docker image
        Press 9: Exit

        ENTER YOUR CHOICE: """))

        if dchoice == 1:
            os.system("dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo")
            os.system("yum install docker-ce --nobest")
            input("Press Enter to Continue")

        if dchoice == 2:
            os.system("systemctl start docker")
            input("Press Enter to Continue")

        if dchoice == 3:
            os.system("systemctl status docker")
            input("Press Enter to Continue")

        if dchoice == 4:
            img = input("Enter the name of image which you want to download (for eg: ubuntu:20.04): ")
            os.system("docker pull {}".format(img))
            input("Press Enter to Continue")

        if dchoice == 5:
            os.system("docker images")
            input("Press Enter to Continue")

        if dchoice == 6:
            img = input("Enter the name of the Docker image(for eg: ubuntu:20.04): ")
            urname = input("Please give name to thet image: ")
            os.system("docker run -it -name {} {}".format(urname,img))
            input("Press Enter to Continue")

        if dchoice == 7:
            os.system("systemctl start docker")
            id = input("Enter name of OS: ")
            os.system("docker start {}".format(id))
            os.system("docker attach {}".format(id))
            input("Press Enter to continue")

        if dchoice == 8:
            id = input("Enter name of OS: ")
            os.system("docker rm {}".format(id))
            input("Press Enter to Continue")
            os.system("clear")

        elif dchoice == 9:
            break

    
    elif choice == 4:

        os.system("tput setaf 3")
        print("\t\t\t AWS CONFIGURATION ")
        print("\t\t\t ***************** ")
        os.system("tput setaf 7")

        flag = False
        while True:
            os.system("clear")
            print("""
            Press 0: To configure AWS
            Press 1: To create a Key Pair
            Press 2: To configure EC2 instance
            Press 3: To configure EBS
            Press 4: To configure Security Group
            Press 5: To configure S3 bucket
            Press 6: To configure CloudFront
            Press 7: To Return to Main Menu
            Press 8: To Exit
            """)

            i = int(input("Enter your choice : "))
            print(i)
            if i == 0:
                awsauto.configure_aws()
            elif i == 1:
                awsauto.key_pair()
            elif i == 2:
                awsauto.ec2()
            elif i == 3:
                awsauto.ebs()
            elif i == 4:
                awsauto.sg()
            elif i == 5:
                awsauto.s3()
            elif i == 6:
                awsauto.cloudfront()
            elif i == 7:
                break
            elif i == 8:
                exit()
            else:
                input("Invalid Option, Press Enter")
                



    elif choice == 5:

        os.system("tput setaf 3")
        print("\t\t\t HADOOP CONFIGURATION ")
        print("\t\t\t ******************** ")
        os.system("tput setaf 7")


        hchoice = int(input("""What do you want from Hadoop?

        Press 1: To create Hadoop Name Node
        Press 2: To create Hadoop Data Node
        Press 3: To Create Hadoop Client Node
        Press 4: To Exit

        ENTER YOUR CHOICE: """))


        if hchoice == 1:
            direc = input("Give name for directory: ")
            form = os.system("mkdir /{}".format(direc))
            os.system("echo '<configuration> \n<property> \n<name>dfs.name.dir</name> \n<value>/{}</value> \n</property> \n</configuration>' > hdfs-site.xml | mv hdfs-site.xml /etc/hadoop/".format(direc))
            ip = int(input("Enter the IP address of ur PC: "))
            port = int(input("Enter port no: "))
            os.system("echo '<configuration> \n<property> \n<name>fs.default.name</name> \n<value>hdfs://{}:{}</value> \n</property> \n</configuration>' > core-site.xml | mv core-site.xml /etc/hadoop/".format(ip,port))
            os.system("hadoop namenode -format")
            os.system("hadoop-daemon.sh start namenode")
            print("Your Master Node is created Successfully!!")

        elif hchoice == 2:
            direc = input("Give name for directory: ")
            form = os.system("mkdir /{}".format(direc))
            os.system("echo '<configuration> \n<property> \n<name>dfs.name.dir</name> \n<value>/{}</value> \n</property> \n</configuration>' > hdfs-site.xml | mv hdfs-site.xml /etc/hadoop/".format(direc))
            ip = int(input("Enter your Master IP address: "))
            port = int(input("Enter port no: "))
            os.system("echo '<configuration> \n<property> \n<name>fs.default.name</name> \n<value>hdfs://{}:{}</value> \n</property> \n</configuration>' > core-site.xml | mv core-site.xml /etc/hadoop/".format(ip,port))
            os.system("hadoop-daemon.sh start datanode")
            print("Your Data Node is created Successfully!!")



        elif hchoice == 3:
            ip = int(input("Enter your Master IP address: "))
            port = int(input("Enter port no: "))
            os.system("echo '<configuration> \n<property> \n<name>fs.default.name</name> \n<value>hdfs://{}:{}</value> \n</property> \n</configuration>' > core-site.xml | mv core-site.xml /etc/hadoop/".format(ip,port))
            print("Your Client Node is created Successfully!!")
            input("Press Enter to Continue")
            os.system("clear")


        elif hchoice == 4:
            break


        else:
            print("Invalid input, please try again!!")



    elif choice == 6:

        os.system("tput setaf 3")
        print("\t\t\t CREATING PARTITION ")
        print("\t\t\t ****************** ")
        os.system("tput setaf 7")

        pchoice = int(input("""What do you want from partition concept?

        Press 1: Creating Partition
        Press 2: Number of disks available
        Press 3: To see Mounted Disks
        Press 4: Exit

        ENTER YOUR CHOICE: """))

        if pchoice == 1:
            os.system("fdisk -l")
            diskName = input("Enter the disk name(eg: sda,sdb,sdc...): ")
            print(""" 
            p. To see disk details
            n. To create new partition
            d. To delete partition
            w. To save changes """)

            os.system("fdisk /dev/{}".format(diskName))
            os.system("udevadm settle")
            os.system("lsblk")
            diskNumber = int(input("How many partition you want to create ?: "))
            if diskNumber == 0:
                break
            else:
                for i in range(diskNumber-1):
                    name = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth']
                    partLoca = input("Enter your {} partition name which you created (like sdc1): ".format(name[i]))
                    partName = input("In which directory you want to mount your partition: ")
                    confirm = sub.getstatusoutput("mkdir {}".format(partName))
                    while confirm[0] != 0:
                        partName = input("This directory {} exists. Please re-type the directory name: ".format(partName))
                        confirm = sub.getstatusoutput("mkdir {}".format(partName))
                    os.system("mkfs.ext4 /dev/{}".format(partLoca))
                    os.system("mount /dev/{} {}".format(partLoca,partName))
                    input("Press Enter to Continue")
                    os.system("clear")


        elif partitionChoice ==2:
            os.system("fdisk -l")
            input("Press Enter to Continue")
            os.system("clear")
        elif partitionChoice ==3:
            os.system("df -h")
            input("Press Enter to Continue")
            os.system("clear")
        elif partitionChoice ==4:
            break


        else:
            print("Invalid Output! Please Try Again")

       

    elif choice == 7:

        os.system("tput setaf 3")
        print("\t\t\t LVM ")
        print("\t\t\t *** ")
        os.system("tput setaf 7")

        lvmChoice = int(input("""Which operations you want to perform in LVM ?
        Press 1: Create or Delete Logical Partition.
        Press 2: Extend Partition Size.
        Press 3: Reduce Partition Size.
        Press 4: Extend Virtual Group Size.
        Press 5: Exit

        ENTER YOUR CHOICE: """))


        if lvmChoice == 1:
            os.system("fdisk -l")
            b=int(input("Enter how much storage partition you want to create:"))
            c=[]
            for i in range(b):
                d=input("Enter the name of storage {}".format(i+1))
                c.append(d)
                os.system("pvcreate /dev/{}".format(d))
                e=input("Please enter the Virtual Group name: ")
                os.system("vgcreate {} /dev/{}".format(e,c[0]))
                x = range(b)
                x.pop(0)
                for p in x:
                    os.system("vgextend {} /dev/{}".format(e,c[p]))
                    f=int(input("Enter the Partition Size: "))
                    g=input("Enter your Paraition Name: ")
                    os.system("lvcreate --size {}G --name {} {}".format(f,g,e))
                    os.system("mkfs.ext4 /dev/{}/{}".format(e,g))
                    h=input("Enter the Directory Name where you want to mount recently created partition: ")
                    os.system("mkdir {}".format(h))
                    os.system("mount /dev/{}/{} {}".format(e,g,h))
                    print("Your Partition is Created Successfully")
                    a=input("Do you want to see details of your storage? (y/n): ")
                    if a in 'y':
                        os.system("lvdisplay {}/{}".format(e,g))
                        input("Press Enter to Continue")
                        os.system("clear")


        elif lvmChoice == 2:
            e=input("Please enter the Virtual Group Name: ")
            g=input("Please enter your Paraition Name (for example sdd2): ")
            l=int(input("Enter how much size you want to increase: "))
            os.system("lvextend --size +{}G /dev/{}/{}".format(l,e,g))
            os.system("resize2fs /dev/{}/{}".format(e,g))
            input("Press Enter to Continue")
            os.system("clear")

        elif lvmChoice == 3:
            e=input("Please enter the Virtual Group Name: ")
            g=input("Please enter your Paraition Name(for example sdd2): ")
            l=int(input("Enter how much size you want to reduce: "))
            os.system("lvreduce -r -L --size +{}G /dev/{}/{}".format(l,e,g))
            input("Press Enter to Continue")
            os.system("clear")
        elif lvmChoice == 4:
            y=input("Enter the Partition Name you want to increase: ")
            os.system("vgextend {} /dev/{}".format(e,y))
            input("Press Enter to Continue")
            os.system("clear")
        elif lvmChoice == 5:
            break
        else:
            print("Invalid input, please try again!")




    elif choice == 8:

        os.system("tput setaf 3")
        print("\t\t\t POPULATION PREDICTION ")
        print("\t\t\t ********************* ")
        os.system("tput setaf 7")


        def prediction():
            print("predict population with respect to number of years")
            dataset = pandas.read_csv("/root/mytasks/population.csv")
            y = dataset["POPULATION"]
            x = dataset["YEARS"]
            x = x.values
            x= x.reshape(-1,1)
            print("Model Fitting \n")
            time.sleep(1)
            model = LinearRegression()
            model.fit(x,y)
            print("Model fit is done \n")
            time.sleep(1)
            exp = input("Enter the year: ")
            print("predicted population is: ", end="")
            print(model.predict([[float(exp)]]))
            input("Press Enter to Continue")

        prediction()
  

    elif choice == 9:
        exit()

    else:
        print("Invalid Input! Please Try Again!!!")


