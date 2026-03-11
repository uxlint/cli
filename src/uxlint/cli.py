import argparse
from . import __version__

def main():
    parser = argparse.ArgumentParser(description="UXLint — AI-powered UX checker")
    parser.add_argument("--version", action="version", version=f"uxlint {__version__}")
    parser.parse_args()

if __name__ == "__main__":
    main()