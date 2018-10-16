Add Python header files for python3.6 (otherwise installing psutil with pip3 will crash):  
	$ sudo apt install python3.6-dev  

Create virtualenv (optional):  
	$ virtualenv env -p python3.6  
	$ source env/bin/activate  

Install requirements:  
	$ (env) pip3 install -r requirements.txt  

Run dummy test:  
	$ (env) python3.6 test_spade.py
