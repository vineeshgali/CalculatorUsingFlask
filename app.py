from flask import Flask,request,render_template,jsonify
app= Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def homepage():
   return render_template('index.html')

@app.route('/math', methods=['POST'])
def math():
    if(request.method == 'POST'):
       ops = request.form['operation'] 
       num1= request.form['num1']
       num2= request.form['num2']
       if(ops=="add"):
          r = int(num1) + int(num2)
          result = "the sum of " + num1 + " and " + num2 + " is " + str(r)
       if(ops=="subtract"):
          r = int(num1) - int(num2)
          result = "the subtraction of " + num1 + " and " + num2 + " is " + str(r)
       if(ops=="multiply"):
          r = int(num1) * int(num2)
          result = "the multiplication of " + num1 + " and " + num2 + " is " + str(r)
       if(ops=="divide"):
          r = int(num1) / int(num2)
          result = "the division of " + num1 + " and " + num2 + " is " + str(r)
       return render_template('result.html', result=result)
       
if __name__ == '__main__':
    app.run(host='0.0.0.0')