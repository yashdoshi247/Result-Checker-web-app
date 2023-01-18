from flask import Flask,redirect,url_for,render_template,request

# WSGI Application
app = Flask(__name__)

@app.route("/") #Route Path
def welcome():
    return render_template('index.html')

@app.route("/subpath1")
def subpath1():
    return 'Welcome to subpath1'

@app.route("/res_dict/<int:score>")
def res_dict(score):
    res=""
    if score<=40:
        res="FAIL"
    else:
        res="PASS"
    exp = {'score':score,'result':res}
    return render_template("result.html",result=exp)
'''@app.route("/results/<int:marks>") #Dynamic URL
def results(marks):
    res=""
    if marks<40:
        res="Failed"
    else:
        res="Passed"
    return render_template('result.html',result=res, score=marks)
'''
@app.route("/submit", methods=['POST','GET'])
def submit():
    avg_score=0
    if request.method=='POST':
        phy=float(request.form['physics'])
        chem=float(request.form['chemistry'])
        math=float(request.form['math'])
        avg_score = (phy+chem+math)/3
    return redirect(url_for("res_dict",score=avg_score))


if __name__ == '__main__':
    app.run(debug=True)  #set debug=True to auto-restart code after update