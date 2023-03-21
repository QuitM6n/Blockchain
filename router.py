from flask import Flask, jsonify, request
import blockchain as blok


app = Flask(__name__)
blockchain_t = blok.Blockhain()

@app.route('/new/transaction', methods=['POST'])
def new_transaction():
    values = request.get_json()
    
    required = ['sender','recipient','amount']
    if not all(k in values for k in required):
            return 'Missing values',400
    
    index = blockchain_t.new_transaction(values['sender'],values['recipient'],values['amount'])
    response = {'message':f'Transaction will be added to Block {index}'}

    return jsonify(response),201

@app.route('/get/block', methods=['GET'])
def get_block():
    last_block = blockchain_t.get_previous_block
    last_proof =last_block['proof']
    proof  = blockchain_t.proof_of_work(last_proof)
    
    blockchain_t.new_transaction(
         sender='0',
         recipient="node_identifier",
         amount = 1 
    )

    previous_hash = blockchain_t.hash_block(last_block)
    block = blockchain_t.create_block(proof, previous_hash)
 
    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transaction'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run()
