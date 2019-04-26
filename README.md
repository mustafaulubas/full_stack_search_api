# CodeDoor Coding Challenge - GifCities

![Hero](/static/header.png)
## The Context

You are to treat this challenge as if you are working as a full-stack web developer at a fictitious startup. A news site has revealed that a big tech company is copying some of GifCities core features. The CTO is under pressure to showcase a minimum viable product to their board of directors by the end of the week.

You are tasked to integrate a Web API that will deliver GIF search results and display these search results using Flask. 
Fortunately, most of the work had already been done and you only need to add some finishing touches.


## Step 1 - Setting up your Dev Environment

To ease the process, the repo provides some files to help you get started. You will need to choose one of the approaches described below:

The simplest way is to use a tool called Vagrant:

- [Setup for a Vagrant-Based Environment](/static/doc/setup-for-vagrant.md)

Alternatively you can use another tool called Docker: 

- [Setup with Docker](/static/doc/setup-for-docker.md)

If you don't use Vagrant/Docker, you need to perform many, many more steps. These steps depend on your operating system: 

- [Install Python](https://docs.python-guide.org/starting/installation/)

> Please note:  We use Python 3.6.5. and you can install all necessary dependencies from `requirements.txt` using pip.

## Step 2 - Getting Familiar with project

Now that you have your server running, you can familiarize yourself with the project.

You're going to use:

- [Flask](http://flask.pocoo.org/docs/1.0/) for our web framework
- [Requests](http://docs.python-requests.org/en/master/) to grab data from [Tenor's GIF API](https://tenor.com/gifapi)

At this point, you should only pay attention to the following:

1. You only need to edit the following three files: 

      * `views.py`, `results.html` and `main.css`
```sh
    .
    ├── ...
    ├── project                   
    │   ├── main              
    │        |── views.py               # Main file for Coding Challenge
    │   ├── templates            
    │        ├── main
    │              ├── results.html     # HTML Skeleton for Search results page 
                   ├── index.html       # HTML Skeleton for Searchform page
    │   ├── static
             ├── main.css               # Global Style Sheet
    └── ...
```
2. Learn the basics of Flask and Requests. Both are easy to learn and these resources listed below are good resources and references for getting started: 
  * [Flask Megatutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) **Chaper 1-3 only**
  * [Routing with Flask](https://www.rithmschool.com/courses/flask-fundamentals/routing-with-flask)
  * [Requests Quickstart](http://docs.python-requests.org/en/master/user/quickstart/)

3. Before moving on, make sure to create a developer account and [request an API key](https://tenor.com/gifapi/documentation). 
   In `views.py` replace "Your API Key" with your actual API key in the code.

## The Challenge - Integrate Tenor's GIF Search API
In `views.py`, do the following:

1. Import `requests` module in views.py
2. Within `query_api`: 
  * Make an API call to execute a GIF Search that matches the given search parameter
  * If the requests succeeds, parse the JSON response to acquire the URL of each GIF

3. Render search results in `results.html` (Hint: Jinja Templates) 

4. Search Results need to be shown in a grid-based layout (Hint: Use Bootstrap) 

These resources listed below might help for your challenge:
* [Python API Tutorial](https://www.dataquest.io/blog/python-api-tutorial/)
* [What is REST?](https://www.codecademy.com/articles/what-is-rest)
* [Tenor's GIF Search API Documentation](https://tenor.com/gifapi/documentation#quickstart-setup)
* [How to use Web APIs in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-web-apis-in-python-3)
* [Templating with Jinja](https://www.rithmschool.com/courses/flask-fundamentals/templating-with-jinja2)


## What do we except

* Commit **early** and **often**. We want to be able to check your progress.
* Your Python code is neatly formatted and follows the [PEP 8 Styleguide](https://www.python.org/dev/peps/pep-0008/)
* Once you're satified with your solution, create a Pull Request in your repo.
* Your solution should work like this:
![Result](/static/results_example.gif)
    
 
Too hard? Got stuck? We encourage to reach out to Tutors and the CodeDoor Slack Community.  
Too easy? Go the extra mile and add additional search functionalities or improve the styling.

**Good Luck and Happy Coding!**
