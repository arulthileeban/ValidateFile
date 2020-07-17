from flask import Flask,request,url_for,render_template
import hashlib
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/file',methods=['GET','POST'])
def file():
    if request.method=="POST":
        ufile=request.files['ufile']
        curr='test'
        while curr!=b'':
            curr=ufile.read(1024)
            hasher.update(curr)
        return hasher.hexdigest()
    return render_template('file.html')

if __name__ == '__main__':
    hasher=hashlib.sha1()
    app.run()
