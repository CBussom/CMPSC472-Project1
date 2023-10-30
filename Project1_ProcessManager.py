import threading
import subprocess
import os
import time
import sys
import logging

logging.basicConfig(filename="process_manager.log", level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")
# Process class to encapsulate a subprocess
class Process:
    def __init__(self, command):
        self.command = command  # Initialize with the command to run
        self.process = None  # Initialize the process as None

    def start(self):
        # Start the process by executing the command as a subprocess
        self.process = subprocess.Popen(self.command, shell=True)
        self.pid = self.process.pid  # Get the process ID (PID)

    def terminate(self):
        # Terminate the subprocess
        self.process.terminate()
        logging.info(f"Process terminated (PID: {self.pid})")

    def is_alive(self):
        # Check if the subprocess is still running
        return self.process.poll() is None

    def get_pid(self):
        if self.process:
            return self.process.pid  # Get the PID if the subprocess exists
        else:
            return None

    def get_ppid(self):
        # Get the Parent Process ID (PPID) of the current process
        return os.getppid()

# Thread class to handle threads
class Thread:
    def __init__(self, target, args):
        # Initialize a thread with a target function and its arguments
        self.thread = threading.Thread(target=target, args=args)

    def start(self):
        # Start the thread
        self.thread.start()

    def join(self):
        # Wait for the thread to complete
        self.thread.join()

# ProcessManager class
class ProcessManager:

    def __init__(self):
        self.processes = {}  # Dictionary to store subprocesses
        self.threads = {}  # Dictionary to store threads
        self.lock = threading.Lock()  # Lock for thread safety

    # Process creation
    def create_process(self, name, command):
        p = Process(command)  # Create a new Process object
        p.start()  # Start the subprocess immediately
        self.processes[name] = p  # Store the process in the dictionary
        print(f"Process '{name}' created")
        logging.info(f"Process created (PID: {p.pid}, Name: {name}, Command: {command})")

    # List processes
    def list_processes(self):
        if not self.processes:
            print("No processes")
            return

        for name, p in self.processes.items():
            pid = p.get_pid()  # Check for a valid PID
            if pid:
                print(name, " PID:", p.get_pid(), "PPID:", p.get_ppid())
                logging.info(f"Process listed (PID: {p.pid}, Name: {name})")


    # Terminate a process
    def terminate_process(self, name):
        with self.lock:
            p = self.processes.get(name)  # Get the process by name
            if p:
                p.process.kill()  # Use kill() to forcibly terminate
                p.process.wait()  # Wait for the process to terminate
                print(f"Process '{name}' terminated")
                
                del self.processes[name]
            else:
                print(f"Process '{name}' not found.")
                logging.error(f"Process termination failed (Name: {name})")

    # Create a thread
    def create_thread(self, name, target, args):
        t = Thread(target, args)  # Create a new Thread object
        self.threads[name] = t  # Store the thread in the dictionary
        print(f"Thread '{name}' created")
        logging.info(f"Thread created (Name: {name}, Target: {target.__name__})")

    # Start a thread
    def start_thread(self, name):
        with self.lock:
            t = self.threads[name]
            t.start()  # Start the thread
            logging.info(f"Thread started (Name: {name})")

    # Wait for a thread
    def wait_thread(self, name):
        with self.lock:
            t = self.threads[name]
            t.join()  # Wait for the thread to complete
            print(f"Thread '{name}' completed")
            logging.info(f"Thread completed (Name: {name})")

    # Producer-consumer synchronization
    def producer_consumer(self):
        buffer = []
        can_produce = threading.Semaphore(3)
        can_consume = threading.Semaphore(0)

        def producer():
            for i in range(10):
                can_produce.acquire()
                buffer.append(i)
                print("Produced", i)
                can_consume.release()

        def consumer():
            for i in range(10):
                can_consume.acquire()
                print("Consumed", buffer.pop(0))
                can_produce.release()

        pt = Thread(producer, ())  # Create a thread for the producer function
        ct = Thread(consumer, ())  # Create a thread for the consumer function
        pt.start()  # Start the producer thread
        ct.start()  # Start the consumer thread
        pt.join()  # Wait for the producer thread to complete
        ct.join()  # Wait for the consumer thread to complete
        logging.info("Producer-consumer synchronization completed")

# Test function with arguments
def test_function(arg1, arg2):
    print("test_function is running with arguments:", arg1, arg2)
    logging.info(f"Test function executed with arguments (arg1: {arg1}, arg2: {arg2})")

if __name__ == "__main__":

    pm = ProcessManager()

    # Command line interface
    while True:
        cmd = input("Command: ")

        if cmd == "exit":
            break

        cmds = cmd.split()

        if cmds[0] == "create_process":
            pm.create_process(cmds[1], " ".join(cmds[2:]))
        elif cmds[0] == "list_processes":
            pm.list_processes()
        elif cmds[0] == "terminate_process":
            pm.terminate_process(cmds[1])
        elif cmds[0] == "create_thread":
            pm.create_thread(cmds[1], eval(cmds[2]), eval(cmds[3]))
        elif cmds[0] == "start_thread":
            pm.start_thread(cmds[1])
        elif cmds[0] == "wait_thread":
            pm.wait_thread(cmds[1])
        elif cmds[0] == "producer_consumer":
            pm.producer_consumer()
        else:
            print("Invalid command!")

