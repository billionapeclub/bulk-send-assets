from ravenrpc import Ravencoin
import time


rpcuser="billionape"
rpcpassword="ravencointothemoon"
rvn = Ravencoin(rpcuser, rpcpassword)

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


for ape in data:
    rvn.walletpassphrase('ravencointothemoon', 100)
    wallet = 'R9mxDnaXDZrHapjnDYFgzetHo2QbKBksRF'
    asset_sent = rvn.transfer(ape, '1', wallet)
    time.sleep(0.1)
    print(asset_sent)
