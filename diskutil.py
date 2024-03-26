import subprocess
import getpass

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def listing():
    try:
        output = subprocess.check_output(["lsblk","-l"]).decode("utf-8")
        lines = output.split('\n')

        print("\nYour mounted disks")
        
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
    print("\n1>format the disk\n2>create new partition\n3>unmount disk\n4>mount disk")
    choice = input("please choose an option: ")
    
    if(choice == "1"):
        print("make sure you have unmounted your disk first by chosing option 3")
        
        sudo = getpass.getpass("please enter your root pass: ")
        
        part_no = input("partition number: ")
        commands = f"g\nn\n{part_no}\n\n\n\nY\nw"
        
        subprocess.run(["sudo", "fdisk", "/dev/sda"], input =f"{sudo}\n{commands}", stderr = subprocess.PIPE, text=True, check=True)
        
        print(f"{GREEN}new partition created{RESET}")

        name = input("new name: ");
        subprocess.run(["sudo","mkfs.exfat","-n",name,f"/dev/sda{part_no}"])
        print(f"{GREEN}format completed, ready to go{RESET}")
        print(f"{GREEN}now mounting to /mnt{RESET}")

        subprocess.run(["sudo","mount",f"/dev/sda{part_no}","/media/man44"])
        print(f"{GREEN}disk has been mounted{RESET}")

    if(choice == "3"):
        
        try:
            partition_no = input("partition no: ")
            result =  subprocess.run(["sudo", "umount", f"/dev/sda{partition_no}"])
            if result.returncode==0:
                print(f"{GREEN}Successfuly unmounted{RESET}")
            else:
                print(f"{RED}Unsuccessful pls check partition number{RESET}")
        
        except subprocess.CalledProcessError as e:
            print(f"{RED}Unsuccessful{RESET}")

def main():
    listing()
    what()

if __name__ == "__main__":
    main()
