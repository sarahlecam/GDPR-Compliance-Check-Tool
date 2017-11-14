from wattx_app.models import db

class Enterprise(db.Model):
    '''class representation of Enterprise record'''

    company_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(), nullable=False)
    address = db.Column(db.String())
    contact = db.Column(db.String())
    website = db.Column(db.String())
    dpo_name = db.Column(db.String())
    dpo_contact = db.Column(db.String())
    company_type = db.Column(db.String())

    def to_dict(self):
        '''return a dictionary representation of an Enterprise'''

        return {
            'company_id' : self.company_id,
            'company_name' : self.company_name,
            'address' : self.address,
            'contact' : self.contact,
            'website' : self.website,
            'dpo_name' : self.dpo_name,
            'dpo_contact' : self.dpo_contact,
            'company_type' : self.company_type
        }


class EnterpriseData(db.Model):
    '''class representation of Enterprise record'''

    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer)
    data_type = db.Column(db.String())
    reason = db.Column(db.String())
    shared = db.Column(db.Boolean)
    uploaded = db.Column(db.DateTime, default=db.func.now())


    def to_dict(self):
        '''return a dictionary representation of an Enterprise'''

        return {
            'id' : self.id,
            'company_id' : self.company_id,
            'data_type' : self.data_type,
            'reason' : self.reason,
            'shared' : self.shared,
            'uploaded' : self.uploaded
        }

class Questions(db.Model):
    ''' contains survey questions for companies'''
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String())
    responseType = db.Column(db.String())
    order = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id' : self.id,
            'question' : self.question,
            'responseType' : self.responseType,
            'order' : self.order
        }
#
# class QuestionResponses(db.model):
#     '''contains responses to survey questions for each company'''
#     id = db.Column(db.Integer, primary_key=true)
