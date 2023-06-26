### args
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", type=str, required=True)
args = parser.parse_args()

file_path = args.file
print(file_path)
with open(file_path, 'r') as file:
    content = file.read()

print(content)