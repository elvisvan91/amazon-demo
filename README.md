# amazon-testing
1. Install python 3
2. Activate virtual environment 
    + amazon-testing\venv\activate.bat
3. Install requirements.txt
	+ pip3 install -r requirements.txt 
4. Set environment for chrome driver
5. How to run test:
    + pytest -s -v testcases\test_search_product.py -k "test_amazon" --html=logs\test_amazon.html --browser gc
