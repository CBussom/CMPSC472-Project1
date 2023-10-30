# Advanced Process Manager

## Implemented Functionalities

- Process creation, termination, and monitoring
- Thread creation and synchronization  
- Inter-process communication using message queues
- Process synchronization primitives like mutexes and semaphores

## Installation  

The code is written in Python. Ensure Python 3.x is installed.

Clone the repository: https://github.com/CBussom/CMPSC472-Project1

## How To Use

The process manager has a command-line interface. To start it:
Project_ProcessManager.py

## Commands
- The `create_process` command creates a new process and starts it.
- The `list_processes` command prints out all of the processes.
- The `terminate_process` command terminates whichever the target process is.
- The `create_thread` command creates a thread of whichever the target function is.
- The `start_thread` command starts the created thread.
- The `wait_thread` command waits until the threads are done to join them together.
  
### Thread Synchronization   
The `producer_consumer` command demonstrates synchronization of threads using semaphores.

# Sample Commands

Run the file in python in the console here are some sample commands you can try: <br> <br> 
`create_process process1 ping google.com `
This command will create a process called process1 and will ping google.com

### Output 
```
Command: create_process process1 ping google.com   
Process 'process1' created
Command: 
Pinging google.com [2607:f8b0:4006:80b::200e] with 32 bytes of data:
Reply from 2607:f8b0:4006:80b::200e: time=14ms 
Reply from 2607:f8b0:4006:80b::200e: time=12ms 
Reply from 2607:f8b0:4006:80b::200e: time=12ms 
Reply from 2607:f8b0:4006:80b::200e: time=20ms 

Ping statistics for 2607:f8b0:4006:80b::200e:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 12ms, Maximum = 20ms, Average = 14ms
```
<br> 

`list_processes` 
This command will show the processes currently created and running
### Output
```
list_processes
process1  PID: 14528 PPID: 20968
```
<br> 

`terminate_process process1`
This command will terminate process1 which was created before

### Output
```
Command: terminate_process process1
Process 'process1' terminated
Command: list_processes
No processes
```
<br> 

`create_thread thread1 test_function 42,24`
This command will create a thread of the function 

### Output
```
Command: create_thread thread1 test_function 42,24   
Thread 'thread1' created
```

<br> 

`start_thread thread1`
This command will start the thread we previously created 

### Output
```
Command: start_thread thread1  
test_function is running with arguments: 42 24
```
<br> 

`wait_thread thread1`
This command waits until the thread has completed to move on

```
Command: wait_thread thread1
Thread 'thread1' completed
```
<br> 

`producer_consumer`
This command implements a classic synchronization problem using threads and semaphores

```
Command: producer_consumer
Produced 0
Produced 1
Consumed 0
Produced 2
Consumed 1
Produced 3
Consumed 2
Produced 4
Consumed 3
Produced 5
Consumed 4
Produced 6
Consumed 5
Produced 7
Consumed 6
Produced 8
Consumed 7
Produced 9
Consumed 8
Consumed 9
```
<br> 
## Discussion

The process manager provides basic capabilities for process and thread management in Python. Key aspects:

- Cross-platform support using Python standard library
- Simple command-line interface for testing  
- Unit tests cover key functionality   
- Producer-consumer example shows synchronization

Future improvements:

- Add logging and better error handling
- Support process groups and pipelines
- Implement more synchronization constructs  
- Performance testing and optimization

Overall, this project demonstrates core concepts like process control, threading, synchronization, and IPC in a simple command-line application. The code can serve as a starting point for more advanced process management functionality.
