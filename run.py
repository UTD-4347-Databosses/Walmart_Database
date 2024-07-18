import logging
from app import create_app

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

