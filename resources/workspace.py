from flask import request, jsonify
from flask_restful import Resource
from http import HTTPStatus
from flask_jwt_extended import get_jwt_identity, jwt_required, jwt_optional

from Models.workspace import Workspace


class WorkspaceListResource(Resource):

    def get(self):
        workspaces = Workspace.get_all_published()
        data = []

        for workspace in workspaces:
            if workspace.is_publish is True:
                data.append(workspace.data())

            return {'data': data}, HTTPStatus.OK

    def post(self):
        json_data = request.get_json()
        current_user = get_jwt_identity()

        workspace = Workspace(name=json_data['name'],
                              workspace_type=json_data['workspace_type'],
                              size=json_data['size'],
                              address=json_data['address'],
                              user_id=current_user)

        workspace.save()

        return workspace.data(), HTTPStatus.CREATED


class WorkspaceResource(Resource):

    @jwt_optional
    def get(self, workspace_id):
        workspace = Workspace.get_by_id(workspace_id=workspace_id)
        if workspace is None:
            return {'message': 'workspace not found'}, HTTPStatus.NOT_FOUND
        current_user = get_jwt_identity()

        if workspace.is_publish == False and workspace.user_id != current_user:
            return {'message': 'Acces is not allowed'}, HTTPStatus.FORBIDDEN

        return workspace.data, HTTPStatus.OK

    @jwt_required
    def put(self, workspace_id):
        json_data = request.get_json()

        workspace = Workspace.get_by_id(workspace_id=workspace_id)

        if workspace is None:
            return {'message': 'workspace not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()
        if current_user != workspace.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        workspace.name = json_data['name']
        workspace.workspace_type = json_data['workspace_type']
        workspace.size = json_data['size']
        workspace.address = json_data['address']

        workspace.save()


        return workspace.data(), HTTPStatus.OK

    @jwt_required
    def delete(self, workspace_id):
        workspace = Workspace.get_by_id(workspace_id=workspace_id)

        if workspace is None:
            return {'message': 'workspace not found'}, HTTPStatus.NOT_FOUND
        current_user = get_jwt_identity()
        if current_user != workspace.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        workspace.delete()

        return {}, HTTPStatus.NO_CONTENT


class WorkspacePublishResource(Resource):

    def put(self, workspace_id):
        workspace = next((workspace for workspace in workspace_list if workspace.id == workspace_id), None)

        if workspace is None:
            return {'message': 'workspace not found'}, HTTPStatus.NOT_FOUND

        workspace.is_publish = True

        return {}, HTTPStatus.NO_CONTENT

    def delete(self, workspace_id):
        workspace = next((workspace for workspace in workspace_list if workspace.id == workspace_id), None)

        if workspace is None:
            return {'message': 'Workspace not found'}, HTTPStatus.NOT_FOUND

        workspace.is_publish = False

        return {}, HTTPStatus.NO_CONTENT
