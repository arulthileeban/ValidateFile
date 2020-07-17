from flask import Flask,request,url_for,render_template
import hashlib
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/file',methods=['GET','POST'])
def file():
    shasher=hashlib.sha1()
    mhasher=hashlib.md5()
    if request.method=="POST":
        ufile=request.files['ufile']
        hash=request.form['hash']
        og_hash=request.form['trhash']
        for line in iter(ufile):
            if hash=="sha1":
                shasher.update(line)
            elif hash=="md5":
                mhasher.update(line)
        final_hash=shasher.hexdigest() if hash=="sha1" else mhasher.hexdigest()
        if final_hash==og_hash:
            return "File is incorrupted. Calculated hash is: "+final_hash
        else:
            return "File is corrupted. Calculated hash is: "+final_hash
    return render_template('file.html')

if __name__ == '__main__':
    app.run()
