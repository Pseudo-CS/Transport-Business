clone repository, then in the cloned folder create a python virtual environment<br>
from the virtual env run:<br>
install django - pip install django<br>
python manage.py runserver<br>
to clear the db: python manage.py flush<br>
once any changes are made to models.py run the following:<br>
python manage.py makemigrations<br>
python manage.py migrate<br>
