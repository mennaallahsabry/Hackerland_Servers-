# Hackerland_Servers-
The fictional world of Hackerland has servers whose efficiencies can be increased by 
adding more cores to them thus allowing more threads to be processed. 
A server has several cores which can process threads for serving client requests. Each second, 
either some thread is assigned to a core and is added to the pool for serving requests, or a 
request comes in. This is denoted by the array server[] where a positive value indicates the 
number of threads added, and -1 indicates a request coming in. 
The requests come in only one at a time. Each thread can serve at most one request and then is 
destroyed. If there are no available threads when a request comes in, the request goes 
unattended and is dropped. Find the number of requests that are dropped

 the code output with the following test cases: 
○ [-1, -1, -1, -1] 

○ [4, -1, -1, -1] 

○ [1, -1, 1, -1]
