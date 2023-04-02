from typing import Optional
import json

from validator_collection import validators

from highcharts_maps import errors
from highcharts_maps.metaclasses import HighchartsMeta


class FetchConfiguration(HighchartsMeta):
    """The configuration settings to apply to a JavaScript ``fetch()`` request."""

    def __init__(self, **kwargs):
        self._url = None
        self._method = None
        self._headers = None
        self._body = None
        self._mode = None
        self._credentials = None
        self._cache = None
        self._redirect = None
        self._referrer = None
        self._referrer_policy = None
        self._integrity = None
        self._keepalive = None

        self.url = kwargs.get('url', None)
        self.method = kwargs.get('method', None)
        self.headers = kwargs.get('headers', None)
        self.body = kwargs.get('body', None)
        self.mode = kwargs.get('mode', None)
        self.credentials = kwargs.get('credentials', None)
        self.cache = kwargs.get('cache', None)
        self.redirect = kwargs.get('redirect', None)
        self.referrer = kwargs.get('referrer', None)
        self.referrer_policy = kwargs.get('referrer_policy', None)
        self.integrity = kwargs.get('integrity', None)
        self.keepalive = kwargs.get('keepalive', None)

    def __str__(self):
        untrimmed = self._to_untrimmed_dict()
        del untrimmed['url']
        trimmed_options = {}
        for key in untrimmed:
            if untrimmed[key] is not None:
                trimmed_options[key] = untrimmed[key]

        options_as_str = None
        if trimmed_options:
            options_as_str = json.dumps(trimmed_options)

        if not options_as_str:
            as_str = f"""fetch("{self.url}")"""
        else:
            as_str = f"""fetch("{self.url}", options = {options_as_str})"""

        return as_str

    @property
    def is_valid(self) -> bool:
        """Indicates whether the :class:`FetchConfiguration` can construct a valid
        (JavaScript) ``fetch()`` call. ``True`` indicates validity, ``False`` means the
        call will fail.

        :rtype: :class:`bool <python:bool>`
        """
        return self.url is not None

    @property
    def url(self) -> Optional[str]:
        """The URL that the (JavaScript) ``fetch()`` function will be requesting. Defaults
        to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._url

    @url.setter
    def url(self, value):
        self._url = validators.url(value, allow_empty = True)

    @property
    def method(self) -> Optional[str]:
        """The HTTP method to use when requesting the
        :meth:`.url <highcharts_maps.utility_classes.fetch_configuration.FetchConfiguration.url>`.
        Defaults to ``'GET'``.

        Accepts:

          * ``'GET'``
          * ``'HEAD'``
          * ``'POST'``
          * ``'PUT'``
          * ``'DELETE'``
          * ``'CONNECT'``
          * ``'OPTIONS'``
          * ``'TRACE'``
          * ``'PATCH'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._method

    @method.setter
    def method(self, value):
        if not value:
            self._method = None
        else:
            value = validators.string(value)
            value = value.upper()
            if value not in ['GET',
                             'HEAD',
                             'POST',
                             'PUT',
                             'DELETE',
                             'CONNECT',
                             'OPTIONS',
                             'TRACE',
                             'PATCH']:
                raise errors.HighchartsValueError(f'method expects a valid HTTP method. '
                                                  f'Received: "{value}"')

            self._method = value

    @property
    def headers(self) -> Optional[dict]:
        """Headers to supply as HTTP headers with the request. Expects a
        :class:`dict <python:dict>` whose keys are the header and whose values are the
        header value. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`dict <python:dict>` or :obj:`None <python:None>`
        """
        return self._headers

    @headers.setter
    def headers(self, value):
        if not value:
            self._headers = None
        else:
            value = validators.dict(value)
            for key, item in value.items():
                if not checkers.is_string(key):
                    raise errors.HighchartsValueError(f'header keys must be strings. '
                                                      f'Received a: '
                                                      f'{key.__class__.__name__}')
                if not checkers.is_string(item):
                    raise errors.HighchartsValueError(f'header values must be strings. '
                                                      f'Received a: '
                                                      f'{item.__class__.__name__}')
            self._headers = value

    @property
    def body(self) -> Optional[str]:
        """The body to supply when making the request. Defaults to
        :obj:`None <python:None>`.

        .. warning::

          Will only be supplied if
          :meth:`.method <highcharts_maps.utility_classes.fetch_configuration.FetchConfiguration.method>`
          is ``'POST'``, ``'PUT'``, or ``'PATCH'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._body

    @body.setter
    def body(self, value):
        self._body = validators.string(value, allow_empty = True)

    @property
    def mode(self) -> Optional[str]:
        """The mode that you wish to use for the request. Defaults to
        :obj:`None <python:None>`.

        Accepts:

          * ``'cors'``
          * ``'no-cors'``
          * ``'same-origin'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._mode

    @mode.setter
    def mode(self, value):
        if not value:
            self._mode = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['cors', 'no-cors', 'same-origin']:
                raise errors.HighchartsValueError(f'mode expects either "cors", '
                                                  f'"no-cors", or "same-origin". '
                                                  f'Received: "{value}"')
            self._mode = value

    @property
    def credentials(self) -> Optional[str]:
        """Determines what browsers do with credentials (cookies, HTTP authentication
        entries, and TLS client certificates). Defaults to :obj:`None <python:None>`,
        which acts as if ``'same-origin'`` was provided.

        Accepts the following:

          * ``'omit'`` - tells browsers to exclude credentials from the request, and
            ignore any credentials sent back in the response (e.g., any ``Set-Cookie``
            header).
          * ``'same-origin'`` (default) - tells browsers to include credentials with
            requests to same-origin URLs, and use any credentials sent back in responses
            from same-origin URLs.
          * ``'include'`` - tells browsers to include credentials in both same- and
            cross-origin requests, and always use any credentials sent back in responses.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._credentials

    @credentials.setter
    def credentials(self, value):
        if not value:
            self._credentials = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['omit', 'same-origin', 'include']:
                raise errors.HighchartsValueError(f'credentials expects either "omit", '
                                                  f'"same-origin", or "include". '
                                                  f'Received: "{value}"')
            self._credentials = value

    @property
    def cache(self) -> Optional[str]:
        """Determines how the request will interact with the browser's HTTP cache.
        Defaults to :obj:`None <python:None>`, which behaves as ``'default'``.

        Accepts the values:

          * ``'default'``
          * ``'no-store'``
          * ``'reload'``
          * ``'no-cache'``
          * ``'force-cache'``
          * ``'only-if-cached'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._cache

    @cache.setter
    def cache(self, value):
        if not value:
            self._cache = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['default',
                             'no-store',
                             'reload',
                             'no-cache',
                             'force-cache',
                             'only-if-cached']:
                raise errors.HighchartsValueError(f'cache expects a value supported by '
                                                  f'the JavaScript Request object. '
                                                  f'Recieved: "{value}"')

            self._cache = value

    @property
    def redirect(self) -> Optional[str]:
        """Determines how to handle a ``redirect`` response. Defaults to
        :obj:`None <python:None>`, which behaves as ``'follow'``.

        Accepts:

          * ``'follow'`` (default) - automatically follow redirects
          * ``'error'`` - abort with an error if a redirect occurs
          * ``'manual'`` - caller intends to process the response in another context

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._redirect

    @redirect.setter
    def redirect(self, value):
        if not value:
            self._redirect = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['follow', 'error', 'manual']:
                raise errors.HighchartsValueError(f'redirect expects either "follow", '
                                                  f'"error", or "manual". Received: '
                                                  f'"{value}"')

            self._redirect = value

    @property
    def referrer(self) -> Optional[str]:
        """A string specifying the referrer of the request. This can be a same-origin URL,
        ``'about:client'``, or an empty string. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._referrer

    @referrer.setter
    def referrer(self, value):
        if value is None:
            self._referrer = None
        else:
            value = validators.string(value, allow_empty = True)
            if not value:
                value = ''

            self._referrer = value

    @property
    def referrer_policy(self) -> Optional[str]:
        """Specifies the referrer policy to use for the request. Defaults to
        :obj:`None <python:None>`.

        Accepts:

          * ``'no-referrer'``
          * ``'no-referrer-when-downgrade'``
          * ``'same-origin'``
          * ``'origin'``
          * ``'strict-origin'``
          * ``'origin-when-cross-origin'``
          * ``'strict-origin-when-cross-origin'``
          * ``'unsafe-url'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._referrer_policy

    @referrer_policy.setter
    def referrer_policy(self, value):
        if not value:
            self._referrer_policy = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['no-referrer',
                             'no-referrer-when-downgrade',
                             'same-origin',
                             'origin',
                             'strict-origin',
                             'origin-when-cross-origin',
                             'strict-origin-when-cross-origin',
                             'unsafe-url']:
                raise errors.HighchartsValueError(f'referrer_policy received an '
                                                  f'unrecognized value: "{value}"')

    @property
    def integrity(self) -> Optional[str]:
        """The subresource integrity value of the request (e.g.
        ``'sha256-BpfBw7ivV8q2jLiT13fxDYAe2tJllusRSZ273h2nFSE='``). Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._integrity

    @integrity.setter
    def integrity(self, value):
        self._integrity = validators.string(value, allow_empty = True)

    @property
    def keepalive(self) -> Optional[bool]:
        """If ``True``, the request can outlive the page (client context) which made the
        fetch request. Defaults to :obj:`None <python:None>`, which behaves as ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._keepalive

    @keepalive.setter
    def keepalive(self, value):
        if value is None:
            self._keepalive = None
        else:
            self._keepalive = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'url': as_dict.get('url', None),
            'method': as_dict.get('method', None),
            'headers': as_dict.get('headers', None),
            'body': as_dict.get('body', None),
            'mode': as_dict.get('mode', None),
            'credentials': as_dict.get('credentials', None),
            'cache': as_dict.get('cache', None),
            'redirect': as_dict.get('redirect', None),
            'referrer': as_dict.get('referrer', None),
            'referrer_policy': as_dict.get('referrerPolicy', None),
            'integrity': as_dict.get('integrity', None),
            'keepalive': as_dict.get('keepalive', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'url': self.url,
            'method': self.method,
            'headers': self.headers,
            'body': self.body,
            'mode': self.mode,
            'credentials': self.credentials,
            'cache': self.cache,
            'redirect': self.redirect,
            'referrer': self.referrer,
            'referrerPolicy': self.referrer_policy,
            'integrity': self.integrity,
            'keepalive': self.keepalive,
        }

        return untrimmed
