# amazon-testing
1. Install python 3
2. Activate virtual environment 
    + amazon-testing\venv\activate.bat
3. Set environment for chrome driver
4. How to run test:
    + pytest -s -v amazon-testing\web-ui\testcases\test_amazon.py -k "test_amazon" --html=logs\test_amazon.html --browser gc
