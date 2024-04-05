# Documentation
```bash
lsblk
```
```bash
sudo umount /dev/sda1  
```


```bash
sudo mkfs.exfat -n "label" /dev/sda1 (formatting) #Could be anything instead of sda1, check using lsblk
```

```bash
df -h #for seeing how much space you have left on each partition
```

## Mounting a disk:
### Most approproate place to mount a disk is in /mnt or /media

```bash
sudo mount /dev/sda1 /mnt/disk1/
```
--> Disk1 is a folder you can create for better viewing in mnt
you can also mount in /media (for temp devices)

--> ncdu is a great utility tool for viewing disk space

```bash
cat /etc/fstab
```
--> This is a very important file which should not be messed with unless you want to add a new hard disk
    basically it contains the names of all the disk through which the computer will go line by line to mount during booting
    adding a line to your new hard disk or ssd will allow it to mount your disk during boot

## Creating a new partition table
```bash
sudo fdisk /dev/sdb
p #(for current partition table)
m #(for help)
g #(for new partition table of gpt type)
n #(for new partition table)
1 #for first partition
#no reason to change first sector 
#fixed size or enter to make it take the entirity of the disk
Y
w
#now changes have been saved 
#now allocate a new partition system on the drive using the mkfs command listed earlierls
```

## Now for creating multiple partition:
```bash
sudo fdisk /dev/sda
```

--> Remember when it asks for end of sector type 1G or 2G or however many
you may have to delete the prev partition using 'd'


## ENCRYPTION of a disk

```bash
sudo cryptsetup luksFormat /dev/sda1
```

--> you will know follow the necessary steps and give passphrase

now to open the disk to mount (done before manually mounting)
also this step is automatically done when you enter the pen drive 
but after encryption if you want to access then youll have to manually open then mount

## STEPS TO FOLLOW FOR THE FIRST TIME

```bash
#OPEN->
sudo cryptsetup open /dev/sda1 any_name

#DONT FORGET TO FORMAT WITH FILE TYPE->
sudo mkfs.exfat /dev/mapper/any_name

#MOUNTING->
sudo mount /dev/maper/any_name

#CLOSING (to close and encrypt again)->
sudo cryptsetup close /dev/mapper/any_name
```

--> When you insert disk again after encryption you wont have to perform these tasks 
as it will automatically be done by the os 
instead of 'any_name' youll see something like luks9894932942093 (something big and long :|)

## REMOVING THE ENCRYPTION:
```bash
sudo cryptsetup luksOpen /dev/sda1 my_drive
sudo cryptsetup luksRemove /dev/sda1
sudo cryptsetup luksClose my_drive
sudo mkfs.exfat /dev/sda1
```



