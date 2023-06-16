# Gawe.in

This is the source code for connecting the machine learning model to the mobile development which feature, login register and uploading files to complete the capstone project for Bangkit 2023

## How To Run
### Prerequisites
1. Virtual machine
2. SSH access to virtual machine
3. Service account key

## Virtual Machine
1. Create virtual machine with the following specifics:
      - Region asia/southeast2 or the least traffic
      - Machine type n1 standard1
      - Allow HTTP and HTTPS
      - Reserve a static external IP
2. Run SSH
3. Update the packages in the VM
   ```shell
   sudo apt update
   sudo apt upgrade
   ```

## Cloning The Repository
1. Clone the code from github
   ```shell
   https://github.com/Seskor910/login-regis.git
   ```
   
2. Change to your github directory
   ```shell
   cd [folder name]

## Setup Environment
1. Install Python by running the following command:
```shell
sudo apt install python3-pip
```
2. Create a virtual environment for your Flask project by executing the following command:
```shell
sudo apt install python3.10-venv
python3 -m venv myenv
```
3. Activate the virtual environment by running the following command:
```shell
source myenv/bin/activate
```

## Configure Nginx
1. Install Nginx on your VM:
```shell
sudo apt-get install -y nginx
```
2. Open the Nginx configuration file for editing:
```shell
sudo nano /etc/nginx/sites-available/default
```
3. Replace the server settings with the following configuration:
```perl
server {
  listen 80;
  server_name YOUR_SERVERS_IP_ADDRESS;

  location / {
    proxy_pass "http://127.0.0.1:8000";
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection 'upgrade';
    proxy_cache_bypass $http_upgrade;
  }
}
```
change the server_name YOUR_SERVERS_IP_ADDRESS with your external IP from intances
4. Save the file and exit the editor.

## Restart Nginx
To apply the changes, restart the Nginx service:
```shell
sudo service nginx restart
```

## Configure Flask
1. Install the required dependencies
   ```shell
   pip install flask
   pip install scikit-learn
   pip install sqlalchemy
   pip install pickle5
   ```
2. Adding and install tesserect
   ```shell
   sudo add-apt-repository ppa:alex-p/tesseract-ocr-devel
   sudo apt update
   sudo apt install tesseract-ocr
   ```
3. Create a service account to obtain the key.json file.
4. Upload the key.json file via SSH.
5. Move the key.json file to the Flask directory.
6. Run the Flask app using the following command:
   ```shell
   python3 main.py
   ```

## Accessing the API
For the endpoint:
 - POST: your_ip/upload
 - POST: your_ip/signup
 - POST: your_ip/login
