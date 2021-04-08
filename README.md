Twitter API
The Twitter API gives developers access to most of Twitter’s functionality. You can use the API to read and write information related to Twitter entities such as tweets, users, and trends.

Technically, the API exposes dozens of HTTP endpoints related to:

Tweets
Retweets
Likes
Direct messages
Favorites
Trends
Media
Tweepy, as we’ll see later, provides a way to invoke those HTTP endpoints without dealing with low-level details.

The Twitter API uses OAuth, a widely used open authorization protocol, to authenticate all the requests. Before making any call to the Twitter API, you need to create and configure your authentication credentials. Later in this article, you’ll find detailed instructions for this.

You can leverage the Twitter API to build different kinds of automations, such as bots, analytics, and other tools. Keep in mind that Twitter imposes certain restrictions and policies about what you can and cannot build using its API. This is done to guarantee users a good experience. The development of tools to spam, mislead users, and so on is forbidden.

The Twitter API also imposes rate limits about how frequently you’re allowed to invoke API methods. If you exceed these limits, you’ll have to wait between 5 and 15 minutes to be able to use the API again. You must consider this while designing and implementing bots to avoid unnecessary waits.

You can find more information about the Twitter API’s policies and limits in its official documentation:

Twitter Automation
Rate limits
What Is Tweepy?
Tweepy is an open source Python package that gives you a very convenient way to access the Twitter API with Python. Tweepy includes a set of classes and methods that represent Twitter’s models and API endpoints, and it transparently handles various implementation details, such as:

Data encoding and decoding
HTTP requests
Results pagination
OAuth authentication
Rate limits
Streams
If you weren’t using Tweepy, then you would have to deal with low-level details having to do with HTTP requests, data serialization, authentication, and rate limits. This could be time consuming and prone to error. Instead, thanks to Tweepy, you can focus on the functionality you want to build.

Almost all the functionality provided by Twitter API can be used through Tweepy. The only current limitation, as of version 3.7.0, is that Direct Messages don’t work properly due to some recent changes in the Twitter API.

Using Tweepy
In this section, you’ll learn how to install Tweepy for development, configure authentication credentials, and interact with the Twitter API.

Installation
Tweepy can be installed using pip, a Python package manager. In this article, we’re going to use a virtual environment (virtualenv) for the projects to avoid depending on system-wide packages. For more information on virtual environments and pip, check out Python Virtual Environments: A Primer and What Is Pip? A Guide for New Pythonistas.

The first step is to create a virtual environment:

$ cd tweepy-bots
$ python3 -m venv venv

The commands above create the virtual environment inside the project directory.

Then you can install the Tweepy package. First, you need to activate the newly created virtual environment and then use pip to do the installation:

$ source ./venv/bin/activate
$ pip install tweepy

Now that Tweepy is installed we can run an example bot as:
$python stream.py

Before you run any tweet bot, make sure to populate the tokens in key.py and keys for a developer account.
