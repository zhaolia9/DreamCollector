import sys
import os

# Add the aurelia directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from backend.app import main

if __name__ == "__main__":
    main()