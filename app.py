from flask import Flask, jsonify, request

productos = [
    {"name":"laptop","price":1200,"quantity":4},
    {"name":"mouse","price":90,"quantity":7},
    {"name":"keyboard","price":120,"quantity":10},
    {"name":"monitor","price":300,"quantity":5}
]

app = Flask(__name__)

@app.route("/productos", methods=['GET'])
def listar_productos():
    return jsonify({"productos":productos})


@app.route("/productos/<string:nombre>")
def obtener_producto(nombre):
    productsFound = [p for p in productos if p['name'] == nombre]
    if len(productsFound) > 0:
        return jsonify(productsFound)
    return jsonify({"message" : "Producto no encontrado"})


@app.route('/productos', methods=['POST'])
def agregar_producto():
    nuevo_producto = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }

    productos.append(nuevo_producto)
    return jsonify({"message": "Producto agregado correctamente"})


@app.route('/productos/<string:nombre>', methods=['PUT'])
def editar_producto(nombre):
    productFound = [p for p in productos if p['name'] == nombre]
    if len(productFound) > 0:
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        print(productFound[0])
        return jsonify({
            "message": "Producto Actualizado",
            "producto": productFound[0]
        })
    return jsonify({"message": "Producto a editar no encontrado"})


@app.route('/productos/<string:nombre>', methods=['DELETE'])
def eliminar_producto(nombre):
    productFound = [p for p in productos if p['name'] == nombre]
    if len(productFound) > 0:
        productos.remove(productFound[0])
        return jsonify({"message":"Producto eliminado correctamente"})
    return jsonify({"message":"Producto a eliminar no encontrado"})


if __name__ == '__main__':
    app.run(debug=True)