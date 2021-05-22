# Running the server
- Navigate to /chrisquiz
- Activate the virtual environment with `source env/bin/activate`
- Start the server with `python3 manage.py runserver`
    - Server now running on [127.0.0.1:8000](http://127.0.0.1:8000)
- To run server on your network, use `python3 manage.py runserver 0.0.0.0:8000`
    - Server now running on `<your computer's IP address>:8000` and accessible by anyone on your network.