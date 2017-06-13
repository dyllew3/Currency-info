# Currency-info
Uses a Bellman Ford algorithm with currency exchange to detect a negative exchange cycle
This gets currency rates using the yahoo finance query api
It uses multithreading to obtain the queries the shortest amount of time,
calculating the optimal number of threads using test.py.
It gets the rates converts them into edge form, where the weight is is -ln(Rate) and
directed, the weight is in this form because to turn rate change from multiplication to addition.
It then looks for a negative cycle and prints all negative cycles
