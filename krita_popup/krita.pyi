from typing import Protocol, List, Never
from PyQt5.QtCore import QObject, QUuid, QByteArray, QRect, QVariant, QPointF, QRectF, QPoint, pyqtSignal
from PyQt5.QtGui import QColor, QImage, QTransform, QIcon
from PyQt5.QtWidgets import QDockWidget, QMainWindow, QWidget, QAction

KoCanvasBase = Never
KisNodeSP = Never
KisLayerSP = Never
KoChannelInfo = Never
KisImage = Never
KisImageSP = Never
KisCloneLayerSP = Never
DockPosition = Never
KisDocument = Never
KisFileLayerSP = Never
KisColorizeMaskSP = Never
KisFilterMaskSP = Never
KisFilterConfigurationSP = Never
KisGeneratorLayerSP = Never
KisAdjustmentLayerSP = Never
KisGroupLayerSP = Never
KisShapeGroupSP = Never
KoShapeGroup = Never
KoColor = Never
KoResourceSP = Never
KisPropertiesConfigurationSP = Never
KisSelectionSP = Never
KisSelectionMaskSP = Never
KoShape = Never
KisTransformMaskSP = Never
KisTransparencyMaskSP = Never
KoShapeControllerBase = Never
KisView = Never
KisShapeLayerSP = Never
KisMainWindow = Never
KoCanvasObserverBase = Never
KoDockFactoryBase = Never
KisPresetChooser = Never

class Canvas(QObject):

  """
    
    
    [Canvas](https://api.kde.org/krita/html/classCanvas.html) wraps the canvas inside a view on an image/document. It is responsible for the view parameters of the document: zoom, rotation, mirror, wraparound and instant preview.
  """

  def __init__(self, canvas: KoCanvasBase, parent: QObject = None) -> None:
  
    ...
  

  def zoomLevel(self) -> "float":
    """
      
      
      # Returns
      
      the current zoomlevel. 1.0 is 100%.
    """
    ...
  

  def setZoomLevel(self, value: float) -> "None":
    """
      setZoomLevel set the zoomlevel to the given `value`. 1.0 is 100%.
    """
    ...
  

  def resetZoom(self) -> "None":
    """
      resetZoom set the zoomlevel to 100%
    """
    ...
  

  def rotation(self) -> "float":
    """
      
      
      # Returns
      
      the rotation of the canvas in degrees.
    """
    ...
  

  def setRotation(self, angle: float) -> "None":
    """
      setRotation set the rotation of the canvas to the given
      
      # Parameters
      
      - angle: float
      
        in degrees.
    """
    ...
  

  def resetRotation(self) -> "None":
    """
      resetRotation reset the canvas rotation.
    """
    ...
  

  def mirror(self) -> "bool":
    """
      
      
      # Returns
      
      return true if the canvas is mirrored, false otherwise.
    """
    ...
  

  def setMirror(self, value: bool) -> "None":
    """
      setMirror turn the canvas mirroring on or off depending on
      
      # Parameters
      
      - value: bool
    """
    ...
  

  def wrapAroundMode(self) -> "bool":
    """
      
      
      # Returns
      
      true if the canvas is in wraparound mode, false if not. Only when OpenGL is enabled, is wraparound mode available.
    """
    ...
  

  def setWrapAroundMode(self, enable: bool) -> "None":
    """
      setWrapAroundMode set wraparound mode to
      
      # Parameters
      
      - enable: bool
    """
    ...
  

  def levelOfDetailMode(self) -> "bool":
    """
      
      
      # Returns
      
      true if the canvas is in Instant Preview mode, false if not. Only when OpenGL is enabled, is Instant Preview mode available.
    """
    ...
  

  def setLevelOfDetailMode(self, enable: bool) -> "None":
    """
      setLevelOfDetailMode sets Instant Preview to
      
      # Parameters
      
      - enable: bool
    """
    ...
  

  def view(self) -> "View":
    """
      
      
      # Returns
      
      the view that holds this canvas
    """
    ...
  

class Channel(QObject):

  """
    
    
    A [Channel](https://api.kde.org/krita/html/classChannel.html) represents a single channel in a [Node](https://api.kde.org/krita/html/classNode.html). [Krita](https://api.kde.org/krita/html/classKrita.html) does not use channels to store local selections: these are strictly the color and alpha channels.
  """

  def __init__(self, node: KisNodeSP, channel: KoChannelInfo, parent: QObject = None) -> None:
  
    ...
  

  def visible(self) -> "bool":
    """
      visible checks whether this channel is visible in the node
      
      # Returns
      
      the status of this channel
    """
    ...
  

  def setVisible(self, value: bool) -> "None":
    """
      setvisible set the visibility of the channel to the given value.
    """
    ...
  

  def name(self) -> "str":
    """
      
      
      # Returns
      
      the name of the channel
    """
    ...
  

  def position(self) -> "int":
    """
      
      
      # Returns
      
      the position of the first byte of the channel in the pixel
    """
    ...
  

  def channelSize(self) -> "int":
    """
      
      
      # Returns
      
      the number of bytes this channel takes
    """
    ...
  

  def bounds(self) -> "QRect":
    """
      
      
      # Returns
      
      the exact bounds of the channel. This can be smaller than the bounds of the [Node](https://api.kde.org/krita/html/classNode.html) this channel is part of.
    """
    ...
  

  def pixelData(self, rect: QRect) -> "QByteArray":
    """
      
      
      Read the values of the channel into the a byte array for each pixel in the rect from the [Node](https://api.kde.org/krita/html/classNode.html) this channel is part of, and returns it.
      
      Note that if [Krita](https://api.kde.org/krita/html/classKrita.html) is built with OpenEXR and the [Node](https://api.kde.org/krita/html/classNode.html) has the 16 bits floating point channel depth type, [Krita](https://api.kde.org/krita/html/classKrita.html) returns 32 bits float for every channel; the libkis scripting API does not support half.
    """
    ...
  

  def setPixelData(self, value: QByteArray, rect: QRect) -> "None":
    """
      setPixelData writes the given data to the relevant channel in the [Node](https://api.kde.org/krita/html/classNode.html). This is only possible for Nodes that have a paintDevice, so nothing will happen when trying to write to e.g. a group layer.
      
      Note that if [Krita](https://api.kde.org/krita/html/classKrita.html) is built with OpenEXR and the [Node](https://api.kde.org/krita/html/classNode.html) has the 16 bits floating point channel depth type, [Krita](https://api.kde.org/krita/html/classKrita.html) expects to be given a 4 byte, 32 bits float for every channel; the libkis scripting API does not support half.
      
      # Parameters
      
      - value: QByteArray
      
        a byte array with exactly enough bytes.
      
      - rect: QRect
      
        the rectangle to write the bytes into
    """
    ...
  

class CloneLayer(Node):

  """
    The [CloneLayer](https://api.kde.org/krita/html/classCloneLayer.html) class A clone layer is a layer that takes a reference inside the image and shows the exact same pixeldata.
    
    If the original is updated, the clone layer will update too.
  """

  def __init__(self, image: KisImageSP, name: str, source: KisLayerSP, parent: QObject = None) -> None:
  
    ...
  

  def __init__(self, layer: KisCloneLayerSP, parent: QObject = None) -> None:
    """
      [CloneLayer](https://api.kde.org/krita/html/classCloneLayer.html) function for wrapping a preexisting node into a clonelayer object.
      
      # Parameters
      
      - layer: KisCloneLayerSP
      
        the clone layer
      
      - parent: QObject = `None`
      
        the parent QObject
    """
    ...
  

  def type(self) -> "str":
    """
      type [Krita](https://api.kde.org/krita/html/classKrita.html) has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
      
      # Returns
      
      clonelayer
    """
    ...
  

  def sourceNode(self) -> "Node":
    """
      sourceNode
      
      # Returns
      
      the node the clone layer is based on.
    """
    ...
  

  def setSourceNode(self, node: Node) -> "None":
    """
      setSourceNode
      
      # Parameters
      
      - node: Node
      
        the node to use as the source of the clone layer.
    """
    ...
  

class ColorizeMask(Node):

  """
    The [ColorizeMask](https://api.kde.org/krita/html/classColorizeMask.html) class A colorize mask is a mask type node that can be used to color in line art.
    
    ```
    window = [Krita](https://api.kde.org/krita/html/classKrita.html).[instance](https://api.kde.org/krita/html/classinstance.html)().[activeWindow](https://api.kde.org/krita/html/classactiveWindow.html)()
    doc = [Krita](https://api.kde.org/krita/html/classKrita.html).[instance](https://api.kde.org/krita/html/classinstance.html)().[createDocument](https://api.kde.org/krita/html/classcreateDocument.html)(10, 3, "Test", "RGBA", "U8", "", 120.0)
    window.addView(doc)
    root = doc.[rootNode](https://api.kde.org/krita/html/classrootNode.html)();
    node = doc.createNode("layer", "paintLayer")
    root.[addChildNode](https://api.kde.org/krita/html/classaddChildNode.html)(node, None)
    nodeData = QByteArray.fromBase64(b"AAAAAAAAAAAAAAAAEQYMBhEGDP8RBgz/EQYMAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARBgz5EQYM/xEGDAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEQYMAhEGDAkRBgwCAAAAAAAAAAAAAAAA");
    node.setPixelData(nodeData,0,0,10,3)
    
    cols = [ [ManagedColor](https://api.kde.org/krita/html/classManagedColor.html)('RGBA','U8',''), [ManagedColor](https://api.kde.org/krita/html/classManagedColor.html)('RGBA','U8','') ]
    cols[0].setComponents([0.65490198135376, 0.345098048448563, 0.474509805440903, 1.0]);
    cols[1].setComponents([0.52549022436142, 0.666666686534882, 1.0, 1.0]);
    keys = [
      QByteArray.fromBase64(b"/48AAAAAAAAAAAAAAAAAAAAAAACmCwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"),
      QByteArray.fromBase64(b"AAAAAAAAAACO9ocAAAAAAAAAAAAAAAAAAAAAAMD/uQAAAAAAAAAAAAAAAAAAAAAAGoMTAAAAAAAAAAAA")
      ]
    
    mask = doc.createColorizeMask('c1')
    node.addChildNode(mask,None)
    mask.setEditKeyStrokes(True)
    
    mask.setUseEdgeDetection(True)
    mask.setEdgeDetectionSize(4.0)
    mask.setCleanUpAmount(70.0)
    mask.setLimitToDeviceBounds(True)
    mask.initializeKeyStrokeColors(cols)
    
    for col,key in zip(cols,keys):
      mask.[setKeyStrokePixelData](https://api.kde.org/krita/html/classsetKeyStrokePixelData.html)(key,col,0,0,20,3)
    
    mask.[updateMask](https://api.kde.org/krita/html/classupdateMask.html)()
    mask.[setEditKeyStrokes](https://api.kde.org/krita/html/classsetEditKeyStrokes.html)(False);
    mask.setShowOutput(True);
    ```
  """

  def __init__(self, image: KisImageSP, name: str, parent: QObject = None) -> None:
  
    ...
  

  def __init__(self, image: KisImageSP, mask: KisColorizeMaskSP, parent: QObject = None) -> None:
  
    ...
  

  def type(self) -> "str":
    """
      type [Krita](https://api.kde.org/krita/html/classKrita.html) has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
      
      
      If the [Node](https://api.kde.org/krita/html/classNode.html) object isn't wrapping a valid [Krita](https://api.kde.org/krita/html/classKrita.html) layer or mask object, and empty string is returned.
      
      # Returns
      
      colorizemask
    """
    ...
  

  def keyStrokesColors(self) -> "List[ManagedColor]":
    """
      keyStrokesColors Colors used in the Colorize Mask's keystrokes.
      
      # Returns
      
      a [ManagedColor](https://api.kde.org/krita/html/classManagedColor.html) list containing the colors of keystrokes.
    """
    ...
  

  def initializeKeyStrokeColors(self, colors: List[ManagedColor], transparentIndex: int = -1) -> "None":
    """
      initializeKeyStrokeColors Set the colors to use for the Colorize Mask's keystrokes.
      
      # Parameters
      
      - colors: List[ManagedColor]
      
        a list of [ManagedColor](https://api.kde.org/krita/html/classManagedColor.html) to use for the keystrokes.
      
      - transparentIndex: int = `-1`
      
        index of the color that should be marked as transparent.
    """
    ...
  

  def removeKeyStroke(self, color: ManagedColor) -> "None":
    """
      removeKeyStroke Remove a color from the Colorize Mask's keystrokes.
      
      # Parameters
      
      - color: ManagedColor
      
        a [ManagedColor](https://api.kde.org/krita/html/classManagedColor.html) to be removed from the keystrokes.
    """
    ...
  

  def transparencyIndex(self) -> "int":
    """
      transparencyIndex Index of the transparent color.
      
      # Returns
      
      an integer containing the index of the current color marked as transparent.
    """
    ...
  

  def keyStrokePixelData(self, color: ManagedColor, x: int, y: int, w: int, h: int) -> "QByteArray":
    """
      keyStrokePixelData reads the given rectangle from the keystroke image data and returns it as a byte array. The pixel data starts top-left, and is ordered row-first.
      
      # Parameters
      
      - color: ManagedColor
      
        a [ManagedColor](https://api.kde.org/krita/html/classManagedColor.html) to get keystrokes pixeldata from.
      
      - x: int
      
        x position from where to start reading
      
      - y: int
      
        y position from where to start reading
      
      - w: int
      
        row length to read
      
      - h: int
      
        number of rows to read
      
      # Returns
      
      a QByteArray with the pixel data. The byte array may be empty.
    """
    ...
  

  def setKeyStrokePixelData(self, value: QByteArray, color: ManagedColor, x: int, y: int, w: int, h: int) -> "bool":
    """
      setKeyStrokePixelData writes the given bytes, of which there must be enough, into the keystroke, the keystroke's original pixels are overwritten
      
      # Parameters
      
      - value: QByteArray
      
        the byte array representing the pixels. There must be enough bytes available. [Krita](https://api.kde.org/krita/html/classKrita.html) will take the raw pointer from the QByteArray and start reading, not stopping before (number of channels * size of channel * w * h) bytes are read.
      
      - color: ManagedColor
      
        a [ManagedColor](https://api.kde.org/krita/html/classManagedColor.html) to set keystrokes pixeldata for.
      
      - x: int
      
        the x position to start writing from
      
      - y: int
      
        the y position to start writing from
      
      - w: int
      
        the width of each row
      
      - h: int
      
        the number of rows to write
      
      # Returns
      
      true if writing the pixeldata worked
    """
    ...
  

  def setUseEdgeDetection(self, value: bool) -> "None":
    """
      setUseEdgeDetection Activate this for line art with large solid areas, for example shadows on an object.
      
      # Parameters
      
      - value: bool
      
        true to enable edge detection, false to disable.
    """
    ...
  

  def useEdgeDetection(self) -> "bool":
    """
      useEdgeDetection
      
      # Returns
      
      true if Edge detection is enabled, false if disabled.
    """
    ...
  

  def setEdgeDetectionSize(self, value: float) -> "None":
    """
      setEdgeDetectionSize Set the value to the thinnest line on the image.
      
      # Parameters
      
      - value: float
      
        a float value of the edge size to detect in pixels.
    """
    ...
  

  def edgeDetectionSize(self) -> "float":
    """
      edgeDetectionSize
      
      # Returns
      
      a float value of the edge detection size in pixels.
    """
    ...
  

  def setCleanUpAmount(self, value: float) -> "None":
    """
      setCleanUpAmount This will attempt to handle messy strokes that overlap the line art where they shouldn't.
      
      # Parameters
      
      - value: float
      
        a float value from 0.0 to 100.00 where 0.0 is no cleanup is done and 100.00 is most aggressive.
    """
    ...
  

  def cleanUpAmount(self) -> "float":
    """
      cleanUpAmount
      
      # Returns
      
      a float value of 0.0 to 100.0 representing the cleanup amount where 0.0 is no cleanup is done and 100.00 is most aggressive.
    """
    ...
  

  def setLimitToDeviceBounds(self, value: bool) -> "None":
    """
      setLimitToDeviceBounds Limit the colorize mask to the combined layer bounds of the strokes and the line art it is filling. This can speed up the use of the mask on complicated compositions, such as comic pages.
      
      # Parameters
      
      - value: bool
      
        set true to enabled limit bounds, false to disable.
    """
    ...
  

  def limitToDeviceBounds(self) -> "bool":
    """
      limitToDeviceBounds
      
      # Returns
      
      true if limit bounds is enabled, false if disabled.
    """
    ...
  

  def updateMask(self, force: bool = False) -> "None":
    """
      updateMask Process the Colorize Mask's keystrokes and generate a projection of the computed colors.
      
      # Parameters
      
      - force: bool = `False`
      
        force an update
    """
    ...
  

  def resetCache(self) -> "None":
  
    ...
  

  def showOutput(self) -> "bool":
    """
      showOutput Show output mode allows the user to see the result of the Colorize Mask's algorithm.
      
      # Returns
      
      true if edit show coloring mode is enabled, false if disabled.
    """
    ...
  

  def setShowOutput(self, enabled: bool) -> "None":
    """
      setShowOutput Toggle Colorize Mask's show output mode.
      
      # Parameters
      
      - enabled: bool
      
        set true to enable show coloring mode and false to disable it.
    """
    ...
  

  def editKeyStrokes(self) -> "bool":
    """
      editKeyStrokes Edit keystrokes mode allows the user to modify keystrokes on the active Colorize Mask.
      
      # Returns
      
      true if edit keystrokes mode is enabled, false if disabled.
    """
    ...
  

  def setEditKeyStrokes(self, enabled: bool) -> "None":
    """
      setEditKeyStrokes Toggle Colorize Mask's edit keystrokes mode.
      
      # Parameters
      
      - enabled: bool
      
        set true to enable edit keystrokes mode and false to disable it.
    """
    ...
  

class DockWidget(QDockWidget, KoCanvasObserverBase):

  """
    
    
    [DockWidget](https://api.kde.org/krita/html/classDockWidget.html) is the base class for custom Dockers. Dockers are created by a factory class which needs to be registered by calling Application.addDockWidgetFactory:
    
    ```
    class HelloDocker(DockWidget):
     def __init__(self):
      super().__init__()
      label = QLabel("Hello", self)
      self.setWidget(label)
      self.label = label
      self.setWindowTitle("Hello Docker")
    
    def canvasChanged(self, canvas):
      self.label.setText("Hellodocker: canvas changed");
    
    Application.addDockWidgetFactory(DockWidgetFactory("hello", DockWidgetFactoryBase.DockRight, HelloDocker))
    ```
    
    One docker per window will be created, not one docker per canvas or view. When the user switches between views/canvases, canvasChanged will be called. You can override that method to reset your docker's internal state, if necessary.
  """

  def __init__(self) -> None:
  
    ...
  

class DockWidgetFactoryBase(KoDockFactoryBase):

  """
    The [DockWidgetFactoryBase](https://api.kde.org/krita/html/classDockWidgetFactoryBase.html) class is the base class for plugins that want to add a dock widget to every window. You do not need to implement this class yourself, but create a [DockWidget](https://api.kde.org/krita/html/classDockWidget.html) implementation and then add the DockWidgetFactory to the [Krita](https://api.kde.org/krita/html/classKrita.html) instance like this:
    
    ```
    class HelloDocker(DockWidget):
     def __init__(self):
      super().__init__()
      label = QLabel("Hello", self)
      self.setWidget(label)
      self.label = label
    
    def canvasChanged(self, canvas):
      self.label.setText("Hellodocker: canvas changed");
    
    Application.addDockWidgetFactory(DockWidgetFactory("hello", DockWidgetFactoryBase.DockRight, HelloDocker))
    ```
  """

  def __init__(self, _id: str, _dockPosition: DockPosition) -> None:
  
    ...
  

  def id(self) -> "str":
  
    ...
  

  def defaultDockPosition(self) -> "DockPosition":
  
    ...
  

class Document(QObject):

  """
    
    
    The [Document](https://api.kde.org/krita/html/classDocument.html) class encapsulates a [Krita](https://api.kde.org/krita/html/classKrita.html) Document/Image. A [Krita](https://api.kde.org/krita/html/classKrita.html) document is an Image with a filename. Libkis does not differentiate between a document and an image, like [Krita](https://api.kde.org/krita/html/classKrita.html) does internally.
  """

  def __init__(self, document: KisDocument, ownsDocument: bool, parent: QObject = None) -> None:
  
    ...
  

  def horizontalGuides(self) -> "List[float]":
    """
      horizontalGuides The horizontal guides.
      
      # Returns
      
      a list of the horizontal positions of guides.
    """
    ...
  

  def verticalGuides(self) -> "List[float]":
    """
      verticalGuides The vertical guide lines.
      
      # Returns
      
      a list of vertical guides.
    """
    ...
  

  def guidesVisible(self) -> "bool":
    """
      guidesVisible Returns guide visibility.
      
      # Returns
      
      whether the guides are visible.
    """
    ...
  

  def guidesLocked(self) -> "bool":
    """
      guidesLocked Returns guide lockedness.
      
      # Returns
      
      whether the guides are locked.
    """
    ...
  

  def clone(self) -> "Document":
    """
      clone create a shallow clone of this document.
      
      # Returns
      
      a new [Document](https://api.kde.org/krita/html/classDocument.html) that should be identical to this one in every respect.
    """
    ...
  

  def batchmode(self) -> "bool":
    """
      
      
      Batchmode means that no actions on the document should show dialogs or popups.
      
      # Returns
      
      true if the document is in batchmode.
    """
    ...
  

  def setBatchmode(self, value: bool) -> "None":
    """
      
      
      Set batchmode to `value`. If batchmode is true, then there should be no popups or dialogs shown to the user.
    """
    ...
  

  def activeNode(self) -> "Node":
    """
      activeNode retrieve the node that is currently active in the currently active window
      
      # Returns
      
      the active node. If there is no active window, the first child node is returned.
    """
    ...
  

  def setActiveNode(self, value: Node) -> "None":
    """
      setActiveNode make the given node active in the currently active view and window
      
      # Parameters
      
      - value: Node
      
        the node to make active.
    """
    ...
  

  def topLevelNodes(self) -> "List[Node]":
    """
      toplevelNodes return a list with all top level nodes in the image graph
    """
    ...
  

  def nodeByName(self, name: str) -> "Node":
    """
      nodeByName searches the node tree for a node with the given name and returns it
      
      # Parameters
      
      - name: str
      
        the name of the node
      
      # Returns
      
      the first node with the given name or 0 if no node is found
    """
    ...
  

  def nodeByUniqueID(self, id: QUuid) -> "Node":
    """
      nodeByUniqueID searches the node tree for a node with the given name and returns it.
      
      # Parameters
      
      - uuid
      
        the unique id of the node
      
      # Returns
      
      the node with the given unique id, or 0 if no node is found.
    """
    ...
  

  def colorDepth(self) -> "str":
    """
      
      
      colorDepth A string describing the color depth of the image: 
      
      - U8: unsigned 8 bits integer, the most common type
      - U16: unsigned 16 bits integer
      - F16: half, 16 bits floating point. Only available if [Krita](https://api.kde.org/krita/html/classKrita.html) was built with OpenEXR
      - F32: 32 bits floating point
      
      # Returns
      
      the color depth.
    """
    ...
  

  def colorModel(self) -> "str":
    """
      colorModel retrieve the current color model of this document:
      
      
      - A: Alpha mask
      - RGBA: RGB with alpha channel (The actual order of channels is most often BGR!)
      - XYZA: XYZ with alpha channel
      - LABA: LAB with alpha channel
      - CMYKA: CMYK with alpha channel
      - GRAYA: Gray with alpha channel
      - YCbCrA: YCbCr with alpha channel
      
      # Returns
      
      the internal color model string.
    """
    ...
  

  def colorProfile(self) -> "str":
    """
      
      
      # Returns
      
      the name of the current color profile
    """
    ...
  

  def setColorProfile(self, colorProfile: str) -> "bool":
    """
      setColorProfile set the color profile of the image to the given profile. The profile has to be registered with krita and be compatible with the current color model and depth; the image data is `not` converted.
      
      # Parameters
      
      - colorProfile: str
      
        
      
      # Returns
      
      false if the colorProfile name does not correspond to to a registered profile or if assigning the profile failed.
    """
    ...
  

  def setColorSpace(self, colorModel: str, colorDepth: str, colorProfile: str) -> "bool":
    """
      setColorSpace convert the nodes and the image to the given colorspace. The conversion is done with Perceptual as intent, High Quality and No LCMS Optimizations as flags and no blackpoint compensation.
      
      # Parameters
      
      - colorModel: str
      
        A string describing the color model of the image: 
      
      - A: Alpha mask
      - RGBA: RGB with alpha channel (The actual order of channels is most often BGR!)
      - XYZA: XYZ with alpha channel
      - LABA: LAB with alpha channel
      - CMYKA: CMYK with alpha channel
      - GRAYA: Gray with alpha channel
      - YCbCrA: YCbCr with alpha channel
      
      - colorDepth: str
      
        A string describing the color depth of the image: 
      
      - U8: unsigned 8 bits integer, the most common type
      - U16: unsigned 16 bits integer
      - F16: half, 16 bits floating point. Only available if [Krita](https://api.kde.org/krita/html/classKrita.html) was built with OpenEXR
      - F32: 32 bits floating point
      
      - colorProfile: str
      
        a valid color profile for this color model and color depth combination.
      
      # Returns
      
      false the combination of these arguments does not correspond to a colorspace.
    """
    ...
  

  def backgroundColor(self) -> "QColor":
    """
      backgroundColor returns the current background color of the document. The color will also include the opacity.
      
      # Returns
      
      QColor
    """
    ...
  

  def setBackgroundColor(self, color: QColor) -> "bool":
    """
      setBackgroundColor sets the background color of the document. It will trigger a projection update.
      
      # Parameters
      
      - color: QColor
      
        A QColor. The color will be converted from sRGB.
      
      # Returns
      
      bool
    """
    ...
  

  def documentInfo(self) -> "str":
    """
      documentInfo creates and XML document representing document and author information.
      
      [https://phabricator.kde.org/source/krita/browse/master/krita/dtd/](https://phabricator.kde.org/source/krita/browse/master/krita/dtd/)
      
      ```
      <?xml version="1.0" encoding="UTF-8"?>
      <!DOCTYPE document-info PUBLIC '-//KDE//DTD document-info 1.1//EN' 'http://www.calligra.org/DTD/document-info-1.1.dtd'>
      <document-info xmlns="http://www.calligra.org/DTD/document-info">
      <about>
       <title>My [Document](https://api.kde.org/krita/html/classDocument.html)</title>
       <description></description>
       <subject></subject>
       <abstract><![CDATA[]]></abstract>
       <keyword></keyword>
       <initial-creator>Unknown</initial-creator>
       <editing-cycles>1</editing-cycles>
       <editing-time>35</editing-time>
       <date>2017-02-27T20:15:09</date>
       <creation-date>2017-02-27T20:14:33</creation-date>
       <language></language>
       </about>
       <author>
       <full-[name](https://api.kde.org/krita/html/classname.html)>Boudewijn Rempt</full-[name](https://api.kde.org/krita/html/classname.html)>
       <initial></initial>
       <author-title></author-title>
       <email></email>
       <telephone></telephone>
       <telephone-work></telephone-work>
       <fax></fax>
       <country></country>
       <postal-code></postal-code>
       <city></city>
       <street></street>
       <position></position>
       <company></company>
       </author>
      </document-info>
      ```
      
      # Returns
      
      a string containing a valid XML document with the right information about the document and author. The DTD can be found here:
    """
    ...
  

  def setDocumentInfo(self, document: str) -> "None":
    """
      setDocumentInfo set the [Document](https://api.kde.org/krita/html/classDocument.html) information to the information contained in document
      
      [https://phabricator.kde.org/source/krita/browse/master/krita/dtd/](https://phabricator.kde.org/source/krita/browse/master/krita/dtd/)
      
      # Parameters
      
      - document: str
      
        A string containing a valid XML document that conforms to the document-info DTD that can be found here:
    """
    ...
  

  def fileName(self) -> "str":
    """
      
      
      # Returns
      
      the full path to the document, if it has been set.
    """
    ...
  

  def setFileName(self, value: str) -> "None":
    """
      setFileName set the full path of the document to
      
      # Parameters
      
      - value: str
    """
    ...
  

  def height(self) -> "int":
    """
      
      
      # Returns
      
      the height of the image in pixels
    """
    ...
  

  def setHeight(self, value: int) -> "None":
    """
      setHeight resize the document to
      
      # Parameters
      
      - value: int
      
        height. This is a canvas resize, not a scale.
    """
    ...
  

  def name(self) -> "str":
    """
      
      
      # Returns
      
      the name of the document. This is the title field in the [documentInfo](https://api.kde.org/krita/html/classdocumentInfo.html)
    """
    ...
  

  def setName(self, value: str) -> "None":
    """
      setName sets the name of the document to `value`. This is the title field in the [documentInfo](https://api.kde.org/krita/html/classdocumentInfo.html)
    """
    ...
  

  def resolution(self) -> "int":
    """
      
      
      # Returns
      
      the resolution in pixels per inch
    """
    ...
  

  def setResolution(self, value: int) -> "None":
    """
      setResolution set the resolution of the image; this does not scale the image
      
      # Parameters
      
      - value: int
      
        the resolution in pixels per inch
    """
    ...
  

  def rootNode(self) -> "Node":
    """
      rootNode the root node is the invisible group layer that contains the entire node hierarchy.
      
      # Returns
      
      the root of the image
    """
    ...
  

  def selection(self) -> "Selection":
    """
      selection Create a [Selection](https://api.kde.org/krita/html/classSelection.html) object around the global selection, if there is one.
      
      # Returns
      
      the global selection or None if there is no global selection.
    """
    ...
  

  def setSelection(self, value: Selection) -> "None":
    """
      setSelection set or replace the global selection
      
      # Parameters
      
      - value: Selection
      
        a valid selection object.
    """
    ...
  

  def width(self) -> "int":
    """
      
      
      # Returns
      
      the width of the image in pixels.
    """
    ...
  

  def setWidth(self, value: int) -> "None":
    """
      setWidth resize the document to
      
      # Parameters
      
      - value: int
      
        width. This is a canvas resize, not a scale.
    """
    ...
  

  def xOffset(self) -> "int":
    """
      
      
      # Returns
      
      the left edge of the canvas in pixels.
    """
    ...
  

  def setXOffset(self, x: int) -> "None":
    """
      setXOffset sets the left edge of the canvas to `x`.
    """
    ...
  

  def yOffset(self) -> "int":
    """
      
      
      # Returns
      
      the top edge of the canvas in pixels.
    """
    ...
  

  def setYOffset(self, y: int) -> "None":
    """
      setYOffset sets the top edge of the canvas to `y`.
    """
    ...
  

  def xRes(self) -> "float":
    """
      
      
      # Returns
      
      xRes the horizontal resolution of the image in pixels per inch
    """
    ...
  

  def setXRes(self, xRes: float) -> "None":
    """
      setXRes set the horizontal resolution of the image to xRes in pixels per inch
    """
    ...
  

  def yRes(self) -> "float":
    """
      
      
      # Returns
      
      yRes the vertical resolution of the image in pixels per inch
    """
    ...
  

  def setYRes(self, yRes: float) -> "None":
    """
      setYRes set the vertical resolution of the image to yRes in pixels per inch
    """
    ...
  

  def pixelData(self, x: int, y: int, w: int, h: int) -> "QByteArray":
    """
      pixelData reads the given rectangle from the image projection and returns it as a byte array. The pixel data starts top-left, and is ordered row-first.
      
      The byte array can be interpreted as follows: 8 bits images have one byte per channel, and as many bytes as there are channels. 16 bits integer images have two bytes per channel, representing an unsigned short. 16 bits float images have two bytes per channel, representing a half, or 16 bits float. 32 bits float images have four bytes per channel, representing a float.
      
      You can read outside the image boundaries; those pixels will be transparent black.
      
      The order of channels is:
      
      - Integer RGBA: Blue, Green, Red, Alpha
      - Float RGBA: Red, Green, Blue, Alpha
      - LabA: L, a, b, Alpha
      - CMYKA: Cyan, Magenta, Yellow, Key, Alpha
      - XYZA: X, Y, Z, A
      - YCbCrA: Y, Cb, Cr, Alpha
      
      The byte array is a copy of the original image data. In Python, you can use bytes, bytearray and the struct module to interpret the data and construct, for instance, a Pillow Image object.
      
      # Parameters
      
      - x: int
      
        x position from where to start reading
      
      - y: int
      
        y position from where to start reading
      
      - w: int
      
        row length to read
      
      - h: int
      
        number of rows to read
      
      # Returns
      
      a QByteArray with the pixel data. The byte array may be empty.
    """
    ...
  

  def close(self) -> "bool":
    """
      close Close the document: remove it from [Krita](https://api.kde.org/krita/html/classKrita.html)'s internal list of documents and close all views. If the document is modified, you should save it first. There will be no prompt for saving.
      
      After closing the document it becomes invalid.
      
      # Returns
      
      true if the document is closed.
    """
    ...
  

  def crop(self, x: int, y: int, w: int, h: int) -> "None":
    """
      crop the image to rectangle described by `x`, `y`, `w` and `h`
      
      # Parameters
      
      - x: int
      
        x coordinate of the top left corner
      
      - y: int
      
        y coordinate of the top left corner
      
      - w: int
      
        width
      
      - h: int
      
        height
    """
    ...
  

  def exportImage(self, filename: str, exportConfiguration: InfoObject) -> "bool":
    """
      exportImage export the image, without changing its URL to the given path.
      
      
      The supported formats have specific configurations that must be used when in batchmode. They are described below:
      
      `png`
      
      - alpha: bool (True or False)
      - compression: int (1 to 9)
      - forceSRGB: bool (True or False)
      - indexed: bool (True or False)
      - interlaced: bool (True or False)
      - saveSRGBProfile: bool (True or False)
      - transparencyFillcolor: rgb (Ex:[255,255,255])
      
      `jpeg`
      
      - baseline: bool (True or False)
      - exif: bool (True or False)
      - filters: bool (['ToolInfo', 'Anonymizer'])
      - forceSRGB: bool (True or False)
      - iptc: bool (True or False)
      - is_sRGB: bool (True or False)
      - optimize: bool (True or False)
      - progressive: bool (True or False)
      - quality: int (0 to 100)
      - saveProfile: bool (True or False)
      - smoothing: int (0 to 100)
      - subsampling: int (0 to 3)
      - transparencyFillcolor: rgb (Ex:[255,255,255])
      - xmp: bool (True or False)
      
      # Parameters
      
      - filename: str
      
        the full path to which the image is to be saved
      
      - exportConfiguration: InfoObject
      
        a configuration object appropriate to the file format. An [InfoObject](https://api.kde.org/krita/html/classInfoObject.html) will used to that configuration.
      
      # Returns
      
      true if the export succeeded, false if it failed.
    """
    ...
  

  def flatten(self) -> "None":
    """
      flatten all layers in the image
    """
    ...
  

  def resizeImage(self, x: int, y: int, w: int, h: int) -> "None":
    """
      resizeImage resizes the canvas to the given left edge, top edge, width and height. Note: This doesn't scale, use scale image for that.
      
      # Parameters
      
      - x: int
      
        the new left edge
      
      - y: int
      
        the new top edge
      
      - w: int
      
        the new width
      
      - h: int
      
        the new height
    """
    ...
  

  def scaleImage(self, w: int, h: int, xres: int, yres: int, strategy: str) -> "None":
    """
      scaleImage
      
      # Parameters
      
      - w: int
      
        the new width
      
      - h: int
      
        the new height
      
      - xres: int
      
        the new xres
      
      - yres: int
      
        the new yres
      
      - strategy: str
      
        the scaling strategy. There's several ones amongst these that aren't available in the regular UI. The list of filters is extensible and can be retrieved with [Krita::filter](https://api.kde.org/krita/html/classKrita::filter.html)
      
      - Hermite
      - Bicubic - Adds pixels using the color of surrounding pixels. Produces smoother tonal gradations than Bilinear.
      - Box - Replicate pixels in the image. Preserves all the original detail, but can produce jagged effects.
      - Bilinear - Adds pixels averaging the color values of surrounding pixels. Produces medium quality results when the image is scaled from half to two times the original size.
      - Bell
      - BSpline
      - Kanczos3 - Offers similar results than Bicubic, but maybe a little bit sharper. Can produce light and dark halos along strong edges.
      - Mitchell
    """
    ...
  

  def rotateImage(self, radians: float) -> "None":
    """
      rotateImage Rotate the image by the given radians.
      
      # Parameters
      
      - radians: float
      
        the amount you wish to rotate the image in radians
    """
    ...
  

  def shearImage(self, angleX: float, angleY: float) -> "None":
    """
      shearImage shear the whole image.
      
      # Parameters
      
      - angleX: float
      
        the X-angle in degrees to shear by
      
      - angleY: float
      
        the Y-angle in degrees to shear by
    """
    ...
  

  def save(self) -> "bool":
    """
      save the image to its currently set path. The modified flag of the document will be reset
      
      # Returns
      
      true if saving succeeded, false otherwise.
    """
    ...
  

  def saveAs(self, filename: str) -> "bool":
    """
      saveAs save the document under the `filename`. The document's filename will be reset to `filename`.
      
      # Parameters
      
      - filename: str
      
        the new filename (full path) for the document
      
      # Returns
      
      true if saving succeeded, false otherwise.
    """
    ...
  

  def createNode(self, name: str, nodeType: str) -> "Node":
    """
      
      
         @brief createNode create a new node of the given type. The node is not added
         to the node hierarchy; you need to do that by finding the right parent node,
         getting its list of child nodes and adding the node in the right place, then
         calling Node::SetChildNodes
      
         @param name The name of the node
      
         @param nodeType The type of the node. Valid types are:
         <ul>
          <li>paintlayer
          <li>grouplayer
          <li>filelayer
          <li>filterlayer
          <li>filllayer
          <li>clonelayer
          <li>vectorlayer
          <li>transparencymask
          <li>filtermask
          <li>transformmask
          <li>selectionmask
         </ul>
      
         When relevant, the new Node will have the colorspace of the image by default;
         that can be changed with Node::setColorSpace.
      
         The settings and selections for relevant layer and mask types can also be set
         after the Node has been created.
      ```
      d = Application.createDocument(1000, 1000, "Test", "RGBA", "U8", "", 120.0)
      root = d.rootNode();
      print(root.childNodes())
      l2 = d.[createNode](https://api.kde.org/krita/html/classcreateNode.html)("layer2", "paintLayer")
      print(l2)
      root.addChildNode(l2, None)
      print(root.childNodes())
      ```
      
      # Returns
      
      the new [Node](https://api.kde.org/krita/html/classNode.html).
    """
    ...
  

  def createGroupLayer(self, name: str) -> "GroupLayer":
    """
      createGroupLayer Returns a grouplayer object. Grouplayers are nodes that can have other layers as children and have the passthrough mode.
      
      # Parameters
      
      - name: str
      
        the name of the layer.
      
      # Returns
      
      a [GroupLayer](https://api.kde.org/krita/html/classGroupLayer.html) object.
    """
    ...
  

  def createFileLayer(self, name: str, fileName: str, scalingMethod: str, scalingFilter: str = "Bicubic") -> "FileLayer":
    """
      createFileLayer returns a layer that shows an external image.
      
      # Parameters
      
      - name: str
      
        name of the file layer.
      
      - fileName: str
      
        the absolute filename of the file referenced. Symlinks will be resolved.
      
      - scalingMethod: str
      
        how the dimensions of the file are interpreted can be either "None", "ImageToSize" or "ImageToPPI"
      
      - scalingFilter: str = `"Bicubic"`
      
        filter used to scale the file can be "Bicubic", "Hermite", "NearestNeighbor", "Bilinear", "Bell", "BSpline", "Lanczos3", "Mitchell"
      
      # Returns
      
      a [FileLayer](https://api.kde.org/krita/html/classFileLayer.html)
    """
    ...
  

  def createFilterLayer(self, name: str, filter: Filter, selection: Selection) -> "FilterLayer":
    """
      createFilterLayer creates a filter layer, which is a layer that represents a filter applied non-destructively.
      
      # Parameters
      
      - name: str
      
        name of the filterLayer
      
      - filter: Filter
      
        the filter that this filter layer will us.
      
      - selection: Selection
      
        the selection.
      
      # Returns
      
      a filter layer object.
    """
    ...
  

  def createFillLayer(self, name: str, generatorName: str, configuration: InfoObject, selection: Selection) -> "FillLayer":
    """
      createFillLayer creates a fill layer object, which is a layer
      
      ```
      from krita import *
      d = Krita.instance().activeDocument()
      i = InfoObject();
      i.setProperty("pattern", "Cross01.pat")
      s = [Selection](https://api.kde.org/krita/html/classSelection.html)();
      s.select(0, 0, d.width(), d.height(), 255)
      n = d.createFillLayer("test", "pattern", i, s)
      r = d.rootNode();
      c = r.childNodes();
      r.addChildNode(n, c[0])
      d.refreshProjection()
      ```
      
      # Parameters
      
      - name: str
      
        
      
      - generatorName: str
      
        - name of the generation filter.
      
      - configuration: InfoObject
      
        - the configuration for the generation filter.
      
      - selection: Selection
      
        - the selection.
      
      # Returns
      
      a filllayer object.
    """
    ...
  

  def createCloneLayer(self, name: str, source: Node) -> "CloneLayer":
    """
      createCloneLayer
      
      # Parameters
      
      - name: str
      
        
      
      - source: Node
      
        
      
      # Returns
    """
    ...
  

  def createVectorLayer(self, name: str) -> "VectorLayer":
    """
      createVectorLayer Creates a vector layer that can contain vector shapes.
      
      # Parameters
      
      - name: str
      
        the name of this layer.
      
      # Returns
      
      a [VectorLayer](https://api.kde.org/krita/html/classVectorLayer.html).
    """
    ...
  

  def createFilterMask(self, name: str, filter: Filter, selection: Selection) -> "FilterMask":
    """
      createFilterMask Creates a filter mask object that much like a filterlayer can apply a filter non-destructively.
      
      # Parameters
      
      - name: str
      
        the name of the layer.
      
      - filter: Filter
      
        the filter assigned.
      
      - selection: Selection
      
        the selection to be used by the filter mask
      
      # Returns
      
      a [FilterMask](https://api.kde.org/krita/html/classFilterMask.html)
    """
    ...
  

  def createFilterMask(self, name: str, filter: Filter, selection_source: Node) -> "FilterMask":
    """
      createFilterMask Creates a filter mask object that much like a filterlayer can apply a filter non-destructively.
      
      # Parameters
      
      - name: str
      
        the name of the layer.
      
      - filter: Filter
      
        the filter assigned.
      
      - selection_source: Node
      
        a node from which the selection should be initialized
      
      # Returns
      
      a [FilterMask](https://api.kde.org/krita/html/classFilterMask.html)
    """
    ...
  

  def createSelectionMask(self, name: str) -> "SelectionMask":
    """
      createSelectionMask Creates a selection mask, which can be used to store selections.
      
      # Parameters
      
      - name: str
      
        - the name of the layer.
      
      # Returns
      
      a [SelectionMask](https://api.kde.org/krita/html/classSelectionMask.html)
    """
    ...
  

  def createTransparencyMask(self, name: str) -> "TransparencyMask":
    """
      createTransparencyMask Creates a transparency mask, which can be used to assign transparency to regions.
      
      # Parameters
      
      - name: str
      
        - the name of the layer.
      
      # Returns
      
      a [TransparencyMask](https://api.kde.org/krita/html/classTransparencyMask.html)
    """
    ...
  

  def createTransformMask(self, name: str) -> "TransformMask":
    """
      createTransformMask Creates a transform mask, which can be used to apply a transformation non-destructively.
      
      # Parameters
      
      - name: str
      
        - the name of the layer mask.
      
      # Returns
      
      a [TransformMask](https://api.kde.org/krita/html/classTransformMask.html)
    """
    ...
  

  def createColorizeMask(self, name: str) -> "ColorizeMask":
    """
      createColorizeMask Creates a colorize mask, which can be used to color fill via keystrokes.
      
      # Parameters
      
      - name: str
      
        - the name of the layer.
      
      # Returns
      
      a [TransparencyMask](https://api.kde.org/krita/html/classTransparencyMask.html)
    """
    ...
  

  def projection(self, x: int = 0, y: int = 0, w: int = 0, h: int = 0) -> "QImage":
    """
      projection creates a QImage from the rendered image or a cutout rectangle.
    """
    ...
  

  def thumbnail(self, w: int, h: int) -> "QImage":
    """
      thumbnail create a thumbnail of the given dimensions.
      
      If the requested size is too big a null QImage is created.
      
      # Returns
      
      a QImage representing the layer contents.
    """
    ...
  

  def lock(self) -> "None":
    """
      
      
      [low-level] Lock the image without waiting for all the internal job queues are processed
      
      WARNING: Don't use it unless you really know what you are doing! Use barrierLock() instead!
      
      Waits for all the `currently running` internal jobs to complete and locks the image for writing. Please note that this function does `not` wait for all the internal queues to process, so there might be some non-finished actions pending. It means that you just postpone these actions until you `unlock()` the image back. Until then, then image might easily be frozen in some inconsistent state.
      
      The only sane usage for this function is to lock the image for `emergency` processing, when some internal action or scheduler got hung up, and you just want to fetch some data from the image without races.
      
      In all other cases, please use barrierLock() instead!
    """
    ...
  

  def unlock(self) -> "None":
    """
      
      
      Unlocks the image and starts/resumes all the pending internal jobs. If the image has been locked for a non-readOnly access, then all the internal caches of the image (e.g. lod-planes) are reset and regeneration jobs are scheduled.
    """
    ...
  

  def waitForDone(self) -> "None":
    """
      
      
      Wait for all the internal image jobs to complete and return without locking the image. This function is handy for tests or other synchronous actions, when one needs to wait for the result of his actions.
    """
    ...
  

  def tryBarrierLock(self) -> "bool":
    """
      Tries to lock the image without waiting for the jobs to finish.
      
      Same as barrierLock(), but doesn't block execution of the calling thread until all the background jobs are finished. Instead, in case of presence of unfinished jobs in the queue, it just returns false
      
      # Returns
      
      whether the lock has been acquired
    """
    ...
  

  def refreshProjection(self) -> "None":
    """
      
      
      Starts a synchronous recomposition of the projection: everything will wait until the image is fully recomputed.
    """
    ...
  

  def setHorizontalGuides(self, lines: List[float]) -> "None":
    """
      setHorizontalGuides replace all existing horizontal guides with the entries in the list.
      
      # Parameters
      
      - lines: List[float]
      
        a list of floats containing the new guides.
    """
    ...
  

  def setVerticalGuides(self, lines: List[float]) -> "None":
    """
      setVerticalGuides replace all existing horizontal guides with the entries in the list.
      
      # Parameters
      
      - lines: List[float]
      
        a list of floats containing the new guides.
    """
    ...
  

  def setGuidesVisible(self, visible: bool) -> "None":
    """
      setGuidesVisible set guides visible on this document.
      
      # Parameters
      
      - visible: bool
      
        whether or not the guides are visible.
    """
    ...
  

  def setGuidesLocked(self, locked: bool) -> "None":
    """
      setGuidesLocked set guides locked on this document
      
      # Parameters
      
      - locked: bool
      
        whether or not to lock the guides on this document.
    """
    ...
  

  def modified(self) -> "bool":
    """
      modified returns true if the document has unsaved modifications.
    """
    ...
  

  def setModified(self, modified: bool) -> "None":
    """
      setModified sets the modified status of the document
      
      # Parameters
      
      - modified: bool
      
        if true, the document is considered modified and closing it will ask for saving.
    """
    ...
  

  def bounds(self) -> "QRect":
    """
      bounds return the bounds of the image
      
      # Returns
      
      the bounds
    """
    ...
  

  def importAnimation(self, files: List[str], firstFrame: int, step: int) -> "bool":
    """
      Import an image sequence of files from a directory. This will grab all images from the directory and import them with a potential offset (firstFrame) and step (images on 2s, 3s, etc)
      
      # Returns
      
      whether the animation import was successful
    """
    ...
  

  def framesPerSecond(self) -> "int":
    """
      frames per second of document
      
      # Returns
      
      the fps of the document
    """
    ...
  

  def setFramesPerSecond(self, fps: int) -> "None":
    """
      set frames per second of document
    """
    ...
  

  def setFullClipRangeStartTime(self, startTime: int) -> "None":
    """
      set start time of animation
    """
    ...
  

  def fullClipRangeStartTime(self) -> "int":
    """
      get the full clip range start time
      
      # Returns
      
      full clip range start time
    """
    ...
  

  def setFullClipRangeEndTime(self, endTime: int) -> "None":
    """
      set full clip range end time
    """
    ...
  

  def fullClipRangeEndTime(self) -> "int":
    """
      get the full clip range end time
      
      # Returns
      
      full clip range end time
    """
    ...
  

  def animationLength(self) -> "int":
    """
      get total frame range for animation
      
      # Returns
      
      total frame range for animation
    """
    ...
  

  def setPlayBackRange(self, start: int, stop: int) -> "None":
    """
      set temporary playback range of document
    """
    ...
  

  def playBackStartTime(self) -> "int":
    """
      get start time of current playback
      
      # Returns
      
      start time of current playback
    """
    ...
  

  def playBackEndTime(self) -> "int":
    """
      get end time of current playback
      
      # Returns
      
      end time of current playback
    """
    ...
  

  def currentTime(self) -> "int":
    """
      get current frame selected of animation
      
      # Returns
      
      current frame selected of animation
    """
    ...
  

  def setCurrentTime(self, time: int) -> "None":
    """
      set current time of document's animation
    """
    ...
  

  def annotationTypes(self) -> "List[str]":
    """
      annotationTypes returns the list of annotations present in the document. Each annotation type is unique.
    """
    ...
  

  def annotationDescription(self, type: str) -> "str":
    """
      annotationDescription gets the pretty description for the current annotation
      
      # Parameters
      
      - type: str
      
        the type of the annotation
      
      # Returns
      
      a string that can be presented to the user
    """
    ...
  

  def annotation(self, type: str) -> "QByteArray":
    """
      annotation the actual data for the annotation for this type. It's a simple QByteArray, what's in it depends on the type of the annotation
      
      # Parameters
      
      - type: str
      
        the type of the annotation
      
      # Returns
      
      a bytearray, possibly empty if this type of annotation doesn't exist
    """
    ...
  

  def setAnnotation(self, type: str, description: str, annotation: QByteArray) -> "None":
    """
      setAnnotation Add the given annotation to the document
      
      # Parameters
      
      - type: str
      
        the unique type of the annotation
      
      - description: str
      
        the user-visible description of the annotation
      
      - annotation: QByteArray
      
        the annotation itself
    """
    ...
  

  def removeAnnotation(self, type: str) -> "None":
    """
      removeAnnotation remove the specified annotation from the image
      
      # Parameters
      
      - type: str
      
        the type defining the annotation
    """
    ...
  

class Extension(QObject):

  """
    
    
    An [Extension](https://api.kde.org/krita/html/classExtension.html) is the base for classes that extend [Krita](https://api.kde.org/krita/html/classKrita.html). An [Extension](https://api.kde.org/krita/html/classExtension.html) is loaded on startup, when the `setup()` method will be executed.
    
    The extension instance should be added to the [Krita](https://api.kde.org/krita/html/classKrita.html) Application object using `Krita.instance()`.addViewExtension or Application.addViewExtension or Scripter.addViewExtension.
    
    Example:
    
    ```
    import sys
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *
    from krita import *
    class HelloExtension(Extension):
    
    def __init__(self, parent):
      super().__init__(parent)
    
    def hello(self):
      QMessageBox.information(QWidget(), "Test", "Hello! This is Krita " + Application.version())
    
    def [setup](https://api.kde.org/krita/html/classsetup.html)(self):
      qDebug("Hello Setup")
    
    def createActions(self, window)
      action = window.createAction("hello")
      action.triggered.connect(self.hello)
    
    Scripter.addExtension(HelloExtension([Krita](https://api.kde.org/krita/html/classKrita.html).instance()))
    ```
  """

  def __init__(self, parent: QObject = None) -> None:
    """
      
      
      Create a new extension. The extension will be owned by `parent`.
    """
    ...
  

  def setup(self) -> "None":
    """
      
      
      Override this function to setup your [Extension](https://api.kde.org/krita/html/classExtension.html). You can use it to integrate with the [Krita](https://api.kde.org/krita/html/classKrita.html) application instance.
    """
    ...
  

  def createActions(self, window: Window) -> "None":
  
    ...
  

class FileLayer(Node):

  """
    The [FileLayer](https://api.kde.org/krita/html/classFileLayer.html) class A file layer is a layer that can reference an external image and show said reference in the layer stack.
    
    If the external image is updated, [Krita](https://api.kde.org/krita/html/classKrita.html) will try to update the file layer image as well.
  """

  def __init__(self, image: KisImageSP, name: str = "", baseName: str = "", fileName: str = "", scalingMethod: str = "", scalingFilter: str = "", parent: QObject = None) -> None:
  
    ...
  

  def __init__(self, layer: KisFileLayerSP, parent: QObject = None) -> None:
  
    ...
  

  def type(self) -> "str":
    """
      type [Krita](https://api.kde.org/krita/html/classKrita.html) has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
      
      # Returns
      
      "filelayer"
    """
    ...
  

  def setProperties(self, fileName: str, scalingMethod: str = "None", scalingFilter: str = "Bicubic") -> "None":
    """
      setProperties Change the properties of the file layer.
      
      # Parameters
      
      - fileName: str
      
        - A String containing the absolute file name.
      
      - scalingMethod: str = `"None"`
      
        - a string with the scaling method, defaults to "None", other options are "ToImageSize" and "ToImagePPI"
      
      - scalingFilter: str = `"Bicubic"`
      
        - a string with the scaling filter, defaults to "Bicubic", other options are "Hermite", "NearestNeighbor", "Bilinear", "Bell", "BSpline", "Lanczos3", "Mitchell"
    """
    ...
  

  def resetCache(self) -> "None":
    """
      makes the file layer to reload the connected image from disk
    """
    ...
  

  def path(self) -> "str":
    """
      path
      
      # Returns
      
      A QString with the full path of the referenced image.
    """
    ...
  

  def scalingMethod(self) -> "str":
    """
      scalingMethod returns how the file referenced is scaled.
      
      # Returns
      
      one of the following: 
      
      - None - The file is not scaled in any way.
      - ToImageSize - The file is scaled to the full image size;
      - ToImagePPI - The file is scaled by the PPI of the image. This keep the physical dimensions the same.
    """
    ...
  

  def scalingFilter(self) -> "str":
    """
      scalingFilter returns the filter with which the file referenced is scaled.
    """
    ...
  

class FillLayer(Node):

  """
    The [FillLayer](https://api.kde.org/krita/html/classFillLayer.html) class A fill layer is much like a filter layer in that it takes a name and filter. It however specializes in filters that fill the whole canvas, such as a pattern or full color fill.
  """

  def __init__(self, image: KisImageSP, name: str, filterConfig: KisFilterConfigurationSP, selection: Selection, parent: QObject = None) -> None:
    """
      [FillLayer](https://api.kde.org/krita/html/classFillLayer.html) Create a new fill layer with the given generator plugin.
      
      
      For a "pattern" fill layer, the [InfoObject](https://api.kde.org/krita/html/classInfoObject.html) can contain a single "pattern" parameter with the name of a pattern as known to the resource system: "pattern" = "Cross01.pat".
      
      For a "color" fill layer, the [InfoObject](https://api.kde.org/krita/html/classInfoObject.html) can contain a single "color" parameter with a QColor, a string that QColor can parse (see [https://doc.qt.io/qt-5/qcolor.html#setNamedColor](https://doc.qt.io/qt-5/qcolor.html#setNamedColor)) or an XML description of the color, which can be derived from a 
      [ManagedColor](https://api.kde.org/krita/html/classManagedColor.html).
      
      # Parameters
      
      - image: KisImageSP
      
        the image this fill layer will belong to
      
      - name: str
      
        "pattern" or "color"
      
      - filterConfig: KisFilterConfigurationSP
      
        a configuration object appropriate to the given generator plugin
      
      - selection: Selection
      
        a selection object, can be empty
      
      - parent: QObject = `None`
    """
    ...
  

  def __init__(self, layer: KisGeneratorLayerSP, parent: QObject = None) -> None:
  
    ...
  

  def type(self) -> "str":
    """
      type [Krita](https://api.kde.org/krita/html/classKrita.html) has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
      
      
      If the [Node](https://api.kde.org/krita/html/classNode.html) object isn't wrapping a valid [Krita](https://api.kde.org/krita/html/classKrita.html) layer or mask object, and empty string is returned.
      
      # Returns
      
      The type of the node. Valid types are: 
      
      - paintlayer
      - grouplayer
      - filelayer
      - filterlayer
      - filllayer
      - clonelayer
      - vectorlayer
      - transparencymask
      - filtermask
      - transformmask
      - selectionmask
      - colorizemask
    """
    ...
  

  def setGenerator(self, generatorName: str, filterConfig: InfoObject) -> "bool":
    """
      setGenerator set the given generator for this fill layer
      
      # Parameters
      
      - generatorName: str
      
        "pattern" or "color"
      
      - filterConfig: InfoObject
      
        a configuration object appropriate to the given generator plugin
      
      # Returns
      
      true if the generator was correctly created and set on the layer
    """
    ...
  

  def generatorName(self) -> "str":
  
    ...
  

  def filterConfig(self) -> "InfoObject":
  
    ...
  

class Filter(QObject):

  """
    
    
    [Filter](https://api.kde.org/krita/html/classFilter.html): represents a filter and its configuration. A filter is identified by an internal name. The configuration for each filter is defined as an [InfoObject](https://api.kde.org/krita/html/classInfoObject.html): a map of name and value pairs.
    
    Currently available filters are:
    
    'autocontrast', 'blur', 'bottom edge detections', 'brightnesscontrast', 'burn', 'colorbalance', 'colortoalpha', 'colortransfer', 'desaturate', 'dodge', 'emboss', 'emboss all directions', 'emboss horizontal and vertical', 'emboss horizontal only', 'emboss laplascian', 'emboss vertical only', 'gaussian blur', 'gaussiannoisereducer', 'gradientmap', 'halftone', 'hsvadjustment', 'indexcolors', 'invert', 'left edge detections', 'lens blur', 'levels', 'maximize', 'mean removal', 'minimize', 'motion blur', 'noise', 'normalize', 'oilpaint', 'perchannel', 'phongbumpmap', 'pixelize', 'posterize', 'raindrops', 'randompick', 'right edge detections', 'roundcorners', 'sharpen', 'smalltiles', 'sobel', 'threshold', 'top edge detections', 'unsharp', 'wave', 'waveletnoisereducer']
  """

  def __init__(self) -> None:
    """
      [Filter](https://api.kde.org/krita/html/classFilter.html): create an empty filter object. Until a name is set, the filter cannot be applied.
    """
    ...
  

  def name(self) -> "str":
    """
      name the internal name of this filter.
      
      # Returns
      
      the name.
    """
    ...
  

  def setName(self, name: str) -> "None":
    """
      setName set the filter's name to the given name.
    """
    ...
  

  def configuration(self) -> "InfoObject":
    """
      
      
      # Returns
      
      the configuration object for the filter
    """
    ...
  

  def setConfiguration(self, value: InfoObject) -> "None":
    """
      setConfiguration set the configuration object for the filter
    """
    ...
  

  def apply(self, node: Node, x: int, y: int, w: int, h: int) -> "bool":
    """
      Apply the filter to the given node.
      
      # Parameters
      
      - node: Node
      
        the node to apply the filter to
      
      - x: int
      
        
      
      - y: int
      
        
      
      - w: int
      
        
      
      - h: int
      
        describe the rectangle the filter should be apply. This is always in image pixel coordinates and not relative to the x, y of the node.
      
      # Returns
      
      `true` if the filter was applied successfully, or `false` if the filter could not be applied because the node is locked or does not have an editable paint device.
    """
    ...
  

  def startFilter(self, node: Node, x: int, y: int, w: int, h: int) -> "bool":
    """
      startFilter starts the given filter on the given node.
      
      # Parameters
      
      - node: Node
      
        the node to apply the filter to
      
      - x: int
      
        
      
      - y: int
      
        
      
      - w: int
      
        
      
      - h: int
      
        describe the rectangle the filter should be apply. This is always in image pixel coordinates and not relative to the x, y of the node.
    """
    ...
  

class FilterLayer(Node):

  """
    The [FilterLayer](https://api.kde.org/krita/html/classFilterLayer.html) class A filter layer will, when compositing, take the composited image up to the point of the location of the filter layer in the stack, create a copy and apply a filter.
    
    This means you can use blending modes on the filter layers, which will be used to blend the filtered image with the original.
    
    Similarly, you can activate things like alpha inheritance, or you can set grayscale pixeldata on the filter layer to act as a mask.
    
    [Filter](https://api.kde.org/krita/html/classFilter.html) layers can be animated.
  """

  def __init__(self, image: KisImageSP, name: str, filter: Filter, selection: Selection, parent: QObject = None) -> None:
  
    ...
  

  def __init__(self, layer: KisAdjustmentLayerSP, parent: QObject = None) -> None:
  
    ...
  

  def type(self) -> "str":
    """
      type [Krita](https://api.kde.org/krita/html/classKrita.html) has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
      
      # Returns
      
      "filterlayer"
    """
    ...
  

  def setFilter(self, filter: Filter) -> "None":
  
    ...
  

  def filter(self) -> "Filter":
  
    ...
  

class FilterMask(Node):

  """
    The [FilterMask](https://api.kde.org/krita/html/classFilterMask.html) class A filter mask, unlike a filter layer, will add a non-destructive filter to the composited image of the node it is attached to.
    
    You can set grayscale pixeldata on the filter mask to adjust where the filter is applied.
    
    Filtermasks can be animated.
  """

  def __init__(self, image: KisImageSP, name: str, filter: Filter, parent: QObject = None) -> None:
  
    ...
  

  def __init__(self, image: KisImageSP, mask: KisFilterMaskSP, parent: QObject = None) -> None:
  
    ...
  

  def type(self) -> "str":
    """
      type [Krita](https://api.kde.org/krita/html/classKrita.html) has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
      
      
      If the [Node](https://api.kde.org/krita/html/classNode.html) object isn't wrapping a valid [Krita](https://api.kde.org/krita/html/classKrita.html) layer or mask object, and empty string is returned.
      
      # Returns
      
      The type of the node. Valid types are: 
      
      - paintlayer
      - grouplayer
      - filelayer
      - filterlayer
      - filllayer
      - clonelayer
      - vectorlayer
      - transparencymask
      - filtermask
      - transformmask
      - selectionmask
      - colorizemask
    """
    ...
  

  def setFilter(self, filter: Filter) -> "None":
  
    ...
  

  def filter(self) -> "Filter":
  
    ...
  

class GroupLayer(Node):

  """
    The [GroupLayer](https://api.kde.org/krita/html/classGroupLayer.html) class A group layer is a layer that can contain other layers. In [Krita](https://api.kde.org/krita/html/classKrita.html), layers within a group layer are composited first before they are added into the composition code for where the group is in the stack. This has a significant effect on how it is interpreted for blending modes.
    
    PassThrough changes this behaviour.
    
    Group layer cannot be animated, but can contain animated layers or masks.
  """

  def __init__(self, image: KisImageSP, name: str, parent: QObject = None) -> None:
  
    ...
  

  def __init__(self, layer: KisGroupLayerSP, parent: QObject = None) -> None:
  
    ...
  

  def type(self) -> "str":
    """
      type [Krita](https://api.kde.org/krita/html/classKrita.html) has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
      
      # Returns
      
      grouplayer
    """
    ...
  

  def setPassThroughMode(self, passthrough: bool) -> "None":
    """
      setPassThroughMode This changes the way how compositing works. Instead of compositing all the layers before compositing it with the rest of the image, the group layer becomes a sort of formal way to organise everything.
      
      Passthrough mode is the same as it is in photoshop, and the inverse of SVG's isolation attribute(with passthrough=false being the same as isolation="isolate").
      
      # Parameters
      
      - passthrough: bool
      
        whether or not to set the layer to passthrough.
    """
    ...
  

  def passThroughMode(self) -> "bool":
    """
      passThroughMode
      
      
      [setPassThroughMode](https://api.kde.org/krita/html/classsetPassThroughMode.html)
      
      # Returns
      
      returns whether or not this layer is in passthrough mode.
    """
    ...
  

class GroupShape(Shape):

  """
    The [GroupShape](https://api.kde.org/krita/html/classGroupShape.html) class A group shape is a vector object with child shapes.
  """

  def __init__(self, parent: QObject = None) -> None:
  
    ...
  

  def __init__(self, shape: KoShapeGroup, parent: QObject = None) -> None:
  
    ...
  

  def type(self) -> "str":
    """
      type returns the type.
      
      # Returns
      
      "groupshape"
    """
    ...
  

  def children(self) -> "List[Shape]":
    """
      children
      
      # Returns
      
      the child shapes of this group shape.
    """
    ...
  

class InfoObject(QObject):

  """
    
    
    [InfoObject](https://api.kde.org/krita/html/classInfoObject.html) wrap a properties map. These maps can be used to set the configuration for filters.
  """

  def __init__(self, configuration: KisPropertiesConfigurationSP) -> None:
  
    ...
  

  def __init__(self, parent: QObject = None) -> None:
    """
      
      
      Create a new, empty [InfoObject](https://api.kde.org/krita/html/classInfoObject.html).
    """
    ...
  

  def properties(self) -> "dict[str,QVariant]":
    """
      
      
      Return all properties this [InfoObject](https://api.kde.org/krita/html/classInfoObject.html) manages.
    """
    ...
  

  def setProperties(self, propertyMap: dict[str,QVariant]) -> "None":
    """
      
      
      Add all properties in the `propertyMap` to this [InfoObject](https://api.kde.org/krita/html/classInfoObject.html)
    """
    ...
  

  def setProperty(self, key: str, value: QVariant) -> "None":
    """
      
      
      set the property identified by `key` to `value`
      
      If you want create a property that represents a color, you can use a QColor or hex string, as defined in [https://doc.qt.io/qt-5/qcolor.html#setNamedColor](https://doc.qt.io/qt-5/qcolor.html#setNamedColor).
    """
    ...
  

  def property(self, key: str) -> "QVariant":
    """
      
      
      return the value for the property identified by key, or None if there is no such key.
    """
    ...
  

class Krita(QObject):

  """
    
    
    [Krita](https://api.kde.org/krita/html/classKrita.html) is a singleton class that offers the root access to the [Krita](https://api.kde.org/krita/html/classKrita.html) object hierarchy.
    
    The `Krita.instance()` is aliased as two builtins: Scripter and Application.
  """

  def __init__(self, parent: QObject = None) -> None:
  
    ...
  

  def activeDocument(self) -> "Document":
    """
      
      
      # Returns
      
      the currently active document, if there is one.
    """
    ...
  

  def setActiveDocument(self, value: Document) -> "None":
    """
      setActiveDocument activates the first view that shows the given document
      
      # Parameters
      
      - value: Document
      
        the document we want to activate
    """
    ...
  

  def batchmode(self) -> "bool":
    """
      batchmode determines whether the script is run in batch mode. If batchmode is true, scripts should now show messageboxes or dialog boxes.
      
      Note that this separate from `Document.setBatchmode()`, which determines whether export/save option dialogs are shown.
      
      # Returns
      
      true if the script is run in batchmode
    """
    ...
  

  def setBatchmode(self, value: bool) -> "None":
    """
      setBatchmode sets the batchmode to
      
      # Parameters
      
      - value;
      
        if true, scripts should not show dialogs or messageboxes.
    """
    ...
  

  def actions(self) -> "List[QAction]":
    """
      
      
      # Returns
      
      return a list of all actions for the currently active mainWindow.
    """
    ...
  

  def action(self, name: str) -> "QAction":
    """
      
      
      # Returns
      
      the action that has been registered under the given name, or 0 if no such action exists.
    """
    ...
  

  def documents(self) -> "List[Document]":
    """
      
      
      # Returns
      
      a list of all open Documents
    """
    ...
  

  def dockers(self) -> "List[QDockWidget]":
    """
      
      
      # Returns
      
      a list of all the dockers
    """
    ...
  

  def filters(self) -> "List[str]":
    """
      Filters are identified by an internal name. This function returns a list of all existing registered filters.
      
      # Returns
      
      a list of all registered filters
    """
    ...
  

  def filter(self, name: str) -> "Filter":
    """
      filter construct a [Filter](https://api.kde.org/krita/html/classFilter.html) object with a default configuration.
      
      # Parameters
      
      - name: str
      
        the name of the filter. Use `Krita.instance()`.`filters()` to get a list of all possible filters.
      
      # Returns
      
      the filter or None if there is no such filter.
    """
    ...
  

  def colorModels(self) -> "List[str]":
    """
      colorModels creates a list with all color models id's registered.
      
      # Returns
      
      a list of all color models or a empty list if there is no such color models.
    """
    ...
  

  def colorDepths(self, colorModel: str) -> "List[str]":
    """
      colorDepths creates a list with the names of all color depths compatible with the given color model.
      
      # Parameters
      
      - colorModel: str
      
        the id of a color model.
      
      # Returns
      
      a list of all color depths or a empty list if there is no such color depths.
    """
    ...
  

  def filterStrategies(self) -> "List[str]":
    """
      filterStrategies Retrieves all installed filter strategies. A filter strategy is used when transforming (scaling, shearing, rotating) an image to calculate the value of the new pixels. You can use th
      
      # Returns
      
      the id's of all available filters.
    """
    ...
  

  def profiles(self, colorModel: str, colorDepth: str) -> "List[str]":
    """
      profiles creates a list with the names of all color profiles compatible with the given color model and color depth.
      
      # Parameters
      
      - colorModel: str
      
        A string describing the color model of the image: 
      
      - A: Alpha mask
      - RGBA: RGB with alpha channel (The actual order of channels is most often BGR!)
      - XYZA: XYZ with alpha channel
      - LABA: LAB with alpha channel
      - CMYKA: CMYK with alpha channel
      - GRAYA: Gray with alpha channel
      - YCbCrA: YCbCr with alpha channel
      
      - colorDepth: str
      
        A string describing the color depth of the image: 
      
      - U8: unsigned 8 bits integer, the most common type
      - U16: unsigned 16 bits integer
      - F16: half, 16 bits floating point. Only available if [Krita](https://api.kde.org/krita/html/classKrita.html) was built with OpenEXR
      - F32: 32 bits floating point
      
      # Returns
      
      a list with valid names
    """
    ...
  

  def addProfile(self, profilePath: str) -> "bool":
    """
      addProfile load the given profile into the profile registry.
      
      # Parameters
      
      - profilePath: str
      
        the path to the profile.
      
      # Returns
      
      true if adding the profile succeeded.
    """
    ...
  

  def notifier(self) -> "Notifier":
    """
      notifier the [Notifier](https://api.kde.org/krita/html/classNotifier.html) singleton emits signals when documents are opened and closed, the configuration changes, views are opened and closed or windows are opened.
      
      # Returns
      
      the notifier object
    """
    ...
  

  def version(self) -> "str":
    """
      version Determine the version of [Krita](https://api.kde.org/krita/html/classKrita.html)
      
      Usage: print(Application.version ())
      
      # Returns
      
      the version string including git sha1 if [Krita](https://api.kde.org/krita/html/classKrita.html) was built from git
    """
    ...
  

  def views(self) -> "List[View]":
    """
      
      
      # Returns
      
      a list of all views. A [Document](https://api.kde.org/krita/html/classDocument.html) can be shown in more than one view.
    """
    ...
  

  def activeWindow(self) -> "Window":
    """
      
      
      # Returns
      
      the currently active window or None if there is no window
    """
    ...
  

  def windows(self) -> "List[Window]":
    """
      
      
      # Returns
      
      a list of all windows
    """
    ...
  

  def resources(self, type: str) -> "dict[str,Resource]":
    """
      resources returns a list of [Resource](https://api.kde.org/krita/html/classResource.html) objects of the given type
      
      
      - pattern
      - gradient
      - brush
      - preset
      - palette
      - workspace
      
      # Parameters
      
      - type: str
      
        Valid types are:
    """
    ...
  

  def recentDocuments(self) -> "List[str]":
    """
      return all recent documents registered in the RecentFiles group of the kritarc
    """
    ...
  

  def createDocument(self, width: int, height: int, name: str, colorModel: str, colorDepth: str, profile: str, resolution: float) -> "Document":
    """
      
      
         @brief createDocument creates a new document and image and registers
         the document with the Krita application.
      
         Unless you explicitly call Document::close() the document will remain
         known to the Krita document registry. The document and its image will
         only be deleted when Krita exits.
      
         The document will have one transparent layer.
      
         To create a new document and show it, do something like:
      ```
      from [Krita](https://api.kde.org/krita/html/classKrita.html) import *
      
      def add_document_to_window():
        d = Application.createDocument(100, 100, "Test", "RGBA", "U8", "", 120.0)
        Application.[activeWindow](https://api.kde.org/krita/html/classactiveWindow.html)().[addView](https://api.kde.org/krita/html/classaddView.html)(d)
      
      add_document_to_window()
      ```
         @param width the width in pixels
         @param height the height in pixels
         @param name the name of the image (not the filename of the document)
         @param colorModel A string describing the color model of the image:
         <ul>
         <li>A: Alpha mask</li>
         <li>RGBA: RGB with alpha channel (The actual order of channels is most often BGR!)</li>
         <li>XYZA: XYZ with alpha channel</li>
         <li>LABA: LAB with alpha channel</li>
         <li>CMYKA: CMYK with alpha channel</li>
         <li>GRAYA: Gray with alpha channel</li>
         <li>YCbCrA: YCbCr with alpha channel</li>
         </ul>
         @param colorDepth A string describing the color depth of the image:
         <ul>
         <li>U8: unsigned 8 bits integer, the most common type</li>
         <li>U16: unsigned 16 bits integer</li>
         <li>F16: half, 16 bits floating point. Only available if Krita was built with OpenEXR</li>
         <li>F32: 32 bits floating point</li>
         </ul>
         @param profile The name of an icc profile that is known to Krita. If an empty string is passed, the default is
         taken.
         @param resolution the resolution in points per inch.
         @return the created document.
    """
    ...
  

  def openDocument(self, filename: str) -> "Document":
    """
      openDocument creates a new [Document](https://api.kde.org/krita/html/classDocument.html), registers it with the [Krita](https://api.kde.org/krita/html/classKrita.html) application and loads the given file.
      
      # Parameters
      
      - filename: str
      
        the file to open in the document
      
      # Returns
      
      the document
    """
    ...
  

  def openWindow(self) -> "Window":
    """
      openWindow create a new main window. The window is not shown by default.
    """
    ...
  

  def addExtension(self, extension: Extension) -> "None":
    """
      addExtension add the given plugin to [Krita](https://api.kde.org/krita/html/classKrita.html). There will be a single instance of each [Extension](https://api.kde.org/krita/html/classExtension.html) in the [Krita](https://api.kde.org/krita/html/classKrita.html) process.
      
      # Parameters
      
      - extension: Extension
      
        the extension to add.
    """
    ...
  

  def extensions(self) -> "List[Extension]":
    """
      
      
      return a list with all registered extension objects.
    """
    ...
  

  def addDockWidgetFactory(self, factory: DockWidgetFactoryBase) -> "None":
    """
      addDockWidgetFactory Add the given docker factory to the application. For scripts loaded on startup, this means that every window will have one of the dockers created by the factory.
      
      # Parameters
      
      - factory: DockWidgetFactoryBase
      
        The factory object.
    """
    ...
  

  def writeSetting(self, group: str, name: str, value: str) -> "None":
    """
      writeSetting write the given setting under the given name to the kritarc file in the given settings group.
      
      # Parameters
      
      - group: str
      
        The group the setting belongs to. If empty, then the setting is written in the general section
      
      - name: str
      
        The name of the setting
      
      - value: str
      
        The value of the setting. Script settings are always written as strings.
    """
    ...
  

  def readSetting(self, group: str, name: str, defaultValue: str) -> "str":
    """
      readSetting read the given setting value from the kritarc file.
      
      # Parameters
      
      - group: str
      
        The group the setting is part of. If empty, then the setting is read from the general group.
      
      - name: str
      
        The name of the setting
      
      - defaultValue: str
      
        The default value of the setting
      
      # Returns
      
      a string representing the setting.
    """
    ...
  

  def icon(self, iconName: str) -> "QIcon":
    """
      icon This allows you to get icons from [Krita](https://api.kde.org/krita/html/classKrita.html)'s internal icons.
      
      # Parameters
      
      - iconName: str
      
        name of the icon.
      
      # Returns
      
      the icon related to this name.
    """
    ...
  

  @staticmethod
  def instance() -> "Krita":
    """
      instance retrieve the singleton instance of the Application object.
    """
    ...
  

  @staticmethod
  def fromVariant(v: QVariant) -> "QObject":
    """
      
      
      Scripter.fromVariant(variant) variant is a QVariant returns instance of QObject-subclass
      
      This is a helper method for PyQt because PyQt cannot cast a variant to a QObject or QWidget
    """
    ...
  

  @staticmethod
  def krita_i18n(text: str) -> "str":
  
    ...
  

  @staticmethod
  def krita_i18nc(context: str, text: str) -> "str":
  
    ...
  

  @staticmethod
  def getAppDataLocation() -> "str":
  
    ...
  

class ManagedColor(QObject):

  """
    The [ManagedColor](https://api.kde.org/krita/html/classManagedColor.html) class is a class to handle colors that are color managed. A managed color is a color of which we know the model(RGB, LAB, CMYK, etc), the bitdepth and the specific properties of its colorspace, such as the whitepoint, chromaticities, trc, etc, as represented by the color profile.
    
    [Krita](https://api.kde.org/krita/html/classKrita.html) has two color management systems. LCMS and OCIO. LCMS is the one handling the ICC profile stuff, and the major one handling that [ManagedColor](https://api.kde.org/krita/html/classManagedColor.html) deals with. OCIO support is only in the display of the colors. [ManagedColor](https://api.kde.org/krita/html/classManagedColor.html) has some support for it in `colorForCanvas()`
    
    All colors in [Krita](https://api.kde.org/krita/html/classKrita.html) are color managed. QColors are understood as RGB-type colors in the sRGB space.
    
    We recommend you make a color like this:
    
    ```
    colorYellow = [ManagedColor](https://api.kde.org/krita/html/classManagedColor.html)("RGBA", "U8", "")
    QVector<float> yellowComponents = colorYellow.[components](https://api.kde.org/krita/html/classcomponents.html)()
    yellowComponents[0] = 1.0
    yellowComponents[1] = 1.0
    yellowComponents[2] = 0
    yellowComponents[3] = 1.0
    
    colorYellow.[setComponents](https://api.kde.org/krita/html/classsetComponents.html)(yellowComponents)
    QColor yellow = colorYellow.[colorForCanvas](https://api.kde.org/krita/html/classcolorForCanvas.html)(canvas)
    ```
  """

  def __init__(self, parent: QObject = None) -> None:
    """
      [ManagedColor](https://api.kde.org/krita/html/classManagedColor.html) Create a [ManagedColor](https://api.kde.org/krita/html/classManagedColor.html) that is black and transparent.
    """
    ...
  

  def __init__(self, colorModel: str, colorDepth: str, colorProfile: str, parent: QObject = None) -> None:
    """
      [ManagedColor](https://api.kde.org/krita/html/classManagedColor.html) create a managed color with the given color space properties.
      
      
      setColorModel() for more details.
    """
    ...
  

  def __init__(self, color: KoColor, parent: QObject = None) -> None:
  
    ...
  

  def colorForCanvas(self, canvas: Canvas) -> "QColor":
    """
      colorForCanvas
      
      # Parameters
      
      - canvas: Canvas
      
        the canvas whose color management you'd like to use. In [Krita](https://api.kde.org/krita/html/classKrita.html), different views have separate canvasses, and these can have different OCIO configurations active.
      
      # Returns
      
      the QColor as it would be displaying on the canvas. This result can be used to draw widgets with the correct configuration applied.
    """
    ...
  

  def colorDepth(self) -> "str":
    """
      
      
      colorDepth A string describing the color depth of the image: 
      
      - U8: unsigned 8 bits integer, the most common type
      - U16: unsigned 16 bits integer
      - F16: half, 16 bits floating point. Only available if [Krita](https://api.kde.org/krita/html/classKrita.html) was built with OpenEXR
      - F32: 32 bits floating point
      
      # Returns
      
      the color depth.
    """
    ...
  

  def colorModel(self) -> "str":
    """
      colorModel retrieve the current color model of this document:
      
      
      - A: Alpha mask
      - RGBA: RGB with alpha channel (The actual order of channels is most often BGR!)
      - XYZA: XYZ with alpha channel
      - LABA: LAB with alpha channel
      - CMYKA: CMYK with alpha channel
      - GRAYA: Gray with alpha channel
      - YCbCrA: YCbCr with alpha channel
      
      # Returns
      
      the internal color model string.
    """
    ...
  

  def colorProfile(self) -> "str":
    """
      
      
      # Returns
      
      the name of the current color profile
    """
    ...
  

  def setColorProfile(self, colorProfile: str) -> "bool":
    """
      setColorProfile set the color profile of the image to the given profile. The profile has to be registered with krita and be compatible with the current color model and depth; the image data is `not` converted.
      
      # Parameters
      
      - colorProfile: str
      
        
      
      # Returns
      
      false if the colorProfile name does not correspond to to a registered profile or if assigning the profile failed.
    """
    ...
  

  def setColorSpace(self, colorModel: str, colorDepth: str, colorProfile: str) -> "bool":
    """
      setColorSpace convert the nodes and the image to the given colorspace. The conversion is done with Perceptual as intent, High Quality and No LCMS Optimizations as flags and no blackpoint compensation.
      
      # Parameters
      
      - colorModel: str
      
        A string describing the color model of the image: 
      
      - A: Alpha mask
      - RGBA: RGB with alpha channel (The actual order of channels is most often BGR!)
      - XYZA: XYZ with alpha channel
      - LABA: LAB with alpha channel
      - CMYKA: CMYK with alpha channel
      - GRAYA: Gray with alpha channel
      - YCbCrA: YCbCr with alpha channel
      
      - colorDepth: str
      
        A string describing the color depth of the image: 
      
      - U8: unsigned 8 bits integer, the most common type
      - U16: unsigned 16 bits integer
      - F16: half, 16 bits floating point. Only available if [Krita](https://api.kde.org/krita/html/classKrita.html) was built with OpenEXR
      - F32: 32 bits floating point
      
      - colorProfile: str
      
        a valid color profile for this color model and color depth combination.
      
      # Returns
      
      false the combination of these arguments does not correspond to a colorspace.
    """
    ...
  

  def components(self) -> "List[float]":
    """
      components
      
      # Returns
      
      a QVector containing the channel/components of this color normalized. This includes the alphachannel.
    """
    ...
  

  def componentsOrdered(self) -> "List[float]":
    """
      [componentsOrdered()](https://api.kde.org/krita/html/classcomponentsOrdered().html)
      
      # Returns
      
      same as Components, except the values are ordered to the display.
    """
    ...
  

  def setComponents(self, values: List[float]) -> "None":
    """
      setComponents Set the channel/components with normalized values. For integer colorspace, this obviously means the limit is between 0.0-1.0, but for floating point colorspaces, 2.4 or 103.5 are still meaningful (if bright) values.
      
      # Parameters
      
      - values: List[float]
      
        the QVector containing the new channel/component values. These should be normalized.
    """
    ...
  

  def toXML(self) -> "str":
    """
      
      
      Serialize this color following Create's swatch color specification available at [https://web.archive.org/web/20110826002520/http://create.freedesktop.org/wiki/Swatches_-_color_file_format/Draft](https://web.archive.org/web/20110826002520/http://create.freedesktop.org/wiki/Swatches_-_color_file_format/Draft)
    """
    ...
  

  def fromXML(self, xml: str) -> "None":
    """
      
      
      Unserialize a color following Create's swatch color specification available at [https://web.archive.org/web/20110826002520/http://create.freedesktop.org/wiki/Swatches_-_color_file_format/Draft](https://web.archive.org/web/20110826002520/http://create.freedesktop.org/wiki/Swatches_-_color_file_format/Draft)
      
      # Parameters
      
      - xml: str
      
        an XML color
      
      # Returns
      
      the unserialized color, or an empty color object if the function failed to unserialize the color
    """
    ...
  

  def toQString(self) -> "str":
    """
      toQString create a user-visible string of the channel names and the channel values
      
      # Returns
      
      a string that can be used to display the values of this color to the user.
    """
    ...
  

  @staticmethod
  def fromQColor(qcolor: QColor, canvas: Canvas = None) -> "ManagedColor":
    """
      fromQColor is the (approximate) reverse of [colorForCanvas()](https://api.kde.org/krita/html/classcolorForCanvas().html)
      
      # Parameters
      
      - qcolor: QColor
      
        the QColor to convert to a KoColor.
      
      - canvas: Canvas = `None`
      
        the canvas whose color management you'd like to use.
      
      # Returns
      
      the approximated [ManagedColor](https://api.kde.org/krita/html/classManagedColor.html), to use for canvas resources.
    """
    ...
  

class Node(QObject):

  """
    
    
    [Node](https://api.kde.org/krita/html/classNode.html) represents a layer or mask in a [Krita](https://api.kde.org/krita/html/classKrita.html) image's [Node](https://api.kde.org/krita/html/classNode.html) hierarchy. Group layers can contain other layers and masks; layers can contain masks.
  """

  @staticmethod
  def createNode(image: KisImageSP, node: KisNodeSP, parent: QObject = None) -> "Node":
  
    ...
  

  def clone(self) -> "Node":
    """
      clone clone the current node. The node is not associated with any image.
    """
    ...
  

  def alphaLocked(self) -> "bool":
    """
      alphaLocked checks whether the node is a paint layer and returns whether it is alpha locked
      
      # Returns
      
      whether the paint layer is alpha locked, or false if the node is not a paint layer
    """
    ...
  

  def setAlphaLocked(self, value: bool) -> "None":
    """
      setAlphaLocked set the layer to value if the node is paint layer.
    """
    ...
  

  def blendingMode(self) -> "str":
    """
      
      
      
      KoCompositeOpRegistry.h
      
      # Returns
      
      the blending mode of the layer. The values of the blending modes are defined in
    """
    ...
  

  def setBlendingMode(self, value: str) -> "None":
    """
      setBlendingMode set the blending mode of the node to the given value
      
      
      KoCompositeOpRegistry.h
      
      # Parameters
      
      - value: str
      
        one of the string values from
    """
    ...
  

  def channels(self) -> "List[Channel]":
    """
      channels creates a list of [Channel](https://api.kde.org/krita/html/classChannel.html) objects that can be used individually to show or hide certain channels, and to retrieve the contents of each channel in a node separately.
      
      Only layers have channels, masks do not, and calling channels on a [Node](https://api.kde.org/krita/html/classNode.html) that is a mask will return an empty list.
      
      # Returns
      
      the list of channels ordered in by position of the channels in pixel position
    """
    ...
  

  def childNodes(self) -> "List[Node]":
    """
      childNodes
      
      # Returns
      
      returns a list of child nodes of the current node. The nodes are ordered from the bottommost up. The function is not recursive.
    """
    ...
  

  def findChildNodes(self, name: str = "", recursive: bool = False, partialMatch: bool = False, type: str = "", colorLabelIndex: int = 0) -> "List[Node]":
    """
      findChildNodes
      
      # Parameters
      
      - name: str = `""`
      
        name of the child node to search for. Leaving this blank will return all nodes.
      
      - recursive: bool = `False`
      
        whether or not to search recursively. Defaults to false.
      
      - partialMatch: bool = `False`
      
        return if the name partially contains the string (case insensitive). Defaults to false.
      
      - type: str = `""`
      
        filter returned nodes based on type
      
      - colorLabelIndex: int = `0`
      
        filter returned nodes based on color label index
      
      # Returns
      
      returns a list of child nodes and grand child nodes of the current node that match the search criteria.
    """
    ...
  

  def addChildNode(self, child: Node, above: Node) -> "bool":
    """
      addChildNode adds the given node in the list of children.
      
      # Parameters
      
      - child: Node
      
        the node to be added
      
      - above: Node
      
        the node above which this node will be placed
      
      # Returns
      
      false if adding the node failed
    """
    ...
  

  def removeChildNode(self, child: Node) -> "bool":
    """
      removeChildNode removes the given node from the list of children.
      
      # Parameters
      
      - child: Node
      
        the node to be removed
    """
    ...
  

  def setChildNodes(self, nodes: List[Node]) -> "None":
    """
      setChildNodes this replaces the existing set of child nodes with the new set.
      
      # Parameters
      
      - nodes: List[Node]
      
        The list of nodes that will become children, bottom-up - the first node, is the bottom-most node in the stack.
    """
    ...
  

  def colorDepth(self) -> "str":
    """
      
      
      colorDepth A string describing the color depth of the image: 
      
      - U8: unsigned 8 bits integer, the most common type
      - U16: unsigned 16 bits integer
      - F16: half, 16 bits floating point. Only available if [Krita](https://api.kde.org/krita/html/classKrita.html) was built with OpenEXR
      - F32: 32 bits floating point
      
      # Returns
      
      the color depth.
    """
    ...
  

  def colorModel(self) -> "str":
    """
      colorModel retrieve the current color model of this document:
      
      
      - A: Alpha mask
      - RGBA: RGB with alpha channel (The actual order of channels is most often BGR!)
      - XYZA: XYZ with alpha channel
      - LABA: LAB with alpha channel
      - CMYKA: CMYK with alpha channel
      - GRAYA: Gray with alpha channel
      - YCbCrA: YCbCr with alpha channel
      
      # Returns
      
      the internal color model string.
    """
    ...
  

  def colorProfile(self) -> "str":
    """
      
      
      # Returns
      
      the name of the current color profile
    """
    ...
  

  def setColorProfile(self, colorProfile: str) -> "bool":
    """
      setColorProfile set the color profile of the image to the given profile. The profile has to be registered with krita and be compatible with the current color model and depth; the image data is `not` converted.
      
      # Parameters
      
      - colorProfile: str
      
        
      
      # Returns
      
      if assigning the color profile worked
    """
    ...
  

  def setColorSpace(self, colorModel: str, colorDepth: str, colorProfile: str) -> "bool":
    """
      setColorSpace convert the node to the given colorspace
      
      # Parameters
      
      - colorModel: str
      
        A string describing the color model of the node: 
      
      - A: Alpha mask
      - RGBA: RGB with alpha channel (The actual order of channels is most often BGR!)
      - XYZA: XYZ with alpha channel
      - LABA: LAB with alpha channel
      - CMYKA: CMYK with alpha channel
      - GRAYA: Gray with alpha channel
      - YCbCrA: YCbCr with alpha channel
      
      - colorDepth: str
      
        A string describing the color depth of the image: 
      
      - U8: unsigned 8 bits integer, the most common type
      - U16: unsigned 16 bits integer
      - F16: half, 16 bits floating point. Only available if [Krita](https://api.kde.org/krita/html/classKrita.html) was built with OpenEXR
      - F32: 32 bits floating point
      
      - colorProfile: str
      
        a valid color profile for this color model and color depth combination.
    """
    ...
  

  def animated(self) -> "bool":
    """
      [Krita](https://api.kde.org/krita/html/classKrita.html) layers can be animated, i.e., have frames.
      
      # Returns
      
      return true if the layer has frames. Currently, the scripting framework does not give access to the animation features.
    """
    ...
  

  def enableAnimation(self) -> "None":
    """
      enableAnimation make the current layer animated, so it can have frames.
    """
    ...
  

  def setPinnedToTimeline(self, pinned: bool) -> "None":
    """
      Sets whether or not node should be pinned to the Timeline Docker, regardless of selection activity.
    """
    ...
  

  def isPinnedToTimeline(self) -> "bool":
    """
      
      
      # Returns
      
      Returns true if node is pinned to the Timeline Docker or false if it is not.
    """
    ...
  

  def setCollapsed(self, collapsed: bool) -> "None":
    """
      
      
      Sets the state of the node to the value of
      
      # Parameters
      
      - collapsed: bool
    """
    ...
  

  def collapsed(self) -> "bool":
    """
      
      
      returns the collapsed state of this node
    """
    ...
  

  def colorLabel(self) -> "int":
    """
      
      
      Sets a color label index associated to the layer. The actual color of the label and the number of available colors is defined by [Krita](https://api.kde.org/krita/html/classKrita.html) GUI configuration.
    """
    ...
  

  def setColorLabel(self, index: int) -> "None":
    """
      setColorLabel sets a color label index associated to the layer. The actual color of the label and the number of available colors is defined by [Krita](https://api.kde.org/krita/html/classKrita.html) GUI configuration.
      
      # Parameters
      
      - index: int
      
        an integer corresponding to the set of available color labels.
    """
    ...
  

  def inheritAlpha(self) -> "bool":
    """
      inheritAlpha checks whether this node has the inherits alpha flag set
      
      # Returns
      
      true if the Inherit Alpha is set
    """
    ...
  

  def setInheritAlpha(self, value: bool) -> "None":
    """
      
      
      set the Inherit Alpha flag to the given value
    """
    ...
  

  def locked(self) -> "bool":
    """
      locked checks whether the [Node](https://api.kde.org/krita/html/classNode.html) is locked. A locked node cannot be changed.
      
      # Returns
      
      true if the [Node](https://api.kde.org/krita/html/classNode.html) is locked, false if it hasn't been locked.
    """
    ...
  

  def setLocked(self, value: bool) -> "None":
    """
      
      
      set the Locked flag to the give value
    """
    ...
  

  def hasExtents(self) -> "bool":
    """
      does the node have any content in it?
      
      # Returns
      
      if node has any content in it
    """
    ...
  

  def name(self) -> "str":
    """
      
      
      # Returns
      
      the user-visible name of this node.
    """
    ...
  

  def setName(self, name: str) -> "None":
    """
      
      
      rename the [Node](https://api.kde.org/krita/html/classNode.html) to the given name
    """
    ...
  

  def opacity(self) -> "int":
    """
      
      
      return the opacity of the [Node](https://api.kde.org/krita/html/classNode.html). The opacity is a value between 0 and 255.
    """
    ...
  

  def setOpacity(self, value: int) -> "None":
    """
      
      
      set the opacity of the [Node](https://api.kde.org/krita/html/classNode.html) to the given value. The opacity is a value between 0 and 255.
    """
    ...
  

  def parentNode(self) -> "Node":
    """
      
      
      return the [Node](https://api.kde.org/krita/html/classNode.html) that is the parent of the current [Node](https://api.kde.org/krita/html/classNode.html), or 0 if this is the root [Node](https://api.kde.org/krita/html/classNode.html).
    """
    ...
  

  def type(self) -> "str":
    """
      type [Krita](https://api.kde.org/krita/html/classKrita.html) has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
      
      
      If the [Node](https://api.kde.org/krita/html/classNode.html) object isn't wrapping a valid [Krita](https://api.kde.org/krita/html/classKrita.html) layer or mask object, and empty string is returned.
      
      # Returns
      
      The type of the node. Valid types are: 
      
      - paintlayer
      - grouplayer
      - filelayer
      - filterlayer
      - filllayer
      - clonelayer
      - vectorlayer
      - transparencymask
      - filtermask
      - transformmask
      - selectionmask
      - colorizemask
    """
    ...
  

  def icon(self) -> "QIcon":
    """
      icon
      
      # Returns
      
      the icon associated with the layer.
    """
    ...
  

  def visible(self) -> "bool":
    """
      
      
      Check whether the current [Node](https://api.kde.org/krita/html/classNode.html) is visible in the layer stack
    """
    ...
  

  def hasKeyframeAtTime(self, frameNumber: int) -> "bool":
    """
      
      
      Check to see if frame number on layer is a keyframe
    """
    ...
  

  def setVisible(self, visible: bool) -> "None":
    """
      
      
      Set the visibility of the current node to
      
      # Parameters
      
      - visible: bool
    """
    ...
  

  def pixelData(self, x: int, y: int, w: int, h: int) -> "QByteArray":
    """
      pixelData reads the given rectangle from the [Node](https://api.kde.org/krita/html/classNode.html)'s paintable pixels, if those exist, and returns it as a byte array. The pixel data starts top-left, and is ordered row-first.
      
      The byte array can be interpreted as follows: 8 bits images have one byte per channel, and as many bytes as there are channels. 16 bits integer images have two bytes per channel, representing an unsigned short. 16 bits float images have two bytes per channel, representing a half, or 16 bits float. 32 bits float images have four bytes per channel, representing a float.
      
      You can read outside the node boundaries; those pixels will be transparent black.
      
      The order of channels is:
      
      - Integer RGBA: Blue, Green, Red, Alpha
      - Float RGBA: Red, Green, Blue, Alpha
      - GrayA: Gray, Alpha
      - [Selection](https://api.kde.org/krita/html/classSelection.html): selectedness
      - LabA: L, a, b, Alpha
      - CMYKA: Cyan, Magenta, Yellow, Key, Alpha
      - XYZA: X, Y, Z, A
      - YCbCrA: Y, Cb, Cr, Alpha
      
      The byte array is a copy of the original node data. In Python, you can use bytes, bytearray and the struct module to interpret the data and construct, for instance, a Pillow Image object.
      
      If you read the pixeldata of a mask, a filter or generator layer, you get the selection bytes, which is one channel with values in the range from 0..255.
      
      If you want to change the pixels of a node you can write the pixels back after manipulation with `setPixelData()`. This will only succeed on nodes with writable pixel data, e.g not on groups or file layers.
      
      # Parameters
      
      - x: int
      
        x position from where to start reading
      
      - y: int
      
        y position from where to start reading
      
      - w: int
      
        row length to read
      
      - h: int
      
        number of rows to read
      
      # Returns
      
      a QByteArray with the pixel data. The byte array may be empty.
    """
    ...
  

  def pixelDataAtTime(self, x: int, y: int, w: int, h: int, time: int) -> "QByteArray":
    """
      pixelDataAtTime a basic function to get pixeldata from an animated node at a given time.
      
      # Parameters
      
      - x: int
      
        the position from the left to start reading.
      
      - y: int
      
        the position from the top to start reader
      
      - w: int
      
        the row length to read
      
      - h: int
      
        the number of rows to read
      
      - time: int
      
        the frame number
      
      # Returns
      
      a QByteArray with the pixel data. The byte array may be empty.
    """
    ...
  

  def projectionPixelData(self, x: int, y: int, w: int, h: int) -> "QByteArray":
    """
      projectionPixelData reads the given rectangle from the [Node](https://api.kde.org/krita/html/classNode.html)'s projection (that is, what the node looks like after all sub-Nodes (like layers in a group or masks on a layer) have been applied, and returns it as a byte array. The pixel data starts top-left, and is ordered row-first.
      
      The byte array can be interpreted as follows: 8 bits images have one byte per channel, and as many bytes as there are channels. 16 bits integer images have two bytes per channel, representing an unsigned short. 16 bits float images have two bytes per channel, representing a half, or 16 bits float. 32 bits float images have four bytes per channel, representing a float.
      
      You can read outside the node boundaries; those pixels will be transparent black.
      
      The order of channels is:
      
      - Integer RGBA: Blue, Green, Red, Alpha
      - Float RGBA: Red, Green, Blue, Alpha
      - GrayA: Gray, Alpha
      - [Selection](https://api.kde.org/krita/html/classSelection.html): selectedness
      - LabA: L, a, b, Alpha
      - CMYKA: Cyan, Magenta, Yellow, Key, Alpha
      - XYZA: X, Y, Z, A
      - YCbCrA: Y, Cb, Cr, Alpha
      
      The byte array is a copy of the original node data. In Python, you can use bytes, bytearray and the struct module to interpret the data and construct, for instance, a Pillow Image object.
      
      If you read the projection of a mask, you get the selection bytes, which is one channel with values in the range from 0..255.
      
      If you want to change the pixels of a node you can write the pixels back after manipulation with `setPixelData()`. This will only succeed on nodes with writable pixel data, e.g not on groups or file layers.
      
      # Parameters
      
      - x: int
      
        x position from where to start reading
      
      - y: int
      
        y position from where to start reading
      
      - w: int
      
        row length to read
      
      - h: int
      
        number of rows to read
      
      # Returns
      
      a QByteArray with the pixel data. The byte array may be empty.
    """
    ...
  

  def setPixelData(self, value: QByteArray, x: int, y: int, w: int, h: int) -> "bool":
    """
      setPixelData writes the given bytes, of which there must be enough, into the [Node](https://api.kde.org/krita/html/classNode.html), if the [Node](https://api.kde.org/krita/html/classNode.html) has writable pixel data:
      
      
      - paint layer: the layer's original pixels are overwritten
      - filter layer, generator layer, any mask: the embedded selection's pixels are overwritten. `Note:` for these
      
      File layers, Group layers, Clone layers cannot be written to. Calling setPixelData on those layer types will silently do nothing.
      
      # Parameters
      
      - value: QByteArray
      
        the byte array representing the pixels. There must be enough bytes available. [Krita](https://api.kde.org/krita/html/classKrita.html) will take the raw pointer from the QByteArray and start reading, not stopping before (number of channels * size of channel * w * h) bytes are read.
      
      - x: int
      
        the x position to start writing from
      
      - y: int
      
        the y position to start writing from
      
      - w: int
      
        the width of each row
      
      - h: int
      
        the number of rows to write
      
      # Returns
      
      true if writing the pixeldata worked
    """
    ...
  

  def bounds(self) -> "QRect":
    """
      bounds return the exact bounds of the node's paint device
      
      # Returns
      
      the bounds, or an empty QRect if the node has no paint device or is empty.
    """
    ...
  

  def move(self, x: int, y: int) -> "None":
    """
      
      
      move the pixels to the given x, y location in the image coordinate space.
    """
    ...
  

  def position(self) -> "QPoint":
    """
      position returns the position of the paint device of this node. The position is always 0,0 unless the layer has been moved. If you want to know the topleft position of the rectangle around the actual non-transparent pixels in the node, use [bounds()](https://api.kde.org/krita/html/classbounds().html).
      
      # Returns
      
      the top-left position of the node
    """
    ...
  

  def remove(self) -> "bool":
    """
      remove removes this node from its parent image.
    """
    ...
  

  def duplicate(self) -> "Node":
    """
      duplicate returns a full copy of the current node. The node is not inserted in the graphic
      
      # Returns
      
      a valid [Node](https://api.kde.org/krita/html/classNode.html) object or 0 if the node couldn't be duplicated.
    """
    ...
  

  def save(self, filename: str, xRes: float, yRes: float, exportConfiguration: InfoObject, exportRect: QRect = QRect()) -> "bool":
    """
      save exports the given node with this filename. The extension of the filename determines the filetype.
      
      # Parameters
      
      - filename: str
      
        the filename including extension
      
      - xRes: float
      
        the horizontal resolution in pixels per pt (there are 72 pts in an inch)
      
      - yRes: float
      
        the horizontal resolution in pixels per pt (there are 72 pts in an inch)
      
      - exportConfiguration: InfoObject
      
        a configuration object appropriate to the file format.
      
      - exportRect: QRect = `QRect()`
      
        the export bounds for saving a node as a QRect If `exportRect` is empty, then save exactBounds() of the node. If you'd like to save the image- aligned area of the node, just pass image->`bounds()` there. See Document->exportImage for [InfoObject](https://api.kde.org/krita/html/classInfoObject.html) details.
      
      # Returns
      
      true if saving succeeded, false if it failed.
    """
    ...
  

  def mergeDown(self) -> "Node":
    """
      mergeDown merges the given node with the first visible node underneath this node in the layerstack. This will drop all per-layer metadata.
    """
    ...
  

  def scaleNode(self, origin: QPointF, width: int, height: int, strategy: str) -> "None":
    """
      scaleNode
      
      # Parameters
      
      - origin: QPointF
      
        the origin point
      
      - width: int
      
        the width
      
      - height: int
      
        the height
      
      - strategy: str
      
        the scaling strategy. There's several ones amongst these that aren't available in the regular UI. 
      
      - Hermite
      - Bicubic - Adds pixels using the color of surrounding pixels. Produces smoother tonal gradations than Bilinear.
      - Box - Replicate pixels in the image. Preserves all the original detail, but can produce jagged effects.
      - Bilinear - Adds pixels averaging the color values of surrounding pixels. Produces medium quality results when the image is scaled from half to two times the original size.
      - Bell
      - BSpline
      - Lanczos3 - Offers similar results than Bicubic, but maybe a little bit sharper. Can produce light and dark halos along strong edges.
      - Mitchell
    """
    ...
  

  def rotateNode(self, radians: float) -> "None":
    """
      rotateNode rotate this layer by the given radians.
      
      # Parameters
      
      - radians: float
      
        amount the layer should be rotated in, in radians.
    """
    ...
  

  def cropNode(self, x: int, y: int, w: int, h: int) -> "None":
    """
      cropNode crop this layer.
      
      # Parameters
      
      - x: int
      
        the left edge of the cropping rectangle.
      
      - y: int
      
        the top edge of the cropping rectangle
      
      - w: int
      
        the right edge of the cropping rectangle
      
      - h: int
      
        the bottom edge of the cropping rectangle
    """
    ...
  

  def shearNode(self, angleX: float, angleY: float) -> "None":
    """
      shearNode perform a shear operation on this node.
      
      # Parameters
      
      - angleX: float
      
        the X-angle in degrees to shear by
      
      - angleY: float
      
        the Y-angle in degrees to shear by
    """
    ...
  

  def thumbnail(self, w: int, h: int) -> "QImage":
    """
      thumbnail create a thumbnail of the given dimensions. The thumbnail is sized according to the layer dimensions, not the image dimensions. If the requested size is too big a null QImage is created. If the current node cannot generate a thumbnail, a transparent QImage of the requested size is generated.
      
      # Returns
      
      a QImage representing the layer contents.
    """
    ...
  

  def layerStyleToAsl(self) -> "str":
    """
      layerStyleToAsl retrieve the current layer's style in ASL format.
      
      # Returns
      
      a QString in ASL format representing the layer style.
    """
    ...
  

  def setLayerStyleFromAsl(self, asl: str) -> "bool":
    """
      setLayerStyleFromAsl set a new layer style for this node.
      
      # Parameters
      
      - aslContent
      
        a string formatted in ASL format containing the layer style
      
      # Returns
      
      true if layer style was set, false if failed.
    """
    ...
  

  def index(self) -> "int":
    """
      index the index of the node inside the parent
      
      # Returns
      
      an integer representing the node's index inside the parent
    """
    ...
  

  def uniqueId(self) -> "QUuid":
    """
      uniqueId uniqueId of the node
      
      # Returns
      
      a QUuid representing a unique id to identify the node
    """
    ...
  

class Notifier(QObject):

  """
    
    
    The [Notifier](https://api.kde.org/krita/html/classNotifier.html) can be used to be informed of state changes in the [Krita](https://api.kde.org/krita/html/classKrita.html) application.
  """

  def __init__(self, parent: QObject = None) -> None:
  
    ...
  

  def active(self) -> "bool":
    """
      
      
      # Returns
      
      true if the [Notifier](https://api.kde.org/krita/html/classNotifier.html) is active.
    """
    ...
  

  def setActive(self, value: bool) -> "None":
    """
      
      
      Enable or disable the [Notifier](https://api.kde.org/krita/html/classNotifier.html)
    """
    ...
  

  applicationClosing: pyqtSignal
  """
    applicationClosing is emitted when the application is about to close. This happens after any documents and windows are closed.
  """
  

  imageCreated: pyqtSignal
  """
    imageCreated is emitted whenever a new image is created and registered with the application.
  """
  

  imageSaved: pyqtSignal
  """
    imageSaved is emitted whenever a document is saved.
    
    # Parameters
    
    - filename: str
    
      the filename of the document that has been saved.
  """
  

  imageClosed: pyqtSignal
  """
    imageClosed is emitted whenever the last view on an image is closed. The image does not exist anymore in [Krita](https://api.kde.org/krita/html/classKrita.html)
    
    # Parameters
    
    - filename: str
    
      the filename of the image.
  """
  

  viewCreated: pyqtSignal
  """
    viewCreated is emitted whenever a new view is created.
    
    # Parameters
    
    - view: View
    
      the view
  """
  

  viewClosed: pyqtSignal
  """
    viewClosed is emitted whenever a view is closed
    
    # Parameters
    
    - view: View
    
      the view
  """
  

  windowIsBeingCreated: pyqtSignal
  """
    windowCreated is emitted whenever a window is being created
    
    # Parameters
    
    - window: Window
    
      the window; this is called from the constructor of the window, before the xmlgui file is loaded
  """
  

  windowCreated: pyqtSignal
  """
    windowIsCreated is emitted after main window is completely created
  """
  

  configurationChanged: pyqtSignal
  """
    configurationChanged is emitted every time [Krita](https://api.kde.org/krita/html/classKrita.html)'s configuration has changed.
  """
  

class Palette(QObject):

  """
    The [Palette](https://api.kde.org/krita/html/classPalette.html) class [Palette](https://api.kde.org/krita/html/classPalette.html) is a resource object that stores organised color data. It's purpose is to allow artists to save colors and store them.
    
    An example for printing all the palettes and the entries:
    
    ```
    import sys
    from krita import *
    
    resources = Application.resources("palette")
    
    for (k, v) in resources.items():
      print(k)
      palette = [Palette](https://api.kde.org/krita/html/classPalette.html)(v)
      for x in range(palette.numberOfEntries()):
      entry = palette.[colorSetEntryByIndex](https://api.kde.org/krita/html/classcolorSetEntryByIndex.html)(x)
      c = palette.colorForEntry(entry);
      print(x, entry.name(), entry.id(), entry.spotColor(), c.toQString())
    ```
  """

  def __init__(self, resource: Resource) -> None:
  
    ...
  

  def numberOfEntries(self) -> "int":
    """
      numberOfEntries
      
      # Returns
    """
    ...
  

  def columnCount(self) -> "int":
    """
      columnCount
      
      # Returns
      
      the amount of columns this palette is set to use.
    """
    ...
  

  def setColumnCount(self, columns: int) -> "None":
    """
      setColumnCount Set the amount of columns this palette should use.
    """
    ...
  

  def comment(self) -> "str":
    """
      comment
      
      # Returns
      
      the comment or description associated with the palette.
    """
    ...
  

  def setComment(self, comment: str) -> "None":
    """
      setComment set the comment or description associated with the palette.
      
      # Parameters
      
      - comment: str
    """
    ...
  

  def groupNames(self) -> "List[str]":
    """
      groupNames
      
      # Returns
      
      the list of group names. This is list is in the order these groups are in the file.
    """
    ...
  

  def addGroup(self, name: str) -> "None":
    """
      addGroup
      
      # Parameters
      
      - name: str
      
        of the new group
      
      # Returns
      
      whether adding the group was successful.
    """
    ...
  

  def removeGroup(self, name: str, keepColors: bool = True) -> "None":
    """
      removeGroup
      
      # Parameters
      
      - name: str
      
        the name of the group to remove.
      
      - keepColors: bool = `True`
      
        whether or not to delete all the colors inside, or to move them to the default group.
      
      # Returns
    """
    ...
  

  def colorsCountTotal(self) -> "int":
    """
      colorsCountTotal
      
      # Returns
      
      the total amount of entries in the whole group
    """
    ...
  

  def colorSetEntryByIndex(self, index: int) -> "Swatch":
    """
      colorSetEntryByIndex get the colorsetEntry from the global index.
      
      # Parameters
      
      - index: int
      
        the global index
      
      # Returns
      
      the colorset entry
    """
    ...
  

  def colorSetEntryFromGroup(self, index: int, groupName: str) -> "Swatch":
    """
      colorSetEntryFromGroup
      
      # Parameters
      
      - index: int
      
        index in the group.
      
      - groupName: str
      
        the name of the group to get the color from.
      
      # Returns
      
      the colorsetentry.
    """
    ...
  

  def addEntry(self, entry: Swatch, groupName: str = "") -> "None":
    """
      addEntry add an entry to a group. Gets appended to the end.
      
      # Parameters
      
      - entry: Swatch
      
        the entry
      
      - groupName: str = `""`
      
        the name of the group to add to.
    """
    ...
  

  def removeEntry(self, index: int, groupName: str) -> "None":
    """
      removeEntry remove the entry at `index` from the group `groupName`.
    """
    ...
  

  def changeGroupName(self, oldGroupName: str, newGroupName: str) -> "None":
    """
      changeGroupName change the group name.
      
      # Parameters
      
      - oldGroupName: str
      
        the old groupname to change.
      
      - newGroupName: str
      
        the new name to change it into.
      
      # Returns
      
      whether successful. Reasons for failure include not knowing have oldGroupName
    """
    ...
  

  def moveGroup(self, groupName: str, groupNameInsertBefore: str = "") -> "None":
    """
      moveGroup move the group to before groupNameInsertBefore.
      
      # Parameters
      
      - groupName: str
      
        group to move.
      
      - groupNameInsertBefore: str = `""`
      
        group to inset before.
      
      # Returns
      
      whether successful. Reasons for failure include either group not existing.
    """
    ...
  

  def save(self) -> "bool":
    """
      save save the palette
      
      # Returns
      
      whether it was successful.
    """
    ...
  

class PaletteView(QWidget):

  """
    The [PaletteView](https://api.kde.org/krita/html/classPaletteView.html) class is a wrapper around a MVC method for handling palettes. This class shows a nice widget that can drag and drop, edit colors in a colorset and will handle adding and removing entries if you'd like it to.
  """

  def __init__(self, parent: QWidget = None) -> None:
  
    ...
  

  def setPalette(self, palette: Palette) -> "None":
    """
      setPalette Set a new palette.
      
      # Parameters
      
      - palette: Palette
    """
    ...
  

  def addEntryWithDialog(self, color: ManagedColor) -> "bool":
    """
      addEntryWithDialog This gives a simple dialog for adding colors, with options like adding name, id, and to which group the color should be added.
      
      # Parameters
      
      - color: ManagedColor
      
        the default color to add
      
      # Returns
      
      whether it was successful.
    """
    ...
  

  def addGroupWithDialog(self) -> "bool":
    """
      addGroupWithDialog gives a little dialog to ask for the desired groupname.
      
      # Returns
      
      whether this was successful.
    """
    ...
  

  def removeSelectedEntryWithDialog(self) -> "bool":
    """
      removeSelectedEntryWithDialog removes the selected entry. If it is a group, it pop up a dialog asking whether the colors should also be removed.
      
      # Returns
      
      whether this was successful
    """
    ...
  

  def trySelectClosestColor(self, color: ManagedColor) -> "None":
    """
      trySelectClosestColor tries to select the closest color to the one given. It does not force a change on the active color.
      
      # Parameters
      
      - color: ManagedColor
      
        the color to compare to.
    """
    ...
  

  entrySelectedForeGround: pyqtSignal
  """
    entrySelectedForeGround fires when a swatch is selected with leftclick.
    
    # Parameters
    
    - entry: Swatch
  """
  

  entrySelectedBackGround: pyqtSignal
  """
    entrySelectedBackGround fires when a swatch is selected with rightclick.
    
    # Parameters
    
    - entry: Swatch
  """
  

class Preset(QObject):

  """
    The [Preset](https://api.kde.org/krita/html/classPreset.html) class [Preset](https://api.kde.org/krita/html/classPreset.html) is a resource object that stores brush preset data.
    
    An example for printing the current brush preset and all its settings:
    
    ```
    from krita import *
    
    view = Krita.instance().activeWindow().activeView()
    preset = Preset(view.currentBrushPreset())
    
    print ( preset.toXML() )
    ```
  """

  def __init__(self, resource: Resource) -> None:
  
    ...
  

  def toXML(self) -> "str":
    """
      toXML convert the preset settings into a preset formatted xml.
      
      # Returns
      
      the xml in a string.
    """
    ...
  

  def fromXML(self, xml: str) -> "None":
    """
      fromXML convert the preset settings into a preset formatted xml.
      
      # Parameters
      
      - xml: str
      
        valid xml preset string.
    """
    ...
  

class PresetChooser(KisPresetChooser, QWidget):

  """
    The [PresetChooser](https://api.kde.org/krita/html/classPresetChooser.html) widget wraps the KisPresetChooser widget. The widget provides for selecting brush presets. It has a tagging bar and a filter field. It is not automatically synchronized with the currently selected preset in the current Windows.
  """

  def __init__(self, parent: QWidget = None) -> None:
  
    ...
  

  def setCurrentPreset(self, resource: Resource) -> "None":
    """
      
      
      Make the given preset active.
    """
    ...
  

  def currentPreset(self) -> "Resource":
    """
      
      
      # Returns
      
      a [Resource](https://api.kde.org/krita/html/classResource.html) wrapper around the currently selected preset.
    """
    ...
  

  presetSelected: pyqtSignal
  """
    
    
    Emitted whenever a user selects the given preset.
  """
  

  presetClicked: pyqtSignal
  """
    
    
    Emitted whenever a user clicks on the given preset.
  """
  

class Resource(QObject):

  """
    
    
    A [Resource](https://api.kde.org/krita/html/classResource.html) represents a gradient, pattern, brush tip, brush preset, palette or workspace definition.
    
    ```
    allPresets = Application.resources("preset")
    for preset in allPresets:
      print(preset.name())
    ```
    
    Resources are identified by their type, name and filename. If you want to change the contents of a resource, you should read its data using data(), parse it and write the changed contents back.
  """

  def __init__(self, resourceId: int, type: str, name: str, filename: str, image: QImage, parent: QObject = None) -> None:
  
    ...
  

  def __init__(self, resource: KoResourceSP, type: str, parent: QObject = None) -> None:
  
    ...
  

  def __init__(self, rhs: Resource) -> None:
  
    ...
  

  def type(self) -> "str":
    """
      
      
      Return the type of this resource. Valid types are: 
      
      - pattern: a raster image representing a pattern
      - gradient: a gradient
      - brush: a brush tip
      - preset: a brush preset
      - palette: a color set
      - workspace: a workspace definition.
    """
    ...
  

  def name(self) -> "str":
    """
      
      
      The user-visible name of the resource.
    """
    ...
  

  def setName(self, value: str) -> "None":
    """
      
      
      setName changes the user-visible name of the current resource.
    """
    ...
  

  def filename(self) -> "str":
    """
      
      
      The filename of the resource, if present. Not all resources are loaded from files.
    """
    ...
  

  def image(self) -> "QImage":
    """
      
      
      An image that can be used to represent the resource in the user interface. For some resources, like patterns, the image is identical to the resource, for others it's a mere icon.
    """
    ...
  

  def setImage(self, image: QImage) -> "None":
    """
      
      
      Change the image for this resource.
    """
    ...
  

class Scratchpad(QWidget):

  """
    The [Scratchpad](https://api.kde.org/krita/html/classScratchpad.html) class A scratchpad is a type of blank canvas area that can be painted on with the normal painting devices.
  """

  def __init__(self, view: View, defaultColor: QColor, parent: QWidget = None) -> None:
  
    ...
  

  def clear(self) -> "None":
    """
      Clears out scratchpad with color specified set during setup.
    """
    ...
  

  def setFillColor(self, color: QColor) -> "None":
    """
      Fill the entire scratchpad with a color.
      
      # Parameters
      
      - Color
      
        to fill the canvas with
    """
    ...
  

  def setModeManually(self, value: bool) -> "None":
    """
      Switches between a GUI controlling the current mode and when mouse clicks control mode.
      
      # Parameters
      
      - Setting
      
        to true allows GUI to control the mode with explicitly setting mode
    """
    ...
  

  def setMode(self, modeName: str) -> "None":
    """
      Manually set what mode scratchpad is in. Ignored if "setModeManually is set to false.
      
      # Parameters
      
      - Available
      
        options are: "painting", "panning", and "colorsampling"
    """
    ...
  

  def linkCanvasZoom(self, value: bool) -> "None":
    """
      Makes a connection between the zoom of the canvas and scratchpad area so they zoom in sync.
      
      # Parameters
      
      - Should
      
        the scratchpad share the zoom level. Default is true
    """
    ...
  

  def loadScratchpadImage(self, image: QImage) -> "None":
    """
      Load image data to the scratchpad.
      
      # Parameters
      
      - Image
      
        object to load
    """
    ...
  

  def copyScratchpadImageData(self) -> "QImage":
    """
      Take what is on the scratchpad area and grab image.
      
      # Returns
      
      the image data from the scratchpad
    """
    ...
  

class Selection(QObject):

  """
    
    
    [Selection](https://api.kde.org/krita/html/classSelection.html) represents a selection on [Krita](https://api.kde.org/krita/html/classKrita.html). A selection is not necessarily associated with a particular [Node](https://api.kde.org/krita/html/classNode.html) or Image.
    
    ```
    from krita import *
    
    d = Application.activeDocument()
    n = d.activeNode()
    r = n.bounds() 
    s = Selection()
    s.select(r.width() / 3, r.height() / 3, r.width() / 3, r.height() / 3, 255)
    s.cut(n)
    ```
  """

  def __init__(self, selection: KisSelectionSP, parent: QObject = None) -> None:
    """
      
      
      For internal use only.
    """
    ...
  

  def __init__(self, parent: QObject = None) -> None:
    """
      
      
      Create a new, empty selection object.
    """
    ...
  

  def duplicate(self) -> "Selection":
    """
      
      
      # Returns
      
      a duplicate of the selection
    """
    ...
  

  def width(self) -> "int":
    """
      
      
      # Returns
      
      the width of the selection
    """
    ...
  

  def height(self) -> "int":
    """
      
      
      # Returns
      
      the height of the selection
    """
    ...
  

  def x(self) -> "int":
    """
      
      
      # Returns
      
      the left-hand position of the selection.
    """
    ...
  

  def y(self) -> "int":
    """
      
      
      # Returns
      
      the top position of the selection.
    """
    ...
  

  def move(self, x: int, y: int) -> "None":
    """
      
      
      Move the selection's top-left corner to the given coordinates.
    """
    ...
  

  def clear(self) -> "None":
    """
      
      
      Make the selection entirely unselected.
    """
    ...
  

  def contract(self, value: int) -> "None":
    """
      
      
      Make the selection's width and height smaller by the given value. This will not move the selection's top-left position.
    """
    ...
  

  def copy(self, node: Node) -> "None":
    """
      copy copies the area defined by the selection from the node to the clipboard.
      
      # Parameters
      
      - node: Node
      
        the node from where the pixels will be copied.
    """
    ...
  

  def cut(self, node: Node) -> "None":
    """
      cut erases the area defined by the selection from the node and puts a copy on the clipboard.
      
      # Parameters
      
      - node: Node
      
        the node from which the selection will be cut.
    """
    ...
  

  def paste(self, destination: Node, x: int, y: int) -> "None":
    """
      paste pastes the content of the clipboard to the given node, limited by the area of the current selection.
      
      # Parameters
      
      - destination: Node
      
        the node where the pixels will be written
      
      - x: int
      
        the x position at which the clip will be written
      
      - y: int
      
        the y position at which the clip will be written
    """
    ...
  

  def erode(self) -> "None":
    """
      
      
      Erode the selection with a radius of 1 pixel.
    """
    ...
  

  def dilate(self) -> "None":
    """
      
      
      Dilate the selection with a radius of 1 pixel.
    """
    ...
  

  def border(self, xRadius: int, yRadius: int) -> "None":
    """
      
      
      Border the selection with the given radius.
    """
    ...
  

  def feather(self, radius: int) -> "None":
    """
      
      
      Feather the selection with the given radius.
    """
    ...
  

  def grow(self, xradius: int, yradius: int) -> "None":
    """
      
      
      Grow the selection with the given radius.
    """
    ...
  

  def shrink(self, xRadius: int, yRadius: int, edgeLock: bool) -> "None":
    """
      
      
      Shrink the selection with the given radius.
    """
    ...
  

  def smooth(self) -> "None":
    """
      
      
      Smooth the selection.
    """
    ...
  

  def invert(self) -> "None":
    """
      
      
      Invert the selection.
    """
    ...
  

  def resize(self, w: int, h: int) -> "None":
    """
      
      
      Resize the selection to the given width and height. The top-left position will not be moved.
    """
    ...
  

  def select(self, x: int, y: int, w: int, h: int, value: int) -> "None":
    """
      
      
      Select the given area. The value can be between 0 and 255; 0 is totally unselected, 255 is totally selected.
    """
    ...
  

  def selectAll(self, node: Node, value: int) -> "None":
    """
      
      
      Select all pixels in the given node. The value can be between 0 and 255; 0 is totally unselected, 255 is totally selected.
    """
    ...
  

  def replace(self, selection: Selection) -> "None":
    """
      
      
      Replace the current selection's selection with the one of the given selection.
    """
    ...
  

  def add(self, selection: Selection) -> "None":
    """
      
      
      Add the given selection's selected pixels to the current selection.
    """
    ...
  

  def subtract(self, selection: Selection) -> "None":
    """
      
      
      Subtract the given selection's selected pixels from the current selection.
    """
    ...
  

  def intersect(self, selection: Selection) -> "None":
    """
      
      
      Intersect the given selection with this selection.
    """
    ...
  

  def symmetricdifference(self, selection: Selection) -> "None":
    """
      
      
      Intersect with the inverse of the given selection with this selection.
    """
    ...
  

  def pixelData(self, x: int, y: int, w: int, h: int) -> "QByteArray":
    """
      pixelData reads the given rectangle from the [Selection](https://api.kde.org/krita/html/classSelection.html)'s mask and returns it as a byte array. The pixel data starts top-left, and is ordered row-first.
      
      The byte array will contain one byte for every pixel, representing the selectedness. 0 is totally unselected, 255 is fully selected.
      
      You can read outside the [Selection](https://api.kde.org/krita/html/classSelection.html)'s boundaries; those pixels will be unselected.
      
      The byte array is a copy of the original selection data.
      
      # Parameters
      
      - x: int
      
        x position from where to start reading
      
      - y: int
      
        y position from where to start reading
      
      - w: int
      
        row length to read
      
      - h: int
      
        number of rows to read
      
      # Returns
      
      a QByteArray with the pixel data. The byte array may be empty.
    """
    ...
  

  def setPixelData(self, value: QByteArray, x: int, y: int, w: int, h: int) -> "None":
    """
      setPixelData writes the given bytes, of which there must be enough, into the [Selection](https://api.kde.org/krita/html/classSelection.html).
      
      # Parameters
      
      - value: QByteArray
      
        the byte array representing the pixels. There must be enough bytes available. [Krita](https://api.kde.org/krita/html/classKrita.html) will take the raw pointer from the QByteArray and start reading, not stopping before (w * h) bytes are read.
      
      - x: int
      
        the x position to start writing from
      
      - y: int
      
        the y position to start writing from
      
      - w: int
      
        the width of each row
      
      - h: int
      
        the number of rows to write
    """
    ...
  

class SelectionMask(Node):

  """
    The [SelectionMask](https://api.kde.org/krita/html/classSelectionMask.html) class A selection mask is a mask type node that can be used to store selections. In the gui, these are referred to as local selections.
    
    A selection mask can hold both raster and vector selections, though the API only supports raster selections.
  """

  def __init__(self, image: KisImageSP, name: str, parent: QObject = None) -> None:
  
    ...
  

  def __init__(self, image: KisImageSP, mask: KisSelectionMaskSP, parent: QObject = None) -> None:
  
    ...
  

  def type(self) -> "str":
    """
      type [Krita](https://api.kde.org/krita/html/classKrita.html) has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
      
      
      If the [Node](https://api.kde.org/krita/html/classNode.html) object isn't wrapping a valid [Krita](https://api.kde.org/krita/html/classKrita.html) layer or mask object, and empty string is returned.
      
      # Returns
      
      selectionmask
    """
    ...
  

  def selection(self) -> "Selection":
  
    ...
  

  def setSelection(self, selection: Selection) -> "None":
  
    ...
  

class Shape(QObject):

  """
    The [Shape](https://api.kde.org/krita/html/classShape.html) class The shape class is a wrapper around [Krita](https://api.kde.org/krita/html/classKrita.html)'s vector objects.
    
    Some example code to parse through interesting information in a given vector layer with shapes. ```
    import sys
    from krita import *
    
    doc = Application.activeDocument()
    
    root = doc.rootNode()
    
    for layer in root.childNodes():
      print (str(layer.type())+" "+str(layer.name()))
      if (str(layer.type())=="vectorlayer"):
      for shape in layer.shapes():
      print(shape.[name](https://api.kde.org/krita/html/classname.html)())
      print(shape.[toSvg](https://api.kde.org/krita/html/classtoSvg.html)())
    ```
  """

  def __init__(self, shape: KoShape, parent: QObject = None) -> None:
  
    ...
  

  def name(self) -> "str":
    """
      name
      
      # Returns
      
      the name of the shape
    """
    ...
  

  def setName(self, name: str) -> "None":
    """
      setName
      
      # Parameters
      
      - name: str
      
        which name the shape should have.
    """
    ...
  

  def type(self) -> "str":
    """
      type
      
      # Returns
      
      the type of shape.
    """
    ...
  

  def zIndex(self) -> "int":
    """
      zIndex
      
      # Returns
      
      the zindex of the shape.
    """
    ...
  

  def setZIndex(self, zindex: int) -> "None":
    """
      setZIndex
      
      # Parameters
      
      - zindex: int
      
        set the shape zindex value.
    """
    ...
  

  def selectable(self) -> "bool":
    """
      selectable
      
      # Returns
      
      whether the shape is user selectable.
    """
    ...
  

  def setSelectable(self, selectable: bool) -> "None":
    """
      setSelectable
      
      # Parameters
      
      - selectable: bool
      
        whether the shape should be user selectable.
    """
    ...
  

  def geometryProtected(self) -> "bool":
    """
      geometryProtected
      
      # Returns
      
      whether the shape is protected from user changing the shape geometry.
    """
    ...
  

  def setGeometryProtected(self, protect: bool) -> "None":
    """
      setGeometryProtected
      
      # Parameters
      
      - protect: bool
      
        whether the shape should be geometry protected from the user.
    """
    ...
  

  def visible(self) -> "bool":
    """
      visible
      
      # Returns
      
      whether the shape is visible.
    """
    ...
  

  def setVisible(self, visible: bool) -> "None":
    """
      setVisible
      
      # Parameters
      
      - visible: bool
      
        whether the shape should be visible.
    """
    ...
  

  def boundingBox(self) -> "QRectF":
    """
      boundingBox the bounding box of the shape in points
      
      # Returns
      
      RectF containing the bounding box.
    """
    ...
  

  def position(self) -> "QPointF":
    """
      position the position of the shape in points.
      
      # Returns
      
      the position of the shape in points.
    """
    ...
  

  def setPosition(self, point: QPointF) -> "None":
    """
      setPosition set the position of the shape.
      
      # Parameters
      
      - point: QPointF
      
        the new position in points
    """
    ...
  

  def transformation(self) -> "QTransform":
    """
      transformation the 2D transformation matrix of the shape.
      
      # Returns
      
      the 2D transformation matrix.
    """
    ...
  

  def setTransformation(self, matrix: QTransform) -> "None":
    """
      setTransformation set the 2D transformation matrix of the shape.
      
      # Parameters
      
      - matrix: QTransform
      
        the new 2D transformation matrix.
    """
    ...
  

  def absoluteTransformation(self) -> "QTransform":
    """
      transformation the 2D transformation matrix of the shape including all grandparent transforms.
      
      # Returns
      
      the 2D transformation matrix.
    """
    ...
  

  def remove(self) -> "bool":
    """
      remove delete the shape.
    """
    ...
  

  def update(self) -> "None":
    """
      update queue the shape update.
    """
    ...
  

  def updateAbsolute(self, box: QRectF) -> "None":
    """
      updateAbsolute queue the shape update in the specified rectangle.
      
      # Parameters
      
      - box: QRectF
      
        the RectF rectangle to update.
    """
    ...
  

  def toSvg(self, prependStyles: bool = False, stripTextMode: bool = True) -> "str":
    """
      toSvg convert the shape to svg, will not include style definitions.
      
      # Parameters
      
      - prependStyles: bool = `False`
      
        prepend the style data. Default: false
      
      - stripTextMode: bool = `True`
      
        enable strip text mode. Default: true
      
      # Returns
      
      the svg in a string.
    """
    ...
  

  def select(self) -> "None":
    """
      select selects the shape.
    """
    ...
  

  def deselect(self) -> "None":
    """
      deselect deselects the shape.
    """
    ...
  

  def isSelected(self) -> "bool":
    """
      isSelected
      
      # Returns
      
      whether the shape is selected.
    """
    ...
  

  def parentShape(self) -> "Shape":
    """
      parentShape
      
      # Returns
      
      the parent [GroupShape](https://api.kde.org/krita/html/classGroupShape.html) of the current shape.
    """
    ...
  

class Swatch:

  """
    The [Swatch](https://api.kde.org/krita/html/classSwatch.html) class is a thin wrapper around the KisSwatch class.
    
    A [Swatch](https://api.kde.org/krita/html/classSwatch.html) is a single color that is part of a palette, that has a name and an id. A [Swatch](https://api.kde.org/krita/html/classSwatch.html) color can be a spot color.
  """

  def __init__(self) -> None:
  
    ...
  

  def __init__(self, rhs: Swatch) -> None:
  
    ...
  

  def name(self) -> "str":
  
    ...
  

  def setName(self, name: str) -> "None":
  
    ...
  

  def id(self) -> "str":
  
    ...
  

  def setId(self, id: str) -> "None":
  
    ...
  

  def color(self) -> "ManagedColor":
  
    ...
  

  def setColor(self, color: ManagedColor) -> "None":
  
    ...
  

  def spotColor(self) -> "bool":
  
    ...
  

  def setSpotColor(self, spotColor: bool) -> "None":
  
    ...
  

  def isValid(self) -> "bool":
  
    ...
  

class TransformMask(Node):

  """
    The [TransformMask](https://api.kde.org/krita/html/classTransformMask.html) class A transform mask is a mask type node that can be used to store transformations.
  """

  def __init__(self, image: KisImageSP, name: str, parent: QObject = None) -> None:
  
    ...
  

  def __init__(self, image: KisImageSP, mask: KisTransformMaskSP, parent: QObject = None) -> None:
  
    ...
  

  def type(self) -> "str":
    """
      type [Krita](https://api.kde.org/krita/html/classKrita.html) has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
      
      
      If the [Node](https://api.kde.org/krita/html/classNode.html) object isn't wrapping a valid [Krita](https://api.kde.org/krita/html/classKrita.html) layer or mask object, and empty string is returned.
      
      # Returns
      
      transformmask
    """
    ...
  

  def finalAffineTransform(self) -> "QTransform":
  
    ...
  

  def toXML(self) -> "str":
    """
      toXML
      
      # Returns
      
      a string containing XML formated transform parameters.
    """
    ...
  

  def fromXML(self, xml: str) -> "bool":
    """
      
      
         @brief fromXML set the transform of the transform mask from XML formatted data.
         The xml must have a valid id
      
         dumbparams - placeholder for static transform masks
         tooltransformparams - static transform mask
         animatedtransformparams - animated transform mask
      ```
      <!DOCTYPE transform_params>
      <transform_params>
       <main id="tooltransformparams"/>
       <data mode="0">
        <free_transform>
        <transformedCenter [type](https://api.kde.org/krita/html/classtype.html)="pointf" x="12.3102137276208" y="11.0727768562035"/>
        <originalCenter [type](https://api.kde.org/krita/html/classtype.html)="pointf" x="20" y="20"/>
        <rotationCenterOffset [type](https://api.kde.org/krita/html/classtype.html)="pointf" x="0" y="0"/>
        <transformAroundRotationCenter value="0" [type](https://api.kde.org/krita/html/classtype.html)="value"/>
        <aX value="0" [type](https://api.kde.org/krita/html/classtype.html)="value"/>
        <aY value="0" [type](https://api.kde.org/krita/html/classtype.html)="value"/>
        <aZ value="0" [type](https://api.kde.org/krita/html/classtype.html)="value"/>
        <cameraPos z="1024" [type](https://api.kde.org/krita/html/classtype.html)="vector3d" x="0" y="0"/>
        <scaleX value="1" [type](https://api.kde.org/krita/html/classtype.html)="value"/>
        <scaleY value="1" [type](https://api.kde.org/krita/html/classtype.html)="value"/>
        <shearX value="0" [type](https://api.kde.org/krita/html/classtype.html)="value"/>
        <shearY value="0" [type](https://api.kde.org/krita/html/classtype.html)="value"/>
        <keepAspectRatio value="0" [type](https://api.kde.org/krita/html/classtype.html)="value"/>
        <flattenedPerspectiveTransform m23="0" m31="0" m32="0" [type](https://api.kde.org/krita/html/classtype.html)="transform" m33="1" m12="0" m13="0" m22="1" m11="1" m21="0"/>
        <filterId value="Bicubic" [type](https://api.kde.org/krita/html/classtype.html)="value"/>
        </free_transform>
       </data>
      </transform_params>
      ```
      
      # Parameters
      
      - xml: str
      
        a valid formated XML string with proper main and data elements.
      
      # Returns
      
      a true response if successful, a false response if failed.
    """
    ...
  

class TransparencyMask(Node):

  """
    The [TransparencyMask](https://api.kde.org/krita/html/classTransparencyMask.html) class A transparency mask is a mask type node that can be used to show and hide parts of a layer.
  """

  def __init__(self, image: KisImageSP, name: str, parent: QObject = None) -> None:
  
    ...
  

  def __init__(self, image: KisImageSP, mask: KisTransparencyMaskSP, parent: QObject = None) -> None:
  
    ...
  

  def type(self) -> "str":
    """
      type [Krita](https://api.kde.org/krita/html/classKrita.html) has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
      
      
      If the [Node](https://api.kde.org/krita/html/classNode.html) object isn't wrapping a valid [Krita](https://api.kde.org/krita/html/classKrita.html) layer or mask object, and empty string is returned.
      
      # Returns
      
      transparencymask
    """
    ...
  

  def selection(self) -> "Selection":
  
    ...
  

  def setSelection(self, selection: Selection) -> "None":
  
    ...
  

class VectorLayer(Node):

  """
    The [VectorLayer](https://api.kde.org/krita/html/classVectorLayer.html) class A vector layer is a special layer that stores and shows vector shapes.
    
    Vector shapes all have their coordinates in points, which is a unit that represents 1/72th of an inch. Keep this in mind wen parsing the bounding box and position data.
  """

  def __init__(self, shapeController: KoShapeControllerBase, image: KisImageSP, name: str, parent: QObject = None) -> None:
  
    ...
  

  def __init__(self, layer: KisShapeLayerSP, parent: QObject = None) -> None:
  
    ...
  

  def type(self) -> "str":
    """
      type [Krita](https://api.kde.org/krita/html/classKrita.html) has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
      
      # Returns
      
      vectorlayer
    """
    ...
  

  def shapes(self) -> "List[Shape]":
    """
      shapes
      
      # Returns
      
      the list of top-level shapes in this vector layer.
    """
    ...
  

  def toSvg(self) -> "str":
    """
      toSvg convert the shapes in the layer to svg.
      
      # Returns
      
      the svg in a string.
    """
    ...
  

  def addShapesFromSvg(self, svg: str) -> "List[Shape]":
    """
      addShapesFromSvg add shapes to the layer from a valid svg.
      
      # Parameters
      
      - svg: str
      
        valid svg string.
      
      # Returns
      
      the list of shapes added to the layer from the svg.
    """
    ...
  

  def shapeAtPosition(self, position: QPointF) -> "Shape":
    """
      shapeAtPoint check if the position is located within any non-group shape's boundingBox() on the current layer.
      
      # Parameters
      
      - position: QPointF
      
        a QPointF of the position.
      
      # Returns
      
      the shape at the position, or None if no shape is found.
    """
    ...
  

  def shapesInRect(self, rect: QRectF, omitHiddenShapes: bool = True, containedMode: bool = False) -> "List[Shape]":
    """
      shapeInRect get all non-group shapes that the shape's boundingBox() intersects or is contained within a given rectangle on the current layer.
      
      # Parameters
      
      - rect: QRectF
      
        a QRectF
      
      - omitHiddenShapes: bool = `True`
      
        true if non-visible() shapes should be omitted, false if they should be included. `omitHiddenShapes` defaults to true.
      
      - containedMode: bool = `False`
      
        false if only shapes that are within or intersect with the outline should be included, true if only shapes that are fully contained within the outline should be included. `containedMode` defaults to false
      
      # Returns
      
      returns a list of shapes.
    """
    ...
  

  def createGroupShape(self, name: str, shapes: List[Shape]) -> "Shape":
    """
      createGroupShape combine a list of top level shapes into a group.
      
      # Parameters
      
      - name: str
      
        the name of the shape.
      
      - shapes: List[Shape]
      
        list of top level shapes.
      
      # Returns
      
      if successful, a [GroupShape](https://api.kde.org/krita/html/classGroupShape.html) object will be returned.
    """
    ...
  

class View(QObject):

  """
    
    
    [View](https://api.kde.org/krita/html/classView.html) represents one view on a document. A document can be shown in more than one view at a time.
  """

  def __init__(self, view: KisView, parent: QObject = None) -> None:
  
    ...
  

  def window(self) -> "Window":
    """
      
      
      # Returns
      
      the window this view is shown in.
    """
    ...
  

  def document(self) -> "Document":
    """
      
      
      # Returns
      
      the document this view is showing.
    """
    ...
  

  def setDocument(self, document: Document) -> "None":
    """
      
      
      Reset the view to show `document`.
    """
    ...
  

  def visible(self) -> "bool":
    """
      
      
      # Returns
      
      true if the current view is visible, false if not.
    """
    ...
  

  def setVisible(self) -> "None":
    """
      
      
      Make the current view visible.
    """
    ...
  

  def canvas(self) -> "Canvas":
    """
      
      
      # Returns
      
      the canvas this view is showing. The canvas controls things like zoom and rotation.
    """
    ...
  

  def activateResource(self, resource: Resource) -> "None":
    """
      activateResource activates the given resource.
      
      # Parameters
      
      - resource: Resource
      
        a pattern, gradient or paintop preset
    """
    ...
  

  def foregroundColor(self) -> "ManagedColor":
    """
      
      
         @brief foregroundColor allows access to the currently active color.
         This is nominally per canvas/view, but in practice per mainwindow.
         @code
       color = Application.activeWindow().activeView().`foregroundColor()` components = color.components() components[0] = 1.0 components[1] = 0.6 components[2] = 0.7 color.setComponents(components) Application.activeWindow().activeView().setForeGroundColor(color)
    """
    ...
  

  def setForeGroundColor(self, color: ManagedColor) -> "None":
  
    ...
  

  def backgroundColor(self) -> "ManagedColor":
  
    ...
  

  def setBackGroundColor(self, color: ManagedColor) -> "None":
  
    ...
  

  def currentBrushPreset(self) -> "Resource":
  
    ...
  

  def setCurrentBrushPreset(self, resource: Resource) -> "None":
  
    ...
  

  def currentPattern(self) -> "Resource":
  
    ...
  

  def setCurrentPattern(self, resource: Resource) -> "None":
  
    ...
  

  def currentGradient(self) -> "Resource":
  
    ...
  

  def setCurrentGradient(self, resource: Resource) -> "None":
  
    ...
  

  def currentBlendingMode(self) -> "str":
  
    ...
  

  def setCurrentBlendingMode(self, blendingMode: str) -> "None":
  
    ...
  

  def HDRExposure(self) -> "float":
  
    ...
  

  def setHDRExposure(self, exposure: float) -> "None":
  
    ...
  

  def HDRGamma(self) -> "float":
  
    ...
  

  def setHDRGamma(self, gamma: float) -> "None":
  
    ...
  

  def paintingOpacity(self) -> "float":
  
    ...
  

  def setPaintingOpacity(self, opacity: float) -> "None":
  
    ...
  

  def brushSize(self) -> "float":
  
    ...
  

  def setBrushSize(self, brushSize: float) -> "None":
  
    ...
  

  def brushRotation(self) -> "float":
  
    ...
  

  def setBrushRotation(self, brushRotation: float) -> "None":
  
    ...
  

  def paintingFlow(self) -> "float":
  
    ...
  

  def setPaintingFlow(self, flow: float) -> "None":
  
    ...
  

  def showFloatingMessage(self, message: str, icon: QIcon, timeout: int, priority: int) -> "None":
    """
      showFloatingMessage displays a floating message box on the top-left corner of the canvas
      
      # Parameters
      
      - message: str
      
        Message to be displayed inside the floating message box
      
      - icon: QIcon
      
        Icon to be displayed inside the message box next to the message string
      
      - timeout: int
      
        Milliseconds until the message box disappears
      
      - priority: int
      
        0 = High, 1 = Medium, 2 = Low. Higher priority messages will be displayed in place of lower priority messages
    """
    ...
  

  def selectedNodes(self) -> "List[Node]":
    """
      
      
         @brief selectedNodes returns a list of Nodes that are selected in this view.
      
      ```
      from krita import *
      w = Krita.instance().activeWindow()
      v = w.activeView()
      selected_nodes = v.selectedNodes()
      print(selected_nodes)
      ```
      
      # Returns
      
      a list of [Node](https://api.kde.org/krita/html/classNode.html) objects which may be empty.
    """
    ...
  

  def flakeToDocumentTransform(self) -> "QTransform":
    """
      flakeToDocumentTransform The transformation of the document relative to the view without rotation and mirroring
      
      # Returns
      
      QTransform
    """
    ...
  

  def flakeToCanvasTransform(self) -> "QTransform":
    """
      flakeToCanvasTransform The transformation of the canvas relative to the view without rotation and mirroring
      
      # Returns
      
      QTransform
    """
    ...
  

  def flakeToImageTransform(self) -> "QTransform":
    """
      flakeToImageTransform The transformation of the image relative to the view without rotation and mirroring
      
      # Returns
      
      QTransform
    """
    ...
  

class Window(QObject):

  """
    
    
    [Window](https://api.kde.org/krita/html/classWindow.html) represents one [Krita](https://api.kde.org/krita/html/classKrita.html) mainwindow. A window can have any number of views open on any number of documents.
  """

  def __init__(self, window: KisMainWindow, parent: QObject = None) -> None:
  
    ...
  

  def qwindow(self) -> "QMainWindow":
    """
      
      
      Return a handle to the QMainWindow widget. This is useful to e.g. parent dialog boxes and message box.
    """
    ...
  

  def dockers(self) -> "List[QDockWidget]":
    """
      dockers
      
      # Returns
      
      a list of all the dockers belonging to this window
    """
    ...
  

  def views(self) -> "List[View]":
    """
      
      
      # Returns
      
      a list of open views in this window
    """
    ...
  

  def addView(self, document: Document) -> "View":
    """
      
      
      Open a new view on the given document in this window
    """
    ...
  

  def showView(self, view: View) -> "None":
    """
      
      
      Make the given view active in this window. If the view does not belong to this window, nothing happens.
    """
    ...
  

  def activeView(self) -> "View":
    """
      
      
      # Returns
      
      the currently active view or 0 if no view is active
    """
    ...
  

  def activate(self) -> "None":
    """
      activate activates this [Window](https://api.kde.org/krita/html/classWindow.html).
    """
    ...
  

  def close(self) -> "None":
    """
      close the active window and all its Views. If there are no Views left for a given [Document](https://api.kde.org/krita/html/classDocument.html), that [Document](https://api.kde.org/krita/html/classDocument.html) will also be closed.
    """
    ...
  

  def createAction(self, id: str, text: str = "", menuLocation: str = "tools/scripts") -> "QAction":
    """
      createAction creates a QAction object and adds it to the action manager for this [Window](https://api.kde.org/krita/html/classWindow.html).
      
      # Parameters
      
      - id: str
      
        The unique id for the action. This will be used to propertize the action if any .action file is present
      
      - text: str = `""`
      
        The user-visible text of the action. If empty, the text from the .action file is used.
      
      - menuLocation: str = `"tools/scripts"`
      
        a /-separated string that describes which menu the action should be places in. Default is "tools/scripts"
      
      # Returns
      
      the new action.
    """
    ...
  

  windowClosed: pyqtSignal
  """
    Emitted when the window is closed.
  """
  

  themeChanged: pyqtSignal
  """
    Emitted when we change the color theme.
  """
  

  activeViewChanged: pyqtSignal
  """
    Emitted when the active view changes.
  """
  

