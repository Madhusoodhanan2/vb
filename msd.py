from flask import Flask,render_template,request,redirect
import pymysql
app=Flask(__name__)
@app.route('/home')
def a():
    return "WELCOME FOR ONLINE TICKET"
@app.route('/')
def home():
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="app")
        ssql="select * from tickets"
        cu=db.cursor()
        cu.execute(ssql)
        data=cu.fetchall()
        db.commit()
        print(data)
        return render_template('dashboard.html',d=data)
    except Exception:
        print("the error is",Exception)


@app.route('/form')
def form():
    return render_template('form.html')
@app.route('/store',methods=['POST'])
def store():
    sa=request.form['name']
    zx=request.form['gender']
    xc=request.form['age']
    vb=request.form['journeydate']
    bn=request.form['class']
    nm=request.form['startingpoint']
    sd=request.form['destination']
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="app")
        insql="insert into tickets(name,gender,age,journeydate,class,startingpoint,destination)values('{}','{}','{}','{}','{}','{}','{}')".format(sa,zx,xc,vb,bn,nm,sd)
        cu=db.cursor()#execute sql queries
        cu.execute(insql)
        db.commit()
        return redirect('/')
    except Exception:
        print("Error is",Exception)

@app.route('/delete/<rid>')
def delete(rid):
    #return "Id is"+rid
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="app")
        cus=db.cursor()
        dsql="delete from tickets where id={}".format(rid)
        cus.execute(dsql)
        db.commit()
        return redirect('/')
    except Exception:
        print("The error is",Exception)
@app.route('/edit/<rid>')
def edit(rid):
    #return "ID is:"+rid
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="app")
        cu=db.cursor()
        sql="select * from tickets where id= '{}'".format(rid)
        cu.execute(sql)
        data=cu.fetchone()
        return render_template('editform.html',d=data)
        
    except Exception as e:
        print("Error:",e)
 
@app.route('/update/<rid>',methods=['POST'])
def update(rid):
    #return "ID to be  update in db is:"+rid
    sa=request.form['name']
    zx=request.form['gender']
    xc=request.form['age']
    vb=request.form['journeydate']
    bn=request.form['class']
    nm=request.form['startingpoint']
    sd=request.form['destination']
    #return sa+zx+xc+vb+bn+nm+sd
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="app")
        cu=db.cursor()
        sql="update tickets SET name='{}',gender='{}',age='{}',journeydate='{}',class='{}',startingpoint='{}',destination='{}' where id='{}'".format(sa,zx,xc,vb,bn,nm,sd,rid) 
        cu.execute(sql)
        db.commit()
        return redirect('/')
    except Exception as e:
        print("Error:",e)

app.run(debug=True)
