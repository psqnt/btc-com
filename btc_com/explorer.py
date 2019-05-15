import requests
from datetime import datetime
from . import util


class Address:
    """
    Bitcoin address util
    """
    def __init__(self, address):
        self.address = address['address']
        self.received = address['received']
        self.sent = address['sent']
        self.balance = address['balance']
        self.tx_count = address['tx_count']
        self.unconfirmed_tx_count = address['unconfirmed_tx_count']
        self.unconfirmed_received = address['unconfirmed_received']
        self.unconfirmed_sent = address['unconfirmed_sent']
        self.unspent_tx_count = address['unspent_tx_count']
        self.first_tx = address['first_tx']
        self.last_tx = address['last_tx']
    
    def __str__(self):
        """
        Return a string representation of this
        """
        address = f'address: {self.address}\n' \
                  f'balance: {self.balance}\n' \
                  f'tx count: {self.tx_count}\n'
        return address


class UnspentTransaction:
    """
    Unspent Transaction data util
    """
    def __init__(self, unspent):
        self.total_count = unspent['total_count']
        self.page = unspent['page']
        self.pagesize = unspent['pagesize']
        self.list = unspent['list']

    def __str__(self):
        """
        Return string representation this
        """
        unspent = f'unspent count: {self.total_count}\n'
        return unspent


class Block:
    """
    Bitcoin block util
    """
    def __init__(self, block):
        self.height = block['height']
        self.version = block['version']
        self.merkle_root = block['mrkl_root']
        self.curr_max_timestamp = block['curr_max_timestamp']
        self.timestamp = block['timestamp']
        self.bits = block['bits']
        self.nonce = block['nonce']
        self.hash = block['hash']
        self.prev_block_hash = block['prev_block_hash']
        self.next_block_hash = block['next_block_hash']
        self.size = block['size']
        self.pool_difficulty = block['pool_difficulty']
        self.pool_difficulty = block['difficulty']
        self.tx_count = block['tx_count']
        self.reward_block = block['reward_block']
        self.reward_fees = block['reward_fees']
        self.created_at = block['created_at']
        self.confirmations = block['confirmations']
        self.extras = block['extras']

    def __str__(self):
        """
        Return a string representation of bitcoin block
        """
        block = f'height: {self.height},\n' \
                f'version: {self.version},\n' \
                f'timestamp: {self.timestamp}' \
                f'tx count: {self.tx_count}'
        return block


class Transaction:
    """
    Bitcoin Transaction util
    """
    def __init__(self, tx):
        self.block_height = tx['block_height']
        self.block_time = tx['block_time']
        self.created_at = tx['created_at']
        self.fee = tx['fee']
        self.hash = tx['hash']
        self.id = self.hash
        self.inputs = tx['inputs']  # can make this a class?/dict?
        self.inputs_count = tx['inputs_count']
        self.inputs_value = tx['inputs_value']
        self.is_coinbase = tx['is_coinbase']
        self.lock_time = tx['lock_time']
        self.outputs = tx['outputs']
        self.outputs_count = tx['outputs_count']
        self.outputs_value = tx['outputs_value']
        self.size = tx['size']
        self.version = tx['version']

    def __str__(self):
        """
        Return a string representation of transaction
        """
        tx = f'hash: {self.hash}\n' \
             f'created: {self.created_at}\n' \
             f'block height: {self.block_height}\n'
        return tx


class BitmainIndex:
    """
    Bitmain Crypto Index util
    """
    def __init__(self, index):
        self.timestamp = index['timestamp']
        self.index = index['index']
        self.sign = index['sign']

    def __str__(self):
        """
        Return string representation of this
        """
        index = f'Index: {self.index}\n' \
                f'Timestamp: {self.timestamp}'
        return index


def get_block(block='latest'):
    """
    Request a block
    :param arg: height, hash, 'latest'
    :return: an instance of :class:`Block` class
    """
    resource = f'block/{block}'
    response = util.call_api(resource)
    return Block(response)


def get_blocks_on_date(ymd):
    """
    Request a list of blocks created on a specific date

    Get block list on 12/15/2015: 
    
    param: ymd -> '20151215'

    :param str ymd: a string representation of a date
    :return list: a list of :class:`Block` objects
    """
    resource = f'block/date/{ymd}'
    response = util.call_api(resource)
    blocks = []
    for block in response:
        blocks.append(Block(block))
    return blocks


def get_transactions_in_block(block='latest', page='1', page_size='50'):
    """
    Get transactions from a specific block. default is latest

    :param str block: block specified by height
    :param str page: number of 'pages' of txs being requested
    :param str page_size: number of txs per 'page' 
    """
    resource = f'block/{block}/tx'
    payload = {'page': page, 'pagesize': page_size}
    print(resource, payload)
    response = util.call_api(resource=resource, payload=payload)
    return response


def get_transaction(tx_hash):
    """
    Request transaction data
    :param str tx_hash: hash/id of a bitcoin transaction
    :return: an instance of :class:`Transaction` class
    """
    resource = f'tx/{tx_hash}'
    response = util.call_api(resource)
    return Transaction(response)


def get_transactions(tx_hashes):
    """
    Request multiple transactions at once
    :param list tx_hashes: a list of transaction hashes
    :return: a list of Transaction objects
    """
    resource = f'tx/'
    for tx_hash in tx_hashes:
        resource += f'{tx_hash},'
    resource = resource[:-1]  # remove last comma
    response = util.call_api(resource)
    txs = []
    for tx in response:
        txs.append(Transaction(tx))
    return txs


def get_unconfirmed_txs():
    """
    Request a list of unconfirmed transaction hashes
    :return list: of strings
    """
    resource = f'tx/unconfirmed'
    response = util.call_api(resource)
    return response


def get_unconfirmed_txs_summary():
    """
    Request a summary of unconfirmed txs, size/count
    :return: dict
    """
    resource = f'tx/unconfirmed/summary'
    response = util.call_api(resource)
    return response


def get_address(address):
    """
    Request information about a bitcoin address
    :param str address: an address hash/id
    :return: an instance of Address class
    """
    resource = f'address/{address}'
    response = util.call_api(resource)
    return Address(response)


def get_address_transactions(address):
    """
    Request transactions made by an address
    :param str address: an addresss hash/id
    :return: a list of Transasction objects
    """
    resource = f'address/{address}/tx'
    response = util.call_api(resource)
    txs = []
    for tx in response:
        txs.append(Transaction(tx))
    return txs


def get_unspent_transactions(address):
    """
    Request unspent transactions for an address
    :param str address: an address hash/id
    :return: list of Transaction objects
    """
    resource = f'address/{address}/unspent'
    response = util.call_api(resource)
    return UnspentTransaction(response)


def get_digital_currency_index(timestamp=None):
    """
    Request digital currency index
    :param int timestamp: int timestamp
    :return: an instance of BitmainTicker class
    """
    if timestamp is None:
        now = datetime.utcnow()
        timestamp = int(datetime.timestamp(now))
    url = f'https://index.btc.com/api/cryptoindex/signindex?timestamp={timestamp}'
    response = requests.get(url).json()['data']
    return BitmainIndex(response)
