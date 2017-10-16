# Lost Pet Finder

<p>The application is developed using Django Web Framework (https://www.djangoproject.com/).
The application is intended to use by the pet owner who can register their pet,
and list their pet online in the event that the pet is missing.</p>

Production URL: https://lostpetfinder.herokuapp.com/

## Table of Contents
1. [Application Usages](#application-usages)
    * [Pet Owner](#pet-owner)
    * [Administrator user](#administrator-user)
    * [Others](#others)
1. [Implementation](#implementation)
    * [Application REST API](#application-rest-api)
    * [Google Maps Geocoding Web Services](#google-maps-geocoding-web-ervices)
    * [Heroku PaaS and Amazon S3 Storage](#heroku-paas-and-amazon-s3-storage)
    * [Database](#database)
1. [Packages Requirement](#packages-requirement)
1. [Installation](#installation)
1. [Contributing](#contributing)
1. [Coding Standards](#coding-standards)
1. [References](#references)
1. [Appendix](#Appendix)
    * [Project File Structure](#project-file-structure)

## Application Usages
### Pet owner
  * Register for new account with email based account activation.
  * Update personal profile including name, email, mobile, and address.
  * Change and reset password with email based password reset.
  * Register for new pet, and list the pet as lost or found status.
  * Update and delete their own pets.
  * Deactivate the account if it is no longer needed.

### Administrator user
  * The administrator user has full access to the application including add, update,
delete users and pets.
  * Beside the built-in Django's admin site, the application also has a customised
admin site that list all users that allow administrator to create an new user,
edit user details such as name, email, as well as deleting specific user.

### Others
* The application has a search function to allow end-user to search for specific
pet with the pet's name, status, pet type, and the lost location of the pet.

**[Back to top](#table-of-contents)**

## Implementation
The application is implemented with following features and connecting to following
web services:

### Application REST API
External application can connect to the application using REST API as below:
  * **GET all pets:** `GET /api/pets/`
  * **Search pets:** `GET /api/pets/?q={search-query}`
  * **Get a specific pet details:** `GET /api/pets/{slug}/` e.g. /api/pets/cute-cat-charles/
  * **Update a specific pet:** `PUT /api/pets/{slug}/edit/` e.g. api/pets/cute-cat-charles/edit/
  * **Delete a pet:** `DELETE /api/pets/{slug}/delete/` e.g. /api/pets/cute-cat-charles/delete/

### Google Maps Geocoding Web Services
The application is using **Google Maps Geocoding** to get the data of
**latitude** and **longitude** of the pet's location, and display its missing
location in Google Maps using Google Maps web service.

### Heroku PaaS and Amazon S3 Storage
<p>The application is deployed in Heroku cloud PaaS (https://www.heroku.com)
for the simplicity of the deployment, with using Amazon S3 storage
(https://aws.amazon.com) to store static files such as CSS, JavaScript files,
and media files for pet's picture.</p>

### Database
The database which is used is **PostgreSQL** database, and it is installed
during the deployment process in Heroku cloud PaaS.

**[Back to top](#table-of-contents)**

### Packages Requirement

Followings are python packages which are used in the application:
```
boto3==1.4.7
botocore==1.7.16
certifi==2017.7.27.1
chardet==3.0.4
dj-database-url==0.4.2
Django==1.11.4
django-crispy-forms==1.6.1
django-storages==1.6.5
django-widget-tweaks==1.4.1
djangorestframework==3.6.4
docutils==0.14
gunicorn==19.7.1
idna==2.6
jmespath==0.9.3
olefile==0.44
Pillow==4.2.1
psycopg2==2.7.3
Pygments==2.2.0
python-dateutil==2.6.1
pytz==2017.2
requests==2.18.4
s3transfer==0.1.11
six==1.11.0
urllib3==1.22
```
**[Back to top](#table-of-contents)**

### Installation
#### Install Python
Install the latest Python distribution. At the time of this writing,
the latest version is **Python 3.6.3** (https://www.python.org/).
```
e.g. Ubuntu installation
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update
$ sudo apt-get install python3.6
```

#### Install pip
Install the latest version of **pip**, a tool to manage and install Python packages.
Refer to https://pip.pypa.io/en/stable/installing/.
```
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python3.6 get-pip.py
```

#### Install *virtualenv*
It is common that a Django project might need to install external libraries
to support the development. Therefore, It is recommended to install **virtualenv**
to run each Django project in each isolated virtual environment.
The following is example of CLI run on Linux..
```
$ sudo pip3.6 install virtualenv
```

#### Create a Project Folder and Activate *virtualenv*
Create a project folder such as **trydjango-1-11**
```
$ mkdir trydjango-1-11 && cd trydjango-1-11
$ virtualenv -p python3.6 . # creating 'virtualenv' in current directory
$ source bin/activate # activating 'virtualenv'
```

#### Fork and Pull Git Repository
Fork **git@github.com:hhtek/aip-assessment-03.git** and pull your git repository
to the project folder created in above step which is **trydjango-1-11**.
```
$ git init
$ git pull <your git repository>
e.g. git pull git@github.com:hhtek/aip-assessment-03.git
```

#### Install Project Packages
The required python packages used for the application is listed in **src/lostpetfinder/requirements.txt**.
```
$ pip install -r src/lostpetfinder/requirements.txt
```

#### Start the Django local application server
```
$ python src/lostpetfinder/manage.py runserver
```

#### Open the application in web browser
http://127.0.0.1:8000/

**[Back to top](#table-of-contents)**

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

**[Back to top](#table-of-contents)**

## Coding Standards
Refer to [Coding Standards](CODINGSTANDARDS.md) for more details.

**[Back to top](#table-of-contents)**

## References
The application is written by following tutorials listed at following references:

1. https://www.codingforentrepreneurs.com/projects/try-django-111/
1. https://www.codingforentrepreneurs.com/blog/go-live-with-django-project-and-heroku/
1. https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
1. https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
1. https://simpleisbetterthancomplex.com/tutorial/2016/11/15/how-to-implement-a-crud-using-ajax-and-json.html
1. https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html
1. https://simpleisbetterthancomplex.com/series/2017/09/25/a-complete-beginners-guide-to-django-part-4.html
1. https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html
1. https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/
1. http://www.django-rest-framework.org/


**[Back to top](#table-of-contents)**

## Appendix
### Project File Structure
<p>Below is the main file structure of the project.</p>

src/
└── lostpetfinder
    ├── accounts
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── __init__.py
    │   ├── migrations
    │   ├── models.py
    │   ├── templates
    │   │   └── accounts
    │   │       ├── account_activation_email.html
    │   │       ├── account_activation_invalid.html
    │   │       ├── account_activation_sent.html
    │   │       ├── account_confirm_deactivate.html
    │   │       ├── admin_partial_user_create.html
    │   │       ├── admin_partial_user_delete.html
    │   │       ├── admin_partial_user_list.html
    │   │       ├── admin_partial_user_update.html
    │   │       ├── admin_user_list.html
    │   │       ├── login.html
    │   │       ├── password_change_done.html
    │   │       ├── password_change.html
    │   │       ├── password_reset_complete.html
    │   │       ├── password_reset_confirm.html
    │   │       ├── password_reset_done.html
    │   │       ├── password_reset_email.html
    │   │       ├── password_reset.html
    │   │       ├── password_reset_subject.txt
    │   │       ├── profile_edit.html
    │   │       ├── profile.html
    │   │       └── register.html
    │   ├── tests.py
    │   ├── tokens.py
    │   ├── urls.py
    │   └── views.py
    ├── db.sqlite3
    ├── lostpetfinder
    │   ├── __init__.py
    │   ├── settings
    │   │   ├── base.py
    │   │   ├── __init__.py
    │   │   ├── local.py
    │   │   ├── production_heroku.py
    │   ├── storage_backends.py
    │   ├── test.py
    │   ├── urls.py
    │   ├── utils.py
    │   └── wsgi.py
    ├── manage.py
    ├── media
    │   └── pets
    │       ├── admins-cat.jpg
    │       ├── boms-cat.jpg
    │       ├── henrys-2nd-cat.jpg
    │       ├── henrys-cat.jpg
    │       ├── henrys-cat.png
    │       ├── henrys-dog-aqal.jpg
    │       ├── henrys-dog.jpg
    │       ├── pets.png
    │       └── test.jpg
    ├── pets
    │   ├── admin.py
    │   ├── api
    │   │   ├── __init__.py
    │   │   ├── permissions.py
    │   │   ├── __pycache__
    │   │   ├── serializers.py
    │   │   ├── urls.py
    │   │   └── views.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── __init__.py
    │   ├── migrations
    │   ├── models.py
    │   ├── templates
    │   │   └── pets
    │   │       ├── pet_confirm_delete.html
    │   │       ├── pet_detail_data.html
    │   │       ├── pet_detail.html
    │   │       ├── pet_form.html
    │   │       └── pet_list.html
    │   ├── templatetags
    │   │   ├── form_tags.py
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── Procfile
    ├── requirements.txt
    ├── static
    │   ├── css
    │   │   ├── accounts.css
    │   │   ├── pets.css
    │   │   └── site_general.css
    │   ├── img
    │   └── js
    │       ├── accounts_users.js
    │       └── googlemap.js
    └── templates
        ├── about.html
        ├── base_accounts.html
        ├── base.html
        ├── contact.html
        ├── home.html
        └── snippets
            ├── form.html
            ├── navigation_bar.html
            ├── page_navigation.html
            └── sidebar.html

**[Back to top](#table-of-contents)**
