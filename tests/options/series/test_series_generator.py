import pytest

from json.decoder import JSONDecodeError

from highcharts_core.options.series.base import SeriesBase as CoreSeriesBase
from highcharts_core.options.series.bar import BarSeries as CoreBarSeries
from highcharts_maps.options.series.base import SeriesBase as MapsSeriesBase
from highcharts_maps.options.series.bar import BarSeries as MapsBarSeries

from highcharts_maps.options.series.series_generator import create_series_obj


@pytest.mark.parametrize('cls, expected, error', [
    (CoreBarSeries, True, None),
    (MapsBarSeries, True, None),
])
def test_isinstance_check(cls, expected, error):
    if not error:
        item = cls()
        result = create_series_obj(item)
        assert isinstance(result, cls) is expected
        assert isinstance(result, CoreSeriesBase) is expected
    else:
        item = cls()
        with pytest.raises(error):
            result = create_series_obj(item)