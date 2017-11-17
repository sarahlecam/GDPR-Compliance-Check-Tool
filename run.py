import argparse
import wattx_app
import os

def cli():
    p = argparse.ArgumentParser()
    p.add_argument('--reset-db', help='drop and recreate db', dest='reset_db', action='store_true')
    p.add_argument('--import-ques', help='import questions from csv file', dest='filepath_ques')
    p.add_argument('--import-recs', help='import recommendations from csv file', dest='filepath_rec')

    args = p.parse_args()

    if args.reset_db:
        wattx_app.reset_db()

    if args.filepath_ques is not None:
        wattx_app.import_questions(os.path.abspath(args.filepath_ques))

    if args.filepath_rec is not None:
        wattx_app.import_recs(os.path.abspath(args.filepath_rec))

    app = wattx_app.create_app()
    app.run(debug=True, use_reloader=False)
    # Set use_reloader to flase, or debug=False to prevent reloading
    # and therefore duplication of questions into table


if __name__ == '__main__':
    cli()
