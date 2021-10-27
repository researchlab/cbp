from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

num = 10

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/nums/fetchNum')
def fetchNum():
    return jsonify({'num':num}) 

@app.route('/nums/updateNum', methods=['POST'])
def updateNum():
    global num
    # action 默认值为add
    action  = request.json.get('action',"add").strip()
    # step 默认值为 10
    step = request.json.get('step', 10)
    if action == 'add':
        num += 10
    elif action == 'div':
        num -= 20
    else:
        num += 100
    return jsonify({'num':num})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
