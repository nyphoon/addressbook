from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from model import setup_model
from api_addrbook import api_addrbook

app = Flask(__name__)
app.register_blueprint(api_addrbook, url_prefix='/api/addrbook')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///addrbook.sqlite3'
db = SQLAlchemy(app)
app.config['model'] = setup_model(db)
db.create_all()

app.run(debug=True)
