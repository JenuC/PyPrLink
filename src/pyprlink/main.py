from pyprlink.tcp_client import ask_PV
from pyprlink import __version__
import sys
import argparse

def main():

    crude_default = False

    if not crude_default:
        
        parser = argparse.ArgumentParser(description='PyPrLink - TCP/IP client for communicating with PrairieView')
        parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')  
        #parser.add_argument('-gmp', choices=['x','y','z'], help='get motor position for motor') 
        #parser.add_argument('-pg', nargs=2, help='set PMT Gain value') 
        
        #args = parser.parse_args()
        #args,message = parser.parse_known_args()
        #print(message)
        args,message = parser.parse_known_intermixed_args()
        print(args, message)
        
        #    if args.gmp is not None:
        #        message = ["-gmp"]+ [args.gmp]
        #    if args.pg is not None:
        #        message = ["-pg"]+ args.pg
        
        #print(message, *message)
        try:
            print(*message)
            ask_PV(*message)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

        
        
        
    if crude_default:
        args = sys.argv[1:]
        
        if '--version' in args:
            args.remove('--version')
            print(f'{__version__}')  
            
        elif '--help' in args:
            args.remove('--help')
            print(f'cmd {args}')  
            
        else:
            try:
                ask_PV(*args)
            except Exception as e:
                print(f"Error: {e}", file=sys.stderr)
                sys.exit(1)

if __name__ == "__main__":
    main()        