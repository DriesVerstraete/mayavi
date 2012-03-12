# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui import api as traitsui

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk

from tvtk.tvtk_classes.area_layout_strategy import AreaLayoutStrategy


class TreeMapLayoutStrategy(AreaLayoutStrategy):
    """
    TreeMapLayoutStrategy - abstract superclass for all tree map
    layout strategies
    
    Superclass: AreaLayoutStrategy
    
    All subclasses of this class perform a tree map layout on a tree.
    This involves assigning a rectangular region to each vertex in the
    tree, and placing that information in a data array with four
    components per tuple representing (Xmin, Xmax, Ymin, Ymax).
    
    Instances of subclasses of this class may be assigned as the layout
    strategy to TreeMapLayout
    
    Thanks:
    
    Thanks to Brian Wylie and Ken Moreland from Sandia National
    Laboratories for help developing this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTreeMapLayoutStrategy, obj, update, **traits)
    
    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('shrink_percentage', 'GetShrinkPercentage'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'shrink_percentage'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TreeMapLayoutStrategy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TreeMapLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['shrink_percentage']),
            title='Edit TreeMapLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TreeMapLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            
