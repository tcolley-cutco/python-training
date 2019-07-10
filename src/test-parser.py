from cli_parser import parse_args
import sys

print(sys.argv)

args = parse_args(sys.argv)
for key, value in args.items():
    print(f"Key: {key} | Value: {value}")

print(sys.argv)
