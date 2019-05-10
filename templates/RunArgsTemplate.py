# More info: https://docs.python.org/3/library/argparse.html
import argparse

parser = argparse.ArgumentParser(prog='this app', description='Here comes the master description',
                                 epilog= "Final words")

# No-option takes default value, option but no arg takes const value
parser.add_argument('-x', '--xpand', dest='expander', nargs='?', const='A', default='D', help="Expander status [A/D/x]")

parser.add_argument('-n', '--nora', dest='pusher', type=int, default=0, help="Pusher level [Def:0]")

parser.add_argument('activity', nargs='?',  default='fly', choices=['fly', 'swim', 'walk'], help="Select among them")

parser.add_argument('comms', metavar='CID', type=int, nargs='+', help=':Comms list')

parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.0')


# Other undefined args collector - commented out
#parser.add_argument('args', nargs=argparse.REMAINDER)

args = parser.parse_args()

print(f"Expander set to: {args.expander}")
print(f"Pusher set to: {args.pusher}")
print(f"Comms set to: {args.comms}")
print(f"Activity set to: {args.activity}")
