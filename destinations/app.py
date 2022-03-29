import os

from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from destinations import config

app = Flask(__name__)

db = SQLAlchemy()


def create_app():
    if os.environ.get("FLASK_ENV") == "production":
        pass
    else:
        app.config.from_object(config.DevelopmentConfig)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    Migrate(app, db)

    # register blueprints
    from destinations.places.views import place_blueprint
    app.register_blueprint(place_blueprint)
    return app


@app.route('/')
def home():
    return render_template('/index.html')
