#!/usr/bin/env python
# coding: utf-8

# # dropdown admonition bug demo
# 
# When I include an image in a dropdown admonition, it only collapses down to the fixed image size.

# ````{admonition} Click here!
# :class: dropdown
# Here is an image. The dropdown menu only collapsed by the height of the test.
# ```{image} image.png
# :width: 300px
# ```
# Here is some more text for demonstration.
# 
# And some more text for demonstration.
# 
# And some more text for demonstration.
# 
# And some more text for demonstration.
# 
# And some more text for demonstration.
# ````

# ````{admonition} Click here!
# :class: dropdown
# Here is a figure. The dropdown menu collapsed all the way.
# ```{figure} image.png
# ---
# width: 300px
# ```
# ````
