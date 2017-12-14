import argparse
import wattx_app
import csv
import os
from wattx_app.models import models
from wattx_app.models.models import Questions, RecText

def cli():
    p = argparse.ArgumentParser()
    p.add_argument('--port', help='specify port to run on', dest='filepath_port')
    p.add_argument('--reset-db', help='drop and recreate db', dest='reset_db', action='store_true')
    p.add_argument('--import-ques', help='import questions from csv file', dest='filepath_ques')
    p.add_argument('--import-recs', help='import recommendations from csv file', dest='filepath_rec')

    args = p.parse_args()
    print(args)

    if args.reset_db:
        wattx_app.reset_db()

    port_num = None
    if args.filepath_port is not None:
        port_num = args.filepath_port

    if args.filepath_ques is not None:
        wattx_app.import_questions(os.path.abspath(args.filepath_ques))

    if args.filepath_rec is not None:
        wattx_app.import_recs(os.path.abspath(args.filepath_rec))

    app = wattx_app.create_app()

    # Check if Questions and RecText tables are filled. If not, fill them.
    with app.app_context():
        try:
            qns = Questions.query.first()
            print('Database exists')
        except:
            print('Resetting database')
            wattx_app.reset_db()


        # Questions table
        q = Questions.query.first()
        if q is None:
            print('Questions table is empty. Filling it up.')
            with open(os.path.abspath('questions.csv'), newline='') as f:
                reader = csv.reader(f, delimiter = ',')
                next(reader)
                for row in reader:
                    try:
                        descval = row[5]
                    except IndexError:
                        descval = 'null'
                    q = Questions(
                    question = row[0],
                    response_type = row[1],
                    order = row[2],
                    section = row[3],
                    section_name = row[4],
                    description = descval
                    )
                    models.db.session.add(q)
                models.db.session.commit()
        else:
            print('Questions table is not empty.')

        # RecText table
        r = RecText.query.first()
        if r is None:
            print('Recommendations table is empty. Filling it up.')
            with open(os.path.abspath('recommendations.csv'), newline='') as f:
                reader = csv.reader(f, delimiter=',')
                next(reader)
                for row in reader:
                    rt = RecText(
                    rec_text = row[0].strip(),
                    section = row[1],
                    completed = row[2]
                    )
                    models.db.session.add(rt)
                models.db.session.commit()
        else:
            print('Recommendations table is not empty.')
    #print(wattx_app.check_shit())

    return app
    # if port_num is not None:
    #     app.run(port=port_num)
    # else:
    #     app.run(debug=True)#, use_reloader=False)
    # Set use_reloader to flase, or debug=False to prevent reloading
    # and therefore duplication of questions into table

app = cli()

if __name__ == '__main__':
    app.run(debug=True)
