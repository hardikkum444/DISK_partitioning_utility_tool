import subprocess
import getpass

def listing():
    try:
        output = subprocess.check_output(["lsblk","-l"]).decode("utf-8")
        lines = output.split('\n')

        print("Your mounted disks")
        
        count = 0
        for line in lines:
            if 'sd' in line:
                parts = line.split()
                disk_name = parts[0]
                if(count == 0):
                    print("->",disk_name)
                else:
                    print("-->",disk_name)
                count+=1
    
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def what():
    print("1>format the disk\n2>create new partition\n3>unmount disk\n4>mount disk")
    choice = input("please choose an option")
    
    if(choice == "1"):
        print("make sure you have unmounted your disk first by chosing option 3")
        
        commands = "g\nn\n1\n\n\n\nY\nw"

        sudo = getpass.getpass("please enter your root pass")
        subprocess.run(["sudo", "fdisk", "/dev/sda"], input =f"{sudo}\n{commands}", stderr = subprocess.PIPE, text=True, check=True)
        print("completed")
        # output = subprocess.check_output(sudo).decode("utf-8")
        # print(output)

        subprocess.run(["sudo","mkfs.exfat","-n","pen","/dev/sda1"])


def main():
    listing()
    what()

if __name__ == "__main__":
    main()
