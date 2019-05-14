from . import util


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


def get_block(block='latest'):
    """
    Request a block
    :param arg: height, hash, 'latest'
    :return: an instance of :class:`Block` class
    """
    resource = f'block/{block}'
    response = util.call_api(resource)
    return Block(response)


block = get_block()
print(block.height, block.hash)
