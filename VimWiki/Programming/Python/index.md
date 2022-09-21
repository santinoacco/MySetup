# Python Index

## My library
    * [NoaccoLib](NoaccoLib/index)
    * [PyROOT](Programming/Python/PyROOT)


-   To "profile" a function:
> ```python
import cProfile
import pstats
with cProfile.Profile() as pr:
    foo
stats = pstats.Stats(pr)
stats.sort_stats(pstats.SortKey.TIME)
stats.print_stats()

```

## Pandas
-   To load 'datetimes' to pandas from strings:
    - > `pd.DataFrame(data,dtype="datetime64[ns]")`
-   To change a column from str to datetime:
    - > df = pd.to_datetime(<cols>,format=<datetime_formta>)
- 

## Bokeh

## Dash

## Security

## Forecasting
-   Given a TimeSerie, extract trend, seasonality and cycles:
    - >
    
# Web Scrapping

## Request
-   syncronous lib

## httpx
-   assyncronous lib.
```python3
import asyncio
import httpx

async def foo():
    async with httpx.AsyncClient( ) as client:
        tasks = (client.get(url) for url in urls)
        reqs = await asyncio.gather(*tasks)

asyncio.run(foo)
```

