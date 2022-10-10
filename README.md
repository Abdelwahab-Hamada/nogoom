
![Logo](https://res.cloudinary.com/abdelwahab-youssef/image/upload/v1664822398/media/projects/7913ac4d-e7a0-4a1e-9ef9-0a67e3c641a0_qsxqxe.png)


# an app to post reviews with help of tagging system
#### 🔗 [**Nogoom fullstack app link**](https://abdelwahab-hamada.github.io/nogoom-app/)
## Technologies 
<p align="left"> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a>  <a href="#" target="_blank" rel="noreferrer"> <img src="https://www.django-rest-framework.org/img/logo.png" alt="django rest framework" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>   </p>

## API Reference ([RESTful Endpoint on heroku](https://nogoom-app.herokuapp.com/))

- #### Authentication 

    ```http
    POST /register
    POST /auth
    ```

    | Parameter | Type     | Description                |
    | :-------- | :------- | :------------------------- |
    | `username` | `string` | **Required** |
    | `password` | `string` | **Required** |

- #### Tags system

    | Method | Endpoint     | Requirements                       |
    | :-------- | :------- | :-------------------------------- |
    | `POST`      | `/tags/search` | label or a letter from label |
    | `POST`      | `/tags/create` | label & **Login Required** |
    | `GET`      | `/tags/followed` | **Login Required** |
    | `GET`      | `/tags/popular` |  |
    | `GET`      | `/tags/recent` |  |

- #### Reviews system

    | Method | Endpoint     | Requirements                       | Description | 
    | :-------- | :------- | :-------------------------------- | :-------- | 
    | `POST`      | `/reviews/create` | `score` `comment` `title` `tags` & **Login Required** |  |  
    | `GET`      | `/reviews/feed` | **Login Required** | gets recent reviews posted in followed tags|
    | `GET`      | `/reviews/user` | **Login Required** | gets reviews posted by logged-in user|
    | `GET`      | `/reviews/stared` | **Login Required** | gets reviews liked by logged-in user|
    
   




## Features

- register
- authintication
- tagging system
- reviews system

