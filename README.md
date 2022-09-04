# bulk-send-assets
installing python and needed libraries
open send_assets - BAC.py and edit the data
```
wget https://github.com/billionapeclub/sending-assets/blob/main/send_assets%20-%20BAC.py
sudo apt-get install python3 python3-venv python3-pip -y
pip install ravenrpc
python3 send_assets - BAC.py
```



don't forget to change with your own rpc password from the raven.conf file located at ./raven folder
```
rpcuser="billionape"
rpcpassword="ravencointothemoon"
```

input one by one the assets you want to send:
```
data = {
'BILLION_APE_CLUB#01025': 1,
'BILLION_APE_CLUB#01024': 1,
'BILLION_APE_CLUB#01023': 1,
'BILLION_APE_CLUB#01022': 1,
'BILLION_APE_CLUB#01021': 1,
'BILLION_APE_CLUB#01020': 1,
'BILLION_APE_CLUB#01019': 1,
'BILLION_APE_CLUB#01018': 1,
'BILLION_APE_CLUB#01017': 1,
'BILLION_APE_CLUB#01016': 1,
}
```

change the wallet address to the address you want to send it to:
```
for ape in data:
    rvn.walletpassphrase('ravencointothemoon', 100)
    wallet = 'R9mxDnaXDZrHapjnDYFgzetHo2QbKBksRF'
    asset_sent = rvn.transfer(ape, '1', wallet)
    time.sleep(0.1)
    print(asset_sent)
```
