# Strømpris

This project provides a web-based visualization of energy prices in Norway, using the Hva Koster Strømmen API: https://www.hvakosterstrommen.no/strompris-api. 

You can view the change in energy prices on the web for a selected time period (default: last 7 days) for 5 regions in Norway (Oslo, Kristiansand, Trondheim, Tromsø, Bergen).


## Package dependencies
- altair
- altair-viewer
- beautifulsoup4
- fastapi[all]
- pandas
- pytest
- requests
- requests-cache
- uvicorn

\* see requirements.txt

## Installation
1. Download the package.
2. Install requirements using:
```bash
pip install -r requirements.txt
```

## How to use
1. Run a server using:
```bash
python3 app.py
```
or
```bash
puvicorn app:app --port 5000
```
\* Press CTRL+C to stop the server

2. See the visualization results:

    Go to the web address `http://127.0.0.1:5000/`

## Comments to the grader
I have done tasks 5.1 and 5.2, and the test passed on both tasks.

\*The assignment text says to fetch data for 8 days including today when 'days'=7, but when I did that, an error occured in `test_fetch_prices()`. So, I implemented 'days' in `fetch_prices()` to be the period including today.