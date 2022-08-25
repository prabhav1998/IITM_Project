from flask import Flask,render_template

app = Flask('__name__')


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/endpoint')
def endpoint():
    return "Hello World"

@app.route('/linker')
def linker():
    return render_template('link.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
    #app.run(debug=True) #can alter host and port number here. Right now the default host is localhost and port is 5000
