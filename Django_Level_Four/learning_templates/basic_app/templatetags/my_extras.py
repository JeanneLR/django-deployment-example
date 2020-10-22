# we created this file in level 4 lesson 8 Template Filters
from django import template

register = template.Library()

@register.filter(name='cut') # using decorators to register custom filters.
# custome filter catted cut
def cut(value,arg):
	"""
	This cuts values of "arg" from the string!
	"""
	return value.replace(arg,'')

# now we register the filter.
#register.filer('cut',cut) 
# the first 'cut' is a string that we call this filter
# which is called in the custom template tag.

# the second cut is a direct call on the function.