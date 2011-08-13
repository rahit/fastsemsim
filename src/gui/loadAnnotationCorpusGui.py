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

from wxPython.wx import *
from GO import GeneOntology
from GO import AnnotationCorpus

class LoadAC(wxFrame):
	filetype = None
	plainfileorder = 0
		
	def __init__(self, parent):
		self.parentobj = parent
		super(LoadAC, self).__init__(self.parentobj, title="Load Annotation Corpus", size=(500,400))
		self.InitUI()
	
	def InitUI(self):
		self.panel = wxPanel(self)
		self.Bind(EVT_CLOSE, self.OnQuit, id=self.GetId())
#------------------------------------------------------------------------------------------------------------------
		#main box
		self.mainbox = wxBoxSizer(wxVERTICAL)
#--------------------------------------------------------------------------------------		
		#file selection box
		self.fileboxline = wxStaticBox(self.panel, wxID_ANY, 'Annotation Corpus file')
		self.filebox = wxStaticBoxSizer(self.fileboxline, wxHORIZONTAL)
		#self.filename_label = wxStaticText(self.panel, label='AC File')
		#self.filename_label.SetFont(self.parentobj.font)
		self.filename = wxStaticText(self.panel, label='No file selected')
		self.filechoosecmd = wxButton(self.panel, wxID_ANY, 'Browse...')
		self.Bind(EVT_BUTTON, self.OnACBrowse, id=self.filechoosecmd.GetId())
		self.filebox.Add(self.filename, flag=wxLEFT|wxRIGHT|wxTOP, border=10)
		self.filebox.Add(self.filechoosecmd, flag=wxLEFT|wxRIGHT|wxTOP, border=10)
		

		self.mainbox.Add(self.filebox, flag=wxEXPAND|wxLEFT|wxRIGHT|wxTOP, border=10)
#--------------------------------------------------------------------------------------

		#file parameters
		self.fileparamsboxline = wxStaticBox(self.panel, wxID_ANY, 'File parameters')
		self.fileparamsbox = wxStaticBoxSizer(self.fileparamsboxline, wxHORIZONTAL)

#--------------------------------------------------------------------------------------
		#file type parameters
		self.filetypebox = wxBoxSizer(wxVERTICAL)
		self.availabletypes = ['GOA','plain']
		self.typebox = wxComboBox(self.panel, wxID_ANY, choices=self.availabletypes, style=wxCB_READONLY)
		self.typelabel = wxStaticText(self.panel, label='File type')
		self.filetypebox.Add(self.typelabel, flag=wxUP|wxDOWN|wxLEFT|wxRIGHT, border=5)
		self.filetypebox.Add(self.typebox, flag=wxLEFT|wxRIGHT, border=10)
		self.Bind(EVT_COMBOBOX, self.OnSelectType, id=self.typebox.GetId())
		
#--------------------------------------------------------------------------------------
		#file format parameters
		self.plainfileformatline = wxStaticBox(self.panel, wxID_ANY, 'Plain file format')
		self.plainfileformatbox = wxStaticBoxSizer(self.plainfileformatline, wxVERTICAL)
		self.plainfileformatoptions = ['object name\tGO term','GO term\tobject name']
		self.plainfileformatradius1 = wxRadioButton(self.panel, wxID_ANY, self.plainfileformatoptions[0], (10, 10), style=wxRB_GROUP)
		self.plainfileformatradius2 = wxRadioButton(self.panel, wxID_ANY, self.plainfileformatoptions[1], (10, 10))
		self.Bind(EVT_RADIOBUTTON, self.OnSelectPlainOrder, id=self.plainfileformatradius1.GetId())
		self.Bind(EVT_RADIOBUTTON, self.OnSelectPlainOrder, id=self.plainfileformatradius2.GetId())
		self.plainfileformat = 0 # obj name first
		self.plainfileformatradius1.Disable()
		self.plainfileformatradius2.Disable()
		self.plainfileformatbox.Add(self.plainfileformatradius1)
		self.plainfileformatbox.Add(self.plainfileformatradius2)

		self.fileparamsbox.Add(self.filetypebox, flag=wxLEFT|wxRIGHT|wxTOP, border=10)
		self.fileparamsbox.Add(self.plainfileformatbox, flag=wxLEFT|wxRIGHT|wxTOP, border=10)
		self.mainbox.Add(self.fileparamsbox, flag=wxLEFT|wxRIGHT|wxTOP, border=10)
#--------------------------------------------------------------------------------------

		# commanbox
		self.commandbox = wxBoxSizer(wxHORIZONTAL)
		self.acload = wxButton(self.panel, wxID_ANY, 'Load')
		self.acload.Disable()
		self.Bind(EVT_BUTTON, self.OnACLoad, id=self.acload.GetId())
		self.doneb = wxButton(self.panel, wxID_ANY, 'Close')
		self.Bind(EVT_BUTTON, self.OnACBrowseDone, id=self.doneb.GetId())
		
		self.commandbox.Add(self.acload, flag=wxLEFT|wxRIGHT|wxTOP, border=10)
		self.commandbox.Add(self.doneb, flag=wxLEFT|wxRIGHT|wxTOP, border=10)
		self.mainbox.Add(self.commandbox, flag=wxEXPAND|wxLEFT|wxRIGHT|wxTOP, border=10)

		self.fakecmd = wxButton(self.panel, wxID_ANY, 'Load')
		self.fakecmd.Hide()
		self.fakecmd.Disable()
		self.Bind(EVT_BUTTON, self.OnFakeCmd, id=self.fakecmd.GetId())
#--------------------------------------------------------------------------------------
		#statusbox
		self.statusbox = wxBoxSizer(wxHORIZONTAL)
		self.status_label = wxStaticText(self.panel, label='No Annotation Corpus loaded.')
		self.status_label.SetFont(self.parentobj.font)
		self.statusbox.Add(self.status_label, border=10)

		self.mainbox.Add(self.statusbox, flag=wxEXPAND|wxLEFT|wxRIGHT|wxTOP, border=10)
		
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
		dialog = wxFileDialog(None, style = wxOPEN)
		if dialog.ShowModal() == wxID_OK:
			self.filename.SetLabel(dialog.GetPath())
			if (not self.filename == None) and (not self.filetype == None):
				self.acload.Enable()

	def OnACLoad(self, event):
		self.filechoosecmd.Disable()
		self.doneb.Disable()
		self.acload.Disable()
		self.parentobj.ac = None
		self.parentobj.ac_ok = False
		self.parentobj.update_ac = True
		self.parentobj.update_ssobject = True
		self.parentobj.update_query = True
		event = wxPyCommandEvent(EVT_BUTTON.typeId, self.fakecmd.GetId())
		wxPostEvent(self.GetEventHandler(), event)

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
					self.parentobj.ac_ok = True
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
		
#self.descbox = wxFlexGridSizer(rows = 4, cols = 2, vgap = 6, hgap = 20)
#self.filename_label = wxStaticText(self.panel, label='AC File')
#self.filename_label.SetFont(self.parentobj.font)
#self.filename = wxStaticText(self.panel, label='')
##self.acobjs_label = wxStaticText(self.panel, label='Objects')
###self.acobjs_label.SetFont(self.parentobj.font)
##self.acobjs = wxStaticText(self.panel, label='')
##self.acobjs.SetFont(self.parentobj.font)
##self.acterms_label = wxStaticText(self.panel, label='Go Terms involved')
##self.acterms_label.SetFont(self.parentobj.font)
##self.acterms = wxStaticText(self.panel, label='')
##self.acterms.SetFont(self.parentobj.font)
##self.descbox.AddMany([(self.filename_label), (self.filename), (self.acobjs_label), (self.acobjs), (self.acterms_label), (self.acterms)])
#self.descbox.AddMany([(self.filename_label), (self.filename)])