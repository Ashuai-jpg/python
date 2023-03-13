#Accpting Arguments
import sys
import argparse

name = sys.argv[1]
print(f"Hello {name}")

parser = argparse.ArgumentParser(
    description="This Program prints the name of my dog"
)

parser.add_argument("-c", "--color", metavar='color', required=True,
                    choices=['red', 'yellow'], help="The color to search for")

args = parser.parse_args()

print(args.color)