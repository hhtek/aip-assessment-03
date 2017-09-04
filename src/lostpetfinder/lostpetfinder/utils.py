"""
User's defined functions or classes used for projects.
"""

import random, string
from django.conf import settings

"""
django.utils.text.slugify
Converts to ASCII if allow_unicode is False (default).
Converts spaces to hyphens.
Removes characters that aren’t alphanumerics, underscores, or hyphens.
Converts to lowercase. Also strips leading and trailing whitespace.
"""
from django.utils.text import slugify

DONT_USE = ['create']
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    """
    Random string generator
    e.g.
    >>> random_string_generator()
    'vpbnwbtk4h'
    >>> random_string_generator(50)
    'il6i3wek0enssekvxqdr8q24qk11sk0jeq9c23qutzdqv1dlin'
    Source: http://joincfe.com/blog/random-string-generator-in-python/
    """
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    Unique slug generator for django
    Source: http://joincfe.com/blog/a-unique-slug-generator-for-django/
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    if slug in DONT_USE:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

# Activation key generator
SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 35)
def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
