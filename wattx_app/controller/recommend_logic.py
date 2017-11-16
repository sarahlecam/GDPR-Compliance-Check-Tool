from wattx_app.models import db
from wattx_app.models.models import Users, Questions, Responses


# Input company id and recommend logic
def rec_logic(c_id):
    # Get distinct section numbers from Questions table
    distinct_sec_nums = [s[0] for s in db.session.query(Questions.section).distinct()]
    print("Distinct sec nums: ", distinct_sec_nums)
    # Loop through each section
    for value in distinct_sec_nums:
        # Get distinct question id's
        distinct_questions = [q[0] for q in db.session.query(Questions.order).filter(Questions.section == value).distinct()]
        resp_vec = []
        # Generate corresponding responses for each question id
        for i in distinct_questions:
            v = Responses.query.filter(Responses.question_id == i).filter(Responses.company_id== c_id)
            resp_vec += [y.to_dict() for y in v]

        resp_sum = 0

        if len(resp_vec) > 0:
            print("Vec: ", resp_vec)

            # Logic to determine recommendation based on each response in the section
            for j in resp_vec:
                # Arbitrary criteria for a decision
                if j['response'] != 'Yes.':
                    resp_sum += 1
            print("Resp_sum: ", resp_sum)
            # Add to Recommendations table
    tmp = "Test string"
    return tmp
