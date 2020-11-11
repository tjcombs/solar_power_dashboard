# solar_power_dashboard

This repository contains an example of how to build a dashboard
using python.

### Docker
The simplest method to build the dashboard is by using docker.
Build a docker image containing the dashboard by running
```bash
docker build -t solar_power_dashboard .
```

Run the dashboard in the container by running

```bash
docker run -p 8050:8050 solar_power_dashboard
```

Access the dashboard at [http://127.0.0.1:8050/](http://127.0.0.1:8050/).

### Anaconda
To run the code in Anaconda, first create a virtual environment and activate it.

```bash
conda create -n solar_power_dashboard python=3.8
conda activate solar_power_dashboard
```

Install fbprophet
```bash
conda install -c conda-forge fbprophet
```

Install the dependencies
```bash
pip install -r requirements.txt
```

Run the dashboard
```bash
python main.py
```
Access the dashboard at [http://127.0.0.1:8050/](http://127.0.0.1:8050/).