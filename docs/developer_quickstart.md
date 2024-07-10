# Development Quickstart

## Project Structure
Our project is a website that is built using the [Flask Framework](https://flask.palletsprojects.com/en/3.0.x/quickstart/). The project structure is as follows:

```
.
├── app
│   ├── __init__.py
│   ├── routes.py <- Backend
│   ├── static <- Frontend
│   │   ├── css
│   │   ├── images
│   │   ├── js
│   ├── templates <- Frontend
│   │   ├── frontent.html
│   │   ├── layout.html
├── docs
│   ├── developer_quickstart.md
├── tests
├── venv
├── .gitignore
├── .flaskenv
├── requirements.txt <- pip can install these
├── run.py <- Entry point
```

## Setting up the project
1. Install necessary languages/tools:
    - Python 3.8 or higher
    - Git
2. Clone the repository:
    ```bash
    git clone https://github.com/UTD-4347-Databosses/Walmart_Database.git
    ```
3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```
5. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
6. Switch branches:
    ```bash
    git checkout dev/backend #OR dev/frontend
    ```
7. Run the application:
    ```bash
    python run.py
    ```
8. Code away

Code is located in the `app` directory. The backend is in `routes.py` and the frontend is in the `static` and `templates` directories.
9. *__PUSH AND PULL REGURLARLY__*

This is vital for us to be able to work synchronously. Make sure you push and pull changes regularly and include descriptive comments on your commits. It is best practice to push your changes every time you stop working on a feature/page. It not only helps everyone stay up to date, but it also helps you write push comments that are descriptive of the changes you made AND prevents the hellish experience of trying to merge conflicts.

This process is done by running the following commands:
```bash
git fetch
git pull
git add {the path to the file you changed}
git commit -m "A descriptive message of what you changed"
git push
```

10. *__TO GET YOUR CHANGES INTO THE MAIN BRANCH__*

Once you have made your changes and are ready to merge them into the main branch, you will need to create a pull request. This is done by going to the github repository and clicking on the "Pull Requests" tab. From there, you will click on the "New Pull Request" button and select the branch you want to merge into the main branch. Once you have done this, you will need to request a review from the @UTD-4347-Databosses/code-review team. Once the review is complete, you can merge the changes into the main branch.