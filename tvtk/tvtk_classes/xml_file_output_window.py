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

from tvtk.tvtk_classes.file_output_window import FileOutputWindow


class XMLFileOutputWindow(FileOutputWindow):
    """
    XMLFileOutputWindow - XML File Specific output window class
    
    Superclass: FileOutputWindow
    
    Writes debug/warning/error output to an XML file. Uses prefined XML
    tags for each text display method. The text is processed to replace
    XML markup characters.
    
    
      display_text - <Text>
    
    
      display_error_text - <Error>
    
    
      display_warning_text - <Warning>
    
    
      display_generic_warning_text - <_generic_warning>
    
    
      display_debug_text - <Debug>
    
    The method display_tag outputs the text unprocessed. To use this
    class, instantiate it and then call set_instance(this).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLFileOutputWindow, obj, update, **traits)
    
    def display_tag(self, *args):
        """
        V.display_tag(string)
        C++: virtual void DisplayTag(const char *)
        Put the text into the log file without processing it.
        """
        ret = self._wrap_call(self._vtk_obj.DisplayTag, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('flush', 'GetFlush'), ('reference_count',
    'GetReferenceCount'), ('file_name', 'GetFileName'), ('append',
    'GetAppend'))
    
    _full_traitnames_list_ = \
    (['append', 'debug', 'flush', 'global_warning_display', 'file_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLFileOutputWindow, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLFileOutputWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['append', 'flush'], [], ['file_name']),
            title='Edit XMLFileOutputWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLFileOutputWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            
