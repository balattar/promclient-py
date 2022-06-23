# promclient-py

Prometheus Client

## Installation
Note that python version 3.10 or greater is required.

```bash
python -m pip install --upgrade pip wheel setuptools
python -m pip install git+ssh//git@github.com:bma5287/promclient-py.git
```

## Usage

```bash
Usage: prom query [OPTIONS] METRIC

  Query METRIC from the Prometheus database.

Options:
  -s, --start TEXT         Start time of the query in your local time
                           [default: 2022-06-21T00:00:00.000Z]
  -e, --end TEXT           End time of the query in your local time  [default:
                           2022-06-22T06:00:00.000Z]
  -t, --time-step INTEGER  Time interval between measurements in seconds
                           [default: 15]
  --plot                   Optionally plot the queried metrics
  --dump                   Optionally dump the queried metrics to stdout
  --help                   Show this message and exit.
```