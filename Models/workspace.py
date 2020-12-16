from extensions import db

# commit Joni



class Workspace(db.Model):

    __tablename__ = 'workspace'
    id = db.Column(db.Integer, primary_key=True)  # generoitu
    name = db.Column(db.String(100), nullable=False)  # huoneen nimi, esim. Alpha tai B1032
    workspace_type = db.Column(db.String(100), nullable=False)  # esim. luentosali, kaytava, luokka
    size = db.Column(db.Integer)  # työtilan arvioitu kantokyky
    address = db.Column(db.String(100))  # esim. lemminkäisenkatu, ICT-talo, Joukahaisenkatu
    is_publish = db.Column(db.Boolean(), default=False)




@property
def data(self):
    return {
        'id': self.id,
        'name': self.name,
        'workspace_type': self.workspace_type,
        'size': self.size,
        'address': self.address
    }

@classmethod
def get_all_published(cls):
    return cls.query.filter_by(is_publish=True).all()

@classmethod
def get_by_id(cls, workspace_id):
    return cls.query.filter_by(id=workspace_id).first()

def save(self):
    db.session.add(self)
    db.session.commit()

def delete(self):
    db.session.delete(self)
    db.session.commit()


#  testausta. don't panic