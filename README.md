<img src="./resources/images/start.png" width="100%" />

<br />

<img src="./resources/images/design1.PNG" width="50%" />

<br />

<img src="./resources/images/design2.PNG" width="50%" />

<br />

<img src="./resources/images/EYDhHM1X0AAd8UP.png" width="50%" />

# PyBlock v0.1.0.1
Bitcoin Blockclock

A simple Python Block Clock to check the Blockcain information.

## Dependences

    a@A:~> pip3 install -r requirements.txt
    
  - Install the [Hexyl](https://github.com/sharkdp/hexyl)
  
## How to execute
  - python3 PyBlock.py

   ## Connect to an external node first steps
   
   #### WARNING! THIS IS NOT A SECURE METHOD OF CONNECTION. DO IT BY YOUR OWN RISK. THE BEST WAY IS DOING IT LOCALLY.
   
   - First log in on A as user a and generate a pair of authentication keys. Do not enter a passphrase:
   
    1. a@A:~> ssh-keygen -t rsa
      Generating public/private rsa key pair.
      Enter file in which to save the key (/home/a/.ssh/id_rsa): 
      Created directory '/home/a/.ssh'.
      Enter passphrase (empty for no passphrase): 
      Enter same passphrase again: 
      Your identification has been saved in /home/a/.ssh/id_rsa.
      Your public key has been saved in /home/a/.ssh/id_rsa.pub.
      The key fingerprint is:
      3e:4f:05:79:3a:9f:96:7c:3b:ad:e9:58:37:bc:37:e4 a@A
    
   - Now use ssh to create a directory ~/.ssh as user b on B. (The directory may already exist, which is fine):
   
    2. a@A:~> ssh b@B mkdir -p .ssh
       b@B's password: 
    
   - Finally append a's new public key to b@B:.ssh/authorized_keys and enter b's password one last time:
    
    3. a@A:~> cat .ssh/id_rsa.pub | ssh b@B 'cat >> .ssh/authorized_keys'
       b@B's password: 
   
   - From now on you can log into B as b from A as a without password:
   
    4. a@A:~> ssh b@B
    
   After this process you can execute Python-Blockclock.py

## How make it work
  It will appear a place you can put your Bitcoin-cli path
  
  - "Path to your Bitcoin-cli: " #Add the path and shoot Enter.
   
  
### Contributors

@Curly60e
@SamouraiDev

### Testers

[@__B__T__C__](https://twitter.com/__B__T__C__)
