# API project featuring Django REST framework and MongoDB

**[Link to the API's root endpoint](https://automatrixapi.pythonanywhere.com/)**
<br/>
**[Link to the front end interface for this API](https://3782291211.github.io/vue-api-interface/)**

Welcome to another one of my backend projects. Here I have created a NoSQL web API with Django REST framework featuring full CRUD functionality and exhaustive integration testing. This API is built upon a document data model and is connected to document collections hosted on a MongoDB database cluster.

Visit the links above to view the API and explore all of its endpoints, HTTP methods and error messages.

## Endpoints
To access each resource, simply append one of these paths to the API's base URL.

- /api/patterns 
    - **GET | POST**
- /api/patterns/:pattern_id 
    - **GET | PUT | DELETE**
- /api/users 
    - **GET | POST**
- /api/users/:user_id 
    - **GET | PUT | DELETE**
- /api/users/:username/patterns 
    - **GET**
- /api/comments
    - **GET | POST**
- /api/comments/:comment_id
    - **DELETE**


## Key product features:
- Based on an MVT design pattern.
- Variety of endpoints providing GET, POST, PUT and DELETE functionality.
- Extensive error handling with custom error messages for distinct concerns.
- Full integration testing using Django's test case class.
- Function-based views and class-based tests.
- Virtual environment for project dependencies.
- Multi-app project structure, in line with best practice.