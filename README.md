The idea behind the API is nothing new; it utilizes HTTP requests to retrieve information from a database and return information to the front-end. This API in particular is a mock of Whitepages, a website that provides basic information about people and is publicly accessible. I thought creating a Whitepages mock-up would be a perfect yet most basic example of frontend and backend communication, and it was.

The information stored in a database is accessible through HTTP GET requests and can be modified through POST, DELETE, and PUT requests. In this project, there are two main classes: people and users. People are the names and information pertaining to those names that are stored in the people database. Users are people who are authorized to create, modify, and delete people from the database. Users must create accounts and log in, where the API will use OAuth2 to create a JWT bearer token that will allow users to have access to POST, DELETE, and PUT functionality. No token is needed to send a GET request, meaning anyone could access the people in the people database (which is the purpose of the Whitepages).

This project does not include front-end functionality quite yet, as developing this API took a lot longer than anticipated. I also did not deploy the API because I did not see it as necessary without a useful frontend (but I look forward to doing so in the near future). That being said, here are some cool features of the API:

*OAuth2.0 JWT bearer token generation for user validation
*Alembic database migration for simple migrations in development (if this were a full-scale web app)
*ORM usage through SQLAlchemy to reduce the raw SQL in code (and lessen the chance of SQL injection)

This is obviously not Google or MacOS, but it was an excellent introduction to API development and showcases the ability to push through challenges (lots and lots of challenges) as well as follow through until the end of a project.
