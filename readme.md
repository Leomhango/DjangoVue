
# SetUp

- in terminal `root folder` run:

virtualenv venv
source venv\bin\activate
pip install requirements.txt

cd backend
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser __follow the instructions__
python manage.py runserver or python manage.py runserver 0.0.0.0:8000 (for mutiple device connection)

- open another terminal in the `root folder`

cd frontend
npm install
npm run serve