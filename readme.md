`Python 3.9.0`
See `requirements.txt` for the rest.

This project is designed to be run as a local website. For that reason, certain steps have been made to make it easier to set up and use, but those steps make the site insecure. Don't host it anywhere public.

# Running the server
## Quick
`source env/bin/activate;python3 manage.py runserver`
## Verbose
- Navigate to /chrisquiz
- Activate the virtual environment with `source env/bin/activate`
- Start the server with `python3 manage.py runserver`
    - Server now running on [127.0.0.1:8000](http://127.0.0.1:8000)
- To run server on your network, use `python3 manage.py runserver 0.0.0.0:8000`
    - Server now running on `<your computer's IP address>:8000` and accessible by anyone on your network.

# Pulling in new changes
- `git pull origin main` pulls in the latest changes.
- If the changes include changes to the database, you must run `python manage.py migrate` to migrate those changes to the database.
