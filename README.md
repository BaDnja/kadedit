# Kadedit

## How to Run

* **Dependencies**:
    * [Python3](https://www.python.org/downloads/) (v3.7 or higher)
    * [PostgreSQL](https://www.postgresql.org/download/) (v10 or higher)
    * _(Optional)_ [pgAdmin](https://www.pgadmin.org/download/)
    

* Open terminal and navigate to the projects folder: `cd /projectsfolder/`
* Paste following code to clone repository `git clone https://github.com/BaDnja/kadedit.git`
    or if you have an ssh set up, paste following: `git clone git@github.com:BaDnja/kadedit.git`
* Navigate to kadedit folder and install project requirements by typing  `pip install requirements.txt`
  * Please bare in mind that if you get an error while installing psycopg2 from requirements,
        install the binary version by typing: `pip install psycopg2-binary`
* While in mobster root folder, create .env file, _copy-paste_ content from .env.example and modify appropriate settings.
* After completing all steps above, run migrations by typing `python manage.py migrate`
* To run a project in a browser type the following: `python manage.py runserver`
