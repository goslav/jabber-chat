Jabber is small asynchronous chat app with different chatrooms that showcases usings WebSockets and the Channels package. 

You can run the app on your local by performing the following steps:

- Create a virtual env based on Python 3.7 (or any higher version).
python3 -m venv venv

- Run the migrations (SQLite will be used initially).
./manage.py migrate

- Run the local server.
./manage.py runserver

Once you get the app running locally, you can just extend the url to access whatever chatroom you like. 

http://127.0.0.1:8000/chat/
---------------------------------------------------------------------------------------------------------------------

Python is a synchrounous language but it support the usage of asyncrounous applications using Coroutines. For futher explanation please refer to the python docs. 

https://docs.python.org/3/library/asyncio-task.html

Django has support for writing asynchrounous ('async') views together will the async-enabled request stack. Async functions can work under WSGI, but to avoid any perfomance issues to to ulitize the ability to have efficient long-running requests we have to use the ASGI, which is a Python standard for anysncrounous web servers and applications. 

- For the purposes of this app, we will be grouping users into a same group. 
- We will be utilizing Channels, a Django package that is build using Django's native async view spport, which allows to handle connections not only to HTTP, but to WebScokets, chatbots and more. For the purposes of this app, we will be making a connection to a WebSocket. 

Instead of defining urls and views, like we do for synchrounous Django applications, we will be definitng routing and consumers respectively. This allows us to put more advanced paths in routing.py, which give us more flexibility. 

A consumer is a basic unit of Channels code, aptly named "consumer" because it consumes events. 

So, when a request or new socket comes in, Channels will follow the order below. 

Request or new socket > goes to routing looking for a consumer > finding the consumer defined in consumers.py.

Channels allows us to group multiple consumers into one bigger app, and moreover to build any protocol into a Django environment. The goal of using the package is to allow Django projects to work across any protocol in the modern web while retaining the familiarity and coding style native to Django. 

- For production purposes we will have to use Redis or RabbitMQ as the message broker in the CHANNEL_LAYERS settings, but that's not covered in this app. 