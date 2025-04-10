from pyprlink.tcp_client import ask_PV
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        args_= sys.argv[1:]
        ask_PV(*args_)        