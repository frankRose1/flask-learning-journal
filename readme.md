# Flask Learning Journal
Using flask I built this personal learning journal which acts as a blog-like web application.
This journal can be used do document progress with code and save references to useful links/learning resources.
App runs locally and data is saved to a local Sqlite database.


## App Features
- Signup/Signin support, data validation, protected routes, & CRUD opertaions
- flash messages are used to notify user of success/error messages
- ```/``` and ```/entries``` will display a users entries if they're autheticated, else they will be prompted with a landing page 
- posting to ```/entry```  will create an entry
- posting to ```/register``` creates a user account
- posting to ```/login``` will authenticate a user and start a session
- ```/entries/<int:entry_id>``` displays a specific entry
- ```/entries//edit/<int:entry_id>``` will populate form with existing values, and allow for updating the record
- ```/entries/delete/<int:entry_id>``` deletes a specific entry
- a 404 template is served for any database records or routes that don't exist


## Packages Used
* peewee 
* flask
* flask-wtf
* flask-bcrypt
* flask-login