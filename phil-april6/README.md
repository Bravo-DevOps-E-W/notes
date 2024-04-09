# Intro to SSH (Secure Shell)

#### What is Secure Shell?
- SSH is primarily used to establish a secure connection between a client and a server over an insecure network (such as the internet)
    - Provides a secure channel over an unsecured network by encrypting the data that is transmitted between the client and the server

### Key Features
- Encryption: SSH encrypts all data transmitted between the client and the server, including passwords, commands, and any other sensitive information
    - Ensures that even if data is intercepted, it cannot be properly deciphered by an attacker

- Authentication: SSH uses various authentication methods, including passwords, public-key cryptography, and multi-factor authentication to verify the identity of users and servers
    - Today we will be focusing on public-key cryptography

##### Components
- SSH Client: The program used to initiate a connection to an SSH server.
    - Typically installed on a user's local machine and allows the user to log in to remote servers securely
- SSH Server: Runs on the remote machine and listens for incoming SSH connections.
    - Authenticates clients and provides access to server resources
- SSH Protocol: Defines the rules and procedures for communication between the client and the server
    - Specifies how data is encrypted, authenticated, and transmitted over the network

###### SSH and Client Server
![alt text](/visuals/ssh-client-server.png)


##### Usage
- Commonly used by system administrators, developers, and anyone who needs to securely access remote systems or transfer files between systems
- Widely used for remote administration of servers, `managing cloud infrastructure`, deploying applications, and securely transferring files

###### Security Best Practices
- Always use strong passwords, or preferably, `public-key` authentication for SSH access
- Keep SSH software and configurations up to date to protect against known vulnerabilities
- Disable root login over SSH and restrict SSH access to only trusted users
- Use firewall rules to limit SSH access to specific IP addresses or networks
- Monitor SSH logs for suspicious activity and enforce security policies to prevent unauthorized access

#### How SSH Works
- SSH provides a text-based interface by creating a remote shell.
- After connecting, all commands ran in your local terminal are sent to the remote server where they will be executed
- The most common way to connect to a remote Linux server is through SSH

### SSH Public Key Authentication

- Public / Private key encyrption is where some encyption algorithm is implemented using a `public key` -- to encyrpt a message
- The `private key` can be used to decrypt the message

![alt text](/visuals/public_key_encryption.png)

- Notice that the `public key` used to encrypt, can be shared safely.
- The `private key` used to decrypt, is not to be shared with anyone.


###### Installing OpenSSH on Linux/Mac
- Almost all Linux distros, including Mac OS X, and the default version of Ubuntu for WSL2 come with OpenSSH already installed and configured

Open SSH gives us access to the following tools:
- Remote operations using `ssh`, `scp`, and `sftp`
- Key management with `ssh-add`, `ssh-keysign`, `ssh-keyscan`, and `ssh-keygen`
- The service side consists of `sshd`, `sftp-server`, and `ssh-agent`.

We will see `ssh`, `ssh-add`, `ssh-keygen`, and `ssh-agent` often.


## Connecting to a Remote Server

1. Open a terminal window on your local machine
2. Create PEM file
- Can be done on AWS console or using `ssh-keygen`
3. Change the permissions of the PEM file once it is on your local machine
```
chmod 400 my-example-file.pem
```
4. Connect to the remote server using pem file with ssh
```
ssh -i "my-example-file.pem" ubuntu@ec2-1-22-333-22.compute1.amazonaws.com
```
(These are examples, this is not a real pem or server)

Note, using the pem file this way, you will either need to ssh from the directory that contains your pem, or provide the path to your pem file within your ssh command


#### Setting Up a Config
The above setup works, but as we interact with more servers and pem files, this can get harder to keep track of and maintain

- A great way to handle this is by creating our config file within our .ssh folder
1. Open a terminal and navigate to your .ssh folder.
```
cd ~/.ssh
```
2. Create a config file
```
vi config
```
Note: You can use nano or vim, You could also use vscode since we are on our local machine.

- This is an example config, where the alias for our server is called "myserver":
```
Host myserver
    HostName server.example.com
    Port 22
    User myusername
    IdentityFile ~/.ssh/id_rsa
```
`Host` is where we assign the alias to which we will refer to this server by
`HostName` specifies the actual host/IP Address. This is the destination of the SSH
`Port` is the port we will be communicating to the server on for authentication
`User` is the User you are trying to log in as on the remote server
`IdentityFile` is the path to the pem needed for authentication

- If this config is set up properly, you will now be able to ssh by using:
```
ssh myserver
```

### Using SCP (Secure Copy)

This works similarly to copying a file (Need path from, path to)

1. Create or find a file that you would like to copy
2. Copy your file to the desired location on the remote server, and include the -i for your pem key

Example:
```
 scp -i /Users/phil/code/devops-bravo/week1/day4/server-lesson/i
d_rsa -r /Users/phil/code/devops-bravo/week1/day4/server-lesson/AWS ubuntu@54.23
6.14.106:/home/ubuntu/phil
```

Note that because we copied a directory of files into the remote server. We also had to provide the `-r` flag to read all of the files in our directory we are copying to the remote server





