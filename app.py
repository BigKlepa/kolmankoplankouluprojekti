from flask import Flask, jsonify, request
from flask_restful import Api
from flask_migrate import Migrate

from Config import Config
from extensions import db
from Models.user import User
from Models.workspace import workspace_list
from resources.workspace import WorkspaceListResource, WorkspaceResource, WorkspacePublishResource


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_resources(app)

    return app
def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)

def register_resources(app):
    api = Api(app)

    api.add_resource(WorkspaceListResource, '/workspaces')
    api.add_resource(WorkspaceResource, '/workspaces/<int:workspace_id>')
    api.add_resource(WorkspacePublishResource, '/workspaces/<int:workspace_id>/publish')





if __name__ == '__main__':
    app = create_app()
    app.run(port=5000, debug=True)