import datetime
from typing import List, Optional

import altair as alt
from fastapi import FastAPI, Query, Request
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from strompris import (
    ACTIVITIES,
    LOCATION_CODES,
    fetch_day_prices,
    fetch_prices,
    plot_activity_prices,
    plot_daily_prices,
    plot_prices,
)

app = FastAPI()
templates = Jinja2Templates(directory='templates')

# `GET /` should render the `strompris.html` template
# with inputs:
# - request
# - location_codes: location code dict
# - today: current date
@app.get("/")
def strompris_html(request: Request, 
                    today: datetime.date=datetime.date.today(),
                    location_codes: Optional[List[str]]=LOCATION_CODES) -> Jinja2Templates:
    """Render the `strompris.html` template by a web request
    Arguments:
        request (Request): Request object with parameters
        location_codes (List[str]): list of location dict(code:name) in Norway. default = all five regions
        today (datetime.date): day to fetch data. default = current date
    Returns:
        Jinja2Templates : Template rendered `strompris.html`
    """
    return templates.TemplateResponse(
        "strompris.html", {
            "request": request,
            "location_codes": location_codes,
            "today": today,
        }
    )


# GET /plot_prices.json should take inputs:
# - locations (list from Query)
# - end (date)
# - days (int, default=7)
# all inputs should be optional
# return should be a vega-lite JSON chart (alt.Chart.to_dict())
# produced by `plot_prices`
# (task 5.6: return chart stacked with plot_daily_prices)
@app.get("/plot_prices.json")
def plot_prices_json(locations: Optional[List[str]]=Query(default=None),
                    end: Optional[datetime.date]=None,
                    days: Optional[int]=7) -> dict:
    """Plot an energy prices chart from the `strompris.html` template by a web request
    Arguments:
        locations (List[str]): location to fetch data. get from Query. default = None
        end (datetime.date): the last day of the period to fetch data. default = None
        days (int): the periods(days) to fetch data. dafault = 7
    Returns:
        dict: chart as dictionary type vega-lite JSON chart
    """
    date_args = dict(end_date=end, days=days)
    if locations is None:
        pass
    else:
        date_args["locations"] = locations

    return alt.Chart.to_dict(plot_prices(fetch_prices(**date_args)))


# Task 5.6:
# `GET /activity` should render the `activity.html` template
# activity.html template must be adapted from `strompris.html`
# with inputs:
# - request
# - location_codes: location code dict
# - activities: activity energy dict
# - today: current date

...

# Task 5.6:
# `GET /plot_activity.json` should return vega-lite chart JSON (alt.Chart.to_dict())
# from `plot_activity_prices`
# with inputs:
# - location (single, default=NO1)
# - activity (str, default=shower)
# - minutes (int, default=10)

...


# mount your docs directory as static files at `/help`

...

if __name__ == "__main__":
    # use uvicorn to launch your application on port 5000
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)

