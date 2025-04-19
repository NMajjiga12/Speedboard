from src.leaderboard_frontend import Frontend
from src.leaderboard_backend import Backend

def main():
    """Main application entry point"""
    backend = Backend()
    frontend = Frontend(backend)
    frontend.run()

if __name__ == "__main__":
    main()