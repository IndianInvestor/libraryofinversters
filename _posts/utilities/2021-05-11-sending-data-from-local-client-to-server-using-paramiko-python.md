---
title: "How to securely send data from local client to remote server using Paramiko (codes included)"
date: 2021-05-11
tags: [python, scp in python, ssh in python]
excerpt: "Paramiko module can be used in Python to securely send data from the local client to the remote server. It is analogous to the SSH and SCP in Linux."
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/paramiko.jpg"
classes:
  - wide
sidebar:
  nav: "all_posts_list"
category: utilities
---

{% include toc %}
In this post, we will see how we can use [Paramiko module in Python](http://docs.paramiko.org/en/stable/index.html) to securely send data and to receive data from the remote server. If you have used `ssh` and `scp` in linux, then everything will come naturally to you. Even if you are unfamiliar with `ssh` command in linux, I will explain each step, so don't worry.

{% include image.html url="https://source.unsplash.com//vIQDv6tUHYk/640x480" description="Networking" %}

## Set parameters
First, we define the location of the data that we want to send to the remote server. And the location of the directory on the server, where we want to store the data. In this case, all the data I want to send is in [`mseed`](/utilities/converting-mseed-data-to-mat-and-analyzing-in-matlab/#what-is-miniseed-format) format. You can change "*.mseed" to any format your data files are in.

I suggest you to go to the remote server and create a separate directory for receiving the data. In my case, I have created data directory in the home folder, named "myClientData/Client1".

```python
import paramiko
from datetime import datetime
import os, glob, sys

dataDirec = "dataDir"
allData = glob.glob(os.path.join(dataDirec, "*.mseed"))

destLoc = destLocation = os.path.join("/","home","myClientData","Client1")
```

I also imported `paramiko` (required for sending data), `datetime` (for logging time) and other libraries (mainly for IO operations).

## Open session for connecting to the server
```python
clientSession = paramiko.SSHClient()
## If host dont exist in your known host list, then add
clientSession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
```
Here, `set_missing_host_key_policy(paramiko.AutoAddPolicy())` is required to auto add the unknown hosts. But for security purpose, I'd recommend you to add your remote server to the known hosts list and use this:

```python
## Use hosts from the system host keys else reject
clientSession.load_system_host_keys()
clientSession.set_missing_host_key_policy(paramiko.RejectPolicy())
```
This will check if the hosts are known by the system or it will reject the host.

## How to add the known hosts?
First, check if the host is known by your system or not by typing:
```
ssh-keygen -F your_host_name_here
```

If this returns nothing, then the host is not in your known hosts list.

You can add known hosts by `ssh`ing to the server and it will ask you if you want to add the host to your known hosts list, then enter "yes"
```
ssh yourusername@your_host_name_here
```

## Connect to the remote server and check the connection

You can connect to the remote server by simply:
```python
clientSession.connect(hostname='your_host_name_here', username='yourusername',password='yourpasswordhere', port=22)
```

The above line will connect you to the remote server. It is also possible to securely encrypt your password instead of hardcoding it as above. I will cover how to do that in the future posts.

You can check for the connection status by:

```python
stdin, stdout, stderr = clientSession.exec_command('hostname')
status = stdout.channel.recv_exit_status()
with open('EarthInversionRunLogs.txt','a') as file:
    file.write("\n")
    if status==0:
        file.write(f"{stdout.read().decode('utf8').strip()}, success, {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
    else:
        file.write(f"{stderr.read().decode('utf8').strip()}, failed with {status}, {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")

#close all the file objects
stdin.close()
stdout.close()
stderr.close()
```
The above codes are simply typing `hostname` command into the server, and redirecting the outout to the `stdin, stdout, stderr`. In case, your connection is successful, the `status` will return 0. We also save the output for the run into `EarthInversionRunLogs.txt` file for future reference. Finally, you are recommended to close the `stdin, stdout, stderr`, your server will appreciate it.

## Send the files securely
We can send the files by opening a sftp client and putting the data into it.

```python
## open sftp to send file
sftp_client = clientSession.open_sftp()

for filetosend in allData:
    filename = os.path.basename(filetosend)
    destFile = os.path.join(destLoc,filename) #renaming the file
    try:
        sftp_client.put(filetosend, destFile) #send datafile filetosend to destFile
        with open('RFidgetRunLogs.txt','a') as file:
            file.write(f"{filetosend}, {destFile}\n") #add the run logs
    except Exception as err:
        print(sys.exc_info())

sftp_client.close()
```

If you intend to rather retrieve the data, use the `get` method.

Also, it is recommended to close the session, after you are done.

```python
clientSession.close()
```

## Conclusions
As you have seen, sending the data to the remote server using Paramiko module is fast, easy and secure. Paramiko module is vast, and I am simply touching the surface of it. In the future posts, I will cover other features of the module.