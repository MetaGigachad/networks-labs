from scapy.all import sr1, IP, ICMP
import argparse
import logging
import sys


def is_reachable(host):
    try:
        response = sr1(IP(dst=host)/ICMP(), timeout=2, verbose=0)
        return response is not None
    except Exception:
        return False


def find_mtu(host, max_mtu):
    left, right = 0, max_mtu

    while left <= right:
        mid = (left + right) // 2

        try:
            response = sr1(IP(dst=host, flags="DF")/ICMP() /
                           ("X" * (mid - 28)), timeout=2, verbose=0)
            if response is not None:
                left = mid + 1
            else:
                right = mid - 1
        except Exception:
            right = mid - 1

    return right


logging.getLogger("scapy.runtime").setLevel(logging.FATAL)

parser = argparse.ArgumentParser(
    description='Find the MTU for host.')
parser.add_argument('host', type=str, help='The host to test MTU against')
parser.add_argument('-m', '--max-mtu', type=int, default=1500,
                    help='Upper bound for mtu search')
args = parser.parse_args()

host = args.host

if not is_reachable(host):
    print(f"Error: The host {host} is not reachable or invalid.")
    sys.exit(1)

try:
    mtu = find_mtu(host, args.max_mtu)
    print(f"The minimum MTU for the host {host} is {mtu}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)
