# UOCIS322 - Project 6 #
> **Author: Ellie Yun, yyun@uoregon.edu**

Brevet time calculator with AJAX, MongoDB, and a RESTful API!

## Design 

This web application is composed with three services, and each service is implemented in a separate directory.

### brevets

In the ACP calculator web page, there are following functionalities:

- There are two buttons `Submit` and `Display` in the ACP calculator page.

- Upon clicking the `Submit` button, the filled-in control times will be inserted into a MongoDB database.

- Upon clicking the `Display` button, the entries from the database will be displayed in a new page.

- It handles some error cases appropriately. For example, `Submit` should return an error if no control times are input. One can imagine many such cases: you'll come up with as many cases as possible.

#### How to test it?

In the web browser, search the following url:

    http://<host:port>/

`Note: Change the values for host and port according to your machine (check docker-compose.yml file for more details)`

### api

This is a Restful service that includes the following functionalities:

* Three basic APIs that exposes what is stored in MongoDB.three basic APIs:
    * "http://<host:port>/listAll" should return all open and close times in the database
    * "http://<host:port>/listOpenOnly" should return open times only
    * "http://<host:port>/listCloseOnly" should return close times only

* Two different representations: one in csv and one in json. For the above, JSON is the default representation for the above three basic APIs. 
    * "http://<host:port>/listAll/csv" should return all open and close times in CSV format
    * "http://<host:port>/listOpenOnly/csv" should return open times only in CSV format
    * "http://<host:port>/listCloseOnly/csv" should return close times only in CSV format

    * "http://<host:port>/listAll/json" should return all open and close times in JSON format
    * "http://<host:port>/listOpenOnly/json" should return open times only in JSON format
    * "http://<host:port>/listCloseOnly/json" should return close times only in JSON format

* A query parameter getting top "k" open and close times. For examples, see below.

    * "http://<host:port>/listOpenOnly/csv?top=3" should return top 3 open times only (in ascending order) in CSV format 
    * "http://<host:port>/listOpenOnly/json?top=5" should return top 5 open times only (in ascending order) in JSON format
    * "http://<host:port>/listCloseOnly/csv?top=6" should return top 5 close times only (in ascending order) in CSV format
    * "http://<host:port>/listCloseOnly/json?top=4" should return top 4 close times only (in ascending order) in JSON format

`Note: Change the values for host and port according to your machine (check docker-compose.yml file for more detials), and use the web browser to check the results.`

### website 

This is a consumer program to use the services that the user expose. The services are described above in the api.

#### How to test it?

In the web browser, search the following url:

    http://<host:port>/

`Note: Change the values for host and port according to your machine (check docker-compose.yml file for more details)`

## Credits

Michal Young, Ram Durairajan, Steven Walton, Joe Istas.
