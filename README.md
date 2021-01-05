# How to set up and run test

### Download and install python 3.6.8
    https://www.python.org/downloads/release/python-368/
    
### Create-activate virtual environment, install requirements and set up chromedriver
##### For Window
    pip install virtualenv
    cd amazon-testing
    virtualenv env
    venv\Scripts\activate.bat
    
```
pip install -r requirements
```
```
Control Panel\All Control Panel Items\System
Open `Advanced system settings`
Open `Environments Variables`
Open `Path` add \pathto\amazon-testing\web_ui\driver
```

##### For Mac/Linux
Ubuntu
```
    apt-get update
    apt-get install python-virtualenv
    cd amazon-testing
    virtualenv -p /usr/bin/python3 venv
    source venv/bin/activate
```
```
    pip install -r requirements
```
```
    wget -N https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip -P ~/
    unzip ~/chromedriver_linux64.zip -d ~/
    rm ~/chromedriver_linux64.zip
    sudo mv -f ~/chromedriver /usr/local/bin/chromedriver
    sudo chown root:root /usr/local/bin/chromedriver
    sudo chmod 0755 /usr/local/bin/chromedriver
```

Mac
```
    cd amazon-testing
    python3 -m venv venv
    source venv/bin/activate
```
```
    Download chrome driver from:
    
    https://sites.google.com/a/chromium.org/chromedriver/downloads
    sudo nano /etc/paths
    add `/usr/local/bin` to paths file
    
    Go to your downloads folder, find the chromedriver_mac64.zip file and unpack it.
    You will see the chromedriver executable file.
    Now, we can run below command and move the chromedriver file to the /usr/local/bin folder.
    
    mv chromedriver /usr/local/bin
```
### Run test:
```
cd amazon-testing\web-ui
pytest -s -v testcases\test_amazon.py -k "test_amazon" --html=logs\test_amazon.html --browser gc
```
