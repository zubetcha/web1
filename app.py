from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def order_post():
   name_receive = request.form['name_give']
   qty_receive = request.form['qty_give']
   address_receive = request.form['address_give']
   cp_receive = request.form['cp_give']

   doc = {
       'name':name_receive,
       'qty':qty_receive,
       'address':address_receive,
       'cp':cp_receive
   }

   db.orders.insert_one(doc)

   return jsonify({'result':'success', 'msg': '주문이 완료되었습니다!'})

@app.route('/order', methods=['GET'])
def order_get():
    orders = list(db.orders.find({}, {'_id': False}))

    return jsonify({'all_orders':orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)