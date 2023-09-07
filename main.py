# main.py
from lib.database import initialize_database
from lib.cli import main

if __name__ == "__main__":
    initialize_database()
    main()
