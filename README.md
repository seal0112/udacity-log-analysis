# Udacity Logs Analysis Project
This project is a simple CLI reporting tool based on tables in a PostgreSQL database.

The tool runs three reports for answers to the following questions:
- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

## Quick start

First you must have the PostgreSQL newsdata.sql database running from the FSND virtual machine.

- From the 'vagrant' directory, run ```vagrant up```.
- SSH to the virtual machine with ```vagrant ssh```.
- Connect to the psql database with ```psql -d news -f newsdata.sql```
- Than we can be able to run the reporting tool as:
```bash
python log_analysis.py
```

## Example output
```bash
What are the most popular three articles of all time?
    "Candidate is jerk, alleges rival" — 342102 views
    "Bears love berries, alleges bear" — 256365 views
    "Bad things gone, say good people" — 171762 views
Who are the most popular article authors of all time?
    Ursula La Multa — 507594 views
    Rudolf von Treppenwitz — 423457 views
    Anonymous Contributor — 170098 views
    Markoff Chaney — 84557 views
On which days did more than 1% of requests lead to errors?
    July 17, 2016 — 2.3% errors
```