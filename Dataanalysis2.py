{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Apple Stock\n",
    "\n",
    "Check out [Apple Stock Exercises Video Tutorial](https://youtu.be/wpXkR_IZcug) to watch a data scientist go through the exercises"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Introduction:\n",
    "\n",
    "We are going to use Apple's stock price.\n",
    "\n",
    "\n",
    "### Step 1. Import the necessary libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "# visualization\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step 3. Assign it to a variable apple"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Adj Close</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2014-07-08</td>\n",
       "      <td>96.27</td>\n",
       "      <td>96.80</td>\n",
       "      <td>93.92</td>\n",
       "      <td>95.35</td>\n",
       "      <td>65130000</td>\n",
       "      <td>95.35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2014-07-07</td>\n",
       "      <td>94.14</td>\n",
       "      <td>95.99</td>\n",
       "      <td>94.10</td>\n",
       "      <td>95.97</td>\n",
       "      <td>56305400</td>\n",
       "      <td>95.97</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2014-07-03</td>\n",
       "      <td>93.67</td>\n",
       "      <td>94.10</td>\n",
       "      <td>93.20</td>\n",
       "      <td>94.03</td>\n",
       "      <td>22891800</td>\n",
       "      <td>94.03</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2014-07-02</td>\n",
       "      <td>93.87</td>\n",
       "      <td>94.06</td>\n",
       "      <td>93.09</td>\n",
       "      <td>93.48</td>\n",
       "      <td>28420900</td>\n",
       "      <td>93.48</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2014-07-01</td>\n",
       "      <td>93.52</td>\n",
       "      <td>94.07</td>\n",
       "      <td>93.13</td>\n",
       "      <td>93.52</td>\n",
       "      <td>38170200</td>\n",
       "      <td>93.52</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date   Open   High    Low  Close    Volume  Adj Close\n",
       "0  2014-07-08  96.27  96.80  93.92  95.35  65130000      95.35\n",
       "1  2014-07-07  94.14  95.99  94.10  95.97  56305400      95.97\n",
       "2  2014-07-03  93.67  94.10  93.20  94.03  22891800      94.03\n",
       "3  2014-07-02  93.87  94.06  93.09  93.48  28420900      93.48\n",
       "4  2014-07-01  93.52  94.07  93.13  93.52  38170200      93.52"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv'\n",
    "apple = pd.read_csv(url)\n",
    "\n",
    "apple.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step 4.  Check out the type of the columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Date          object\n",
       "Open         float64\n",
       "High         float64\n",
       "Low          float64\n",
       "Close        float64\n",
       "Volume         int64\n",
       "Adj Close    float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "apple.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step 5. Transform the Date column as a datetime type"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0   2014-07-08\n",
       "1   2014-07-07\n",
       "2   2014-07-03\n",
       "3   2014-07-02\n",
       "4   2014-07-01\n",
       "Name: Date, dtype: datetime64[ns]"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "apple.Date = pd.to_datetime(apple.Date)\n",
    "\n",
    "apple['Date'].head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step 6.  Set the date as the index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Adj Close</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2014-07-08</th>\n",
       "      <td>96.27</td>\n",
       "      <td>96.80</td>\n",
       "      <td>93.92</td>\n",
       "      <td>95.35</td>\n",
       "      <td>65130000</td>\n",
       "      <td>95.35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2014-07-07</th>\n",
       "      <td>94.14</td>\n",
       "      <td>95.99</td>\n",
       "      <td>94.10</td>\n",
       "      <td>95.97</td>\n",
       "      <td>56305400</td>\n",
       "      <td>95.97</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2014-07-03</th>\n",
       "      <td>93.67</td>\n",
       "      <td>94.10</td>\n",
       "      <td>93.20</td>\n",
       "      <td>94.03</td>\n",
       "      <td>22891800</td>\n",
       "      <td>94.03</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2014-07-02</th>\n",
       "      <td>93.87</td>\n",
       "      <td>94.06</td>\n",
       "      <td>93.09</td>\n",
       "      <td>93.48</td>\n",
       "      <td>28420900</td>\n",
       "      <td>93.48</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2014-07-01</th>\n",
       "      <td>93.52</td>\n",
       "      <td>94.07</td>\n",
       "      <td>93.13</td>\n",
       "      <td>93.52</td>\n",
       "      <td>38170200</td>\n",
       "      <td>93.52</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Open   High    Low  Close    Volume  Adj Close\n",
       "Date                                                       \n",
       "2014-07-08  96.27  96.80  93.92  95.35  65130000      95.35\n",
       "2014-07-07  94.14  95.99  94.10  95.97  56305400      95.97\n",
       "2014-07-03  93.67  94.10  93.20  94.03  22891800      94.03\n",
       "2014-07-02  93.87  94.06  93.09  93.48  28420900      93.48\n",
       "2014-07-01  93.52  94.07  93.13  93.52  38170200      93.52"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "apple = apple.set_index('Date')\n",
    "\n",
    "apple.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step 7.  Is there any duplicate dates?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# NO! All are unique\n",
    "apple.index.is_unique"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step 8.  Ops...it seems the index is from the most recent date. Make the first entry the oldest date."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Adj Close</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1980-12-12</th>\n",
       "      <td>28.75</td>\n",
       "      <td>28.87</td>\n",
       "      <td>28.75</td>\n",
       "      <td>28.75</td>\n",
       "      <td>117258400</td>\n",
       "      <td>0.45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1980-12-15</th>\n",
       "      <td>27.38</td>\n",
       "      <td>27.38</td>\n",
       "      <td>27.25</td>\n",
       "      <td>27.25</td>\n",
       "      <td>43971200</td>\n",
       "      <td>0.42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1980-12-16</th>\n",
       "      <td>25.37</td>\n",
       "      <td>25.37</td>\n",
       "      <td>25.25</td>\n",
       "      <td>25.25</td>\n",
       "      <td>26432000</td>\n",
       "      <td>0.39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1980-12-17</th>\n",
       "      <td>25.87</td>\n",
       "      <td>26.00</td>\n",
       "      <td>25.87</td>\n",
       "      <td>25.87</td>\n",
       "      <td>21610400</td>\n",
       "      <td>0.40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1980-12-18</th>\n",
       "      <td>26.63</td>\n",
       "      <td>26.75</td>\n",
       "      <td>26.63</td>\n",
       "      <td>26.63</td>\n",
       "      <td>18362400</td>\n",
       "      <td>0.41</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Open   High    Low  Close     Volume  Adj Close\n",
       "Date                                                        \n",
       "1980-12-12  28.75  28.87  28.75  28.75  117258400       0.45\n",
       "1980-12-15  27.38  27.38  27.25  27.25   43971200       0.42\n",
       "1980-12-16  25.37  25.37  25.25  25.25   26432000       0.39\n",
       "1980-12-17  25.87  26.00  25.87  25.87   21610400       0.40\n",
       "1980-12-18  26.63  26.75  26.63  26.63   18362400       0.41"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "apple.sort_index(ascending = True).head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step 9. Get the last business day of each month"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Adj Close</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1980-12-31</th>\n",
       "      <td>30.481538</td>\n",
       "      <td>30.567692</td>\n",
       "      <td>30.443077</td>\n",
       "      <td>30.443077</td>\n",
       "      <td>25862523</td>\n",
       "      <td>0.473077</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1981-01-30</th>\n",
       "      <td>31.754762</td>\n",
       "      <td>31.826667</td>\n",
       "      <td>31.654762</td>\n",
       "      <td>31.654762</td>\n",
       "      <td>7249866</td>\n",
       "      <td>0.493810</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1981-02-27</th>\n",
       "      <td>26.480000</td>\n",
       "      <td>26.572105</td>\n",
       "      <td>26.407895</td>\n",
       "      <td>26.407895</td>\n",
       "      <td>4231831</td>\n",
       "      <td>0.411053</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1981-03-31</th>\n",
       "      <td>24.937727</td>\n",
       "      <td>25.016818</td>\n",
       "      <td>24.836364</td>\n",
       "      <td>24.836364</td>\n",
       "      <td>7962690</td>\n",
       "      <td>0.387727</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1981-04-30</th>\n",
       "      <td>27.286667</td>\n",
       "      <td>27.368095</td>\n",
       "      <td>27.227143</td>\n",
       "      <td>27.227143</td>\n",
       "      <td>6392000</td>\n",
       "      <td>0.423333</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 Open       High        Low      Close    Volume  Adj Close\n",
       "Date                                                                       \n",
       "1980-12-31  30.481538  30.567692  30.443077  30.443077  25862523   0.473077\n",
       "1981-01-30  31.754762  31.826667  31.654762  31.654762   7249866   0.493810\n",
       "1981-02-27  26.480000  26.572105  26.407895  26.407895   4231831   0.411053\n",
       "1981-03-31  24.937727  25.016818  24.836364  24.836364   7962690   0.387727\n",
       "1981-04-30  27.286667  27.368095  27.227143  27.227143   6392000   0.423333"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "apple_month = apple.resample('BM').mean()\n",
    "\n",
    "apple_month.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step 10.  What is the difference in days between the first day and the oldest"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12261"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(apple.index.max() - apple.index.min()).days"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step 11.  How many months in the data we have?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "404"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "apple_months = apple.resample('BM').mean()\n",
    "\n",
    "len(apple_months.index)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step 12. Plot the 'Adj Close' value. Set the size of the figure to 13.5 x 9 inches"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAxYAAAILCAYAAAB1gQpWAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAIABJREFUeJzs3XmYHGW99vH7mUxmJvtkISsJe1hCQkA2ZRv2EBFQEWUx\nAVxQQDwqu4oJrwoiHMEDnHM4LEIkIIIKCEgIMCIBJOyQQAhEEpOQkD2Zfabnef94pqjunu6eXqq7\nunu+n+uaq6qrq6t+6QRSd57NWGsFAAAAALmoCLsAAAAAAKWPYAEAAAAgZwQLAAAAADkjWAAAAADI\nGcECAAAAQM4IFgAAAAByRrAAAPTIGDPTGPOPsOtIxRjzrDHm3LDrAIDeimABAGXGGFNvjNlojOkb\n8KWzWvjIGLOXMeZJY8yGrroWGmOmdb13hDHm38GWCQAIA8ECAMqIMWYHSYdK6pR0UsjleB6V9KSk\nUZJGSrpI0tau94yyDCwAgOJCsACA8jJD0ouSfifp7Og3jDF3GWP+2xgzzxiztavr0ISo9zuNMd8z\nxnxojPnEGHNdspsYY/bous4GY8y7xpivJDlvuKQdJd1ure3o+nnRWvuCMaa/pMcljTXGbOuqabQx\npsoYc6MxZpUxZqUx5jfRrS/GmJONMa8bY7YYY5YaY45LcN8xxpg3jTE/yuTLAwBkj2ABAOVlhqTf\nS5or6XhjzHZx758habak4ZLelHRv3PunSNqv6+fkRGMWugLBvK77jJD0NUm3GGP2iD/XWrtB0geS\n7u0KBCOj3muSdIKk1dbaQdbawdbaNZJ+IulASVMk7dO1/5Ouex8o6W5JP7LWDpF0uKSP4urbUVK9\npN9aa29I8j0BAAJGsACAMmGMOVTSBEkPWGtfk3ugPyPutMestQuste2Sfizps8aYcVHvX2ut3WKt\nXSnpRkmnJ7jViZL+Za29xzpvSvqTpIStFpKOlPQvSddLWt01BmSXFL+UMyTNttZu6AomsyV9veu9\ncyXdYa19RpKstR9ba9+P+uwkSc9K+qm19o4U9wAABIxgAQDlY4akedbaTV2v75M0M+6cTwdKW2sb\nJW2UNDbq/ZVR+8vj3vPsIOngroHYG40xm+TCwOhERVlrV1trL7LW7tb12SZJ96T4dYyVtCJJHeMl\nfZjis2d0/RoeSnEOACAPKsMuAACQO2NMjaTTJFUYYz7uOlwlqdYYM9la+3bXsfFRnxkoaZikVVGX\nGi/p3a79CZJWJ7jdvyXVW2uPz7ROa+0qY8wtcl21pMQDt1fJBRCvjh2i6vi3pFStHbMkTZN0nzHm\nq9ZaBoYDQIHQYgEA5eGLkjok7Sk3LmGfrv3n5VoyPNONMZ8zxlRJ+n+SXrTWRoeHS4wxtcaY8ZK+\nL+n+BPf6q6SJxpizjDGVxpi+xpj9E42x6LrWLGPMLsYZIded6cWuU9ZKGm6MGRz1sfsl/cQYM6Lr\n/J9KmtP13h2SzjHGHNl1vbHGmIlRn22X65I1QNIcY4zp4XsDAASEYAEA5WGGpDuttaustZ94P5Ju\nlnSmMcb7//1cuX/V3yBpX0lnxV3nYUmvSnpNbprYO+NvZK1tkHSc3KDt1V0/18q1kMRrk5sV6ilJ\nWyS9JalF0jld11oi12VrWVe3qtGSfi7pla5z3+za/0XX+Qu7Pntj1/Xq5Vo0pK7WD2tth6QvyU1t\nyzgLACgQ01MrsTHmDrmBemuttVO6jg2V9Ae5/5l/JOk0a+2WrveukPvXqA5J37fWzstb9QCAtBlj\n7pL0b2vtVUne75S0q7V2WWErAwCUg3RaLO6SFN+P9nJJ8621u0t6RtIVkltdVa6P755yUwjeSjM0\nAAAAUP56DBbW2uclbYo7fLLcPOLq2p7StX+SpPu7FkD6SNJSufnHAQDh62kgMwOdAQBZy3ZWqJHW\n2rWSZK1dE7Xg0Tj5A/IkN7PHuPgPAwAKz1rbbbG7uPf7FKoWAED5CWrwNv/KBQAAAPRi2bZYrDXG\njLLWru2aweOTruOrFDVHuqTtFTs/+qeMMYQRAAAAoARZa7uNo063xcJ0/XgekXR21/5MuekJveNf\nM8ZUGWN2krSrpJdTFFRyPz/72c9Cr6E3/PA98z2X0w/fM99xufzwPfM9l9MP33P2P8n02GJhjJkr\nqU5uAaMVkn4mN1/5H40x50paLjcTlKy1i40xD0haLLdI0fk21d0BAAAAlIUeg4W19owkbx2T5Pxr\nJF2TS1EAAAAASgsrb2eorq4u7BJ6Bb7nwuB7Lgy+5/zjOy4MvufC4HsuDL7n4PW48nbebmwMvaQA\nAACAEmOMkc1h8DYAAAAAJEWwAAAAAJAzggUAAACAnBEsAAAAAOSMYAEAAAAgZwQLAAAAADkjWAAA\nAADIGcECAAAAQM4IFgAAAAByRrAAAAAAkDOCBQAAAFAE/vlP6dBDw64iewQLAAAAoAg8/LC0YEHY\nVaT29NPJ3yNYAAAAAEUgEgm7gp4dc0zy9wgWAAAAQBGorg67gtwQLAAAAIAiUOzBoqcWFYIFAAAA\nUARqasKuILXW1tTvEywAAACAIlBZ6bYdHeHWkUxLi1Rbm/x9ggUAAABQBLyuRo2N4daRTGtr6u5a\nBAsAAACgCHgtFcU6O1Rra+ruWpWFKwUAAABAMl6w6OwMt45E5s7tucWCYAEAAAAUgWIOFmee6bZT\npiQ/h65QAAAAQBEo5mDhYYwFAAAAUOQIFgAAAABy9tJLbvvUU+HWkUqqwdsECwAAAKAIPPus2z73\nXLh1pEKLBQAAAFDEors/Fet0sxItFgAAAEBRe/VVf58xFgAAAACycuCB/n4xBwtaLAAAAIASUczB\nghYLAAAAoETcd1/YFSRHsAAAAACQM7pCAQAAAMgZLRYAAAAAckaLBQAAAFCkNm0Ku4L00WIBAAAA\nFKlVq8KuILXoWaoqK5OfR7AAAAAAQmRt2BWk9uCD/v7SpcnPI1gAAAAAIfJaBAYMCLeOZH7/e38/\nEkl+HsECAAAACJH3sN7QIJ10Uri1JGKMvz9oUPLzUvSSAgAAAJBv0WMYvvtdqbU1vFoSqapy29df\nl3bfXfrVrxKfR7AAAAAAQuQ9uEtSRUVs0CgG3kxQU6emPo+uUAAAAEDI9t7bbYsxWEyaJO24Y8/n\nESwAAACAEEUi/jSuFRWpB0iHob1dOuusns8jWAAAAAAh6uiQ+vRx+1VV0vLl0ubN4dYUrbU19cJ4\nHoIFAAAAEKLoFouqKulf/5JOOSXcmqK1tREsAAAAgKIX32IhSatXh1dPPFosAAAAgBIQ32LhHSsW\nBAsAAACgBCRqsSBYAAAAAMhIohaL6NWuw0awAAAAAEpAohaLlpbw6onX2hq7iF8yBAsAAAAgRIla\nLLZsCa+eeG1tBAsAAACg6CVqsfCCRjHo6JD69u35PIIFAAAAEKL2dj9IeA/wxTTGIhLxg08qBAsA\nAAAgj6yVtm1L/n5TkzRggNv3Bklv3Zr/utIV3aKSCsECAAAAyKObb5YGD07+fkODNGhQ4erJFC0W\nAAAAQBF4+unU7zc0SAMHFqaWbGzaJNXW9nwewQIAAADIo566NTU2+l2hitGWLQQLAAAAIHTWpn4/\neoxFMdq6NXVXLg/BAgAAAMijzs7U7zc1Sf37F6aWTHkDz9MZA0KwAAAAAPIonRaLfv3818OG5bee\nTDQ1STU16a2rQbAAAAAA8iidYFGsLRbPP59+N60iWtMPAAAAKD+ZBouezi+kadPSP5cWCwAAACCP\nehpj8fjj6a0TUewIFgAAAEAepdMCET0lbTG1WGSCYAEAAADkUaoWi7Y2t919d//Y5s35rSdfCBYA\nAABAHr38cvL3GhulIUOkffYpXD3peuaZzM4nWAAAAAB5Eomkfr+YV91+/fXMzidYAAAAAHnS3p78\nvQ8/lH74Q6m6OvZ4dLeoMDU3Z3Y+080CAAAAeeKNoUhk111jt550FqMrhL32ctv4+pKhxQIAAADI\nk1TBwvPBB7Gv//CH/NSSqepqaYcdpKefTu98ggUAAACQJ9HBwpj0PuO1FIQ97WwkIk2eLE2YkN75\nBAsAAAAgT9JpsYhnjFswr6eF9fItEsmsWxbBAgAAAMiTpUuz+1xlZeqB34XQ0ZHZiuAECwAAACBP\njjuu53O+/OXuxwYOlBoagq8nE5EIwQIAAAAoGYsXdz82eLC0ZUvha4lGVygAAACgyEUPzE7UMjFk\nSPjBgq5QAAAAQJGLHj+RaIB3377Shg2FqycRukIBAAAARa6ngdkLF0pnnVWYWpIhWAAAAABFrrVV\nqq1N/v6YMdKMGYWrJxHGWAAAAABFYupUacSI7sdbW93K1lLihfBOPlnacUfpyivDWyiPMRYAAABA\nkZg8Wbr++u7H29qkqiq3n6hVwBjpo4+ka66RXnwxryUm1dkpVWSQFnIKFsaYHxhj3jHGvGWMudcY\nU2WMGWqMmWeMWWKMedIYMySXewAAAAClqr3dDcSOF91i4QWMaBUVfkvFxx/nr75UrHUBJ11ZBwtj\nzFhJ35O0n7V2iqRKSadLulzSfGvt7pKekXRFtvcAAAAAStmHHyYOFm1tqYNF9AP97bfnpzZJWrIk\n+XsFCxZd+kgaYIyplNRP0ipJJ0u6u+v9uyWdkuM9AAAAgJK0cKG0YIH/2muFaG31A0Wi4GGMGzwt\nSYcfnr/69tgj+QrfmQaLDMZ5x9/IrjbG3CBphaQmSfOstfONMaOstWu7zlljjBmZ7T0AAACAUhf9\n4N7e7gLF/vtL22/vjiVqsZg3z29NSDV7VLbWr5e2287tt7RIAwd2P6eQXaFq5VondpA0Vq7l4kxJ\n8ePWQxrHDgAAAIRv3Dh/P3r9itWr3TZRsIjuopTJzEzpeuwxf7+pKfE5BWuxkHSMpGXW2o2SZIz5\ns6TPSVrrtVoYY0ZL+iTZBWbNmvXpfl1dnerq6nIoBwAAACgu/fpJX/+6dPXV7nVHh/9e//6uNaOn\ntSK8LlFB2rjR329sTHyOFyzq6+tVX1/f4zVzCRYrJB1sjKmR1CrpaEkLJTVIOlvSryTNlPRwsgtE\nBwsAAACg3Gy3XWxwiG6xSDa2IV5nZ7A1SdKkSf5+T8EivgFg9uzZCc/PuiuUtfZlSQ9Kel3Sm5KM\npNvkAsWxxpglcmHj2mzvAQAAAJSy+O5E7e3Ss8/GntNTd6N8tFhE3/PllxOfU9BZoay1s621e1pr\np1hrZ1pr2621G621x1hrd7fWHmet3ZzLPQAAAIBSZW3sInOrVklHHZX5NYIWXdMFFyS/byGnmwUA\nAACQRGenezgf2TVPaqJ1IxI9vD/xRH4GbXvip7iNHvvhIVgAAAAARcJrsfAe0Fta0vtcnz5+F6h8\ntFisXx/7epddup9TyFmhAAAAAKTgtVh4D+jxU7t+61vSkUd2/1z0A30+gsWXvxz7esWK7ucQLAAA\nAIAi4T2ce2tVxM8EddttiT+XyQN9vtAVCgAAACgSXleoiRPd69/8Jr3PRQ+uzkeLRToIFgAAAECR\n8LpCeYOl161L73P57gp17LHdj61aFfuaYAEAAAAUCe/hvCLuqfvOO6VXX03+uXx3hTr4YKm2NvbY\n1KnSuedKzc3SypUECwAAAKBoeF2h4oPF6NHSfvsl/1y+Wywike7T2a5fL911l3T55dL48QQLAAAA\noGh4XaHig0X8IO54hQgW8TVJ0gEH+N21Vq0iWAAAAABFIX4dC8/Chak/l+ihP0iRSOK1K2pq/Fpf\neIFgAQAAABSFZC0WP/5x6s8VosXi1FOlGTO6vxddK8ECAAAAKALeOIVTT5UGDXLHvv51aciQ1J/z\nHuiNye8Yi/jgED2ugjEWAAAAQJHwukKdfrrrWiRJxx/f8+e8B/r4AdZB8YLFNdfEHl+xQpozx783\nwQIAAAAoAl5XKMlffTudsOB9pqIivy0WY8bEHl+xwt+nxQIAAAAoEtEP59XVbptOsPDGOXjBYsuW\nYANGoulm4zU3EywAAACAouB1hZKyb7Ho7HSL2f35z8HV1dHRcx0ffig98kj61yRYAAAAAHkSvV6E\nFywqK3v+3Jo1btvUJP3kJ25/9epg60on4Lz8cvrXJFgAAAAAedDW5loe+vZ1rzNpsdiyJX91SS5Y\neAHnwQelyZNzvybBAgAAAMiDxkZpwAD/dSZjLPr1634sX2MsvvzlYK5NsAAAAADyID5YeC0X6ayq\nnehBP4iH/+nTpZtvll59NTbgtLfnfu00engBAAAAyNQPfhA7LiJ64bmeJDonnUDSkyeecD9S8mAx\nerQ/xuPGG9O/Ni0WAAAAQB48+GDi4+kEhM7O7D6XiWTBYulSF4okaebM9K9HsAAAAAAKKJ2AMHVq\n92OZrCmRjmTBoqJCGjjQ7aczg9WnnwumLAAAAADpSCdYTJyY3ecy4YUHya1r4enTx3WHkggWAAAA\nQNHKtuUh6BaL6NAQHSwk6eyz3dabySqt6+VcEQAAAIC0ZdvyEHSLhdcqIfnB4qGH3HobxrhZrTIJ\nMwQLAAAAoICybXkIOljsuKO/H4m47Ze+5B/r3z+z69EVCgAAACigTALCZz/r7xeyK1Q2CBYAAABA\nAWUSLCZNyu5zmdbhtVjkdL3cLwEAAAAgXZm0PAwe7O8vWhRcDbffHvs60boZmSJYAAAAAHkwdqx0\n002xx+65R9pvv/Q+v2CB9JOf+K9//evcaxoyRLr4Yumkk7q/F72uRTaMTWdN8Twwxtiw7g0AAADk\n25Qp0pw50j77ZH+Njg6pb1//da6Pz/36SRs3um00Y9zUsi0tPV/DGCNrbbd2F1osAAAAgDxob89s\ngblEgh5X0dbmppNNJNcWC4IFAAAAkAebNknDhuV2jSBngurocNdLFiByDkG5fRwAAABAvM5OacMG\nacSI3K6Ta7Cor3cBR5JaW5O3VkgECwAAAKDoNDW5h/jo8RFhOPJI6dvflt54wwWLmprk59IVCgAA\nACgyzc2pH+KzscMO0vr1mX/uwQelffd1waK6Ovl5tFgAAAAARaalpfvMS7lavtwFhGy1tKQOFqNG\nZX9tScoxlwAAAACI19wcfLCQpNWrs/9sqhaLq66SDj88+2tLBAsAAAAgcPkKFrlMP5sqWMyenf11\nPXSFAgAAAAIW5BiLN9+U/vM/3X4mA6zjF9PrqStUrggWAAAAQMCCHGMxZYp04oluP5MWi/hVtLdu\nlQYPDqamRAgWAAAAQMBuvllavDi463ktFc3N6X8mvsVi0yZp6NDgaorHGAsAAAAgYA89FOz1sllj\norPT3x84MP/BghYLAAAAoMhlM2g7usVi+HBpyxaptja4muIRLAAAAIAi57VYVFWl/5noFovly6Xn\nngt+0b5oBAsAAACgyHnB4uyz0/9M/BiLxx7LLJhkimABAAAAFDkvWGTS4hDdYuF5881g6kmEYAEA\nAAAUuWwHb9fWSocd5h8LelB5NIIFAAAAUOSyCRbWSpWV0sUX+8f69g2upngECwAAACAPrr8+uGt5\nwcKY9D/T2enOj55RasSI4GqKR7AAAAAAAjZxor9adhCyCRbWulARHSz23Te4muIRLAAAAICAtbYG\nOwNTtmMsjIn97C9/GVxN8QgWAAAAQMA6Otz4hqB4rQ65tljss09wNcUjWAAAAAABi0Sya2VIJpuV\ntzs73eeCrCMVggUAAAAQsKCDhTHSRRdlFjDiB2/fcUdw9SRCsAAAAAACFnSwkKTx46X586X/+I/0\nzo/vCrXTTsHWE49gAQAAAAQs6DEWkmt9ePNN6aab0js/fvB2PtewkAgWAAAAQODy0WKRycBtqXuL\nRdBBJx7BAgAAAAhYMQSL+BYLggUAAABQYvIRLDLV2urPDCXlvytUnnMLAAAA0PsUQ4vF5MluS1co\nAAAAoARZ61oKwg4WHrpCAQAAACXIG9uQbRAImtcFimABAAAAlJCOjvyMZ8g2qHi1MN0sAAAAUELy\nsYaFlHuwoMUCAAAAKCH5Chbx6uulbdvc/S64IPl5BAsAAACgBBWqxeLII6U5c6T166Vbb03+OYIF\nAAAAUII6OvKzhkWirlCDBkmffJL6c4yxAAAAAEpQIbpCffCB21rrukR59402YIB09920WAAAAAAl\nqRBdoZqb/f0pU9x2wYLY8wcPlo45hmABAAAAlKSmJql//+Cv29np7zc0uK0xfmB47bXY81tapJoa\nP1jko3tWNIIFAAAAEKCNG6Vhw4K/7ksv+fsPPeS21kptbW7/hz+U7rnHP6e5WerXT6qokNascdt8\nIlgAAAAAAdq4URo6NPjrDhjg73utFNHBQpJmzvSPt7a6FgtJGjUq+HriESwAAACAALW0uJaCoEV3\nZWpt9fejg8WgQX4N1dXZL6qXjQIs3QEAAAD0HtdfL738cvDXbW/392+80W0jkdjjtbVu63WDKiRa\nLAAAAIAA5SNUSLEBwhOJxLZYeC0Uzc1+N6hCocUCAAAACNCFF0q77Rb8dePXqZC6BwtvP1/dsVKh\nxQIAAAAIUGNj7EDroCRqsejsjA0Wa9a4bRhdoWixAAAAAALU1FS4YBGJSMuWdT/+yCPSokXB15AK\nLRYAAABAgBob87NAXqJg0d4u3XBD9+Nz5wZ//54QLAAAAIAA/fWv/srYQfKCxRFH+Meip531pqNt\nbpZ+9CNp+PDga0glp2BhjBlijPmjMeZdY8wiY8xBxpihxph5xpglxpgnjTFDgioWAAAAKAXvvBP8\nNb1gceGF/rHoYLHddi5MNDZKAwdKdXXB15BKri0WN0l63Fq7p6R9JL0n6XJJ8621u0t6RtIVOd4D\nAAAAKClnnhn8Nevq3GxT3loVkgsW3/mO21+zxnXBampyK29XFLhvUta3M8YMlnSYtfYuSbLWdlhr\nt0g6WdLdXafdLemUnKsEAAAASsSECfkZvP3Tn0rvvx8bGK69Vpo3z3+9erW0fLm0cmXsbFGFkMus\nUDtJWm+MuUuuteIVSf8haZS1dq0kWWvXGGNG5l4mAAAAUBqs9Reqy4f4lghvVqiDD5Zeekk68URp\n69b83T+ZXIJFpaT9JF1grX3FGPMbuW5QNu68+NefmjVr1qf7dXV1qit0RzAAAAAgYIUOFh5v8PaR\nR0oPPxzc/err61VfX9/jecbapM/9qT9ozChJL1prd+56fahcsNhFUp21dq0xZrSkZ7vGYMR/3mZ7\nbwAAAKBYbb+99OKL0vjx+bn+ggXSoYfGHjv7bOmKK6T773fjLn75S3c8H4/bxhhZa7tFp6zHWHR1\nd/q3MWZi16GjJS2S9Iiks7uOzZQUYF4CAAAAilu+Wyz69u1+bNo0aeJEqbJSeuut/N07lVxX3r5I\n0r3GmL6Slkk6R1IfSQ8YY86VtFzSaTneAwAAACgZ+Q4W1dVuO3269Pjjbr+y0t8WejYoT07Bwlr7\npqQDErx1TC7XBQAAAEpVoVosvv99P1h44ysqK910s2Fg5W0AAAAgQPkOFl7rxKRJ3Y9VVkrvvZe/\ne6dCsAAAAAAC8sQT0tq1hWmxGDjQPxYdLFauzN+9UyFYAAAAAAHxFqvL5+SnXrAYMsQ/Ft0VynPe\nefmrIRGCBQAAABAQb7XrSCR/9xg2rPux6BYLz//8T/5qSIRgAQAAAARk0SK3zWew6N/fbxGZM8dt\nEwWLQiNYAAAAABlqaZH23Vfq6PCPRSLS3//u7xeCN7VsfFeoG24ozP1jain8LQEAAIDS9uST0htv\nSBs3+seip3nt7CxMHV6w8AJFVZXb7rZbYe4fU0vhbwkAAACUtpEj3Ta661F7u7+/886FqSM+WNTU\ndK+rUAgWAAAAQIa8MQ7RXZ7a2lzgsLZwq1/Hd4UiWAAAAAAlxBtbEd3lqa3N74pUKPEtFtXVsduC\n1lL4WwIAAAClq6Eh8bSy7e3hBYv4FotC1yFJIU5IBQAAAJSeQYPcjFBSbItFS0vhWwriAwUtFgAA\nAEAJeestt41usdiyRRo8uLB1eC0WXrAIs8WCYAEAAABkyBi3jW6x2LJFqq0tbB1esOjXz21psQAA\nAABKUHyLxZAhhb0/LRYAAABAGfj61/3Vtk8/XfrTnwp7f2/aWy9IeC0VBAsAAACgBHjTzb70knTj\njd2PF4q3KJ/XNSt+EHchESwAAACAFFau9B/cE/Gmng1Da2vsa6+lom/fwtdCsAAAAABSWLUq9fub\nN/v7he4KFR9qKiqk3XbzWy4KiXUsAAAAgBRStVZI/qrXEyZIU6fmv55oiVpL3n+/sDV4aLEAAAAA\ncvDFL7ptGLNChdkNKx7BAgAAAEjBG8fwwguJ36+sdLMzbdtW+AXyotfRCBvBAgAAAEihsdFt//a3\nxO9HIm52pj59/G5RhXL22VJ9fWHvmQxjLAAAAIAUtm512z59Er/f0RHO9K6SG6R9xBHh3DsewQIA\nAABIobnZbeODxYAB0qmnurEVIFgAAAAAKXljLIYNk775Tf/4eee5lorVq8Opq9gQLAAAAIAUvJmX\nhg2T7rjDP15ZKb34YvGMcQgbg7cBAACAFLwWi02bYo/36SO9/nrh6ylWBAsAAAAgBa/FYv362OOV\nleEN2i5GBAsAAAAgBS9YXH117HFj3ABuOAQLAAAAIAWvK1RHR+zxSESqrS18PcWKYAEAAACk4LVY\nxItEpKFDC1tLMSNYAAAAACl4LRbxGhqkE08sbC3FjGABAAAApJCsxeLmm6Wvf93tf+1rLJRHsAAA\nAABSaGuTKqKemi+5xN+vqnLbhx+WBg8ubF3FhmABAAAApNDaKnV2+q8nTvT3a2rctqWlsDUVI4IF\nAAAAkEJ8V6hzz/X3vRYLawtXT7EiWAAAAAApRA/erq31u0Uddlg49RSryrALAAAAAIpZdIuFMW57\n6qnStGnh1FOsCBYAAABAColmhfrjH2Nf779/YWopZnSFAgAAAFKI7grltVjEq+CpmmABAAAApJJs\nHYtoyQJHb0JXKAAAAPRaxkgbN0pDhyY/p7VVGjjQrbSdyC9+IU2dmp/6SomxIc2NZYyxYd0bAAAA\nkFyw+OADaZddkp+z++5SZaW0eLE0bJi0YUPh6itGxhhZa7u10dAVCgAAAL1Se7vb7rqra7VI5OWX\npfffl/r1kpp8AAAgAElEQVT1c6/p8pQcwQIAAAC90ve/7+9v2pT4nLfectv+/fNfT6kjWAAAAKBX\n+u//9ve3bUt8jhcovBaLkSPzW1MpI1gAAACgV6qMmsbok08Sn+MFi5oat/3HP/JbUykjWAAAAKBX\nuvRSf//449125kzpvfe6n3vggW47fHj+6ypVBAsAAAD0SpFI7OvLL5fuuSe2VaKlRfrKV6Qrr4xd\nKA/dESwAAADQKzU1xb7+1a/c9tvf9tes2LpVGjzYzQZVVVXY+koNwQIAAAC9jjHd16OIHnNxzTXS\nu++6YDFkSGFrK1UECwAAAPQqXheoNWtij3d0+Pu//KW0117Sli0Ei3QRLAAAANCrNDa67TPP9Hwu\nwSJ9BAsAAAD0Kt74iUSGDZNOOMHtV1T4YyzQM4IFAAAAepVHHkn+XmVl7Crbra3+GhZIjWABAACA\nXmXnnZO/V1kpPfSQ/7qjQ+rTJ/81lQOCBQAAAHqVbdv8/UGDYsdQxK9tEYkQLNJFsAAAAECvEj3G\nYt066YEH/Ndr1/r7nZ0uWERPQ4vkCBYAAADoVaJbLKqr3U8ybW0Ei3QRLAAAANCreMGioutJOL77\nkxc0hg1jgbxMECwAAADQq3jBwmuJaG2NfX/xYrfduFF64QVp6NDC1VbKCBYAAADoVbxg4Q3KbmmJ\nfX/nnaWPP/Zf19YWpq5SR7AAAABAr+IN3vZaLI49Vnr0Uenzn/fPGT7c36fFIj0ECwAAAPQq8S0W\nAwdKJ54oTZ7sr7Ldt69/fr9+ha2vVBlrbTg3NsaGdW8AAAD0TsuXSzvuKF11lfSlL0n77OO/Z62b\nYtYLHMb4x+Ezxshaa+KP02IBAACAXuOoo9x28uTYUCG5IBG9GN6BBxaurnJAsAAAAECvMXas244c\n2fO5rLidGYIFAAAAeoU//EF6/nnXEnH44T2fb7p19kEqBAsAAACULWul5mbp1lulr33NHXv88fQ+\nW1WVv7rKEcECAAAAZeuyy6T+/aULLvCPRU8lm8qAAfmpqVwRLAAAAFC2/vrX2NfpdIHyECwyQ7AA\nAABA2dq0Kfb1pEnpf/baa6UHHwy2nnJWGXYBAAAAQL7Er0FRU5P+Z3fayf0gPbRYAAAAoGw1NcW+\n3nXXcOroDVh5GwAAAGUrfsrYzk6mkc0VK28DAACg19l//9jXhIr8IVgAAACgbE2ZEnYFvQfBAgAA\nAGWrIuppd+zY8OroDQgWAAAAKFudnf5+e3t4dfQGBAsAAACUrbY2f7+jI7w6eoOc17EwxlRIekXS\nSmvtScaYoZL+IGkHSR9JOs1auyXX+wAAAACZamyUfvQjqU8f1qTItyAWyPu+pMWSBne9vlzSfGvt\ndcaYyyRd0XUMAAAAKKjGRumYY6Rp08KupPzl1BXKGLO9pOmSbo86fLKku7v275Z0Si73AAAAALLV\n1CT17x92Fb1DrmMsfiPpEknRK92NstaulSRr7RpJI3O8BwAAAJCV9eul2tqwq+gdsg4WxpjPS1pr\nrX1DUqqlRlheGwAAAAXX0CC9/760xx5hV9I75DLG4hBJJxljpkvqJ2mQMWaOpDXGmFHW2rXGmNGS\nPkl2gVmzZn26X1dXp7q6uhzKAQAAAHyDBrltVVW4dZS6+vp61dfX93iesTb3BgVjzBGSftQ1K9R1\nkjZYa3/VNXh7qLW22+BtY4wN4t4AAABAIqarTw2PnMEyxsha263HUj7WsbhW0rHGmCWSju56DQAA\nAKCMBdJikdWNabEAAABAHtFikR+FbLEAAAAAQtXeHnYFvQ/BAgAAAGWnqSnsCnofggUAAADKDsGi\n8AgWAAAAKDuNjWFX0PsQLAAAAFB2aLEoPIIFAAAAys7q1VL//tIHH4RdSe/BdLMAAAAoO/vtJ73+\nOlPN5gPTzQIAAKAsGSPdeWfssfPPl/bfP5x6eiuCBQAAAEreN74R+7qyUpo0KZxaeiuCBQAAAErK\n009LxxyT+pz2dhcuUDgECwAAAJSUhQtduIgeP7HPPrHnNDZKAwYUtq7ejmABAACAkuIFhuXL/WNv\nvhl7zoYN0vDhhasJBAsAAACUmD593PaWW5Kfs3GjNGxYYeqBQ7AAAABASfHGTixdKv3Xf7n9z3xG\n+stfpDlz3GtaLAqPIS0AAAAoKV6LxQsvSA8/7PatlWbOlLZulb74Renjj6XRo8OrsTeixQIAAAAl\npaLrCXbdOv9YJOJChSRdeqnbr60tfG29GcECAAAAJaWzs/ux6MHb220nvfGG1K9f4WoCwQIAAAAl\nJhJJ/X5Dg9sOHJj/WuAjWAAAAKCk9BQs2tpcN6jtty9MPXAIFgAAACgpqYLFwQdLra3ShAmFqwcO\nwQIAAAAlJVWw2LxZ+r//86ekReEQLAAAAFBSUgWL995z2759C1MLfAQLAAAAlJT33+/5HFosCo9g\nAQAAgJLyv/+b/L1TT3Xb5ubC1AIfwQIAAABl47rr3HbLlnDr6I0IFgAAACh51krjx0vjxrnXTU3h\n1tMbGWttODc2xoZ1bwAAAJQuY7ofi36s9N7nUTM/jDGy1nb7XaDFAgAAACXj3/+WamqkUaPc64MO\nkjZsCLcmOAQLAAAAlIzrr5daWqTqavd6yBBp2LDu59XUFLYuECwAAABQQnbYQTrhBKmz071ONK3s\nsmXStm2FrQsECwAAAJSQt9+WjjrKHz8xe3b3c3baiXUswsDgbQAAAJQMY6Rzz5U++1lp5Upp1qyw\nK+p9kg3eJlgAAACgZNTUSH//uxu0jXAwKxQAAABK3ujR0ogRYVeBRGixAAAAQElobXUtFh0dUp8+\nYVfTe9FiAQAAgJL27LNuS6goTgQLAAAAlIQ77gi7AqRCVygAAACUBNPV+YZHyHDRFQoAAAAlizBR\n/AgWAAAAKHqtrW47cGC4dSA5ggUAAACKXkODmxFq1aqwK0EyBAsAAAAUvcWLpdpaafDgsCtBMgQL\nAAAAFL1PPpH23TfsKpAKwQIAAABFa+lSt41EGF9R7CrDLgAAAABIJHp62Y4OqZIn16JGiwUAAACK\nTvwg7UiEFbeLHcECAAAARWf77WNfEyyKH8ECAAAARa2jw003yxiL4kawAAAAQNFYssRtDz3UP/br\nX0sffyyNHh1OTUgPwQIAAACh27ZN2rJF2mMP6a9/lYYM8desmDNHWrlSGjcu3BqRGsECAAAAodtz\nT2nXXd3+Kae47k933OFeV1e7wdxjx4ZXH3pGsAAAAEDo1qyR1q93+5GI+6mtda/feEN65hnXioHi\nRbAAAABA6MaMiX3d0iJVVcUe69+/cPUgcwQLAACAMnf99dLuu4ddRWoVcU+lmzf7LRae+KCB4kKw\nAAAAKHOXXCK9/37YVaTmrVExc6bbvvOONGJE4nNQnAgWAAAAZa6uLuwKeua1WEQvjBcfLJhutrgR\nLAAAAMrYwoXSRx+5/Ugk1FJSShQsqqqkYcPc/gsvSIMGFb4upK8y7AIAAACQP3V1UlOT2+/oKN7u\nRF6w8Nau8Gzc6LZ7713YepA5ggUAAEAZOucct+6DFyokqbMzvHpSaW/3V9yODxZnnCHNnUtrRSkw\n1tpwbmyMDeveAAAA5c4Y15Worc0/1tAgDRiQ/Py//c0tUrfLLoWpMfrenmeflY48UrrwQum//quw\ndSA9xhhZa038ccZYAAAAlKnoUCFJyf5N1zs+bZq/+nUhHXywvz9ggHT44dLJJxe+DuSGYAEAAFBm\n1qzx9ydO9PeTdYV69NH81tOTxkbpi190LSoHHCD9/e/SMceEWxMyR7AAAAAoMzNmuO2pp0pbt/rH\nkwWLMFsHxoyR3n5bmj49eTctlAaCBQAAQJl5/nm3bWyMbb0oxsHbXn3etLIoXQQLAACAMnPuuW7b\n2Oi2558vDRmSfIzF1Kmxr7dty19t8UaOLNy9kF8ECwAAgDLjjauoqnLbGTNcl6iGhsTn77df7OvB\ng11LgrXS+vX5q1PyQ80+++T3Psg/ggUAAECZ8bo8tbS47aBBLiTsuGPi8xMFjj33lO67T9puu7yU\n+KmWFqm+vvBT3CJ4BAsAAIAy09np1oZoapI+8xlpr71Sn9/Q0L1L0ubN0gcfuP3ly/NTp+SCRXV1\n/q6PwiFYAAAAlJlIxHWDamrqvpJ1Io2N0pw5fpDweAvXXXFF8DV6CBblg2ABAABQZubMkVpbpebm\n9B7aGxrcrEzxrRa1tW57333B1yi5lpVly9ILPyh+BAsAAIAy8/bbbrt+vTRwYM/nb9vmzvMGe3vW\nrQu+tmhXXulCzYQJ+b0PCoNgAQAAUKYaG6XJk91+slYBa6VVq9xCddXV0mOP+e+tXi0ddJB0yin5\nqW/+fLft2zc/10dhESwAAADKSGenVFnpT+P64Ydu++ij0qGHdj9/61YXQIYMca+9xfUkN4B75Mjk\n09Tm4pvflF59NXFNKE0ECwAAgDLyu99JHR3SuHHutbc+RJ8+iVfenjUr9vW3v+3vb9vmpoGdPz/5\n4nrZaGyU7rjD7Xd0BHddhItgAQAAUEa87kV77um2/fq5bUWFmy0q3tKlsa933NEfWzFvnrTbbm6/\ntTW4Gg86yN/v0ye46yJcBAsAAIAy4i2K53Vt8gJBnz6Jg8Xmzd2PjRjh7w8f7hbYCzJYLFrk7996\na3DXRbgIFgAAAGXECw/eNLPnn++2ybpCbdmS+npVVVJNjR9YgjB9uttOmeJ+UB4qwy4AAAAAwTn4\nYGntWn+mJW8K2fXrpdde635+ohaLaFVVLqQE2WLhreTNwnjlhRYLAACAMrJsmVRX52aGiuZ1b2pv\njz1+/PGpr1dV5bpVbdoUTH3r17uuUMZIhx0WzDVRHAgWAAAAZeT226Vf/ar72hCf+YwLF/EBYcwY\n6eqru1/nC19w2+pqN6Dba2XIlbcgXmendMMNwVwTxYFgAQAAUGZ22inxonPDhkkbNvivN26Ufv7z\n7ituS9KkSW4bibjB242NwdTW3OzPVIXyQrAAAAAoE95aE088kTgs9O8vNTX5r+vr3TbRoO7ttnPb\nhoZgB28TLMpX1sHCGLO9MeYZY8wiY8zbxpiLuo4PNcbMM8YsMcY8aYwZEly5AAAASKa52W3HjZNO\nOEH68Y9j34+fGcpbUTvRInUXXeS248e7tTEefDCYGh94QHrjjWCuheKSy6xQHZJ+aK19wxgzUNKr\nxph5ks6RNN9ae50x5jJJV0i6PIBaAQAAkEJDg2tpGDjQ/fz857Hvx69l4bVeJGrdqKz0W0BWrnQ/\nQfjzn4O5DopP1sHCWrtG0pqu/QZjzLuStpd0sqQjuk67W1K9CBYAAAB519DgAkUy8cHCmyGqooc+\nLNdd56awDcJJJ0mjRgVzLRSXQMZYGGN2lDRV0kuSRllr10qfho+RQdwDAAAAqW3bllmw8LpO9e+f\n+rrV1VJbW+71SW6sRk1NMNdCcck5WHR1g3pQ0vettQ2SbNwp8a8BAAAQkNtu8wPCxo1u5qdkknWF\nOvXU1PeoqgouWDQ3EyzKVU4rbxtjKuVCxRxr7cNdh9caY0ZZa9caY0ZL+iTZ52fNmvXpfl1dnerq\n6nIpBwAAoFexVjrvPLcuxGc+I738sjR8ePLz44PF7Nnu8z11Tco1WDQ3S+efL915Jy0Wpai+vl71\n3hRiKeQULCTdKWmxtfamqGOPSDpb0q8kzZT0cILPSYoNFgAAAMjMc8+57dat0oknumAxc2by8+OD\nhZReYMg1WKxYIf3ud9Kee0r33uvGWaB0xDcAzJ49O+F5WQcLY8whks6U9LYx5nW5Lk9XygWKB4wx\n50paLum0bO8BAACA5LzF7laulFatcvvxK2tHiw4W3oxPBx7Y832qqvwQk0udl13mttXV2V8LxSuX\nWaEWSOqT5O1jsr0uAAAA0uOtht3S4q9J8cgjyc+PDhatrW47ZUrP9+nTR/r3v90aGD3NIJXI+vWx\nrydOzPwaKH6svA0AAFCizj7b3/dCxlVXJT8/Olhs2+bGY3zucz3fxwsTXhjJVHywGDo0u+uguBEs\nAAAAStShh7rt3Ln+6tnnnpv8/PhgMWhQevcJOljU1mZ3HRS3XAdvAwAAICTeA/+iRf6x0aOTn//0\n027la2szCxZ9ujq/ZxssvDEWHmaFKk+0WAAAAJSgzk7pH//ofjzVwOitW/395cvdoO90eMGipSX9\n+jyLFrkQc/PN7rW32jfKD8ECAACgBL3wQvepYzNxxhmpZ5CK5rWMzJ2b2T3a2qS993bTzQ4a5FpK\nKukvU7YIFgAAACWoXz+3jZ4G9tprU39mzBi3/Z//8Qd7p8MLFr/9bfqfkfyxFR98IA0enNlnUXoI\nFgAAACWorU2aNEk65BD/2C67pP7MU0+57Xe/67b9+6d3r2wHb3vBYsmS9MdzoHQRLAAAAEpQa6ub\nLjZ6XYkBA1J/ZtKk2NdNTenda+pUt800HETPBkWLRfmjlxsAAECJWbzYdUuKH6g9bVpm1/nOd9I7\nb/hwafp06fDDM7v+0Uf7+7RYlD+CBQAAQInxWh6mT489bkxm1zn//PTP3WuvzK7vravhGTgw/c+i\nNNEVCgAAoIREP7A//ri/X5HFU503jWw6Kiu7h4VU3nsv9jVdocofwQIAAKCEXHxx4uO77Zbe5ydP\n9vfTHWMhxa7anY4PPoh9TbAof3SFAgAAKCHRi+I9/bS/n+76EG+95XdpmjAh/ftmGiy++EW3veKK\n7FpTUHoIFgAAACXkrLOk116T6uqko47yj3vrWqSjvd0FhUzGTFRWuiluM/XLX2b+GZQmggUAAEAJ\n6d9fOvts6bbb/GNLlmTW1Sib1a/79MlsjIUkffWrmd8HpYuGKQAAgBJy333SkCFS377+sYkTpdGj\n83vf9eulZ55J71xr3faKK/JXD4qPsd7vfKFvbIwN694AAAClyhg3TewttxT+vpIfGlJpb5dqajIb\nk4HSYYyRtbZbRzpaLAAAAEpES4vbjhsXXg0HHNDz2IyGhsLUguJCsAAAACgR//mfbvujH4VXwyuv\n9HzOCSdInZ35rwXFha5QAAAAJSKT7kj5urcnVQ1h1on8S9YVilmhAAAASsSxx0oHHRR2FUBidIUC\nAAAoEevWSaecEs69Z80K574oHQQLAACAErFqVXgDt6dPT/3+2rXSDTe4/YMOkh5/PP81obgQLAAA\nAEpAa6u0ebM0cmQ490+0qF70AO177pEuvtjt//Of0vbbF6YuFA+CBQAAQAn43/9160NUhPT0Fr0g\nnyQ1NbnVuD3eVLjWugX8CBa9D8ECAACgiHzwgdTY2P14e3vP3ZEKaf16t331Vbddt85tN25061gM\nHBhOXQgPwQIAAKCI7LabdOaZ/uuVK6UFC1wLwb77hlfXqFGxr884w22fecZta2rcdu5ct+J2fAsH\nyh/TzQIAABQJb90HrzVAkk46SXr9dWm77aRLLgmnLsndP9qCBW576aUuVNTXu9fPP1/QslBECBYA\nAABFwhsMfcgh/rHXX3fbdeuk8eMLX1M6LrrI349E/NYM9C50hQIAAAiZMdIuu7hxFJK0ZYv/3rHH\nSmPGuP0JEwpfW6YeesiNsUDvQ7AAAAAoAsuWuXEUkptWduVK6corpaeekq66yh3fddfw6vNcdlnP\n5zzySP7rQPEhWAAAAISoo8PfP/ZYt928WbrzTumaa9zr885z4y/CWsMi2lFHJV7TYq+9pEmTCl8P\nigfBAgAAIEPWJp4SNhuffOI/qL/2mts++aT06KNuf++9XVepYmCtdNxxbjE8KXagdkuLdNppbn/E\niMLXhvARLAAAADK0YIFbpyF65elsnXNObKuF55VX3Pbaa3O/R9CqqtzWG/shSW1tfpet5ubC14Tw\nESwAAAAytHWr2wYxSHnePLf95z/9Y5df7u+fcELu9wiaN8h8552lVavcfmur2/bvzxoWvRXTzQIA\nAGTI+xf55mZp8ODsrzNsmNsuXOgvQPfkk26sxVlnFe+YhbY2f3/sWLf1vpPFiwtfD4oDwQIAACBD\n0cEiW9ZKmza5/e23l0aPlo44QtpxRzemolhDhSTttFP3Y17rzQ47FLYWFA+6QgEAAGTImxZ248bs\nP79hg//aa62or5cmTsyptII47DB/lXBJGjcuvFpQPAgWAAAAGXr7bbc9++zsPv/Vr7qBz4MHS//4\nR/HM+pStBQvoAgXJ2Oi4WcgbG2PDujcAAEA2Ghqkv/5VOv10/1g2jzPRQYLHIZQaY4ystd3iMGMs\nAAAA0nTWWdLDD8ce6+yUKjLoAzJ/frA1AcWCrlAAAABpig4V553ntr//vbR8udtfuVL6059Sd5Hy\nVte+5x7pvffyUiYQCrpCAQAApMnrwvSNb0g33yz16+de77ij6yK1997+ufGPOevWuRWpKyqkL3xB\neuSRgpQMBI6uUAAAADlYuNBtP/zQLQwX7aOPuneHam+PXShu5Eg3nawk3Xhj3soEQkNXKAAAgDSs\nWOG2Q4cmfv/WW2NfR4+l8Fal/vvf3TY+mADlgGABAACQhnnzXBeoZMHi5pv9/ZNPltav9197oUSS\npk3LT31A2AgWAAAAabjtNmnQoNhj3/iGNHZs7LFf/MIN8p4xwz+2Zo2//8QT+asRCBPBAgAAoAeL\nFrntuefGHr/9dmnVKunoo/1jV14pXXCB23/1Vbddt86trv2LX+S/ViAszAoFAADQA282qM2bpSFD\nur/f0uLPEOU93nifsdaFDWMIFigPyWaFosUCAACgBzvsII0fnzhUSFJNjdt+5zvd3zPGjbHYddf8\n1QcUA4IFAABACp2dbgG8++5Lfd6zz0pXXeW/fvFFf//ee/3wAZQrggUAAEAKBx7otiNGpD6vrk4a\nM8Z/fdBB0okn+q8JFih3BAsAAIAkpk/3B2APH57ZZ42RHn1UmjXLva6uDrQ0oOgQLAAAABK4/vrY\nqWF7arFIZuZMt41uzQDKEbNCAQAAxLFWqoj659c//1k65ZTsrrVpkzRsmLR1a/d1MIBSxKxQAAAA\naVq3zm2PPdZt9947+2vV1kr330+oQPmjxQIAACDKAw9IjzwiLVggLV0qvfCCdNhh/roUQG+XrMWC\nYAEAABAlOkDwqAJ0R1coAADQax1/vAsMr7/uVs/eti3xebfeKo0d6/b/+c/C1QeUA1osAABA2UvU\njSn+MWT1amncOLe/dCkrZQPJ0GIBAAB6rd12S3x840bp44/d/rPPuu3++0s771yYuoByQrAAAABl\n7brrXAvE+ee715ddJvXp4/aPPdZ1fdqwwbVYfPOb0sKFsVPNAkgP/9kAAICydtddbvuTn7jZni67\nTKqsdFPKtra690aMkC69VBo/Prw6gVLHGAsAADLwxhuuH/5224VdCdJ15JEuNJxwgnvd2irV1CQ+\nd8MGt5gdgOSYbhYAgAB4g4D5K6x4bdvmfsaMkfr2lSIRNxPUkCHu/fhVtX/7W9c16sQTpQkTwqkZ\nKCXJgkVlGMUAAFCK3n/f31+yRNp99/BqQXKnny499ph08cUuVJxxhh8qJBcOrZWef1566CHpe98L\nr1agnNBiAQBAmtKZstRzyy1SW5v0gx/ktyZ017+/1Nzsv372WamuLrRygLJDiwUAAGnq7JTeekua\nOtU/Nnduz597/XVpl12kwYOlCy90x555Rnr00fzUicQmTJCGD5e+8AXppJOkvfYKuyKgd6DFAgCA\nODfc4LrRLF0q/e1vbjahLVv89w86yF+VuaVFqq52oWK//dyxzs7YPvz8dVc477wjTZ4srV/vwgWA\n4LFAHgAAafrkE7fdbTfX/94LFTvv7N6bPt0/d4cd3LSlXqiQpFWrpFGj/NeRSP5rhrRmjQsVEjM7\nAWEgWAAAEMdb2yDaSSdJH37oppm96iq/FWLtWqmhIfbc8ePd8T/9Kfn1ELynnnJhsKMj8XgYAPlF\nsAAAoIu17oH0pptij8+aJf36193Pv/NOt915Z7eNDhA//KH0+c/npUwk0NYmzZghffnL/qraAAqL\nMRYAAHRZvdotfuftDx/uxk+sWRPbtcnT2Rn7EGutG3Px4x+7MDJokDRggGu9GDiwIL+EXssbbN/S\nIlVVhV0NUN4YYwEAQAJtbW49A0m6914XJjo73eJqVVXSSy8lDhWSG6BdUSFNmuR3jaqpcYO/Bw3y\nz+Hf0fLve99zv0+ECiA8TDcLAOi1rHUtEpL0l79Il17qujVF988/6KDU1+hpYHZFhQsqyI9Fi6S9\n93b7O+0Ubi1Ab0eLBYBPLVzoHqh+8Yvgrvncc/4MO0CxWb/e3z/lFLd9991g70GwCM6KFa6b2dtv\nu65q777rh4pFi9zgegDhYYwFAHV0uCkzV6/2j3V2Zj+rysMP+w9pngMPlObPl9rbpYcekr7xjdh5\n/ntirQsoo0e7VXQPPzyzzwPx1q2TRo6MPVZX5/58BWn4cOn991lTIRttbe5n4ED3/45E3ZwGD45d\nYwRA/jHGAr3KU0+5h1j07J57pL59/VDxxz+67Xe/m/j8bdtiZ75ZvdoNlty40b1etswPFSNGSMcc\n41Ygfvll9wAwfLj07W+7Aa9PP526tkhEOuQQF3AqKlyokKQjj5TOOku64grpZz+TGhvd8TvvdOf+\n5jeZfw/oPf7yF/fnxAsV8+ZJDzzgFsQLOlRImbdYRCLS4493n8I2CNu2lcZ4j2OOcS0R1dVurMpx\nx/mh4sUXpYkT3e/XmDFu0DaAImGtDeXH3RoIzvr11k6bZq37a9P9LFsWdlW+9nZrV6+2duPGxO93\ndlq7ZIm1bW2Fq+nBB9331KePtbNnW9va6o7fcYc7ftpp1j73nH/+G2/Efr977hn7epdd3Pbkk62N\nRGLv9dZb/nlr11p7yiluv77e2nfesbax0X0H119v7W23ue+qf3//M1/5irXz51u7ZYu1778fe9/4\nn5qa7vcPSyRi7aJF7teWyrvvWnvAAdYecYS1f/mL+/OydWtBSiwLmzdb++GHid+75BJrzzrL2j/+\n0YO5V50AABjiSURBVP352G47/8/K22/nvzbJ2nnz0jt30SJrjz7ar+/dd91/H8OGudep/hytWmXt\nCy+4ayxaFPvfREVF9/9OXnwxmF9fOlpbrX3tNWvXrLH2s5+19rvfjf3ut2619uqr3f9vrrgits4B\nA9z2s5/lvwmgWHQ9x3d/vk90sBA/BAsEIRKxtrnZ/WXUr5//F9GMGdaOHm3tnDn+uW1t1v7859b+\n+c/uL+c333QP1Pvua21HhzvW3u4CypFHWnvQQe5h9uKLrf3b39w15s2z9umnuz+0dna6h/RkDzbx\nD+Rr1rjP3H+/e6A//PDuf+nPmOEeDuK1tVn7xBPWPvmke+CYP989hDc0WPu5z7mH6tmzkz9Yd3Za\nO3eu+4tdsvbyy7uf8/bbsbWcdpq/P2SI+w691zvv7P7i33VXa487zgWGpqaef++stXbgwNj71NZ2\n/x6SBTFPa6v/oPjoo+6YZO0FF6RXQ5B+9jP3Xey/v7XLl7vv+tJL/V/b+PHWPvCA+z1sb3d/dj/3\nOWtHjEgekk46yb/+ihXWzpzprtHRUfhfX1juvtvaQYPcn+l//ct9d21t/kP2kiX+93XHHbEPn+3t\nib/X994rXP3R9z3nnNjfu0succfnzEkdlr2ft97qHi4iEff/s1SfmznT2gMP7P5nbf78/Pya29ut\nvesua6urU9c1ZIjb7rZb7PHzzus5jAMID8ECJct7QN640dp//MM98EvuX3bj/5KK/oto4kR3bNAg\nFzz23rv7+d6/Asb/jB9v7YknWvutb/n/Ch//M3Wqq2X//V1A8Y6PHm3tr3/tQsHcudaOHWttVZV7\nQHzzTWt32qn7tc4/3z1g3n+/tRdeaO3pp1u7xx7WTpli7VVXWbtwobUbNriHaO9f+pP9nHyyvz9q\nlHsQ8zz3XGyrzk03Jf/evbB0yy3u+/jWt6y99dZgWwI+/NAFpDvvtPa++6z9zW9cCFu71n0Pa9Zk\nd92LL3a/vupqa5cuTXxOJOIe1Nvb3etly9z3P3GitX37WltZae3vfmftypWxD7GexkZr//Qna3/6\nU2snT3a/f8l+Tw44wMb8y2v0T2Wla6WZM8fV0tLi7vnaa+7+ya75rW9Z+4UvWPvKK9l9R6Xg5pvT\ne9iWrB0+3D04J3rPGBc+7rzThY6XXy7sr2PFiu41tbRYe8ghyX89S5a4P3M77OBev/qqtRMmxJ7z\nwx9ae8YZscemT3fh6pJL3P8zN21yLRmJ1NT4n3vrLRd44v/7fvxx9w8Y6TzkP/aYaxmJbhHyfsaO\ndf/NzJ5t7fPPu/Pvvdfa/fZz7199tfv/W0NDTl81gAJJFiwYvB2wDRukm2+WDj1UOvrosKspbdZK\nt9/u+uNHmzZNWrxYOu006eCD3UwgZ54pDR0qDRvmnzd9uvTEE7GfXbFCeucdaeVK9/64cW7/lVf+\nf3v3HmdVXe5x/PNwH1AwjSFFuQWZmiBoCIYHDgnoycRSC6VUOFoeo4um5/TqYkOWmpaiotDFW3K0\n1LycrNRMUdI081KJ4iVBbiKI4DgODjDznD+e33Y20wAzs2fvzd5836/Xfs3ee6219289s/Zav/uC\nffaJftDPPw+f//yWA5dXr4Zf/jLGDtTWRj/se+6J50cdBZ/+dIwnuPFG+NnPos//iy/Gtt/8Jpx4\nYuPMJe7xPXffDWPHxriD5gYhr14dc7IfcEDsY0bHjjGv/tChsT+9e8cYh+XLYfjw+Kw1a+CQQ2I5\nwH77RX/yhx6KdWbPhtGj2z44uxS8+WaM55g6FVasgHPPjX7anTrBtGlw/fWN644cGWNAMqqq4oZo\n114bA0czDjwQpk+HD34Qjjkm3svc5Xft2hhgeued0Ud+3jxYvz7Gl2TfQG3pUjjrrEjfVVfF/2Zb\n/4eHHoK//S1m7JowIe4svGBBDF7PGD48Pue882Kq1OrqOM7mzoUTToB99912nCDikrnvQluOi9//\nPo7r1txp2j1+M2+8EbOHPfBAjAG44or4f8ybF+tNnx7/i113jfPqnXfC+PFxrGfGUr3xRvy/ly6N\nMVannRbvX3op7LUXfPazrd+n9uQe+7ZkCQwb1vh+//7x3sKFsPfe0KvX1j+jtjY+53e/g9/8JmIH\ncNhhcM018OEPty5Ny5fHea+pfv1g//3jHJdt/PgYQL377vG/XrUqxj3V1MSYh4cfjv//qlUxCP7U\nU3UHbJFytbXB23krWJjZkcAsYoD4Ne7+wybLS7JgMX/+fMaOHcctt0QGdcyYyBi+/HJc8Ju6+ebI\njHbrVvi0lqKFCyMDPGPGfG65ZRwAkyfHPPKVlXDSSVBR0bLPqq2NO942NERGY+BAGDIkf2lvKnN4\nt0fmfdky6N49Mq5durTuM6++Gr70pXj+5z9HYSxj/vz5jBs3LvcE7qCmT4frrmt+2YwZ8PWvw6OP\nRgZt2rTI1E2atOV6d90VGdm+feGnP41CW8bKlTF4dHvyFedNm+Ab34hCaG1tZMzXr29+3blzY/3L\nL4/Md3aBqanx4+GOO+Lclm3DhjiXNXf8VVREAXfixMZz4vDhMGtWFAgy29TURIHghRdgxIgtP2P6\n9Ph/rF0b2/zkJzGIF6KwlimAb9gQv4dspXQs339/XBtOPjkqF9pq9eqIRf/+uaXntdeiMmXKlChs\nvPhiFMaefTYqShoa4th6/XV45ZX5vPvuOPr3j9/E5s2waFFMAjFlShSWO3fOLT1SWsdzKVOc266g\nBQsz6wC8CHwcWAk8AUxx90VZ6/hxxzkjRsDhh0eNS6Zmo74+LtjucO+9kZEaNy73k2dbrFgRNWdL\nl8YF9a67qli8uIpFi6LWpkePyPRB1IBfdllkXtevjxkrrr02MoOnnRYX9gsuiExe0ynz6utjmy5d\n4oLq3nghXrYsLkI9ekQGu0+fqGWqr4dnnolaqoqKf631do8L9OuvR/orKqKWO7tWv71VV0dt1YoV\nsb/V1VEb17NnXJyOOy6WLVsWF5/+/WM/1qyBV19tvPttt25VVFZW8dhjLcu4ybbV1UWNbt++W75f\nVVVFVVVVUdJUKJnfUkMDvPQS3HRTtDwcf3zbPm/z5jhXtaZwV6g4u8esXHvsEb/9QYOiReKccxpb\naCZNikzkffdFpvSTn4xzyKBB8VucOxcuuSSWDRzYeD565pnG7+ncOQqoFRVROFiwAB55JFrBPvGJ\nmFlsyBC47bbGbSZPjrh///uN740aFd83dGi8zqUQvjMcyzsCxbkwFOfCUJzbbmsFi3zdeXsk8JK7\nv5q+/JfAZGBR9kpr10ZN8re+FRfqnj3jol1TE91KGhoau3acempsM2RINBcPGRLLOnfe8uZbq1ZF\nJrpzZxgwID7zAx+ITHlFRfzdbbfoNtOrV9R6VVTExbdHj5hysK4uMr/z5sVF+rDDohbtoIPi4vqx\njzU2u0NcdDdubLx7K8TnX3MNXHhhXNBfey2Wn302fPvb0W3h5Zdjv559Fp5+OvZ748a4uLpHunbZ\nJWoBO3aMebrd43s3bYpMO0SBp64uvjPiHTFauhTWrYsY1NdHgWLZsojbgQfGZ3TtGvs9ZEh0uVm1\nKr5zjz0ihps2RZoyMVmyJL5vzZrIpGXmDq+tjfdWroxuIu9/f8T99NPj/fXr4ckno0Vir72iG8mj\nj8Z39ewZBYxDD42CZPfu0RVFv/X207XrvxYqdhaZzGqHDtElaObM3D6vU77Omu3ALH5/EOc5iN/y\ndddFBn7VqsYKmqlTm/+M886Lu08vXBjdm6qr49xy9NHRylNdHTcn694d5s+H22+P2C5YEC24EOd0\niN/8W29FZcicOXH/khkz4OKLY3lLWx9FRKQ05OsS2RdYlvV6OVHY2EJmvnD3qFV/663GueozfX0z\n1q2LzHdlZfT7XLIkuiesXx+tGZnMQ/fuURCoro7nb78dhZcnnoDBgyOj/OabsbymJjLEdXWRuX7n\nnch4jB4dmeqZM6N2r3fvxnQ0l+E127JQka2yMi7SEK0Z1dXxd+nSqKUbMCD6d48ZE/1aX3kllo0e\nHWmtqWnM5GfU18c+NDRE5qFr13ieaQno0yeeV1ZGv9fsloyamohfTU3sd8eO0fR9++1www2xfm1t\nFPo2b44WlM6d47HnnpE5rauLvxMnRuFs2bKIbWVlPJp2Udia6dNbtp6I5K5r15a3+nbrBgcfHI+m\n+vRp7FJ45JFw0UVb/5zs7WfPbnlaRUSkNOWrK9RxwCR3/0J6/TlgpLt/JWud0htgISIiIiIiBe0K\ntQLol/V67/TeNhMjIiIiIiKlqZlJLtvFE8BgM+tvZl2AKcD/5em7RERERESkyPLSYuHu9WY2A7iP\nxulmn8/Hd4mIiIiISPEV7QZ5IiIisuOxUr3RlIgUXb66QpU8s3K+J/GOwcx2TX8VaxFpEZ0vCkK3\nuCsAMzvCzJqZe03ak5np/u8FpIJFFjP7iJlNMrNOqq3JHzMbYWa3Af8JoFjnh5ntmf7qpJpHZjbS\nzC5INwaVPDCz/c3scND5Ip/M7BAzuxW4xMzG6NyRH2Y23Mx+D9wBDC52esqRmY02s+9BdM8vdnp2\nJjvwrZ4Kx8zeB/wAOAz4J3CEmc11938WN2Xlxcz2AKqAjwK7A4+l9zvqh99+zGwXYA4w1cyGufs/\nFOP2Z2Y9gQuJ4/l6d29QF5L2ZWadgdnAKOAFMxsFPODuT5pZB3dvKG4Ky0NqBboQOAK4krgX1Qxi\nNsfFRUxaWUkFtTnACOD7wFJgv7RMx3M7MbNTgG8Rkwg96+63pArjzcVO285ANWzhXKDO3Q8CTgMO\nANTc3v5+RFQ4jiLi/HlQbUIeHE3coHIWcRFTjPPjm0SGd6K7Xw2qTc+DA4Be7j4M+C9gE3CWmXVX\nJqz9pON2ATDB3W8ArgMcWFPUhJWZdB7+A3C4u98J3A78u5l10/HcrpYC44EjgR8DuPtmdaMsjJ22\nYJG643w4vZzp7mel5xOJ2vQDMmMApO1SnPdNL8/IukniGuC5rGWSAzMbaGYV6eW9wCx3PxvoZ2ZT\n0jpqocxRinPm3vK/II7jSjM73sx+ZGZTzKzfNj5CtiPFuFt62QMYnlrc1gLvAvsTFRMab5EDMzvR\nzGaa2WQAd/+tu69LXc4eAwYAPzCzCcVMZ6lLcf6emR0D4O63uvuGdOzWAy8C3bf5IbJNZjbWzA7N\nems+sMrd7wNeNbPz0/u6BhbATlewSBet3wJXATeY2Xh3r0vLxgLnADcAxwLnmdnexUtt6WoS519k\n4pyVuW0A9gJq0/rKILSBmQ1IfXV/Dswzs33dfZ27r06rnA1cDFFjU6x0lromcb7RzPZ39+eIWt57\niW4jLwAnAOfqvNF6TWL8v6ni52/An4A5ZjYIGE30Sx9hZu9XC1HrWTgD+G9gCXCxmU3LqkhbD5zq\n7qOBp4ETsyrhpIWaxHkxMW5lWuqqmmklWgR8HOiW2aZY6S1FZrarmd1OnBO+mLq1Q/Q4ybTSfxH4\nipn1cfdNxUjnzmanKFg0+bGeAzyTTpp3kmq+ANz9IXf/qLvPITJjvYEhBU1sCWtJnDOZW3d/gfjh\nTy50OktdM3F+3N0/DjwInG9mB2QWuvttwHIzm5m27Ya0SAviPBC4BKhy93Hu/jPgO8AuwMCCJ7gE\nbSfGVcDeREzfBS4HniRuttoBWFfQxJaJlKEdDVzk7tcBXyIyt/+W+vn/w90fTKs/DLwPqClOakvX\nduJsaZ3lwOPA8VnbSMttBB4APgesJCp2cPcGd/fU0rkQuBW4CMDMjipWYncWO0XBgi1rA94h+ukC\n9AKez+6OY2lml3RDv0qiRkdapsVxTm4lupF01Am1VTJxzrT+PAfg7rOBkcSg7cqs9Y8lamyqgMvN\nrE8B01rKthXng4masF1Sn3TSsueADxB9fGX7thXjUcA0oDZ1oTzO3a8AXgL2ACr+9eOkOWZ2cuou\nsnt663mgr8WA1vuBfwAfIwZtZ5tA5BPeLlxqS1cL4zwG2Cet35k4nt8pSoJLUFaMd0u9TX4O3E90\nKTvEzD6U1jNinBDufhpwipmtA4aZZvDLq7IOrplNMLM/EE2Qn0mZ1z8BQ8zsaWJgT0eiC8lES1Pr\nmdlkM/sj8Brwhpont60Ncc7Esy+wjwYWt0wzcd4MvEn0QR9mZsOAZ4F+xDihjN5AT2AcMNvdXy9w\n0ktKK+K8N1H5kNnumHTeWAm8qfPG1rUixn2JghpAvUU/9YeBv5K6UUrzUlecPc3sQeAUYCpwpcVs\nZsuIYzcz1emviNmJ9kjbTjKzvwL/AfyPu79V8B0oEW2M8+4AqWvOLsR4FtmKrcT4KovukO+6+0bg\nz8Bq4DPwXuuPm1n/1F1qATFo/iINlM8zdy/LB/FDfpzoajMcuAk4Jy3bF7g9a93vAJel50cAfwGO\nLfY+lMKjDXGeReMd3wcCRxV7H0rh0UycbwbOBHZNcb2bKMwdkv4HM9J2ewNzgc8Wex9K4ZFDnA8j\nuunovJG/GO8L/Br4dLH3YUd/AB3T3w8B8zLvAVcTYwg7A9cQM/P1SsuvJyYyARgKHF3s/djRH7nG\nOb22Yu/HjvzYRoyvzM5fpPc/lWI/mGgN7UBUqo0s9n7sTI+yGiGf1Y2pATgUeNLd70rL7gcuNbMb\niZqxZWa2n0eXpweBr6X+pfcTzWqyFbnGOfM57r4YzZG+VS2I84+BW939fDMb5O6vpGWPAHVp2+XA\nGcVIf6nIIc6PEn3/cfdHie5R0ox2OpZfAI4rRvpLRWp1Px/oaGa/IzJV9RBTnZrZl4mW+P2JQtun\niMqHC4kJNf6S1v078PeC70CJaK84p/XVDbgZLYjxV4GVZjbW3R9K799hZvsB9xAtQeM9uqf+pdkv\nkbwom65QZjYNWE4ciBB9GadYDLCEqDl4JS1/m2iK/Eo6OH9CFCZc3Re2rZ3iLNvRgjh3Im7meFl6\nvTht9wXijuZPFS61pSvHOE9Hcd4uHcuFYTGr4ZPEYOuXiXhvIu6TMBLeu4/CTOCH7v5H4KfAGDN7\nPG03vwhJLymKc/61MMYNxAQPVVnbnUDcGO9BYGgqVEiBWTkUli2mb5tHHEynACe5+yIzmwX0Ifqc\nLwZ+SMz2dHx67wiiuX2Ouz9WjLSXEsW5MFoZ54uA6e7+upl9jeh7eqa7P1Gc1JcOxTn/FOPCsbj/\nxAB3vzG9vpooxG0AvuzuB6eWo0qiG8m57r7EzHYDerj7imKlvZQozvnXyhhfQYwDWpy2w90XFCnp\nAuUzxgLol/5eBPwqPe9I1JiPSa/3Ifo9dil2ekv1oTjvcHG+HuiaXncvdrpL7aE4K8bl8iBustaV\nxj7pU4EL0/NniAwZRCXPzcVOb6k+FOcdLsY3FTu9emz5KJuuUO6emd5xFjDQzCZ5NEe+5e5/SsvO\nIKZ10yxEbaQ4F0Yr4lwLZO4NollyWklxzj/FuDDcvdbd67xxlr0JxJ3hIabt3c/M7iYGy6t7WRsp\nzvnXyhg/XYw0ytaVRVeopszsi0ST+9j0eiTR764z0dS+qpjpKxeKc2EozoWhOOefYpx/adCrA78l\nanZfNrPBwBvAR4DFru44OVOc808xLk1lV7BIMzs1mNltxKwMdcSA4Zfc/Z/FTV35UJwLQ3EuDMU5\n/xTjwkgTkHQhbhx2BzHJwFoiY1ZdzLSVE8U5/xTj0lRW081CzBRgZt2JQT3jgO+5+z3FTVX5UZwL\nQ3EuDMU5/xTjwnB3N7PhRL/0gcB17n5NkZNVdhTn/FOMS1PZFSySM4m+jRM8bvku+aE4F4biXBiK\nc/4pxoWxnOhidqninFeKc/4pxiWm7LpCQWOTe7HTUe4U58JQnAtDcc4/xVhEpLyVZcFCREREREQK\nq2ymmxURERERkeJRwUJERERERHKmgoWIiIiIiORMBQsREREREcmZChYiIiIiIpIzFSxERKRFzKze\nzJ4ys2fN7GkzOzvdHXdb2/Q3sxMLlUYRESkeFSxERKSl3nH3Ee7+EWACcBTw3e1sMxA4Ke8pExGR\nolPBQkREWs3d3wC+AMyA91omHjazv6bHqLTqhcCY1NLxVTPrYGYXm9njZvaMmZ1erH0QEZH2pRvk\niYhIi5hZtbv3bPLem8C+wNtAg7tvNLPBwM3u/lEzGwt83d2PSeufDvR29wvMrAvwCHC8u79a2L0R\nEZH21qnYCRARkZKWGWPRBZhtZgcB9cCQraw/ETjQzE5Ir3umdVWwEBEpcSpYiIhIm5jZIGCzu68x\ns+8Cq9x9qJl1BDZsbTPgy+7+h4IlVERECkJjLEREpKXemwHKzHoDc4Ar01u9gNfS85OBjun528Cu\nWZ9xL3CmmXVKnzPEzCrymWgRESkMtViIiEhLdTOzp4huT5uAX7j7ZWnZ1cCvzexk4B7gnfT+34EG\nM3sauN7dLzezAcBTaara1cCxBdwHERHJEw3eFhERERGRnKkrlIiIiIiI5EwFCxERERERyZkKFiIi\nIiIikjMVLEREREREJGcqWIiIiIiISM5UsBARERERkZypYCEiIiIiIjlTwUJERERERHL2/8ZGdsur\nQlYWAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x116367690>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# makes the plot and assign it to a variable\n",
    "appl_open = apple['Adj Close'].plot(title = \"Apple Stock\")\n",
    "\n",
    "# changes the size of the graph\n",
    "fig = appl_open.get_figure()\n",
    "fig.set_size_inches(13.5, 9)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### BONUS: Create your own question and answer it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}