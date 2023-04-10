from typing import Optional, List
from collections import UserDict

from validator_collection import validators, checkers

from highcharts_maps import constants, errors
from highcharts_maps.options.plot_options.generic import HighchartsMeta


class MapBaseOptions(HighchartsMeta):
    """Base class for Map Plot Options."""

    def __init__(self, **kwargs):
        self._all_areas = None
        self._join_by = None

        self.all_areas = kwargs.get('all_areas', None)
        self.join_by = kwargs.get('join_by', None)

        super().__init__(**kwargs)

    @property
    def all_areas(self) -> Optional[bool]:
        """If ``True``, all areas defined in the map's
        :meth:`.map_data <highcharts_maps.options.series.base.MapSeriesBase.map_data>`
        should be rendered, with areas that do not have a related data point rendered as
        null values. If ``False``, areas of the map that do not have a related data point
        are skipped and not rendered. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._all_areas

    @all_areas.setter
    def all_areas(self, value):
        if value is None:
            self._all_areas = None
        else:
            self._all_areas = bool(value)

    @property
    def join_by(self) -> Optional[str | List[str] | constants.EnforcedNullType]:
        """The property which should be used to join the series'
        :meth:`.map_data <highcharts_maps.options.series.base.MapSeriesBase.map_data>` to
        its ``.data``. When :obj:`None <python:None>`, defaults to ``'hc-key'``.

        Accepts three possible types of value:

          * a string, which joins on the same property in both the ``.mapData`` and
            ``.data``

            .. note::

              For maps loaded from :term:`GeoJSON`, the keys may be held in each point's
              ``properties`` object.

          * a 2-member collection, where the first represents the key in ``.mapData`` and
            the second represents a (different) key in ``.data``
          * :obj:`highcharts_maps.constants.EnforcedNull`, where items are joined by their
            positions in the ``.mapData`` and ``.data`` arrays

        .. tip::

          Using :obj:`highcharts_maps.constants.EnforcedNull` performs much faster than
          the other two options. This is the recommended value when rendering more than a
          thousand data points, assuming that you are using a backend that can preprocess
          the data into parallel arrays.

        :rtype: :obj:`highcharts_maps.constants.EnforcedNull` or :class:`str <python:str>`
          or 2-member :class:`list <python:list>` of :class:`str <python:list>`, or
          :obj:`None <python:None>`

        :raises HighchartsValueError: if supplied an iterable that has more than 2 members
        """
        return self._join_by

    @join_by.setter
    def join_by(self, value):
        if value is None:
            self._join_by = None
        elif isinstance(value, constants.EnforcedNullType):
            self._join_by = constants.EnforcedNull
        elif checkers.is_iterable(value, forbid_literals = (str, bytes, dict, UserDict)):
            if len(value) > 2:
                raise errors.HighchartsValueError(f'join_by expects a 2-member iterable.'
                                                  f'Received a {len(value)}-member '
                                                  f'iterable.')
            elif len(value) == 2:
                self._join_by = [
                    validators.string(value[0]),
                    validators.string(value[1])
                ]
            else:
                self._join_by = validators.string(value)
        else:
            self._join_by = validators.string(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'all_areas': as_dict.get('allAreas', None),
            'join_by': as_dict.get('joinBy', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'allAreas': self.all_areas,
            'joinBy': self.join_by,
        }

        return untrimmed
