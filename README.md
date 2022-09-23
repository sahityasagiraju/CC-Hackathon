# Cloud-Computing-Hackathon
Problem Statement 3

_**Breaking the monolith architecture**_


Decouple the arithmetic functions from landing-service. 


The four arithmetic functions currently reside under landing-service. 
However, if landing-service were to become unavailable for whatever reason, the four functions would be unavailable as well. **Create separate flask applications, Addition, Subtraction, Multiplication and Division.**

Each application will consist of a class which inherits the Resource class of flask_restful module. Define a GET method within the class with necessary parameters. An example of this class with the method defined can be found here and here Use the add_resource function to add the class as a resource and define the API endpoint.

Make sure to also mention the type of the parameters in the endpoint. Example: api.add_resource(, '/int:argument0/int:argument1') Update the Docker-compose.yaml to recognize the newly added flask applications as separate services. The Docker-compose.yaml lets you define the port number and network alias that will be used by landing-service to communicate within the entire architecture - Test the new microservices-based application.


Add three more services Proceed to add three more services that perform a certain function. You will also have to make changes to the frontend defined in index.html to make these functions available. 

**Mentioned below are possible functions you could implement but feel free to add your own.**

**gcd:** Takes two numbers as arguments and returns their Greatest Common Divisor 

**lcm:** Takes two numbers as arguments and returns their Least Common Multiple 

**modulus:** Returns the remainder of two numbers after division. 

**Reference exponent:** Returns the result of the arithmetic operation ab 

**greater_than:** Return True if the first value is greater than the second else ```False`` 

**less_than**: return True if the first value is less than the second else False 

**equal:** return True if the first value is equal to the second else False
