from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
import time 
from ScriptController import ScriptController
app = Flask(__name__)
CORS(app)  # 允许所有域名访问

vins_controller = ScriptController('vinsfusion.sh')
bag_controller = ScriptController('bag.sh')

@app.route('/hello', methods=['POST'])
def hello():
    print("hello")
    threading.Thread(target=start_scripts).start()
    return jsonify({"message": "Hello received!"}), 200

def start_scripts():
    vins_controller.start()
    time.sleep(1)
    bag_controller.start()

@app.route('/stop', methods=['POST'])
def stop():
    bag_controller.stop()
    vins_controller.stop()
    return jsonify({"message": "Scripts stopped!"}), 200  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
