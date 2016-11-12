import web
import json 
render = web.template.render('views/')

urls=(
    '/home(.*)','index'
)
def GET(self, datos):
        datos =[]
        with open('data.json','r') as file:
            datos=json.load(file)
        return render.tnp(datos['results'])
if __name__ == "__main__":
    app = web.application(urls, globals())
    web.config.debug = True
    app.run()