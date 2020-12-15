from extensions import db
import datetime

class Reservation(db.Model):
    __tablename__ = 'reservation'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))
    workspace_id = db.Column(db.Integer(), db.ForeignKey("workspace.id"))
    start_time = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    end_time = db.Column(db.DateTime(), nullable=False, server_default=start_time + datetime.timedelta(hours=1))
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def save(self):
        db.session.add(self)
        db.session.commit()