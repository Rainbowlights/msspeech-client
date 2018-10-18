#!/usr/bin/env python

# For some reason Python 2 and Python 3 disagree about how to import this.
try:
    from msclient.msclient import main as other_main
except Exception:
    from msclient import main as other_main


def main():
    """Run the program."""
    other_main()

if __name__ == "__main__":
    main()
