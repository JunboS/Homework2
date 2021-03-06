# Random numbers and visualization.  
## Scripts:
1a.py : generate 1000 random numbers over 0-100.  
1b.py : generate another 1000 new random numbers from the output of 1a using the equation y = 3x + 6.  
1c.py : visualize the results from 1a and 1b.  
random_number_generator.ipynb : run all 3 steps of 1a, 1b, and 1c, and visualize each step in jupyter notebook  
## Instructions:
### How to create a virtual environment
We will use pip in this tutorial  
1. Ensure you can run pip from the command line  
   pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4  
   you can check python version by running:  
        `python --version`
2. install virtualenv by running:  
        `pip install virtualenv`  
3. change to Homework2 directory and create a virtual environment by running:  
        `py -m venv dsci560H4`  
   dsci560H4 is the name of environment  
![q1](https://github.com/JunboS/Homework2/blob/master/q1.png?raw=true)

4. you have to activate it by running:  
        `.\dsci560H4\Scripts\activate`  
![q1](https://github.com/JunboS/Homework2/blob/master/q2.png?raw=true)

5. install the required package matplotlib for the scripts  
        `pip install matplotlib`  
### Execute the scripts  
6. by running:  
    `python 1a.py`  
    `python 1b.py`  
    `python 1c.py`  
    
![q3](https://github.com/JunboS/Homework2/blob/master/q3.png?raw=true)

7. when you are done, stop the virtual environment by running:  
         `deactivate`  
         
## Compare the packages
### manually installed:  
matplotlib 3.3.2  
### extracted dependency:  
certifi==2020.6.20  
cycler==0.10.0  
kiwisolver==1.3.0  
matplotlib==3.3.2  
numpy==1.19.3  
Pillow==8.0.1  
pyparsing==2.4.7  
python-dateutil==2.8.1  
six==1.15.0  

Open the notebook by clicking this Binder badge [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/JunboS/Homework2/75136a423d5b0f3a08d9864c2e8991378d4943fc)

Zenodo badge with the DOI [![DOI](https://zenodo.org/badge/298488549.svg)](https://zenodo.org/badge/latestdoi/298488549)
