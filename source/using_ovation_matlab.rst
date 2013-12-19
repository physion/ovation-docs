***************************
Using the Matlab client API
***************************

The Ovation Matlab API wraps the Ovation Java API for use with the Matlab(r) Technical Computing Environment. Through this API, Matlab users can access the full functionality of the Ovation ecosystem.

*Matlab is a registered trademark of The MathWorks*.

Requirements
============

* Matlab 2012b or later

Installation
============

1. `Download <https://github.com/physion/ovation-matlab/releases>`_ or clone the Ovation Matlab API
2. Add the folder containing `+ovation/` to the Matlab path.
3. Windows users must start Matlab as an Administrator the *first* time using Ovation. OS X and Linux users will be prompted for their system administrator password during first run.


Usage
=====


1. Load the Ovation package::

    >>> import ovation.*
    
2. Open a new `DataContext` with the `NewDataContext` function::

    >>> context = NewDataContext();
