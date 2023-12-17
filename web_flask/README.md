# Learning Objectives

### What is a Web Framework?

A web framework is like a toolbox that helps build websites or web applications. It provides tools and structure to make it easier for developers to create and organise the code for their web projects.

### How to build a web framework with Flask?

Flask is a web framework that can be used to build web applications using Python.

### How to define routes in Flask?

Routes in Flask are URLs that users can visit in web applications. To define a route, use a decorator.

`@app.route('/home')` is a decorator that defines a route for the '/home' URL.

### What is a route?

A route is a specific URL in a web application. When users visit a route, they trigger a particular function or piece of code in the web application.

### How to handle variables in a route?

Include variables in a route by putting them in the URL pattern.

`@app.route('/user/<username>')` defines a route that takes a variable called 'username'. The variable can be used in the code.

### What is a template?

A template is a file that contains a mix of HTML and special placeholders for dynamic content. In web frameworks like Flask, templates help separate the structure of your web page from the actual data that gets displayed.

### How to create an HTML response in Flask by using a template?

A template is rendered using the `render_template` function. The name of the template file and any data needed is passed in the template. The function then generates HTML and sends it as a response to the user's browser.

### How to create a dynamic template (loops, conditions…)?

Make templates dynamic by using template engines like Jinja2 (default). With Jinja2, use loops and conditions in templates to handle dynamic content and display different information based on certain conditions.

### How to display in HTML data from a MySQL database?

To display data from a MySQL database in Flask, connect to the database, retrieve the data using SQL queries, and then pass that data to the template for rendering. Use SQLAlchemy (database connector) to interact with the MySQL database in the Flask application.
