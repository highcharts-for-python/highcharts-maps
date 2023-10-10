from validator_collection import validators

from highcharts_core.utility_functions import *

from highcharts_maps import errors


def validate_bounding_array(value,
                            allow_singleton = True,
                            allow_percentage_strings = True,
                            allow_numbers = True):
    """Validates that ``value`` is either a single value or a 4-member collection.

    :param value: The value to validate.

    :param allow_singleton: If ``True``, accepts either a collection or a single value.
      Defaults to ``True``.
    :type allow_singleton: :class:`bool <python:bool>`

    :param allow_percentage_strings: If ``True``, accepts percentage strings. If ``False``
      rejects them. Defaults to ``True``.
    :type allow_percentage_strings: :class:`bool <python:bool>`

    :param allow_numbers: If ``True``, accepts numerical values. If ``False``, rejects
      them. Defaults to ``True``.
    :type allow_numbers: :class:`bool <python:bool>`

    :returns: The validated ``value``.
    :rtype: :class:`str <python:str>`, :class:`int <python:int>`,
      4-member :class:`list <python:list>` of :class:`str <python:str>` or
      :class:`int <python:int>`, or :obj:`None <python:None>`
    """
    if value is None:
        return None
    else:
        try:
            value = validators.iterable(value)
            processed_value = []
            for item in value:
                if allow_percentage_strings and allow_numbers:
                    try:
                        item = validators.string(item)
                        if '%' not in item:
                            raise errors.HighchartsValueError(
                                'padding accepts either numbers'
                                ' or percentage strings. No "%"'
                                ' found.'
                            )
                    except (ValueError, TypeError):
                        try:
                            item = validators.numeric(item)
                        except (ValueError, TypeError):
                            raise errors.HighchartsValueError(
                                f'padding received an '
                                f'unacceptable value: {item}'
                            )
                elif allow_percentage_strings:
                    item = validators.string(item)
                    if '%' not in item:
                        raise errors.HighchartsValueError(
                            'padding accepts either numbers'
                            ' or percentage strings. No "%"'
                            ' found.'
                        )
                elif allow_numbers:
                    try:
                        item = validators.numeric(item)
                    except (ValueError, TypeError):
                        raise errors.HighchartsValueError(
                            f'padding received an '
                            f'unacceptable value: {item}'
                        )

                processed_value.append(item)

            if len(processed_value) == 1 and allow_singleton:
                return processed_value[0]
            elif len(processed_value) != 4:
                raise errors.HighchartsValueError(f'if an iterable, expects 4 members. '
                                                  f'Received a '
                                                  f'{len(processed_value)}-member value.')

            return processed_value

        except (ValueError, TypeError):
            if not allow_singleton:
                raise errors.HighchartsValueError('did not receive a collcetion, but '
                                                  'allow_singleton was set to False')

            if allow_percentage_strings and allow_numbers:
                try:
                    value = validators.string(value)
                    if '%' not in value:
                        raise errors.HighchartsValueError('accepts either numbers'
                                                          ' or percentage strings. No "%"'
                                                          ' found.')
                except (ValueError, TypeError):
                    try:
                        value = validators.numeric(value)
                    except (ValueError, TypeError):
                        raise errors.HighchartsValueError(f'received an '
                                                          f'unacceptable value: {value}')
            elif allow_percentage_strings:
                value = validators.string(value)
                if '%' not in value:
                    raise errors.HighchartsValueError('accepts either numbers'
                                                      ' or percentage strings. No "%"'
                                                      ' found.')
            elif allow_numbers:
                try:
                    value = validators.numeric(value)
                except (ValueError, TypeError):
                    raise errors.HighchartsValueError(f'received an '
                                                      f'unacceptable value: {value}')

            return value
