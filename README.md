My first "big" fullstack project on Django and React.

Features:

1. Service info board for machine manufacturer, their clients and service companies (backend + frontend + database);
2. Blocked registration for users (only admin via administration panel);
3. Three roles of users: manufacturer manager, service manager, customer;
4. ~~Check list of your machines when authenticated~~; (in work)
5. ~~Control status of technical maintenance, reclamations;~~ (in work)
6. ~~Search machines with serial number, when not authenticated~~; (in work)
7. ~~Check more details about parts of your machines~~; (in work)
8. ~~Sort machines in your table~~; (in work)
9. Custom personalized design (works for mobile devices too);
10. REST-ful API (DRF);
11. ~~Docker support (with autocompile)~~; (in work)


Requirements:

In requirements.txt file


How to start this app (for now):
1. Make sure you have `git`, `pip` and `npm` on your system;
2. Clone this repo with `git clone` command;
3. Create virtual environment `py -m venv venv` and activate it `\venv\Scripts\activate`;
4. Install requirements from "requirements.txt" `pip install -r requirements.txt`;
5. Create file `keys.py` with parameters: 

    DJANGO_KEY = "your own key" (you may take it from your other Django project)
    DJANGO_ALLOWED_HOSTS = ['localhost', '127.0.0.1']
    
6. Run `py manage.py makemigrations` and `py manage.py migrate` to create your database;
7. Create superuser `py manage.py createsuperuser`;
8. Run server `py manage.py runserver`;
9. Make sure it works on `http://127.0.0.1/admin`. Login via superuser and add some Lorem info;
10. Open separate Terminal;
11. Go in `frontend_app` folder and run `npm start` in 2nd Terminal;
12. Page will open automatically in your browser.


Made for final practice exercise in "Fullstack developer" course for SkillFactory (FPW-62)

For education purpose only. Workability is not guarantee.

If you'll have suggestions or encounter errors in project, feel free to contact me, please.

Made by IvanDamNation (a.k.a. IDN) GNU General Public License v3, 2023.