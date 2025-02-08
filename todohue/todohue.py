import argparse
from commands import*
from dbwarehouse import makedware
from rainbow import rainbow
import json

text ="Welcome to todo hue A colorful command-line tool to brigthen up your productivity"
text = rainbow(text)

makedware()
parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,description=text)

parser.add_argument("-add","-a","-ADD","-A",type= str,help="Add your tasks")
parser.add_argument("-list","-l","-L","-LIST",action="store_true",help="Show list of Tasks")
parser.add_argument("-clear","-c","-C","-CLEAR",action="store_true",help="Clear All your Tasks")
parser.add_argument("-done","-d",type=int, help="Remove completed tasks")
parser.add_argument("-edit","-e",type=int, help="Edit specific Tasks")

args = parser.parse_args()

if args.add:
    add(f'{args.add}')
elif args.list:
    lst()
elif args.clear:
    clear()
elif args.done:
    done(args.done)
elif args.edit:
    edit(args.edit)
    