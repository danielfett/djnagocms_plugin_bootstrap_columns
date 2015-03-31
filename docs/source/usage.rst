Usage
=====

DjagnoCMS Bootstrap Columns main purpose is to provide a quick and easy way to
create dynamic layouts using Twitter Bootstrap. The project provides the
following plugins:

* Bootstrap Container
* Bootstrap Row
* Bootstrap Columns

If you are familar with Twitter Bootstrap these three plugins line up perfectly
with .container (.container-fluid), .row, and .col-*. If you are unfamilar with
Twitter Bootstrap read the documenation `here <http://getbootstrap.com>`_.

Each plugin is very flexible allowing users to add multiple extra classes,
attributes, and styles.

Bootstrap Container
-------------------
Bootstrap Container can be placed directly inside of Placeholder objects.
Additionally this plugin has the following options:

* **Title** - The name that shows in for plugin rendering.
* **Classes** - Additionally CSS classes can be added in this box to render the
  element.
* **Element ID's** - Additional Elemnt ID's (<div id="...") to be rendered with 
  this plugin
* **Element Style** = Additional HTML styles to be rendered with this plugin
  (<div style="...").
* **Is Fluid** - Toggles the container class between .container and
  .container-fluid

Bootstrap Row
-------------
Bootstrap Row can be placed directly inside of a Placeholder object or inside
of Bootstrap Container plugins. Bootstrap Row also has the following options:

* **Title** - The name that shows in for plugin rendering.
* **Classes** - Additionally CSS classes can be added in this box to render the
  element.
* **Element ID's** - Additional Elemnt ID's (<div id="...") to be rendered with 
  this plugin
* **Element Style** = Additional HTML styles to be rendered with this plugin
  (<div style="...").


Bootstrap Column
----------------
Bootstrap Column can only be placed inside of Bootstrap Container plugins. 
Bootstrap Column also has the following options:

* **Title** - The name that shows in for plugin rendering.
* **Mobile/Small/Medium/Large** Device Width - These options corrispond with
  col-xs/sm/md/lg-* in Twitter Bootstrap. These options provide a 0-12 option
  that renders into the sizing for the column.
* **Classes** - Additionally CSS classes can be added in this box to render the
  element.
* **Element ID's** - Additional Elemnt ID's (<div id="...") to be rendered with 
  this plugin
* **Element Style** = Additional HTML styles to be rendered with this plugin
  (<div style="...").
* **Hide on Mobile** - Hides the element on devices with a resolution less
  than 768px.
* **Hide on Small** - Hides the element on devices with a resolution
  between 768px - 992px
* **Hide on Medium** - Hides the element on devices with a resolution
  between 992px - 1200px
* **Hide on Large** - Hides the element on devices with a resolution larger
  than 1200px.
* **Mobile/Small/Medium/Large Device Offset** - Applies offset-xs/sm/md/lg-* to the
  rendered element.
* **Mobile/Small/Medium/Large Device Pull** - Applies pull-xs/ms/md/lg-* to the
  rendered element.
