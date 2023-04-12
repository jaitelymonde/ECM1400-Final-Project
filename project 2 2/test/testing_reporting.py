import pytest
from reporting import daily_average, daily_median, monthly_average, hourly_average, peak_hour_date, count_missing_data, fill_missing_data

def test_daily_average():
    assert daily_average(data_set)
    

    with pytest.raises(ZeroDivisionError):
        
