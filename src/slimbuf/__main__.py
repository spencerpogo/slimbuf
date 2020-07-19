import sys

from . import slimbuf

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <filename>", file=sys.stderr)
        sys.exit(1)

    with open(sys.argv[1], "r") as f:
        fdef_data = f.read()

    fdef = bufcompile.FuncDef()
    fdef.parse(fdef_data)
    fdef.write_from_data()
