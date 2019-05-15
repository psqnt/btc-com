import datetime

from explorer import explorer
from time import sleep


sleep_time = .25  # don't overstep rate limits
block = ''
# get latest block
block = explorer.get_block()
print(block)
sleep(sleep_time)

# get block by height
block = explorer.get_block(50)
print(block)
sleep(sleep_time)

# get block by hash
block = explorer.get_block(block.height)
print(block)
sleep(sleep_time)


# get blocks on specific date
yesterday = '20170512'
blocks = explorer.get_blocks_on_date(yesterday)
for block in blocks:
	print(block)
print(f'There were {len(blocks)} created on {yesterday} ')


# get transactions in a block with default payload
txs = explorer.get_transactions_in_block()
print(txs)
print('ffff')
# get transaction in a block with specific payload
txs = explorer.get_transactions_in_block(page=2, page_size=10)
print(txs)


# get a transaction by hash
tx_hash = '937c3fb03b370557a8047f51c9efc2af17df2ed05fa48774c3105ef835133b3a'
tx = explorer.get_transaction(tx_hash)
print(tx)

t1 = 'e35d41072f68a9fc1afd21bd9577a36162175a6ee80f126e12ed955ac7ead7b9'
t2 = '8bf367738201bd51b65ec4212eeb57d9a7c5e7f569254df9a73c82fcd7b9ed93'
t3 = '265da4b0111ee0a65f81feb5467e0b73b939de7474fd01341058feaa16aee656'

txs = explorer.get_transactions([t1, t2, t3])

for tx in txs:
	print(tx)


address_id = '15urYnyeJe3gwbGJ74wcX89Tz7ZtsFDVew'
address = explorer.get_address(address_id)
print(address)

unspent_tx_data = explorer.get_unspent_transactions(address_id)

print(unspent_tx_data)

index = explorer.get_digital_currency_index()
print(index)

