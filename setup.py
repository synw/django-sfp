from setuptools import setup
from sfp import __version__

setup(
    name='django-sfp',
    version=__version__,
    description="Serve static pages for a Vuejs frontend",
    long_description=open('README.md').read(),
    author_email='synwe@yahoo.com',
    url='https://github.com/synw/django-sfp',
    license='MIT',
    packages=['sfp'],
    include_package_data=True,
    package_data={'': ['README.md']},
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=["graphene"],
)
