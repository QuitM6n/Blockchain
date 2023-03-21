from flask import Flask, jsonify, request, render_template
import blockchain as blok
import database as db 


app = Flask(__name__)
blockchain_t = blok.Blockhain()

@app.route('/new/transaction', methods=["GET", "POST"])
def new_transaction():
    if request.method == "POST": 
        sender = request.form.get("sender")
        recipient = request.form.get("recipient")
        amount = request.form.get("amount")
        db.insert_transaction(sender,recipient,amount)
        index = blockchain_t.new_transaction(sender, recipient, amount)
        response = {'message': f'Transaction will be added to Block {index}'}
    return render_template("index.html")


@app.route('/get/block', methods=['GET'])
def get_block():
    last_block = blockchain_t.get_previous_block
    last_proof = last_block['proof']
    proof = blockchain_t.proof_of_work(last_proof)

    blockchain_t.new_transaction(
        sender='0',
        recipient="node_identifier",
        amount=1
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
