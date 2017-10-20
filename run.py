import argparse
import wattx_app

def cli():
    p = argparse.ArgumentParser()
    p.add_argument('--reset-db', help='drop and recreate db', dest='reset_db', action='store_true')

    args = p.parse_args()

    if args.reset_db:
        wattx_app.reset_db()

    app = wattx_app.create_app()
    app.run(debug=True)


if __name__ == '__main__':
    cli()
