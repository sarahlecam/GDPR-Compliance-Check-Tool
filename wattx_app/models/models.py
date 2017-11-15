from wattx_app.models import db

class Users(db.Model):
    '''class representation of Enterprise record'''

    company_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String())
    password = db.Column(db.String())
    created = db.Column(db.DateTime, default=db.func.now())
    responses = db.relationship('Responses')


    def to_dict(self):
        '''return a dictionary representation of an Enterprise'''

        return {
            'company_id' : self.company_id,
            'company_name' : self.company_name,
            'email' : self.email,
            'password' : self.password,
        }

class Questions(db.Model):
    ''' contains survey questions for companies'''
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String())
    response_type = db.Column(db.Integer)
    order = db.Column(db.Integer)
    section = db.Column(db.Integer)
    section_name = db.Column(db.String())
    description = db.Column(db.String())

    def to_dict(self):
        return {
            'id' : self.id,
            'question' : self.question,
            'response_type' : self.response_type,
            'order' : self.order,
            'section' : self.section,
            'section_name' : self.section_name,
            'description' : self.description
        }

class Responses(db.Model):
    '''contains responses to survey questions for each company'''
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey(Questions.order))
    company_id = db.Column(db.Integer, db.ForeignKey(Users.company_id))
    response = db.Column(db.String())

    def to_dict(self):
        return {
            'id' : self.id,
            'question_id' : self.question_id,
            'company_id' : self.company_id,
            'response' : self.response
        }



class Recommendations(db.Model):
    ''' contains recommendations for each section of questions/responses '''
    id = db.Column(db.Integer, primary_key=True)
