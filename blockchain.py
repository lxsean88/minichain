import datetime
import hashlib
import json


class Blockchain:

    def __init__(self):
        # a list to save the blocks
        self.chain = []
        # create first block
        self.create_block(proof = 1, previous_hash = '0')
    
    def create_block(self, proof, previous_hash):
        block = {
            # index always increased by 1
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block
    
    def get_prevous_block(self):
        return self.chain[-1]

    # blockchain mining, proof of work
    # we need something hard to find but easy to verify
    def proof_of_work(self, previous_proof):
        new_proof =  1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:4] = '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    def hash(self, block):
        encoded_block = json.dump(block, sort_keys =  True).encode()
        return hashlib.sha256(encoded_block).hexdigest()