import flask
import json


class Persona:
    def __init__(self, nombre, rut):
        self.nombre = nombre
        self.rut = rut
        self.id = next(Persona.pid)

    def get_id(self):
        pid = 0
        while True:
            yield pid
            pid += 1

    pid = get_id()


app = flask.Flask(__name__)

# El recurso solo responderá al método GET
@app.route('/api', methods=['GET'])
def api_echo():
    p = Persona('Jason Kruger', '20.000.000-0')
    resp = flask.Response(json.dumps(p.__dict__), status=200)

    return resp

if __name__ == '__main__':
    app.run(port=80)  # el servicio estará disponible por el puerto 8080