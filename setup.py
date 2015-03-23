from setuptools import setup, find_packages
import os
import cmsplugin_bootstrap_columns

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
]

setup(
    author="Jeremy Spencer",
    author_email="jeremytiki@gmail.com",
    name='djangocms-bootstrap-columns',
    version=cmsplugin_bootstrap_columns.__version__,
    description='Adds three plugins (container, row, columns) for Twitter Bootstrap',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    url='https://github.com/jtiki/djnagocms_plugin_bootstrap_columns',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
