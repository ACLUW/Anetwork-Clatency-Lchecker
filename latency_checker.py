# Network Latency Checker with Logging and Error Handling
# Author: ACL
# Description: This script pings a list of servers to check network latency and logs the results.
# Date: 2025

import logging
from ping3 import ping

# Configure logging
logging.basicConfig(filename="latency_logs.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

# List of servers to test latency
servers = ["8.8.8.8", "1.1.1.1", "8.8.4.4"]  # Google and Cloudflare DNS

def check_latency(server):
    """Ping a server and return the latency in milliseconds. (ACL)"""
    try:
        latency = ping(server, unit='ms')  # Ping and get response time in ms
        if latency is None:
            result = f"Server {server} is unreachable."
        else:
            result = f"Server {server} responded in {latency:.2f} ms."
        logging.info(result)  # Log the result
        return result
    except Exception as e:
        error_msg = f"Error pinging {server}: {str(e)}"
        logging.error(error_msg)
        return error_msg

def main():
    print("Network Latency Checker (ACL)")
    for server in servers:
        print(check_latency(server))

if __name__ == "__main__":
    main()
