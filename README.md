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

Run the file in python in the console here are some sample commands you can try:
`create_process p1 timeout /t 5`
This command will create a process called p1 with a sleep of 5 seconds

![Process Creation Test](images/test_process_creation.png)

`list_processes` 
This command will show the processes currently created and running

`create_thread t1 test_function 10 20`
This command will create a thread of the function 


## Discussion

The process manager provides basic capabilities for process and thread management in Python. Key aspects:

- Cross-platform support using Python standard library
- Simple command-line interface for testing  
- Unit tests cover key functionality   
- Producer-consumer example shows synchronization

Limitations:

- Currently only supports basic process and thread operations
- No parallel execution of multiple processes
- Minimal error handling

Future improvements:

- Add logging and better error handling
- Support process groups and pipelines
- Implement more synchronization constructs  
- Performance testing and optimization

Overall, this project demonstrates core concepts like process control, threading, synchronization, and IPC in a simple command-line application. The code can serve as a starting point for more advanced process management functionality.
