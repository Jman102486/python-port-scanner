import socket
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import csv

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NETBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}

def grab_banner(sock):
    try:
        sock.settimeout(1)
        banner = sock.recv(1024).decode().strip()
        return banner
    except:
        return ""

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((host, port))

            if result == 0:
                service = COMMON_PORTS.get(port, "Unknown")
                banner = grab_banner(sock)
                return (port, service, banner)
    except:
        pass
    return None

def scan_target(host, ports, threads):
    print(f"\nScanning {host}")
    print(f"Started at: {datetime.now()}\n")

    open_ports = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(scan_port, host, port) for port in ports]

        for future in futures:
            result = future.result()
            if result:
                port, service, banner = result
                print(f"[OPEN] Port {port} ({service})")
                if banner:
                    print(f"       Banner: {banner}")
                open_ports.append(result)

    print("\nScan Complete")
    return open_ports

def save_to_csv(results, filename="results.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Port", "Service", "Banner"])
        writer.writerows(results)
    print(f"\nSaved to {filename}")

def parse_ports(port_range):
    start, end = map(int, port_range.split("-"))
    return range(start, end + 1)

def main():
    parser = argparse.ArgumentParser(description="Python Port Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP or domain")
    parser.add_argument("-p", "--ports", required=True, help="Port range (e.g. 1-100)")
    parser.add_argument("-th", "--threads", type=int, default=200, help="Number of threads")
    parser.add_argument("-o", "--output", help="Save results to CSV")

    args = parser.parse_args()

    ports = parse_ports(args.ports)
    results = scan_target(args.target, ports, args.threads)

    if args.output:
        save_to_csv(results, args.output)

if __name__ == "__main__":
    main()
