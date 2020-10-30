## Random numbers and visualization.  

# Instructions:
# How to create a virtual environment
We will use pip in this tutorial  
1. Ensure you can run pip from the command line  
   pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4  
   you can check python version by running:  
        'python --version'
2. run the following command to install virtualenv:  
        'pip install virtualenv'  
3. change to a favor directory and create a virtual environment by running:  
        'py -m venv dsci560H4'  
   dsci560H4 is the name of environment  
4. you have to activate it by running:  
        '.\dsci560H4\Scripts\activate'  
5. install the dependencies for the scripts  
        'pip install matplotlib'  
6. running the 3 scripts:  
    'python 1a.py'  
    'python 1b.py'  
    'python 1c.py'  
    
![q3](https://github.com/JunboS/Homework2/blob/master/q3.png?raw=true)
1a.py script generates 1000 random numbers over 0-100.  
1b.py script generates another 1000 new random numbers from the output of 1a using the equation y = 3x + 6.  
1c.py script visualizes the results from 1a and 1b.  
random_number_generator.ipynb script shows the 3 steps by calling 1a, 1b, and 1c.   

Zenodo badge with the DOI [![DOI](https://zenodo.org/badge/298488549.svg)](https://zenodo.org/badge/latestdoi/298488549)

[![Binder](https://mybinder.org/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/JunboS/Homework2/06df3d8c0fc5cc9b0311c3f22d656a58f92291f9)
