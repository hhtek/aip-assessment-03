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

TODO: Describe the installation process

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
### HTML

### JavaScript

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
