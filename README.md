## btc-com
A python 3 api wrapper for btc.com block explorer

docs: https://github.com/pasquantonio/btc.com-api-wrapper/blob/master/docs.md

api docs: https://btc.com/api-doc

block explorer: https://btc.com/block

## Install
```
pip install btc-com
```
must be python3 so if not in a python3 virtualenv use
```
pip3 install btc-com
```

## Usage
```python
from btc_com import explorer

# get transaction by id
tx_id = '56a5b477182cddb6edb460b39135a3dc785eaf7ea88a572052a761d6983e26a2'
tx = explorer.get_transaction(tx_id)

# get address data
address = '3ADPkym6mQ2HyP7uASh5g3VYauhCWZpczF'
addr_info = explorer.get_address(address)
```

## Examples
examples.py shows multiple examples of calling functions
https://github.com/pasquantonio/btc.com-api-wrapper/blob/master/examples.py

## Donate
BTC: `3ADPkym6mQ2HyP7uASh5g3VYauhCWZpczF`
