import datetime
import hashlib
import json
from flask import Flask


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

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            # check previous hash
            if block['previous_hash'] != self.hash(previous_block):
                return False
            
            # check proof
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            
            previous_block =  block
            block_index += 1
        return True

app = Flask(__name__)

blockchain = Blockchain()

@app.route('/mine_block'i, method=['GET'])
def mine_block():
    pass
