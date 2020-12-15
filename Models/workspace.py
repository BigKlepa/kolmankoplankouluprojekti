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
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    workspace_type = db.Column(db.String(100), nullable=False)
    size = db.Column(db.Integer)
    address = db.Column(db.String(100))
    is_publish = db.Column(db.Boolean(), default=False)




@property
def data(self):
    return {
        'id': self.id,
        'name': self.name,
        'workspace_type': self.workspace_type
    }

#  testausta. don't panic