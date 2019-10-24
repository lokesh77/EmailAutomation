# EmailAutomation
A simple Django based EmailAutomation done with Rest API

# Creating VirtualEnv
```
virtualenv Envname -p C:\python37\python.exe

cd Envname
.\Scripts\activate
```

# Installing Dependencies


```bash
pip install django        
pip install djangorestframework    
pip install django-cors-headers
```

# GUI

- Django used
- Easy extraction and interpretation using GUI
- For running GUI execute:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

- Visit `http://127.0.0.1:8000/api/gdpr/customer/` to view the GUI
