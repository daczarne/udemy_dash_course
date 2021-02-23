# Deployment

To deploy to Heroku complete the following steps:

1. Create a `virtualenv` and install the dependencies

1. Install `gunicorn` via `pip install`

1. Add the line `server = app.server` to the application

1. Add a `.gitignore` file and add `venv`, `*.pyc`, `.DS_Store`, and `.env`

1. Add a `Procfile`

``` txt
Web: gunicorn app:server
```

where `app` is the name of the `.py` file with the apps source code.

6. Add `requirements.txt`. To do so, in the command line, `cd` into the apps directory, make sure your virtual environment is activated (if not, run `.\venv\Scripts\activate`), and run:

``` bash
pip freeze > requirements.txt
```

7. Login to your Heroku account by running `heroku login` in the command line and supplying your credentials

8. Run `heroku create <app_name>` where `<app_name>` is a unique name for the application. The name must start with a letter, and can only contain letters, numbers and dashes

9. When Heroku finishes updating, it will promp the URL the application will have once that it's pushed

10. Now run `git add .` to stage all the files, `git commit -m "Initial launch"`, and `git push heroku master` to push the files to Heroku.

11. Once it finishes pushing, run `heroku ps:scale web=1` (where `web=1` is Heroku's free tier)
