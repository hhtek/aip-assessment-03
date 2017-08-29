# Lost Pet Finder

TODO: Write a project description

## Table of Contents
1. [Implementation](#implementation)
1. [Contributing](#contributing)
1. [Coding Standards](#coding-standards)
1. [History](#history)
1. [References](#references)
1. [License](#license)

## Implementation

### Dependencies

TODO: Describe the depenencies list, package requirements

### Installation

OS : Linux Ubuntu
Front-end Framework : Bootstrap
Back-end Framework : Django
Database : Mysql

### Usage

TODO: Write usage instructions

### API
TODO: List of APIs which are used in the project.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

**[Back to top](#table-of-contents)**

## Coding Standards

Describe the coding styles which are used in the project for readability and code maintenance.

### Python

Reference: https://www.python.org/dev/peps/pep-0008/

1. Indentation using SPACES with the size of 4
    ```python
    urlpatterns = [
        url(r'^$', PetListV iew.as_view(), name='list'),
        url(r'^register/$', PetCreateView.as_view(), name='create'),
        url(r'^(?P<pk>\d+)/edit/$', PetUpdateView.as_view(), name='update'),
        url(r'^(?P<pk>\d+)/$', PetDetailView.as_view(), name='detail'),
    ]
    ```

1. Use single quote for STRING
    ```python
    context['title'] = 'Update Pet'
    template_name = 'pet-form.html'
    ```

1. Use trailing comma when listing the values, importing libraries line by line. For clarity, it is recommended to surround the latter line in (technically redundant) parentheses.
    ```python
    PET_CHOICES = (
        ('Cat', 'Cat'),
        ('Dog', 'Dog'),
    )
    # Django class base views
    from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
    )
    ```
1. Tuple declaration<br/>
    Tubple declaration with all CAPITAL LETTERS
    ```python
     PET_CHOICES = (
         ('Cat', 'Cat'),
         ('Dog', 'Dog'),
     )
    ```
2. Use triple quote comment for group declarations such as list/tuple , fields, or multiple lines comment.
    ```python
    """
    Pre-defined TUPLES
    Tubple declaration with all CAPITAL LETTERS.
    """
    ```
3. Imported libraries are categorised, sorted in alphabetical order, and separated by an empty line.<br/>
    Below is an example of grouping django's libraries, and project's libraries/functions
    ```python
    from django.conf import settings
    from django.core.urlresolvers import reverse
    from django.db import models
    from django.db.models.signals import pre_save, post_save

    from lostpetfinder.utils import unique_slug_generator
    ```
### HTML & CSS

Reference: https://google.github.io/styleguide/htmlcssguide.html

1. Use a new line for every block, list, or table element, and indent every such child element.<br/>
	Independent of the styling of an element (as CSS allows elements to assume a different role per display property), put every block, list, or table element on a new line.<br/>
	Also, indent them if they are child elements of a block, list, or table element.<br/>
	```
	<blockquote>
	<p><em>Space</em>, the final frontier.</p>
	</blockquote>
	```
	```
	<ul>
	<li>Moe
	<li>Larry
	<li>Curly
	</ul>
	```
	```
	<table>
	<thead>
		<tr>
		<th scope="col">Income
		<th scope="col">Taxes
	<tbody>
		<tr>
		<td>$ 5.00
		<td>$ 4.50
	</table>
	```

1. HTML Quotation Marks.<br/>	
	When quoting attributes values, use double quotation marks.<br/>
	Use double ("") rather than single quotation marks ('') around attribute values.<br/>
	```
	<a class="maia-button maia-button-secondary">Sign in</a>	
	```

1.  CSS Validity<br/>
	Use valid CSS where possible.<br/>
	Unless dealing with CSS validator bugs or requiring proprietary syntax, use valid CSS code.	<br/>
	
1.  ID and Class Name Style<br/>
	Use ID and class names that are as short as possible but as long as necessary.<br/>
	Try to convey what an ID or class is about while being as brief as possible.<br/>
	```
	#nav {}
	.author {}
	```

1. CSS Declaration Order<br/>
	Alphabetize declaration	
	```
	background: fuchsia;
	border: 1px solid;
	-moz-border-radius: 4px;
	-webkit-border-radius: 4px;
	border-radius: 4px;
	color: black;
	text-align: center;
	text-indent: 2em;
	```
	
1. Block Content Indentation</br>
	Indent all block content.
	```	
	@media screen, projection {
		html {
			background: #fff;
			color: #444;
		}
	}
	```
	
### JavaScript

Reference: https://www.w3schools.com/js/js_conventions.asp

1. 	Variable Names<br/>
	All names start with a letter.
	```	
	firstName = "John";
	lastName = "Doe";
	```	

1.	Spaces Around Operators<br/>
	Always put spaces around operators ( = + - * / ), and after commas
	```	
	var x = y + z;
	var values = ["Volvo", "Saab", "Fiat"];
	```

1.	Code Indentation<br/>
	4 spaces for indentation of code blocks
	```	
	function toCelsius(fahrenheit) {
		return (5 / 9) * (fahrenheit - 32);
	}
	```	
**[Back to top](#table-of-contents)**

## History

TODO: Write history

**[Back to top](#table-of-contents)**

## References

TODO: List of references which are used in this project

**[Back to top](#table-of-contents)**

## License

TODO: Write license

**[Back to top](#table-of-contents)**
