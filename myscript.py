import socket
import threading
import time
import logging

# Setting up logging to record the scan results into a file
logging.basicConfig(filename='port_scan_results.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Function to scan a single port
def scan_port(target, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout of 1 second for the connection attempt
        
        # Attempt to connect to the port on the target
        result = sock.connect_ex((target, port))  # connect_ex returns 0 if successful
        
        if result == 0:
            # If the port is open, log and print the result
            print(f"Port {port} is open on {target}")
            logging.info(f"Port {port} is open on {target}")
        
        sock.close()
    except socket.error as err:
        # Handle errors during connection attempt
        print(f"Error occurred while scanning port {port}: {err}")
        logging.error(f"Error occurred while scanning port {port}: {err}")

# Function to perform the port scan using multi-threading
def port_scan(target, ports, threads):
    # Split the work among threads for faster execution
    def scan_worker(start, end):
        for port in range(start, end):
            scan_port(target, port)

    # Calculate the number of ports per thread
    num_ports = len(ports)
    ports_per_thread = num_ports // threads
    threads_list = []

    # Create and start the threads
    for i in range(threads):
        start_port = i * ports_per_thread
        end_port = (i + 1) * ports_per_thread if i != threads - 1 else num_ports
        thread = threading.Thread(target=scan_worker, args=(start_port, end_port))
        threads_list.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads_list:
        thread.join()

# Main function to run the script
def main():
    print("Welcome to the Python Port Scanner!")
    
    # Input from the user for the target IP or domain
    target = input("Enter target IP or domain (e.g., 192.168.1.1 or example.com): ").strip()

    # Validate the target IP or domain
    try:
        socket.gethostbyname(target)  # Check if the target resolves to an IP address
    except socket.gaierror:
        print(f"Invalid target: {target}. Please enter a valid IP address or domain.")
        return

    # Define the port range to scan (1 to 1024, which includes many common services)
    ports = list(range(1, 1025))

    # Number of threads to use for multi-threading
    threads = 10
    print(f"\nStarting port scan on {target} with {threads} threads...")

    # Log the start of the scan
    logging.info(f"Starting port scan on {target} with {threads} threads.")

    # Record the start time
    start_time = time.time()

    # Run the port scan
    port_scan(target, ports, threads)

    # Record the end time
    end_time = time.time()

    # Display the result time
    print(f"\nScan completed in {end_time - start_time:.2f} seconds.")
    logging.info(f"Scan completed on {target} in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()
{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import socket\
import threading\
import time\
import logging\
\
# Setting up logging to record the scan results into a file\
logging.basicConfig(filename='port_scan_results.log', level=logging.INFO, \
                    format='%(asctime)s - %(levelname)s - %(message)s')\
\
# Function to scan a single port\
def scan_port(target, port):\
    try:\
        # Create a socket object\
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\
        sock.settimeout(1)  # Set a timeout of 1 second for the connection attempt\
        \
        # Attempt to connect to the port on the target\
        result = sock.connect_ex((target, port))  # connect_ex returns 0 if successful\
        \
        if result == 0:\
            # If the port is open, log and print the result\
            print(f"Port \{port\} is open on \{target\}")\
            logging.info(f"Port \{port\} is open on \{target\}")\
        \
        sock.close()\
    except socket.error as err:\
        # Handle errors during connection attempt\
        print(f"Error occurred while scanning port \{port\}: \{err\}")\
        logging.error(f"Error occurred while scanning port \{port\}: \{err\}")\
\
# Function to perform the port scan using multi-threading\
def port_scan(target, ports, threads):\
    # Split the work among threads for faster execution\
    def scan_worker(start, end):\
        for port in range(start, end):\
            scan_port(target, port)\
\
    # Calculate the number of ports per thread\
    num_ports = len(ports)\
    ports_per_thread = num_ports // threads\
    threads_list = []\
\
    # Create and start the threads\
    for i in range(threads):\
        start_port = i * ports_per_thread\
        end_port = (i + 1) * ports_per_thread if i != threads - 1 else num_ports\
        thread = threading.Thread(target=scan_worker, args=(start_port, end_port))\
        threads_list.append(thread)\
        thread.start()\
\
    # Wait for all threads to complete\
    for thread in threads_list:\
        thread.join()\
\
# Main function to run the script\
def main():\
    print("Welcome to the Python Port Scanner!")\
    \
    # Input from the user for the target IP or domain\
    target = input("Enter target IP or domain (e.g., 192.168.1.1 or example.com): ").strip()\
\
    # Validate the target IP or domain\
    try:\
        socket.gethostbyname(target)  # Check if the target resolves to an IP address\
    except socket.gaierror:\
        print(f"Invalid target: \{target\}. Please enter a valid IP address or domain.")\
        return\
\
    # Define the port range to scan (1 to 1024, which includes many common services)\
    ports = list(range(1, 1025))\
\
    # Number of threads to use for multi-threading\
    threads = 10\
    print(f"\\nStarting port scan on \{target\} with \{threads\} threads...")\
\
    # Log the start of the scan\
    logging.info(f"Starting port scan on \{target\} with \{threads\} threads.")\
\
    # Record the start time\
    start_time = time.time()\
\
    # Run the port scan\
    port_scan(target, ports, threads)\
\
    # Record the end time\
    end_time = time.time()\
\
    # Display the result time\
    print(f"\\nScan completed in \{end_time - start_time:.2f\} seconds.")\
    logging.info(f"Scan completed on \{target\} in \{end_time - start_time:.2f\} seconds.")\
\
if __name__ == "__main__":\
    main()\
}
