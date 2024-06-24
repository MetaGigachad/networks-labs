import argparse
import icmplib
import sys


def is_reachable(host):
    result = icmplib.ping(host)
    return result.is_alive


def find_mtu(host, max_mtu):
    left, right = 0, max_mtu
    while left < right:
        mid = (left + right + 1) // 2
        print(f"Current mid: {mid}, left: {left}, right: {right}")

        try:
            status = icmplib.ping(
                host,
                payload_size=mid - 28,
                timeout=2,
                count=1,
                interval=0,
            )
            if status.is_alive:
                left = mid
            else:
                right = mid - 1
        except icmplib.exceptions.DestinationUnreachable:
            print(f"Error: The host {host} is not reachable.")
            sys.exit(1)
        except icmplib.exceptions.NameLookupError:
            print(f"Error: The host {host} is not resolved.")
            sys.exit(1)
    return right


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
