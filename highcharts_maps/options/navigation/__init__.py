from typing import Optional

from highcharts_core.options.navigation import NavigationBase

from highcharts_maps.decorators import class_sensitive
from highcharts_maps.options.annotations import Annotation


class Navigation(NavigationBase):

    @property
    def annotation_options(self) -> Optional[Annotation]:
        """Additional options to be applied to all annotations.

        :rtype: :class:`Annotation <highcharts_maps.options.annotations.Annotation>`
          or :obj:`None <python:None>`
        """
        return self._annotation_options

    @annotation_options.setter
    @class_sensitive(Annotation)
    def annotation_options(self, value):
        self._annotation_options = value
