# Krita Popup

Provide a configurable Popup widget which can be triggered with shortcuts displaying under cursor or at specific locations. This plugin is determined to **minimalize hand movements** while painting, striking a balance between keyboard shortcuts and mouse.

TODO there should be a gif

This popup is configurable, Many type of widgets can be placed and configured on it, including:

1. [X] Tools
2. [X] Dockers those krita provided (multiple window support...?)
3. [x] Brushes
4. [ ] Current Layer States, like blending mode, opacity, inherit alpha, locked...
6. [ ] View States, like brush size, flow
7. [ ] (checkable) Actions like eraser mode, mirror.
8. [ ] A minimal tool option which will changes corresponding with current tool (mark: must get the shardtooldocker's widget in `__init__`)
9. [ ] other resources rather than brushes
10. Menus
   1. [X] main menu 
   2. [ ] submenu within main menu like 'Filter'

TODO:

1. [X] Add Widgets in editing mode
2. [X] Edit item (item specific)
3. [X] custom mask for items
4. [X] multiple layout 
5. [X] Fixed item (always displayed at specific locations nomatter where the cursor is)
7. [ ] documentation

known bugs:

1. [ ] when focus on popup, all shortcuts will lose. 