# WATTx-Team
Code and team repository for CheckMate, a GDPR compliance checklist service.

## Usage
To enter your virtual environment:
`source activate wattx-env`

To first establish a cleared database run:
`python run.py --reset-db`

To import the questions.csv file into the database:
`python run.py --import-ques questions.csv`

To import the recommendations.csv file into the database:
`python run.py --import-recs recommendations.csv`

To run the server after set up:
`python run.py`
