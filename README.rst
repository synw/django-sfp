Django Sfp
==========

|version| |license|

Serve flat pages from templates. Advantages:

* No database hits
* Keep your pages in a version control system

Installation
------------

Install the latest release with pip:

``pip install django-sfp``

Configuration
-------------

1. Add ``sfp`` to your ``INSTALLED_APPS``.
2. Add ``sfp.middleware.SfpFallbackMiddleware`` to your
   ``MIDDLEWARE`` settings.
3. Create a ``pages`` template directory. This should be a
   subdirectory of one of the templates in your ``TEMPLATES`` setting. Any
   templates you include here (except for a ``base.html``) will get served as
   a static page.

For example, assuming your project-level template directory is named
"templates", then:

* The url ``/about/`` will render ``templates/pages/about.html``
* The url ``/about/team/`` will render ``templates/pages/about/team.html``

Settings
--------

To serve ``pages/index.html`` as homepage use this setting:

``SFP_HANDLE_HOMEPAGE = True``

Edit pages online
-----------------

To edit pages at runtime you can use `django-dirtyedit <https://github.com/synw/django-dirtyedit>`_

.. |version| image:: http://img.shields.io/pypi/v/django-sfp.svg?style=flat-square
    :alt: Current Release
    :target: https://pypi.python.org/pypi/django-sfp/

.. |license| image:: http://img.shields.io/pypi/l/django-sfp.svg?style=flat-square
    :alt: License
    :target: https://pypi.python.org/pypi/django-sfp/
