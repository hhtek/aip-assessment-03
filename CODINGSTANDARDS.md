# Coding Standards

<p>The application is mainly written in Python programming language, and follow
follow coding standards for ease of readability and code maintenance.</p>

<p>Refer to [README](README.md) for application implementation details.</p>


## Table of Contents
1. [Python](#python)
1. [HTML and CSS](#html-and-css)
1. [JavaScript](#javascript)

## Python

Reference: https://www.python.org/dev/peps/pep-0008/

1. Indentation using SPACES with the size of 4.
    ```python
    urlpatterns = [
        url(r'^$', PetListV iew.as_view(), name='list'),
        url(r'^register/$', PetCreateView.as_view(), name='create'),
        url(r'^(?P<pk>\d+)/edit/$', PetUpdateView.as_view(), name='update'),
        url(r'^(?P<pk>\d+)/$', PetDetailView.as_view(), name='detail'),
    ]
    ```

1. Use single quote for STRING.
    ```python
    context['title'] = 'Update Pet'
    template_name = 'pet-form.html'
    ```
1. Use double quote for long STRING.
    ```python
    long_string = "This is a long string"
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
1. Use triple quote comment for group declarations such as list/tuple , fields or multiple lines comment.
    ```python
    """
    Pre-defined TUPLES
    Tubple declaration with all CAPITAL LETTERS.
    """
    ```

1. Each class or function have triple quote comment within and beginning of their code block.
    ```python
    class PetDetailView(DetailView):
        """
        Get specific pet details
            GET /finder/pets/slug/
        """
        def get_queryset(self):
            """
            Get specific pet based on pet's slug
            """
            slug = self.kwargs.get('slug')
            return Pet.objects.filter(slug=slug)    
    ```
1. Imported libraries are categorised, sorted in alphabetical order, and separated by an empty line.<br/>
    Below is an example of grouping django's libraries, and project's libraries/functions
    ```python
    from django.conf import settings
    from django.core.urlresolvers import reverse
    from django.db import models
    from django.db.models.signals import pre_save, post_save

    from lostpetfinder.utils import unique_slug_generator
    ```

1. HTML template has multiline comment using django multiline comment block
`{% comment %}{% endcomment %}`. The block needs to be placed after django template
tag `{% extends ... %}`.
    ```
    {% extends "base.html" %}

    {% comment %}
      File name: pet_list.html
      Description: the HTML file used to display a list of pets
                   which are used for the views of lost/found pets and user's pets.
      Note: this comment block needs to be after the template tag {% extends ... %}.
    {% endcomment %}

    {% load static %}

    {% block head_title %}{{ title }} || {{ block.super }}{% endblock head_title %}
    ```

**[Back to top](#table-of-contents)**    

## HTML and CSS

Reference: https://google.github.io/styleguide/htmlcssguide.html

1. Use a new line for every block, list, or table element, and indent every such child element.<br/>
  * Independent of the styling of an element (as CSS allows elements to assume a different role per display property), put every block, list, or table element on a new line.
  * Also, indent them if they are child elements of a block, list, or table element.
  * Use 2 spaces indentation for HTML and 4 spaces indentation for CSS.
	```
  	<blockquote>
    	<p><em>Space</em>, the final frontier.</p>
  	</blockquote>
	```
	```
  	<ul>
    	<li>Moe</li>
    	<li>Larry</li>
    	<li>Curly</li>
  	</ul>
	```
  ```
    <table>
      <thead>
        <tr>
        <th scope="col">Income</th>
        <th scope="col">Taxes</th>
        </tr>
      </thead>
      <tbody>
        <tr>
        <td>$ 5.00</td>
        <td>$ 4.50</td>
        </tr>
      </tbody>
    </table>
  ```

1. HTML Quotation Marks.
  * When quoting attributes values, use double quotation marks ("") rather than
  single quotation marks ("")
  ```
    <a class="maia-button maia-button-secondary">
      Sign in
    </a>
  ```

1. CSS Validity
  * Use valid CSS where possible.
  * Unless dealing with CSS validator bugs or requiring proprietary syntax, use valid CSS code.

1. ID and Class Name Style
  * Use ID and class names that are as short as possible but as long as necessary.
  * Try to convey what an ID or class is about while being as brief as possible.
  * Use 4 spaces indentation within curly bracket code block for readability.
  ```
    .card-title {
        color: #283593;
    }
  ```

1. CSS Declaration Order
  * Alphabetise declaration
  ```
    .class-example {
        background: fuchsia;
        border: 1px solid;
        border-radius: 4px;
        color: black;
        -moz-border-radius: 4px;
        text-align: center;
        text-indent: 2em;
        -webkit-border-radius: 4px;
    }
  ```

1. Block Content Indentation
  * Indent all block content with 4 spaces.
	```
  	@media screen, projection {
    		html {
      			background: #fff;
      			color: #444;
    		}
  	}
	```

**[Back to top](#table-of-contents)**

## JavaScript

Reference: https://www.w3schools.com/js/js_conventions.asp

1. 	Variable Names
  * All names start with a letter.

  ```javascript
  	firstName = "John";
  	lastName = "Doe";
  ```

1.	Spaces Around Operators
	Always put spaces around operators ( = + - * / ), and after commas
	```javascript
  	var x = y + z;
  	var values = ["Volvo", "Saab", "Fiat"];
	```

1.	Code Indentation
  * Use 2 spaces for indentation of code blocks

	```javascript
  	function toCelsius(fahrenheit) {
  		return (5 / 9) * (fahrenheit - 32);
  	}
	```

**[Back to top](#table-of-contents)**
