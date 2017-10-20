from wattx_app.models import db

class Enterprise(db.Model):
    '''class representation of Enterprise record'''

    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer)
    company_name = db.Column(db.String(), nullable=False)
    data_type = db.Column(db.String())
    reason = db.Column(db.String())
    shared = db.Column(db.Boolean)
    uploaded = db.Column(db.DateTime, default=db.func.now())


    def to_dict(self):
        '''return a dictionary representation of an Enterprise'''

        return {
            'id' : self.id,
            'company_id' : self.company_id,
            'company_name' : self.company_name,
            'data_type' : self.data_type,
            'reason' : self.reason,
            'shared' : self.shared,
            'uploaded' : self.uploaded
        }
