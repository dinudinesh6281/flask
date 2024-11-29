from flask import Flask,render_template
FI=Flask(__name__)

@FI.route('/first')
def first():
    return 'this is my fist flaskproject'


@FI.route('/second')
def second():
    return render_template('pro.html')

@FI.route('/wish')
def wish():
    return render_template('pro1.html',name='dinu')

@FI.route('/hello/<data>')
def hello(data):
    return f'hlo macha {data}'

@FI.route('/img')
def img():
    return render_template('img.html')



if __name__=='__main__':
    FI.run(debug=True,host='192.168.18.140',port=5001)