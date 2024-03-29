# Cloud Based ERP System - Django
A cloud based ERP system solution that covers basic aspects of most businesses in an agnostic way.

## TABLE OF CONTENTS
1. INTRODUCTION
    1. Usage
    2. Goals
2. INSTALLATION
3. USAGE
4. CREDITS
5. OUTSTANDING WORK

## 1. INTRODUCTION
### 1.1 Usage
This cloud Enterprise Resource Planning system will help aid business to move their operations to the cloud space.
It will include the following packages :
* Warehousing System
* CRM (Customer Relationship Management)
* POS (Point of Sale)
* Reporting
* Accounting
* Order Management
* User Management
* Supply Management
* Catalogue Management

### 1.2 Goals
This system aims to address issues and help improve on:

* Keeping track of all historical data and movement of sales, orders and inventory
* Speed and accuracy of reporting, accounting and ordering
* All data will be stored and visually represented in one solution
* Inter company communication and structures
* Accessibility of systems due to cloud infrastructure
* Minimize human error with proper error handling stuctures and proper UI/UX implementation
* Modern UI aspects to make it more enjoyable for employees to work
* API links to connect to eCommerce websites to make a centralized network of systems

## 2. INSTALLATION
*Note that these steps are for the **Windows** environment. Installation steps for other eco systems will be created at a later stage*
*You can also use pip install -r requirements.txt to install required packages*

1. Clone Git Repo
    1. Open the Terminal and run the following command : "git clone https://github.com/whybee0405/django_erp.git"

2. Install Python
    1. Download the latest stable version of Python here : [Download Python](https://www.python.org/downloads/)
    2. Make sure your global ENV variables are set properly

3. Install PIP
    1. [Click Here for Tutorials](https://docs.djangoproject.com/en/1.8/howto/windows/)
    2. Use the following cmd prompt to install PIP : 'python -m pip install pip'

4. Install virtualenv package
    1. Use the following cmd prompt : 'python -m pip install virtualenv'

5. Install virtualenvwrapper package
    1. Use the following cmd prompt : 'pip install virtualenvwrapper-win'
    2. If in Linux, try 'sudo pip install virtualenvwrapper'
    3. Don't forget to run your terminal in Administrator mode in Windows

6. Install Django
    1. Set up a virtual environment (call it whatever you want) using : 'mkvirtualenv <environment name>'
    2. Activate the virtual environment using : 'workon <environment name>'
    3. Install Django into the virtual environment using : 'pip install django'

5. Start Server
    1. CD into the directory of the project that has the 'manage.py' file
    2. Run the following command in the terminal to start the localhost server : python manage.py runserver

6. Open an internet browser of your choice and open the localhost server at the port that it opened in

## 3. USAGE

1. Create a user through the admin panel (make sure that a superuser has been set). Access it through http://127.0.0.1:8000/admin
    1. Set a superuser using 'python manage.py createsuperuser'

2. Log in through the login page
![Login Page](/assets/images/readme_login_page.png)


## 4. CREDITS
Credits to whybee0405 (Young Bin Na) for the creation of the project. [Github](https://github.com/whybee0405)


## 5. OUTSTANDING WORK
- [x] Create base Django templating for features
- [ ] Implement MySQL database structures
- [ ] Use Javascript framework (like VueJS) for the frontend
- [ ] Style using CSS, Bootstrap and other frameworks (like GrapeJS)
- [ ] Architect all packages to be included in the system
- [ ] Look into white labeling the software (make it agnostic)