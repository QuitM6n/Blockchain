from time import time
import json
import hashlib


class Blockhain(object):
    def __init__(self):
        self.chain = []
        self.transaction = []
        self.create_block(proof=1   , previous_hash='0')

    def create_block(self, proof, previous_hash=None):
        block = {'index': len(self.chain)+1,
                 'timestamp': time(),
                 'transaction': self.transaction,
                 'proof': proof,
                 'previous_hash': previous_hash,
                 }

        self.current_transactions = []
        self.chain.append(block)

        return block

    def new_transaction(self, sender, recipient, amount):
        self.transaction.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.get_previous_block['index']+1
    
    def get_previous_block(self):
        return self.chain[-1]
    
    def hash_block(self,block):
        to_hash = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(to_hash).hexdigest

    def proof_of_work(self, last_proof):
        proof = 0
        while self.block_IsValid(last_proof, proof) is False:
            proof += 1
        return proof
    
    @staticmethod
    def block_IsValid(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"