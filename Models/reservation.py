from extensions import db
from datetime import datetime, timedelta

reservation_list = []


def get_last_id():
    if reservation_list:
        last_reservation = reservation_list[-1]
    else:
        return 1
    return last_reservation + 1


class Reservation(db.Model):

    __tablename__ = 'reservation'

    id = db.Column(db.Integer, primary_key=True)  # generoitu
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))  # varauksen tekijän id
    workspace_id = db.Column(db.Integer(), db.ForeignKey("workspace.id"))  # työtilan id

    # default lähinnä testinä, todellisuudessa ei tietty voi varata tilaa ilman aikaa
    start_time = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())  # aloitusaika

    # defaultend = db.func.now() + timedelta(hours=1)
    # server_default= defaultend
    # ilmesesti sqalkemian timestamp-hässäkkä ei ole yhteensopiva pythonin oman timestamp-hässäkän kanssa
    end_time = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())  # lopetusaika
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(username=id).first()

    @classmethod
    def get_by_user_id(cls, user_id):
        return cls.query.filter_by(email=user_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
