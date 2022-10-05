# Social-media-web-app

<p align="center">
<a href="https://www.python.org/"><img src="https://forthebadge.com/images/badges/made-with-python.svg" border="0" title="Made with Python" />
</p>

<p align="center">
<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif" border="0" alt="Powered by Django." title="Powered by Django." /></a>
</p>

### Installation

1. - Fork the [repo](https://github.com/pkini2002/Social-media-web-app)
   - Clone the repo to your local system
   ```git
   git clone https://github.com/pkini2002/Social-media-web-app.git
   cd Social-media-web-app
   ```
   Make sure you have python installed on your system.
2. Create a Virtual Environment for the Project

   If u don't have a virtualenv installed

   ```bash
   pip install virtualenv
   ```
   **For Windows Users**
   ```bash
   virtualenv env
   env/Scripts/activate
   ```


   **For Linux Users**
   ```bash
   virtualenv env
   source env/Scripts/activate
   ```

   If you are giving a different name than `env`, mention it in `.gitignore` first

3. Install all the requirements

   ```bash
   pip install -r requirements.txt
   ```

    ```bash
   cd socials
   ```


4. Make migrations/ Create db.sqlite3

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a super user.
   This is to access Admin panel and admin specific pages.

   ```djangotemplate
   python manage.py createsuperuser
   ```
   

   Enter your username, email and password.

6. Run server
   ```bash
   python manage.py runserver
   
   
 ## To do list
 
 - [ ] Login Form
 - [ ] Signup Form
 - [ ] Profile Update Form
 - [ ] Forgot Password Form
 - [ ] Create a post
 - [ ] Home page
 - [ ] Friends Page
 - [ ] Others Profile Page
 - [ ] Search a name and design a logo for the application
 
 
 ## Features
 
 - [ ] Like & Comment on Others posts
 - [ ] Post images and news on Social media
 - [ ] Search bar to search people
 - [ ] Follow and Unfollow users
 - [ ] Display Leaderboard page in home
 
 ### Points distribution
 
 <table>
 <tr>
 <td>Signup</td>
 <td>3 points</td>
 </tr>
 
 <td>Login</td>
 <td>1 points</td>
 </tr>
 
 <td>Creating a Post</td>
 <td>2 points</td>
 </tr>
 </table>
 
 
      
      
