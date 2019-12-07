from flask import Flask, render_template, request, json 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route('/Acercade')
def about():
    return render_template("about.html")

@app.route('/signup',methods=["POST"])
def signup():
    return render_template("formulario.html")

@app.route('/signUpUser',methods=["POST"])
def signupuser():
    nombre = request.form['nom']
    trol = request.form['trol']
    #return render_template("mensaje.html",nom=nombre,ctrol=trol)
    return 
@app.route('/Articulos/')
def articulos():
    return "<h1>Articulos</h1>"

@app.route('/Articulos/<id>')
def lista_articulos(id):
    return "<h1>Consulta de articulo: {}</h1>".format(id)

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Pagina no encontrada</h1>"

if __name__ == "__main__":
    app.run(port=80,debug=True)