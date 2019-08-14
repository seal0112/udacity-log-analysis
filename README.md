# Udacity Logs Analysis Project
This project is a simple CLI reporting tool based on tables in a PostgreSQL database.

The tool runs three reports for answers to the following questions:
- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

## Quick start

1. I recommend the user use a virtual machine to ensure they are using the same environment that this project was developed on, running on your computer. You can download [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) to install and manage your virtual machine.
2. Then you must have the PostgreSQL newsdata.sql database running from the FSND virtual machine.
Download the newsdata.sql provided by Udacity [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip the file in order to extract newsdata.sql. This file should be inside the Vagrant folder.
3. From the 'vagrant' directory, run ```vagrant up```.
4. SSH to the virtual machine with ```vagrant ssh```.
5. Connect to the psql database with ```psql -d news -f newsdata.sql```
6. Than we can be able to run the reporting tool as:
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