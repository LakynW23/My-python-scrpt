This Python script performs a multi-threaded port scan to identify open ports on a target IP address or domain. It scans ports from 1 to 1024, commonly used for network services. Key features include: 
Multi-threading: Speeds up the scan by using multiple threads to check different ports concurrently.
Timeout Handling: Each connection attempt has a timeout of 1 second to avoid long delays.
Logging: Results are logged into a file (port_scan_results.log), recording open ports and errors.
Simple User Input: The user provides the target IP/domain, and the script handles the rest.
Ideal for network security assessments and identifying open services on a host.
