import argparse
parser=argparse.ArgumentParser(description="Count the no. of lines in a file")
parser.add_argument("file_path",type=str,help="Path of the file.")
args=parser.parse_args()
try:
    with open(args.file_path,"r") as f:
        lines=f.readlines()
        print(f"No. of lines is {len(lines)}")
except FileNotFoundError:
    print("Error: File not Found")
except Exception as e:
    print(f"Error:{e}")


