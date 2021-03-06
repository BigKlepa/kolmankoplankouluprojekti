from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from Config import Config
from extensions import db, jwt
from resources.reservation import ReservationListResource, ReservationResource, ReservationPublishResource
from resources.user import UserListResource, UserResource, MeResource
from resources.workspace import WorkspaceListResource, WorkspaceResource, WorkspacePublishResource
from resources.token import TokenResource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_resources(app)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt.init_app(app)


def register_resources(app):
    api = Api(app)

    api.add_resource(UserListResource, '/users')
    api.add_resource(UserResource, '/users/<string:username>')
    api.add_resource(TokenResource, '/token')
    api.add_resource(MeResource, '/me')
    api.add_resource(WorkspaceListResource, '/workspaces')
    api.add_resource(WorkspaceResource, '/workspaces/<int:workspace_id>')
    api.add_resource(WorkspacePublishResource, '/workspaces/<int:workspace_id>/publish')
    api.add_resource(ReservationListResource, '/reservations')
    api.add_resource(ReservationResource, '/workspaces/<int:reservation_id>')
    api.add_resource(ReservationPublishResource, '/reservations/<int:reservation_id>/publish')


if __name__ == '__main__':
    app = create_app()
    app.run()
