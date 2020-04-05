# AffineVi

AffineVi is a module for visualization of affine transformations in 2-dimensional Euclidean space.

9 transformations are supported:
- Identity
- Translation
- Scaling
- Rotation
- Shearing in x and y directions
- Reflection about origin, x-axis, and y-axis

<center>
  <img src = "images/affine-transformations.gif", height = "700"></img>
</center>

## Installation

AffineVi can be installed with

```
pip install git+https://github.com/MinNq/affinevi.git#egg=affine
```

NumPy and Matplotlib modules are required. You also need to install [ImageMagick](https://imagemagick.org/index.php) as a gif writer.

## Functions

### affinevi.ShowAffineTransformations

```python
ShowTransformations(data, gif_length = 1, fps = 60)
```

This function creates a gif with affine transformations applied to given data.

**Parameters:**
- `data`: *array_like*. Coordinates in 2-d Cartesian space.
- `gif_length`: *int or float*. Length of ouput gif in second. 
- `fps`: *int*. Frame rate of output gif.

**Example**

```python
>>> import numpy as np
>>> from affinevi.Visualize import *
>>> Data = np.random.rand(20,2)
>>> ShowTransformations(Data)
```
<center>
  <img src = "images/affine-transformations.gif", height = "700"></img>
</center>
