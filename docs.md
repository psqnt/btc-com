# explorer documentation

## Import 
```python
from explorer import explorer
```

## API Rate Limits
I haven't found anything formal but this limit works so far
```python
sleep_time = .25  # don't overstep rate limits
```

## get latest block
```python
block = explorer.get_block()
```

## get block by height
```python
block = explorer.get_block(50)
```

## get block by hash
```python
hash = '0000000000000000002750e4de8f033d28883024de470f775cedad6305b277c0'
block = explorer.get_block(hash)
```

## get blocks on specific date
```python
date = '20170512'
blocks = explorer.get_blocks_on_date(date)
print(f'There were {len(blocks)} created on {date} ')
```

## get transactions in a block with default payload
```python
txs = explorer.get_transactions_in_block()
```

## get transactions in a block, specify which page and number of txs
```python
txs = explorer.get_transactions_in_block(page=2, page_size=10)
```

## get a transaction by hash
```python
tx_hash = '937c3fb03b370557a8047f51c9efc2af17df2ed05fa48774c3105ef835133b3a'
tx = explorer.get_transaction(tx_hash)

t1 = 'e35d41072f68a9fc1afd21bd9577a36162175a6ee80f126e12ed955ac7ead7b9'
t2 = '8bf367738201bd51b65ec4212eeb57d9a7c5e7f569254df9a73c82fcd7b9ed93'
t3 = '265da4b0111ee0a65f81feb5467e0b73b939de7474fd01341058feaa16aee656'

txs = explorer.get_transactions([t1, t2, t3])
```

## get an address
```python
address_id = '15urYnyeJe3gwbGJ74wcX89Tz7ZtsFDVew'
address = explorer.get_address(address_id)
```

## get unspent transaction data of an address
```python
unspent_tx_data = explorer.get_unspent_transactions(address_id)
```

## get bitmain digital currency index
```python
index = explorer.get_digital_currency_index()
```
