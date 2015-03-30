Django CMS Bootstrap Columns
============================
Django CMS Bootstrap Columns is a plugin for Django CMS [http://djangocms.org]
and aims to provide the Twitter Bootstrap [http://getbootstrap] grid system for 
Django CMS.

Currently this package provides three plugins:
- Bootstrap Container
- Bootstrap Row
- Bootstrap Column

Bootstrap Container 
-------------------
This plugin generates a basic div to act as the bootstrap container. The
container provides the following options:
- Title - Just a name for the plugin
- Classes - allows additional classes to be added
- Element ID - allows users to add id attributes
- Element Style - allows users to add the style attribute and inline styles
- Is Fluid - a boolean which swaps between container and container-fluid
This plugin can be put inside any other plugin (allows any parent), but can
only have Bootstrap Row Plugins placed inside of it (as child plugins).

Bootstrap Row
-------------
This plugin generates a div that acts as a bootstrap row. The row provides the
following options:
- Title - Just a name for the plugin
- Classes - allows additional classes to be added
- Element ID - allows users to add id attributes
- Element Style - allows users to add the style attribute and inline styles
This plugin can be put inside any other plugin (allows any parent), but can
only have Bootstrap Column Plugins placed inside of it (as child plugins).

Bootstrap Column
----------------
This pluging enerates a div that acts as bootstrap column (col-). The column
provides the following options:
- Title - Just a name for the plugin
- Classes - allows additional classes to be added
- Element ID - allows users to add id attributes
- Element Style - allows users to add the style attribute and inline styles
- Mobile/Small/Medium/Large Device Width - Uses a dropdown/choice field select
  a value between 0 - 12. This value affects the width of the column. Example:
  if you set Mobile Device Width to 4/12, the column will generate with 
  col-xs-4.
- Hide on Mobile/Small/Medium/Large adds the bootstrap class ```hidden_$1```
- Mobile/Small/Medium/Large Offset - Sets bootstarp offset values
- Mobile/Small/Medium/Large Pull - Sets bootstarp pull values
- Mobile/Small/Medium/Large Push - Sets bootstarp push values
