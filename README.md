# Publix Random Sub Orderer Python3 Debian/Mac/Win
I hate the publix deli and their online ordering, so I wrote a handy little script to do it for me!

Python 3 Download: https://www.python.org/downloads/

FOR EDUCATIONAL PURPOSES ONLY

DOESNT WORK AFTER 8-8:30PM WHEN THEY STOP TAKING ONLINE ORDERS FOR THE DAY

## Setup:
Must install "names" module from pip and have Newest Chrome installed.
```
# Debian Install
$ bash install-chromex64.sh
$ bash install-deps-user.sh
$ bash setup-chromedriver.sh

# Mac Install
Install Chrome the usual way...
$ bash install-deps-mac.sh
$ bash setup-chromdriver.sh

# Win Install
Install Chrome the usual way...
$ install-deps-win.bat
```
## Run:
The only thing you need to do is find the store # and the phone number area code, everything else is random.

Clone the Repo:
```
$ git clone https://github.com/sawyermade/pubSubOrderer
$ cd pubSubOrderer
```
### Linux:
OS = linux
```
python3 pubSubOrder.py OS storeNum areaCode numOrders

# Example
python3 pubSubOrder.py linux 840 813 2

# Headless
python3 pubSubOrder.py linux 840 813 2 headless
```
### Mac:
OS = mac
```
python3 pubSubOrder.py OS storeNum areaCode numOrders

# Example
python3 pubSubOrder.py mac 840 813 2

# Headless
python3 pubSubOrder.py mac 840 813 2 headless
```
### Win:
OS = win
```
python3 pubSubOrder.py OS storeNum areaCode numOrders

# Example
python3 pubSubOrder.py win 840 813 2

# Headless
python3 pubSubOrder.py win 840 813 2 headless
```