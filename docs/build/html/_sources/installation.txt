Installation
============

DjangoCMS Bootstrap Columns only requires the base DjagnoCMS 3.0 installation.
Django CMS installation instructions can be found `here <https://www.django-cms.org/en/>`_.

Once DjangCMS is installed DjangoCMS Bootstrap Columns can be installed as
well. First download the project and add it to your pythong path. This can be
accomplished like so: ::

    $ pip install djangocms-bootstrap-columns

Now the project should be installed correctly. Next you will need to add the
project to  your Djagno Project: ::

    project/settings.py

    ...
    INSTALLED_APPS = (
    ...
    'cmsplugin_bootstrap_columns',
    ...)

Make sure to have twitter bootstrap linking to your page as a CSS stylesheet.::

    <head>
    ...
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
    ...
    </head>


Reload your server. Now DjangoCMS Bootstrap Columns should start showing in
your plugins dropdown.
