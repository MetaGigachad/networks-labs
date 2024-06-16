import argparse
from scapy.all import sr1, IP, ICMP
import sys


def is_reachable(host):
    try:
        response = sr1(IP(dst=host)/ICMP(), timeout=2, verbose=0)
        return response is not None
    except Exception:
        return False


def find_mtu(host):
    left, right = 0, 1500

    while left <= right:
        mid = (left + right) // 2

        try:
            response = sr1(IP(dst=host, flags="DF")/ICMP() /
                           ("X" * mid), timeout=2, verbose=0)
            if response is not None:
                left = mid + 1
            else:
                right = mid - 1
        except Exception:
            right = mid - 1

    return right


parser = argparse.ArgumentParser(
    description='Find the MTU for host.')
parser.add_argument('host', type=str, help='The host to test MTU against')
args = parser.parse_args()

host = args.host

if not is_reachable(host):
    print(f"Error: The host {host} is not reachable or invalid.")
    sys.exit(1)

try:
    mtu = find_mtu(host)
    print(f"The minimum MTU for the host {host} is {mtu}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)
