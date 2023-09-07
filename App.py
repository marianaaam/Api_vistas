from flaskr import create_app
from .modelos import db, Cancion, Usuario, Album, Medio, AlbumSchema
from flask_restful import Api
from .vistas import VistaCanciones, VistaCancion

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaCanciones, '/canciones')
api.add_resource(VistaCancion, '/canciones/<int:id_cancion>')

#with app.app_context():
    #Album_Schema = AlbumSchema()
    #A = Album(titulo='prueba', anio=1999, descripcion='texto', medio=Medio.CD)
    #db.session.add(A)
    #db.session.commit()
    #print([Album_Schema.dumps(album) for album in Album.query.all()])


#with app.app_context():
    #u = Usuario(nombre_usuario='Juan', contrasena='12345')
    #a = Album(titulo='prueba', anio=1999, descripcion='texto', medio=Medio.CD)
    #c = Cancion(titulo='mi cancion', minutos=1, segundos=15, interprete='Kiss')
    #u.albumes.append(a)
    #a.canciones.append(c)
    #db.session.add(u)
    #db.session.add(c)
    #db.session.commit()
    #print(Usuario.query.all())
    #print(Album.query.all()[0].canciones)
    #print(Cancion.query.all())
    #db.session.delete(a)
    #print(Album.query.all())
    #print(Cancion.query.all())

