# btc-com explorer documentation
A python api-wrapper for https://btc.com blockchain explorer
# Usage
## Install
```
pip install btc-com
```

## Import 
```python
from btc_com import explorer
```

## API Rate Limits
There is nothing formal in the documentation but this works
```python
sleep_time = .25  # don't overstep rate limits
```

# Blocks
The `get_block()` function is used to get a specific block. This can be done by passing either a block height or a block hash

`get_blocks_on_date()` is used to get all blocks that were mined on a specific date

## Block Class
JSON Block Response from API available here: 
https://btc.com/api-doc#Block

Python Class fields available in the `Block` class
```
+ height: int
+ version: int
+ merkle_root: str
+ curr_max_timestamp: int
+ timestamp: int
+ bits: int
+ nonce: int
+ hash: str
+ prev_block_hash: str, None if doesn't exist
+ next_block_hash: str, None if doesn't exist
+ size: int
+ pool_difficulty: int
+ difficulty: int
+ tx_count: int
+ reward_block: int
+ reward_fees: int
+ created_at: int
+ confirmations: int
+ extras: dict
    - relayed_by: str
```
Access fields like any python class
```python
block = explorer.get_block()

height = block.height
version = block.version
merkle_root = block.merkle_root
curr_max_timestamp = block.curr_max_timestamp
timestamp = block.timestamp
bits = block.bits
nonce = block.nonce
hash = block.hash
prev_block_hash = block.prev_block_hash
next_block_hash = block.next_block_hash
size = block.size
pool_difficulty = block.pool_difficulty
difficulty = block.difficulty
tx_count = block.tx_count
reward_block = block.reward_block
reward_fees = block.reward_fees
created_at = block.created_at
confirmations = block.confirmations
extras = block.extras
relayed_by = block.extras['relayed_by']
```

## get latest block
Returns an instance of `Block` class

Default parameter for `get_block()` is `latest`
```python
block = explorer.get_block()
```
This function hits this api endpoint:

https://chain.api.btc.com/v3/block/latest

## get block by height
Returns an instance of `Block` class

```python
block = explorer.get_block(50)
```
This function hits this api endpoint:

https://chain.api.btc.com/v3/block/50

## get block by hash
Returns an instance of `Block` class

```python
hash = '0000000000000000002750e4de8f033d28883024de470f775cedad6305b277c0'
block = explorer.get_block(hash)
```
This function hits this api endpoint:

https://chain.api.btc.com/v3/block/0000000000000000002750e4de8f033d28883024de470f775cedad6305b277c0

## get blocks on specific date
Returns a list of `Block` class objects

```python
date = '20170512'
blocks = explorer.get_blocks_on_date(date)
print(f'There were {len(blocks)} created on {date} ')
```
This function hits this api endpoint:

https://chain.api.btc.com/v3/block/date/20170512


# Transactions
JSON Transaction Response from API available here: 
https://btc.com/api-doc#Transaction

Python Class fields available in the `Transaction` class
```
+ block_height: int
+ block_time: int
+ created_at: int
+ fee: int
+ hash: str
+ id: str (id == hash)
+ inputs: list
+ inputs_count: int
+ inputs_value: int
+ is_coinbase : boolean
+ lock_time: int
+ outputs: list
+ outputs_count: int
+ outputs_value: int
+ size: int
+ version: int
```
Access fields like any python class
```python
tx_hash = '937c3fb03b370557a8047f51c9efc2af17df2ed05fa48774c3105ef835133b3a'
tx = get_transaction(tx_hash)

block_height = tx.block_height
block_time = tx.block_time
created_at = tx.created_at
fee = tx.fee
hash = tx.hash
id = tx.id
inputs = tx.inputs
inputs_count = tx.inputs_count
inputs_value = tx.inputs_value
is_coinbase = tx.is_coinbase
lock_time = tx.lock_time
outputs = tx.outputs
outputs_count = tx.outputs_count
outputs_value = tx.outputs_value
size = tx.size
version = tx.version
```

## get transactions in the block
Function: `get_transactions_in_block()`

Function parameters:

`block` default is `latest` (block can be height or hash)

`page` default is `1`

`pagesize` default is `50` (min: 1, max: 50)

## get transactions in the latest block
Returns a list of `Transaction` objects

```python
txs = explorer.get_transactions_in_block()
```
note: default parameters are used here.

This function hits this api endpoint:

https://chain.api.btc.com/v3/block/latest/tx

## get transactions in the latest block, specific page and number of txs
Returns a list of `Transaction` objects
```python
txs = explorer.get_transactions_in_block(page=2, page_size=10)
```
This gets 10 transactions on page 2 of the latest block. So Transactions 51 to 60

This function hits this api endpoint:

https://chain.api.btc.com/v3/block/latest/tx?page=2&pagesize=10

## get transactions in specific block, specific page and number of txs
Returns a list of `Transaction` objects
```python
txs = explorer.get_transactions_in_block(block='50', page=2, page_size=10)
```
This gets 10 transactions on page 2 in the 50th block. So Transactions 51 to 60 in block 50

This function hits this api endpoint:

https://chain.api.btc.com/v3/block/50/tx?page=2&pagesize=10

## get a transaction
Returns an instance of `Transaction` class
```python
tx_hash = '937c3fb03b370557a8047f51c9efc2af17df2ed05fa48774c3105ef835133b3a'
tx = explorer.get_transaction(tx_hash)
```

## get multiple transactions
Returns a list of `Transaction` objects
```python
t1 = 'e35d41072f68a9fc1afd21bd9577a36162175a6ee80f126e12ed955ac7ead7b9'
t2 = '8bf367738201bd51b65ec4212eeb57d9a7c5e7f569254df9a73c82fcd7b9ed93'
t3 = '265da4b0111ee0a65f81feb5467e0b73b939de7474fd01341058feaa16aee656'

txs = explorer.get_transactions([t1, t2, t3])
```
`txs` here is a list of `Transaction` objects

# Addresses
JSON Address Response from API available here: 
https://btc.com/api-doc#Address

Python Class fields available in the `Address` class
```
+ address: str
+ received: int
+ sent: int
+ balance: int
+ tx_count: int
+ unconfirmed_tx_count: int
+ unconfirmed_received: int
+ unconfirmed_sent: int
+ unspent_tx_count: int
+ first_tx
+ last_tx
```
Access fields like any python class
```python
addr_hash = '15urYnyeJe3gwbGJ74wcX89Tz7ZtsFDVew'
addr = explorer.get_address(addr_hash)

address = addr.address
received = addr.received
sent = addr.sent
balance = addr.balance
tx_count = addr.tx_count
unconfirmed_tx_count = addr.unconfirmed_tx_count
unconfirmed_received = addr.unconfirmed_received
unconfirmed_sent = addr.unconfirmed_sent
unspent_tx_count = addr.unconfirmed_tx_count
first_tx = addr.first_tx
last_tx = addr.last_tx
```

## get an address
Returns an instance of `Address`
```python
address_id = '15urYnyeJe3gwbGJ74wcX89Tz7ZtsFDVew'
address = explorer.get_address(address_id)
```

# Unspent
JSON Unspent Response from API available here: 
https://btc.com/api-doc#Unspent

Python Class fields available in the `UnspentTransaction` class
```
+ tx_hash: str
+ tx_output_n: int
+ tx_output_n2: int
+ value: int
+ confirmations: int
```
Access fields like any other python class
```python
addr_id = '385cR5DM96n1HvBDMzLHPYcw89fZAXULJP'
unspent_txs = get_unspent_transactions(addr_id)  # returns list

unspent_one = unspent_txs[0]
tx_hash = unspent_one.tx_hash
tx_output_n = unspent_one.tx_output_n
tx_output_n2 = unspent_one.tx_output_n2
value = unspent_one.value
confirmations = unspent_one.confirmations
```

## get unspent transaction data of an address
Returns a list of `UnspentTransaction` objects
```python
unspent_txs = explorer.get_unspent_transactions(address_id)
```
# Bitmain Digital Currency Index
JSON Bitmain digital currency index Response from API available here: 
https://btc.com/api-doc#digital%20currency%20index


Python Class fields available in the `BitmainIndex` class
```
+ timestamp: int
+ index: int
+ sign: str
```
Access fields like any python class
```python
index = explorer.get_digital_currency_index()

timestamp = index.timestamp
index = index.index
sign = index.sign
```
## get bitmain digital currency index
Returns an instance of `BitmainIndex` class
```python
index = explorer.get_digital_currency_index()
```
