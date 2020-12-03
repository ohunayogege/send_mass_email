# Send Mass Email

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://twitter.com/ohunayogege)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://ohunayogege.com)

Send Mass Email is a mai sending tutorial created with Django to assist people that are in need of it.

### How to Install

  - Clone the project
  - create and activate your environment
  - pip install -r requirements.txt
  - run "python manage.py makemigrations && python manage.py migrate" to migrate the database
  - run 'python manage.py createsuperuser' to create admin account.
  - Create customer's account as much as you can.

# Library Used for project!

  - Django
  - Django Rest Framework (DRF)


### How to Send Email:
  - The url to send request to is url/send_mai/
  - Using **POST** request, data to send are {"to": "all or single"}
  - if single is selected then we need to add email field {"to": "single", "email": "customer email"}
  - if all is selected then no need to add email field.
  - Email can then be sent.
****
To change message kindly see folder _mail/message/_ there you will find the necessary files to edit such as body.html, body.txt, subject.txt
****
****
> Email contains html if body.html is correct.
> Email sent will be saved as local until you change 
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "inbox") to the original mail settings.
> Mail saved as local can be found in __inbox__
****
For more info/help/assistant
kindly reach me via **WhatsApp** 
**+2348149983395**