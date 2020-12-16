from flask import request, jsonify
from flask_restful import Resource
from http import HTTPStatus

from Models.reservation import Reservation, reservation_list


class ReservationListResource(Resource):

    def get(self):
        data = []

        for reservation in reservation_list:
            if reservation.is_publish is True:
                data.append(reservation.data)

            return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()

        reservation = Reservation(user_id=data['user_id'],
                                  workspace_id=data['workspace_id'],
                                  start_time=data['start_time'],
                                  )

        reservation_list.append(reservation)

        return reservation.id, HTTPStatus.CREATED


class ReservationResource(Resource):

    def get(self, reservation_id):
        reservation = next((reservation for reservation in reservation_list if reservation.id == reservation_id
                          and reservation.is_publish == True), None)
        if reservation is None:
            return {'message': 'reservation not found'}, HTTPStatus.NOT_FOUND

        return reservation.data, HTTPStatus.OK

    def put(self, reservation_id):
        data = request.get_json()

        reservation = next((reservation for reservation in reservation_list if reservation.id == reservation_id), None)

        if reservation is None:
            return {'message': 'reservation not found'}, HTTPStatus.NOT_FOUND

        reservation.workspace_id = data['workspace_id']
        reservation.start_time = data['start_time']

        return reservation.data, HTTPStatus.OK

    def delete(self, reservation_id):
        reservation = next((reservation for reservation in reservation_list if reservation.id == reservation_id), None)

        if reservation is None:
            return {'message': 'reservation not found'}, HTTPStatus.NOT_FOUND

        reservation_list.remove(reservation)

        return {}, HTTPStatus.NO_CONTENT


class ReservationPublishResource(Resource):

    def put(self, reservation_id):
        reservation = next((reservation for reservation in reservation_list if reservation.id == reservation_id), None)

        if reservation is None:
            return {'message': 'reservation not found'}, HTTPStatus.NOT_FOUND

        reservation.is_publish = True

        return {}, HTTPStatus.NO_CONTENT

    def delete(self, reservation_id):
        reservation = next((reservation for reservation in reservation_list if reservation.id == reservation_id), None)

        if reservation is None:
            return {'message': 'Reservation not found'}, HTTPStatus.NOT_FOUND

        reservation.is_publish = False

        return {}, HTTPStatus.NO_CONTENT
