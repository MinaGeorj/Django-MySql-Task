<h3>Welcome to my task repo! </h3><br/>

<large>Pleasse follow these steps to be able to run this project on any pc that has docker and docker-compose installed.<large><br/>

A) Get containers up: `docker-compose up`. <br/><br/>
B) Log into MySql container as a root user `mysql -u root` <br/><br/>
C) Create a new user to allow our Django application to communicate with our MySql database. <br/>
    `CREATE USER 'maww'@'%' IDENTIFIED WITH mysql_native_password BY 'password';`<br/>
    `grant all on *.* to 'maww'@'%';` <br/>
    `CREATE DATABASE task;`<br/><br/>
D) Stop the containers: `docker-compose down` <br/><br/>
E) Migrate the database: `docker-compose run --rm web python manage.py migrate` <br/><br/>
F) And finally: `docker-compose up` <br/><br/>

---
THANK YOU :)

 
