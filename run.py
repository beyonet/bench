import os
#from flask_migrate import Migrate

from app import create_app#, db


#config_name = os.getenv('FLASK_CONFIG')
config_name = 'production'
app = create_app(config_name)

#migrate = Migrate(app, db)

app.jinja_env.auto_reload = True

if __name__ == '__main__':
    app.run(debug=True)
