#!/usr/bin/env python3

import os
import connexion
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from backend import encoder

database_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.environ['DBUSER'],
    dbpass=os.environ['DBPASS'],
    dbhost=os.environ['DBHOST'],
    dbname=os.environ['DBNAME']
)

db = SQLAlchemy()
migrate = Migrate()


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.app.config.update(
        SQLALCHEMY_DATABASE_URI=database_uri,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    app.add_api('swagger.yaml', arguments={'title': 'www.jabber.ru api'}, pythonic_params=True)
    db.init_app(app.app)
    migrate.init_app(app.app, db)

    app.run(port=8080)


if __name__ == '__main__':
    main()
