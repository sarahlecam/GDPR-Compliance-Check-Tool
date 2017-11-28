from wattx_app.models import db
from wattx_app.models.models import Users, Questions, Responses, RecText, Recommendations

# Input company id and recommend logic
def rec_logic(c_id, sec):

    # Get distinct question id's
    distinct_questions = [q[0] for q in db.session.query(Questions.order).filter(Questions.section == sec).distinct()]
    resp_vec = []
    # Generate corresponding responses for each question id
    for i in distinct_questions:
        v = Responses.query.filter(Responses.question_id == i).filter(Responses.company_id== c_id).all()
        resp_vec += [y.to_dict() for y in v]

    resp_sum = 0
    if len(resp_vec) > 0:
        # Logic to determine recommendation based on each response in the section
        for j in resp_vec:
            # Arbitrary criteria for a decision. If not yes, then add to resp_sum
            if j['response'] != 'true':
                resp_sum += 1
        # Set Yes/No (yn) variable depending on number of 'No' responses
        if resp_sum > 0:
            yn = 0
        else:
            yn = 1
        rt = RecText.query.filter(RecText.section == sec).filter(RecText.completed == yn).first()
        rt_dict = rt.to_dict()
        # Return recommendation string
        return rt_dict['rec_text'], yn
    return "", 0
