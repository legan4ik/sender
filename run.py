import sys
import sender

"""This is the file to run
Prerequisites (ubuntu):
apt-get install python-pip python-dev -y
pip install virtualenv
virtualenv venv
pip install -r requirements.txt (from this repo)

Prerequisites (windows):
tbd (install python and requirements)

Run example: python run.py 4 http://test.com
"""

print("Checking command line arguments")
if len(sys.argv) == 3:
    # 1st element in this list is file name,
    # 2nd will be number of requests argument
    # and 3rd will be endpoint
    count = int(sys.argv[1])
    endpoint = sys.argv[2]
else:
    raise Exception("Please specify number of requests and endpoint\n"
                    "Run example: python run.py 4 http://test.com")

sender.Sender(count, endpoint).send()
