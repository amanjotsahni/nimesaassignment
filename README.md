# data.py:- 
It is used to ingest/get data from the API and manipulate the data so that we get a complexity of O(1)[constant time].
# deploycode.py:-
It is used to find all the attributes like temperature, time, pressure, wind speed etc.
# server.py:- 
It is a web API for our python code using flask framework.


# Points to be noted:-
* I have used serialization to further save time and to get low latency from the code for the application. We don't need to manipulate the data again.
* I used flask so as to manage the application pages and to terminate the program. Used the concept of request and render from the framework to get data. It is used as a bridge to map front end as well as backend.
* Basically we have performed the communication of data from the html form and delivered it to the backend python code for processing and execution. Once the output is generated flask pushes the output on result.html and it gets displayed.
