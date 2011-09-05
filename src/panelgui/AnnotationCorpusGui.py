# -*- coding: iso-8859-1 -*-
'''
Copyright 2011 Marco Mina. All rights reserved.

This file is part of fastSemSim

fastSemSim is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

fastSemSim is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with fastSemSim.  If not, see <http://www.gnu.org/licenses/>.
'''

#from wx.Python.wx import *
import wx
from GO import GeneOntology
from GO import AnnotationCorpus

class AnnotationCorpusGui(wx.Frame):
	filetype = None
	plainfileorder = 0
		
	def __init__(self, parent):
		self.parentobj = parent
		super(AnnotationCorpusGui, self).__init__(self.parentobj, title="Load Annotation Corpus", size=(500,400))
		self.InitUI()
	
	def InitUI(self):
		self.panel = wx.Panel(self)
		self.Bind(wx.EVT_CLOSE, self.OnQuit, id=self.GetId())
#------------------------------------------------------------------------------------------------------------------
		#main box
		self.mainbox = wx.BoxSizer(wx.VERTICAL)
#--------------------------------------------------------------------------------------		
		#file selection box
		self.fileboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Annotation Corpus file')
		self.filebox = wx.StaticBoxSizer(self.fileboxline, wx.HORIZONTAL)
		#self.filename_label = wx.StaticText(self.panel, label='AC File')
		#self.filename_label.SetFont(self.parentobj.font)
		self.filename = wx.StaticText(self.panel, label='No file selected')
		self.filechoosecmd = wx.Button(self.panel, wx.ID_ANY, 'Browse...')
		self.Bind(wx.EVT_BUTTON, self.OnACBrowse, id=self.filechoosecmd.GetId())
		self.filebox.Add(self.filename, flag=wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		self.filebox.Add(self.filechoosecmd, flag=wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		

		self.mainbox.Add(self.filebox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
#--------------------------------------------------------------------------------------

		#file parameters
		self.fileparamsboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'File parameters')
		self.fileparamsbox = wx.StaticBoxSizer(self.fileparamsboxline, wx.HORIZONTAL)

#--------------------------------------------------------------------------------------
		#file type parameters
		self.filetypebox = wx.BoxSizer(wx.VERTICAL)
		self.availabletypes = ['GOA','plain']
		self.typebox = wx.ComboBox(self.panel, wx.ID_ANY, choices=self.availabletypes, style=wx.CB_READONLY)
		self.typelabel = wx.StaticText(self.panel, label='File type')
		self.filetypebox.Add(self.typelabel, flag=wx.UP|wx.DOWN|wx.LEFT|wx.RIGHT, border=5)
		self.filetypebox.Add(self.typebox, flag=wx.LEFT|wx.RIGHT, border=10)
		self.Bind(wx.EVT_COMBOBOX, self.OnSelectType, id=self.typebox.GetId())
		
#--------------------------------------------------------------------------------------
		#file format parameters
		self.plainfileformatline = wx.StaticBox(self.panel, wx.ID_ANY, 'Plain file format')
		self.plainfileformatbox = wx.StaticBoxSizer(self.plainfileformatline, wx.VERTICAL)
		self.plainfileformatoptions = ['object name\tGO term','GO term\tobject name']
		self.plainfileformatradius1 = wx.RadioButton(self.panel, wx.ID_ANY, self.plainfileformatoptions[0], (10, 10), style=wx.RB_GROUP)
		self.plainfileformatradius2 = wx.RadioButton(self.panel, wx.ID_ANY, self.plainfileformatoptions[1], (10, 10))
		self.Bind(wx.EVT_RADIOBUTTON, self.OnSelectPlainOrder, id=self.plainfileformatradius1.GetId())
		self.Bind(wx.EVT_RADIOBUTTON, self.OnSelectPlainOrder, id=self.plainfileformatradius2.GetId())
		self.plainfileformat = 0 # obj name first
		self.plainfileformatradius1.Disable()
		self.plainfileformatradius2.Disable()
		self.plainfileformatbox.Add(self.plainfileformatradius1)
		self.plainfileformatbox.Add(self.plainfileformatradius2)

		self.fileparamsbox.Add(self.filetypebox, flag=wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		self.fileparamsbox.Add(self.plainfileformatbox, flag=wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		self.mainbox.Add(self.fileparamsbox, flag=wx.LEFT|wx.RIGHT|wx.TOP, border=10)
#--------------------------------------------------------------------------------------

		# commanbox
		self.commandbox = wx.BoxSizer(wx.HORIZONTAL)
		self.acload = wx.Button(self.panel, wx.ID_ANY, 'Load')
		self.acload.Disable()
		self.Bind(wx.EVT_BUTTON, self.OnACLoad, id=self.acload.GetId())
		self.doneb = wx.Button(self.panel, wx.ID_ANY, 'Close')
		self.Bind(wx.EVT_BUTTON, self.OnACBrowseDone, id=self.doneb.GetId())
		
		self.commandbox.Add(self.acload, flag=wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		self.commandbox.Add(self.doneb, flag=wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		self.mainbox.Add(self.commandbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		self.fakecmd = wx.Button(self.panel, wx.ID_ANY, 'Load')
		self.fakecmd.Hide()
		self.fakecmd.Disable()
		self.Bind(wx.EVT_BUTTON, self.OnFakeCmd, id=self.fakecmd.GetId())
#--------------------------------------------------------------------------------------
		#statusbox
		self.statusbox = wx.BoxSizer(wx.HORIZONTAL)
		self.status_label = wx.StaticText(self.panel, label='No Annotation Corpus loaded.')
		self.status_label.SetFont(self.parentobj.font)
		self.statusbox.Add(self.status_label, border=10)

		self.mainbox.Add(self.statusbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		
		self.panel.SetSizerAndFit(self.mainbox)

#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

	def OnSelectType(self, event):
		self.filetype = self.availabletypes[self.typebox.GetSelection()]
		if self.filetype == 'GOA':
			self.plainfileformatradius1.Disable()
			self.plainfileformatradius2.Disable()
		else:
			self.plainfileformatradius1.Enable()
			self.plainfileformatradius2.Enable()
		if (not self.filename == None) and (not self.filetype == None):
			self.acload.Enable()

	def OnSelectPlainOrder(self, event):
			if self.plainfileformatradius1.GetValue():
				self.plainfileorder = 0
			elif self.plainfileformatradius2.GetValue():
				self.plainfileorder = 1

	def OnACBrowse(self, event):
		dialog = wx.FileDialog(None, style = wx.OPEN)
		if dialog.ShowModal() == wx.ID_OK:
			self.filename.SetLabel(dialog.GetPath())
			if (not self.filename == None) and (not self.filetype == None):
				self.acload.Enable()

	def OnACLoad(self, event):
		self.filechoosecmd.Disable()
		self.doneb.Disable()
		self.acload.Disable()
		self.parentobj.ac = None
		self.parentobj.SetAcOk(False)
		self.parentobj.update_ac = True
		self.parentobj.update_ssobject = True
		self.parentobj.update_query = True
		event = wx.PyCommandEvent(wx.EVT_BUTTON.typeId, self.fakecmd.GetId())
		wx.PostEvent(self.GetEventHandler(), event)

	def OnFakeCmd(self, event):
		self.filechoosecmd.Enable()
		self.doneb.Enable()
		self.acload.Enable()
		self.ac = AnnotationCorpus.AnnotationCorpus(self.parentobj.go)
		param = {}
		if self.plainfileorder == 0:
			param['AC_OBJ_FIRST'] = None
		elif self.plainfileorder == 1:
			param['AC_TERM_FIRST'] = None
		try:
			if self.ac.parse(str(self.filename.GetLabel()), self.filetype, param):
				if self.ac.sanitize():
					#self.acobjs.SetLabel(str(len(self.ac.annotations)))
					#self.acterms.SetLabel(str(len(self.ac.reverse_annotations)))
					self.parentobj.ac = self.ac
					self.parentobj.SetAcOk(True)
					self.parentobj.update_ac = False
					self.status_label.SetLabel("Annotation Corpus loaded.")
					return
			self.status_label.SetLabel("Failed to load Annotation Corpus.")
		except:
			self.status_label.SetLabel("Failed to load Annotation Corpus.")
				

	def OnACBrowseDone(self, event):
		self.Hide()
		
	def OnQuit(self, event):
		self.Hide()
		
#self.descbox = wx.FlexGridSizer(rows = 4, cols = 2, vgap = 6, hgap = 20)
#self.filename_label = wx.StaticText(self.panel, label='AC File')
#self.filename_label.SetFont(self.parentobj.font)
#self.filename = wx.StaticText(self.panel, label='')
##self.acobjs_label = wx.StaticText(self.panel, label='Objects')
###self.acobjs_label.SetFont(self.parentobj.font)
##self.acobjs = wx.StaticText(self.panel, label='')
##self.acobjs.SetFont(self.parentobj.font)
##self.acterms_label = wx.StaticText(self.panel, label='Go Terms involved')
##self.acterms_label.SetFont(self.parentobj.font)
##self.acterms = wx.StaticText(self.panel, label='')
##self.acterms.SetFont(self.parentobj.font)
##self.descbox.AddMany([(self.filename_label), (self.filename), (self.acobjs_label), (self.acobjs), (self.acterms_label), (self.acterms)])
#self.descbox.AddMany([(self.filename_label), (self.filename)])