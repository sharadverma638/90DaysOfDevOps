# Linux Volume Management (LVM)

## Commands Used

```bash
# Task 1: Check current storage


lsblk
# Shows disks and partitions.

df -h
# Shows current disk usage.

sudo pvs
# Shows existing physical volumes.

sudo vgs
# Shows existing volume groups.

sudo lvs
# Shows existing logical volumes.
```

```bash
# Task 2: Create a virtual disk


sudo dd if=/dev/zero of=/tmp/lvm-disk.img bs=1M count=1000
# Creates a 1 GB virtual disk file.

sudo losetup --find --show /tmp/lvm-disk.img
# Connects the file to a loop device.
```

```bash
# Task 3: Create physical volume


sudo pvcreate /dev/loop0
# Creates an LVM physical volume on the virtual disk.

sudo pvs
# Verifies the physical volume.
```

```bash
# Task 4: Create volume group


sudo vgcreate devops-vg /dev/loop0
# Creates a volume group named devops-vg.

sudo vgs
# Verifies the volume group.
```

```bash
# Task 5: Create logical volume


sudo lvcreate -L 500M -n app-data devops-vg
# Creates a 500 MB logical volume named app-data.

sudo lvs
# Verifies the logical volume.
```

```bash
# Task 6: Format and mount the volume


sudo mkfs.ext4 /dev/devops-vg/app-data
# Formats the logical volume with ext4.

sudo mkdir -p /mnt/app-data
# Creates the mount directory.

sudo mount /dev/devops-vg/app-data /mnt/app-data
# Mounts the logical volume.

df -h /mnt/app-data
# Verifies that the volume is mounted.
```

```bash
# Task 7: Extend the logical volume


sudo lvextend -L +200M /dev/devops-vg/app-data
# Adds 200 MB to the logical volume.

sudo resize2fs /dev/devops-vg/app-data
# Expands the ext4 filesystem to use the extra space.

df -h /mnt/app-data
# Verifies the new size.
```

## What I Learned

* Learned how to check disks and storage in Linux.
* Learned how to create a virtual disk using a loop device.
* Learned how to create physical volumes, volume groups and logical volumes.
* Learned how to format and mount an LVM volume.
* Learned how to extend a logical volume and filesystem.
