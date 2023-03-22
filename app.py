from flask import Flask, jsonify, request, render_template
import blockchain as block
import database as db
import json

app = Flask(__name__)
blockchain_t = block.Blockhain()

@app.route('/new/transaction', methods=["GET", "POST"])
def new_transaction():
    if request.method == "POST":
        sender = request.form.get("sender")
        recipient = request.form.get("recipient")
        amount = request.form.get("amount")
        db.insert_transaction(sender, recipient, amount)
        index = blockchain_t.new_transaction(sender, recipient, amount)
        response = {'message': f'Transaction will be added to Block {index}'}
    return render_template("index.html")


@app.route('/get/block', methods=['GET'])
def get_block():
     previous_block = blockchain_t.get_previous_block()
     previous_proof = previous_block['proof']
     proof = blockchain_t.proof_of_work(previous_proof)
     previous_hash = blockchain_t.hash_block(previous_block)
     block = blockchain_t.create_block(proof, previous_hash)
 
     response = {'message': 'A block is MINED',
                  'index': str(block['index']),
                  'timestamp': str(block['timestamp']),
                 'proof': str(block['proof']),
                 'previous_hash': str(block['previous_hash'])}
     return jsonify(response), 200

if __name__ == '__main__':
    app.run()
