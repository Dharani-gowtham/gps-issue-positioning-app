#### python version 3.10.0
## Steps for Starting

## Installation

Creating Virtual Environment

    python -m venv venv

Activating the Environment

    ./venv/Scripts/activate

Installing the Requirements

    pip install -r requirements.txt

Running the `api.py` file in the beginning to get the server ip address

    python api.py

Get the `ip` address from the flask application and replace with the ip in the `Dashboard.py` and `pages\History.py` file

Now run the `Dashboard.py` file

    streamlit run Dashboard.py