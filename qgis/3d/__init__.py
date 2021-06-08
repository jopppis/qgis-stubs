# -*- coding: utf-8 -*-

"""
***************************************************************************
    __init__.py
    ---------------------
    Date                 : May 2014
    Copyright            : (C) 2014 by Nathan Woodrow
    Email                : woodrow dot nathan at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Nathan Woodrow'
__date__ = 'May 2014'
__copyright__ = '(C) 2014, Nathan Woodrow'

from qgis.PyQt import QtCore
from qgis._3d import *
"""
This folder is completed using sipify.pl script
It is not aimed to be manually edited
"""
# The following has been generated automatically from src/3d/materials/qgsabstractmaterialsettings.h
QgsAbstractMaterialSettings.RenderingTechnique = QgsMaterialSettingsRenderingTechnique
# monkey patching scoped based enum
QgsAbstractMaterialSettings.Triangles = QgsMaterialSettingsRenderingTechnique.Triangles
QgsAbstractMaterialSettings.Triangles.is_monkey_patched = True
QgsAbstractMaterialSettings.Triangles.__doc__ = "Triangle based rendering (default)"
QgsAbstractMaterialSettings.Lines = QgsMaterialSettingsRenderingTechnique.Lines
QgsAbstractMaterialSettings.Lines.is_monkey_patched = True
QgsAbstractMaterialSettings.Lines.__doc__ = "Line based rendering, requires line data"
QgsAbstractMaterialSettings.InstancedPoints = QgsMaterialSettingsRenderingTechnique.InstancedPoints
QgsAbstractMaterialSettings.InstancedPoints.is_monkey_patched = True
QgsAbstractMaterialSettings.InstancedPoints.__doc__ = "Instanced based rendering, requiring triangles and point data"
QgsAbstractMaterialSettings.Points = QgsMaterialSettingsRenderingTechnique.Points
QgsAbstractMaterialSettings.Points.is_monkey_patched = True
QgsAbstractMaterialSettings.Points.__doc__ = "Point based rendering, requires point data"
QgsAbstractMaterialSettings.TrianglesWithFixedTexture = QgsMaterialSettingsRenderingTechnique.TrianglesWithFixedTexture
QgsAbstractMaterialSettings.TrianglesWithFixedTexture.is_monkey_patched = True
QgsAbstractMaterialSettings.TrianglesWithFixedTexture.__doc__ = "Triangle based rendering, using a fixed, non-user-configurable texture (e.g. for terrain rendering)"
QgsAbstractMaterialSettings.TrianglesFromModel = QgsMaterialSettingsRenderingTechnique.TrianglesFromModel
QgsAbstractMaterialSettings.TrianglesFromModel.is_monkey_patched = True
QgsAbstractMaterialSettings.TrianglesFromModel.__doc__ = "Triangle based rendering, using a model object source"
QgsAbstractMaterialSettings.TrianglesDataDefined = QgsMaterialSettingsRenderingTechnique.TrianglesDataDefined
QgsAbstractMaterialSettings.TrianglesDataDefined.is_monkey_patched = True
QgsAbstractMaterialSettings.TrianglesDataDefined.__doc__ = "Triangle based rendering with possibility of datadefined color \since QGIS 3.18"
QgsMaterialSettingsRenderingTechnique.__doc__ = 'Material rendering techniques\n\n.. versionadded:: 3.16\n\n' + '* ``Triangles``: ' + QgsMaterialSettingsRenderingTechnique.Triangles.__doc__ + '\n' + '* ``Lines``: ' + QgsMaterialSettingsRenderingTechnique.Lines.__doc__ + '\n' + '* ``InstancedPoints``: ' + QgsMaterialSettingsRenderingTechnique.InstancedPoints.__doc__ + '\n' + '* ``Points``: ' + QgsMaterialSettingsRenderingTechnique.Points.__doc__ + '\n' + '* ``TrianglesWithFixedTexture``: ' + QgsMaterialSettingsRenderingTechnique.TrianglesWithFixedTexture.__doc__ + '\n' + '* ``TrianglesFromModel``: ' + QgsMaterialSettingsRenderingTechnique.TrianglesFromModel.__doc__ + '\n' + '* ``TrianglesDataDefined``: ' + QgsMaterialSettingsRenderingTechnique.TrianglesDataDefined.__doc__
# --
