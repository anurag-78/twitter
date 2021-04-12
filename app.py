from flask import Flask, request, render_template 
import tweety
 
app = Flask(__name__)
tweeterhandle=''
@app.route('/', methods = ['GET','POST'])
def index():
    global tweeterhandle
    if request.method == 'POST':
        tweeterhandle = request.form.get("handle")
        tweety.main(tweeterhandle)
        print(tweeterhandle)

    return render_template("index.html")


@app.route('/about',methods = ['GET','POST'])
def about():
       return render_template("about.html")
    


@app.route('/additionals',methods = ['GET','POST'])
def additionals():
       return render_template("additionals.html")
    

@app.route('/contact',methods = ['GET','POST'])
def contact():
       return render_template("contact.html")




if __name__ == "__main__":
    app.run( debug=True)