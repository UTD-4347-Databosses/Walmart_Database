import logging
from app import create_app
import subprocess
from threading import Timer



# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')


app = create_app()

# opens web browser
def open_browser():
    subprocess.run(["python", "-m", "webbrowser", "-t", "http://127.0.0.1:8080/"])

if __name__ == '__main__':
    # Set a timer to open the browser after a short delay
    Timer(1, open_browser).start()
    app.run(host='0.0.0.0', port=8080, debug=True)

