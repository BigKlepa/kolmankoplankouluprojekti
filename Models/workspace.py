from extensions import db

workspace_list = []


def get_last_id():
    if workspace_list:
        last_workspace = workspace_list[-1]
    else:
        return 1
    return last_workspace + 1


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

#  testausta. don't panic