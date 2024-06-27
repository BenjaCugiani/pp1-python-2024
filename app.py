from flask import Flask, render_template, request

app = Flask(__name__)

listado_productos = [
    {
        'id': '1',
        'products': 'Gabinete',
        'category': 'Nuevo'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos', methods=['GET'])
def productos():
    return render_template('productos.html', productos=listado_productos)

@app.route('/productos/add', methods=['POST', 'GET'])
def agregar_producto():
    if request.method == 'POST':
        id = request.form['id']
        products = request.form['producto']
        category = request.form['categoria']
        
        nuevo_producto = {
            'id': id,
            'products': products,
            'category': category
        }
        
        listado_productos.append(nuevo_producto)
    
    return render_template('agregar_producto.html')

if __name__ == '__main__':
    app.run(debug=True)
