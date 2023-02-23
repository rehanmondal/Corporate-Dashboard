from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL
import time

app = Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "userwithdatabase"

mysql = MySQL(app)

@app.route('/', methods=['GET','POST'])
def dashboard():
    if request.method == 'POST':
        message = request.form.get('message')
        query = "Insert into support(message) values('{}')".format(message)
        cur = mysql.connection.cursor()
        cur.execute(query)
        mysql.connection.commit()
        cur.close()
    return render_template('dashboard.html')

@app.route('/newregistration', methods=['GET','POST'])
def newregistration():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = int(request.form.get('phone'))
        query = "Insert into user(userName,phone) values('{}',{})".format(name, phone)
        cur = mysql.connection.cursor()
        cur.execute(query)
        mysql.connection.commit()
        # cur.close()

        q = "select * from user where phone={}".format(phone)
        cur.execute(q)
        for row in cur:
            id = row[0]

            return render_template('newregistration.html',id=id)
    return render_template('newregistration.html')

@app.route('/view', methods =['GET','POST'])
def view():
    if request.method == 'POST':
        try:
            spu_id = int(request.form.get('spu_id'))
            cur = mysql.connection.cursor()
            q = "Select * from user where userId={}".format(spu_id)
            data = cur.execute(q)
            if data>0:
                details = cur.fetchall()
                return render_template('view.html',details =  details)
            else:
                return "<h2>The ID does not exists !</h2>"
        except:
            return "<h2>The ID does not exists ! You Must Check The ID must be Integer</h2>"
    return render_template('view.html')

@app.route('/admin', methods =['GET','POST'])
def admin():
    if request.method == 'POST':
        try:
            aid =int(request.form.get('aid'))
            apass = request.form.get('apass')
            cur = mysql.connection.cursor()
            q = "select * from adminofuser where id={} and password='{}'".format(aid, apass)
            cur.execute(q)
            if cur.rowcount>0:
                cur = mysql.connection.cursor()
                q = "Select * from user"
                cur.execute(q)
                details = cur.fetchall()
                return render_template('details.html', details=details)

            else:
                return "<h2>Invalid Admin Id Or Password !</h2>"
        except:
            return "<h3>Invalid Admin Id Or Password ! You Must Check Admin Id is Interger only<h3>"
    return render_template('admin.html')

@app.route('/details/<int:userId>',methods =['GET','POST'])
def ad_del(userId):

    query = "DELETE FROM user WHERE userId={}".format(userId)
    cur = mysql.connection.cursor()
    cur.execute(query)
    mysql.connection.commit()
    return "<h1>This user has been Deleteed Successfully.<h1>"

@app.route('/admin_update/<int:userId>',methods =['GET','POST'])
def ad_updt(userId):

    return render_template('update.html')

@app.route('/update',methods =['GET','POST'])
def update():
    if request.method =='POST':
        try:
            uid = int(request.form.get('uid'))
            uname = request.form.get('uname')
            uphone = int(request.form.get('uphone'))

            query = "Update user set userName='{}',phone ={} where userId={}".format(uname, uphone, uid)
            cur = mysql.connection.cursor()
            cur.execute(query)
            mysql.connection.commit()

        except:
            return "<h2>The ID does not exists ! </h2>"

    return render_template('update.html')

@app.route('/delete',methods =['GET','POST'])
def delete():
    if request.method == 'POST':
        try:
            del_id = int(request.form.get('del_id'))
            cur = mysql.connection.cursor()
            q = "Select * from user where userId={}".format(del_id)
            data = cur.execute(q)
            if data>0:
                del_id = del_id
                query = "Delete from user where userId={}".format(del_id)
                cur = mysql.connection.cursor()
                cur.execute(query)
                mysql.connection.commit()
                time.sleep(2)
                return "<h2Your Account has been deleted Succesfully.</h2>"
        except:
            return "<h2>The ID does not exists ! You Must Check The ID is Interger Only </h2>"

        else:
            time.sleep(1)
            return "<h2>The ID does not exists !</h2>"

    return render_template('delete.html')

@app.route('/<int:id>/admin_delete',methods =['GET','POST'])
def admin_delete(userId):
    if request.method == 'POST':
        query = "DELETE from user WHERE userId={}".format(userId)
        cur = mysql.connection.cursor()
        cur.execute(query)
        mysql.connection.commit()
        return redirect('/admin')
    return render_template('admin_delete.html')

if __name__ == "__main__":
    app.run(debug=True)
