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
    
    def get_previous_block(self):
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
    # Blockchain class implemented 'create_block', which need two parameters: proof, previous_hash
    # We can get proof by calling 'proof_of_work', which requires 'previous_proof'.
    # 'previous_proof' is sitting in previous block, which we can get by calling 'get_previous_block'
    # 'previous_hash', we can get by calling blockchain.hash, which require previous block.
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_has = blockchain.hash(prevous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {
        'message': 'Congratulations, you just mined a block',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }
    return jsonify(response), 200

@app.route('/get_chaink'i, method=['GET'])
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

app.run(host = '0.0.0.0', port=5000)
