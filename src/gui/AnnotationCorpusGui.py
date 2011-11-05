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
from GO import PlainAnnotationCorpus
from GO import GAF2AnnotationCorpus
from gui import WorkProcess

GAF2_FILE_TYPE = 'GAF 2.0 (GOA)'
PLAIN_FILE_TYPE = 'plain'
AC_FILE_TYPES = [ GAF2_FILE_TYPE, PLAIN_FILE_TYPE]

class AnnotationCorpusGui(wx.Dialog):
	filetype = None
	plainfileorder = 0
	ac_filename = None
		
	def __init__(self, parent):
		self.parent = parent
		super(AnnotationCorpusGui, self).__init__(self.parent, title="Load Annotation Corpus")
		self.InitUI()
	
	def InitUI(self):
		self.panel = wx.Panel(self)
		self.Bind(wx.EVT_CLOSE, self.OnQuit, id=self.GetId())
#------------------------------------------------------------------------------------------------------------------
		#main box
		self.mainbox = wx.BoxSizer(wx.VERTICAL)
		self.fileboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Annotation Corpus file')
		self.filebox = wx.StaticBoxSizer(self.fileboxline, wx.VERTICAL)
		self.filegridbox= wx.FlexGridSizer(rows = 2, cols = 3, vgap = 6, hgap = 10)
		self.filebox.Add(self.filegridbox,wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=15)
		#self.filenamebox = wx.BoxSizer(wx.HORIZONTAL)
		#self.filetypebox= wx.BoxSizer(wx.HORIZONTAL)
		#self.acboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Annotation Corpus')
		#self.acbox = wx.StaticBoxSizer(self.acboxline, wx.HORIZONTAL)
		self.acstatsboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Annotation Corpus statistics')
		self.acstatsbox = wx.StaticBoxSizer(self.acstatsboxline, wx.HORIZONTAL)
		self.commandbox = wx.BoxSizer(wx.HORIZONTAL)
		
		self.mainbox.Add(self.filebox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		#self.filebox.Add(self.filenamebox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		#self.filebox.Add(self.filetypebox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		#self.mainbox.Add(self.acbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		self.mainbox.Add(self.acstatsbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		self.mainbox.Add(self.commandbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		
#FILE CHOOSER
		self.label_filenamelabel = wx.StaticText(self.panel, label='File name')
		self.label_filename = wx.StaticText(self.panel, label='', size=(200,20), style = wx.ST_NO_AUTORESIZE) #style= wx.ST_ELLIPSIZE_MIDDLE | 
		self.button_selectfile = wx.Button(self.panel, wx.ID_ANY, 'Select...')
		self.Bind(wx.EVT_BUTTON, self.OnFileBrowse, id=self.button_selectfile.GetId())

#FILE TYPE CHOOSER
		self.box_filetype = wx.ComboBox(self.panel, wx.ID_ANY, choices=AC_FILE_TYPES, style=wx.CB_READONLY) #size=(100,30)
		self.label_filetypelabel = wx.StaticText(self.panel, label='File type')
		self.Bind(wx.EVT_COMBOBOX, self.OnSelectType, id=self.box_filetype.GetId())
		self.button_filetypeparams = wx.Button(self.panel, wx.ID_ANY, 'Advanced...')
		self.Bind(wx.EVT_BUTTON, self.OnAdvanced, id=self.button_filetypeparams.GetId())

#OTHER COMMANDS

		self.button_load = wx.Button(self.panel, wx.ID_ANY, 'Load')
		self.Bind(wx.EVT_BUTTON, self.OnLoad, id=self.button_load.GetId())
		#self.button_load.Disable()
		self.Bind(wx.EVT_BUTTON, self.OnLoad, id=self.button_load.GetId())
		self.button_reset = wx.Button(self.panel, wx.ID_ANY, 'Reset')
		self.Bind(wx.EVT_BUTTON, self.OnReset, id=self.button_reset.GetId())
		self.button_done = wx.Button(self.panel, wx.ID_ANY, 'Close')
		self.Bind(wx.EVT_BUTTON, self.OnDone, id=self.button_done.GetId())
		

# PUTTING ALL TOGETHER
		#self.filenamebox.Add(self.label_filename, flag=wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		#self.filenamebox.Add(self.button_selectfile, flag=wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		#self.filetypebox.Add(self.label_filetype, flag=wx.UP|wx.DOWN|wx.LEFT|wx.RIGHT, border=5)
		#self.filetypebox.Add(self.box_filetype, flag=wx.UP|wx.DOWN|wx.LEFT|wx.RIGHT, border=5)
		#self.filetypebox.Add(self.button_filetypeparams, flag=wx.UP|wx.DOWN|wx.LEFT|wx.RIGHT, border=5)

		self.filegridbox.AddMany([(self.label_filenamelabel), (self.label_filename), (self.button_selectfile), (self.label_filetypelabel), (self.box_filetype), (self.button_filetypeparams)])
		
		self.commandbox.Add(self.button_load, flag=wx.LEFT|wx.RIGHT, border=10)
		self.commandbox.Add(self.button_reset, flag=wx.LEFT|wx.RIGHT, border=10)
		self.commandbox.Add(self.button_done, flag=wx.LEFT|wx.RIGHT, border=10)

		self.fakecmd = wx.Button(self.panel, wx.ID_ANY, 'Load')
		self.fakecmd.Hide()
		self.fakecmd.Disable()
		self.Bind(wx.EVT_BUTTON, self.OnFakeCmd, id=self.fakecmd.GetId())


		#statusbox
		#self.statusbox = wx.BoxSizer(wx.HORIZONTAL)
		#self.status_label = wx.StaticText(self.panel, label='No Annotation Corpus loaded.')
		#self.status_label.SetFont(self.parent.font)
		#self.statusbox.Add(self.status_label, border=10)

		#self.mainbox.Add(self.statusbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		
		self.panel.SetSizerAndFit(self.mainbox)
		self.InitMainUI()
		self.OnReset(None)
		return True


	def OnFileBrowse(self, event):
		dialog = wx.FileDialog(None, style = wx.OPEN)
		if dialog.ShowModal() == wx.ID_OK:
			self.label_filename.SetLabel(dialog.GetPath())
			self.filename = dialog.GetPath()
			self.OnCanStart()

	def OnDone(self, event):
		self.Hide()
		
	def OnQuit(self, event):
		self.OnDone(event)
		
	def OnReset(self, event):
		self.filename = None
		self.filetype = None
		self.label_filename.SetLabel("None specified.")
		self.box_filetype.SetValue('')
		self.params = None
		self.button_load.Disable()
		self.button_filetypeparams.Disable()

	def OnAdvanced(self, event):
		self.advancedGui = AdvancedGui(self)
		self.advancedGui.ShowModal()

	def OnSelectType(self, event):
		if self.filetype == AC_FILE_TYPES[self.box_filetype.GetSelection()]:
			pass
		else:
			self.filetype = AC_FILE_TYPES[self.box_filetype.GetSelection()]
			self.params = None
		self.button_filetypeparams.Enable()
		self.OnCanStart()

	def OnCanStart(self):
		if (not self.filename == None) and (not self.filetype == None):
			self.button_load.Enable()
		else:
			self.button_load.Disable()

#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
	def InitMainUI(self):
		#self.parent.ac_status_pic= wx.StaticBitmap(self.parent.panel)
		self.parent.SetAcOk(False)
		self.parent.ac_cmd = wx.Button(self.parent.panel, wx.ID_ANY, 'Load Annotation Corpus...')
		self.parent.ac_box.Add(self.parent.ac_cmd, flag=wx.ALL|wx.CENTER, border = 8)
		#self.parent.ac_box.Add(self.parent.ac_status_pic,flag=wx.ALL|wx.CENTER, border = 8)
		self.parent.Bind(wx.EVT_BUTTON, self.OnShowAC, id=self.parent.ac_cmd.GetId())
		
	def OnShowAC(self, event):
		self.parent.ACGui.ShowModal()
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

	def OnLoad(self, event):
		self.filechoosecmd.Disable()
		self.doneb.Disable()
		self.acload.Disable()
		self.parent.ac = None
		self.parent.SetAcOk(False)
		self.parent.update_ac = True
		self.parent.update_ssobject = True
		self.parent.update_query = True
		event = wx.PyCommandEvent(wx.EVT_BUTTON.typeId, self.fakecmd.GetId())
		wx.PostEvent(self.GetEventHandler(), event)

	def OnFakeCmd(self, event):
		self.parent.ac_running = True
		self.filechoosecmd.Disable()
		self.doneb.Disable()
		self.acload.Disable()
		self.ac = AnnotationCorpus.AnnotationCorpus(self.parent.go)
		param = {}
		if self.filetype == 'GOA':
			param= {'simplify':True}
		elif self.filetype == 'plain':
			param = {}
			param['multiple'] = False
			param['term first'] = False
			param['separator'] = '\t'
		else:
			param = None
			#if self.plainfileorder == 0:
				#param['AC_OBJ_FIRST'] = None
			#elif self.plainfileorder == 1:
				#param['AC_TERM_FIRST'] = None
		self.parent.lock()
		self.parent.gui2ssprocess_queue.put((WorkProcess.CMD_LOAD_AC, self.filename, self.filetype, param))
		self.status_label.SetLabel("Loading Annotation Corpus from file " + str(self.filename))
		self.TIMER_ID = 1000
		self.timer = wx.Timer(self.parent.panel, self.TIMER_ID)
		wx.EVT_TIMER(self.parent.panel, self.TIMER_ID, self.AC_timer)
		self.timer.Start(self.parent.UPDATE_INTERVAL)
		return False

	def AC_timer(self, event):
		try:
			data = self.parent.ssprocess2gui_queue.get(False)
			self.parent.unlock()
			self.filechoosecmd.Enable()
			self.doneb.Enable()
			self.acload.Enable()
			self.timer.Stop()
			if data[0] == WorkProcess.CMD_LOAD_AC:
				if data[1]:
					self.parent.SetAcOk(True)
					self.parent.update_ac = False
					self.status_label.SetLabel("Annotation Corpus loaded.")
					self.parent.ac_running = False
					return True
				self.status_label.SetLabel("Failed to load Annotation Corpus.")
			print("Failed to load Annotation Corpus.")
			self.parent.ac_running = False
			return False
		except Exception:
			#self.parent.unlock()
			#self.parent.ac_running = False
			return False


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

class AdvancedGui(wx.Dialog):

	def __init__(self, parent):
		self.parent = parent
		super(AdvancedGui, self).__init__(self.parent, title="Advanced settings", size=(600,600))
		self.InitUI()
	
	def InitUI(self):
		self.panel = wx.Panel(self)
		self.mainbox = wx.BoxSizer(wx.VERTICAL)
		
		if self.parent.filetype == PLAIN_FILE_TYPE:
			#self.fileformatboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Annotation Corpus file')
			#self.filebox = wx.StaticBoxSizer(self.fileboxline, wx.VERTICAL)
			self.gridbox= wx.FlexGridSizer(rows = 3, cols = 3, vgap = 30, hgap = 40)
			self.mainbox.Add(self.gridbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
			#self.filebox.Add(self.filegridbox,wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=15)
			##self.filenamebox = wx.BoxSizer(wx.HORIZONTAL)
			##self.filetypebox= wx.BoxSizer(wx.HORIZONTAL)
			##self.acboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Annotation Corpus')
			##self.acbox = wx.StaticBoxSizer(self.acboxline, wx.HORIZONTAL)
			#self.acstatsboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Annotation Corpus statistics')
			#self.acstatsbox = wx.StaticBoxSizer(self.acstatsboxline, wx.HORIZONTAL)
			#self.commandbox = wx.BoxSizer(wx.HORIZONTAL)

			self.label_separatorlabel = wx.StaticText(self.panel, wx.ID_ANY, 'Separator')
			self.separatorbox = wx.BoxSizer(wx.VERTICAL)
			self.separatoroptions = ['[tab] (\\t)\'','[space]','']
			self.radius_separator_1 = wx.RadioButton(self.panel, wx.ID_ANY, self.separatoroptions[0], (10, 10), style=wx.RB_GROUP)
			self.radius_separator_2 = wx.RadioButton(self.panel, wx.ID_ANY, self.separatoroptions[1], (10, 10))
			self.customseparatorbox = wx.BoxSizer(wx.HORIZONTAL)
			self.radius_separator_3 = wx.RadioButton(self.panel, wx.ID_ANY, self.separatoroptions[2], (10, 10))
			self.text_separator = wx.TextCtrl(self.panel, size=(20,20))
			self.Bind(wx.EVT_RADIOBUTTON, self.OnSelectSeparator, id=self.radius_separator_1.GetId())
			self.Bind(wx.EVT_RADIOBUTTON, self.OnSelectSeparator, id=self.radius_separator_2.GetId())
			self.Bind(wx.EVT_RADIOBUTTON, self.OnSelectSeparator, id=self.radius_separator_3.GetId())
			
			self.text_separator.Disable()
			self.separatorbox.Add(self.radius_separator_1) 
			self.separatorbox.Add(self.radius_separator_2)
			self.separatorbox.Add(self.customseparatorbox)
			self.customseparatorbox.Add(self.radius_separator_3)
			self.customseparatorbox.Add(self.text_separator)
			self.label_separatorexplanation = wx.StaticText(self.panel, wx.ID_ANY, 'You should select the character used to separate fields within the single rows.', size=(250,60))
			
			self.label_rowtypelabel = wx.StaticText(self.panel, wx.ID_ANY, 'Row format')
			self.check_manyperline = wx.CheckBox(self.panel, wx.ID_ANY, 'Many associations per line')
			self.Bind(wx.EVT_CHECKBOX, self.OnManyperline, id=self.check_manyperline.GetId())
			self.check_manyperline.SetValue(False)
			self.label_rowtypeexplanation = wx.StaticText(self.panel, wx.ID_ANY, 'Check this option if each row contains more than one association between protein/genes and GO Terms.', size=(250,60))

			self.label_rowformatlabel = wx.StaticText(self.panel, wx.ID_ANY, 'Data order')
			#self.rowformatboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Row format')
			#self.rowformatbox = wx.StaticBoxSizer(self.rowformatboxline, wx.VERTICAL)
			self.rowformatbox = wx.BoxSizer(wx.VERTICAL)
			self.rowformatoptions = ['object name\tGO term','GO term\tobject name']
			self.radius_rowformat_1 = wx.RadioButton(self.panel, wx.ID_ANY, self.rowformatoptions[0], (10, 10), style=wx.RB_GROUP)
			self.radius_rowformat_2 = wx.RadioButton(self.panel, wx.ID_ANY, self.rowformatoptions[1], (10, 10))
			self.rowformatbox.Add(self.radius_rowformat_1)
			self.rowformatbox.Add(self.radius_rowformat_2)
			self.label_rowformatexplanation = wx.StaticText(self.panel, wx.ID_ANY, 'Select whether the first field of each row is the protein\gene or a GO Term.', size=(250,60))
			
			self.gridbox.AddMany([(self.label_separatorlabel), (self.separatorbox), (self.label_separatorexplanation), (self.label_rowtypelabel), (self.check_manyperline), (self.label_rowtypeexplanation), self.label_rowformatlabel, self.rowformatbox, self.label_rowformatexplanation])

			self.button_save = wx.Button(self.panel, wx.ID_ANY, 'Save')
			self.button_cancel = wx.Button(self.panel, wx.ID_ANY, 'Cancel')
			self.Bind(wx.EVT_BUTTON, self.OnSave, id=self.button_save.GetId())
			self.Bind(wx.EVT_BUTTON, self.OnCancel, id=self.button_cancel.GetId())
			
			self.mainbox.Add(self.button_save, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP)
			self.mainbox.Add(self.button_cancel, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP)

		self.panel.SetSizerAndFit(self.mainbox)
		self.OnRestore()

	def OnManyperline(self, event):
		pass

	def OnRestore(self):
		if not self.parent.params == None:
			if self.parent.params[PlainAnnotationCorpus.SEPARATOR] == '\t':
				self.radius_separator_1.SetValue(True)
			elif self.parent.params[PlainAnnotationCorpus.SEPARATOR] == ' ':
				self.radius_separator_2.SetValue(True)
			else:
				self.radius_separator_3.SetValue(True)
				self.text_separator.SetValue(self.parent.params[PlainAnnotationCorpus.SEPARATOR])
			self.check_manyperline.SetValue(self.parent.params[PlainAnnotationCorpus.MANYASSPERROW])
			self.radius_rowformat_1.SetValue(self.parent.params[PlainAnnotationCorpus.TERMFIRST])
			self.OnSelectSeparator(None)
				
	def OnSave(self, event):
		self.parent.params = {}
		if self.radius_separator_1.GetValue():
			self.parent.params[PlainAnnotationCorpus.SEPARATOR] = '\t'
		elif self.radius_separator_2.GetValue():
			self.parent.params[PlainAnnotationCorpus.SEPARATOR] = ' '
		else:
			self.parent.params[PlainAnnotationCorpus.SEPARATOR] = self.text_separator.GetValue()
		self.parent.params[PlainAnnotationCorpus.MANYASSPERROW] = self.check_manyperline.GetValue()
		self.parent.params[PlainAnnotationCorpus.TERMFIRST] = self.radius_rowformat_1.GetValue()
		self.Close()

	def OnCancel(self, event):
		self.Close()

	def OnSelectSeparator(self, event):
			if self.radius_separator_1.GetValue() or self.radius_separator_2.GetValue():
				self.text_separator.Disable()
			else:
				self.text_separator.Enable()

	#def OnLoad(self, event):
		#self.filechoosecmd.Disable()
		#self.doneb.Disable()
		#self.acload.Disable()
		#self.parent.ac = None
		#self.parent.SetAcOk(False)
		#self.parent.update_ac = True
		#self.parent.update_ssobject = True
		#self.parent.update_query = True
		#event = wx.PyCommandEvent(wx.EVT_BUTTON.typeId, self.fakecmd.GetId())
		#wx.PostEvent(self.GetEventHandler(), event)

	#def OnFakeCmd(self, event):
		#self.parent.ac_running = True
		#self.filechoosecmd.Disable()
		#self.doneb.Disable()
		#self.acload.Disable()
		#self.ac = AnnotationCorpus.AnnotationCorpus(self.parent.go)
		#param = {}
		#if self.filetype == 'GOA':
			#param= {'simplify':True}
		#elif self.filetype == 'plain':
			#param = {}
			#param['multiple'] = False
			#param['term first'] = False
			#param['separator'] = '\t'
		#else:
			#param = None
			##if self.plainfileorder == 0:
				##param['AC_OBJ_FIRST'] = None
			##elif self.plainfileorder == 1:
				##param['AC_TERM_FIRST'] = None
		#self.parent.lock()
		#self.parent.gui2ssprocess_queue.put((WorkProcess.CMD_LOAD_AC, self.filename, self.filetype, param))
		#self.status_label.SetLabel("Loading Annotation Corpus from file " + str(self.filename))
		#self.TIMER_ID = 1000
		#self.timer = wx.Timer(self.parent.panel, self.TIMER_ID)
		#wx.EVT_TIMER(self.parent.panel, self.TIMER_ID, self.AC_timer)
		#self.timer.Start(self.parent.UPDATE_INTERVAL)
		#return False

	#def AC_timer(self, event):
		#try:
			#data = self.parent.ssprocess2gui_queue.get(False)
			#self.parent.unlock()
			#self.filechoosecmd.Enable()
			#self.doneb.Enable()
			#self.acload.Enable()
			#self.timer.Stop()
			#if data[0] == WorkProcess.CMD_LOAD_AC:
				#if data[1]:
					#self.parent.SetAcOk(True)
					#self.parent.update_ac = False
					#self.status_label.SetLabel("Annotation Corpus loaded.")
					#self.parent.ac_running = False
					#return True
				#self.status_label.SetLabel("Failed to load Annotation Corpus.")
			#print("Failed to load Annotation Corpus.")
			#self.parent.ac_running = False
			#return False
		#except Exception:
			##self.parent.unlock()
			##self.parent.ac_running = False
			#return False

		
##self.descbox = wx.FlexGridSizer(rows = 4, cols = 2, vgap = 6, hgap = 20)
##self.filename_label = wx.StaticText(self.panel, label='AC File')
##self.filename_label.SetFont(self.parent.font)
##self.filename = wx.StaticText(self.panel, label='')
###self.acobjs_label = wx.StaticText(self.panel, label='Objects')
####self.acobjs_label.SetFont(self.parent.font)
###self.acobjs = wx.StaticText(self.panel, label='')
###self.acobjs.SetFont(self.parent.font)
###self.acterms_label = wx.StaticText(self.panel, label='Go Terms involved')
###self.acterms_label.SetFont(self.parent.font)
###self.acterms = wx.StaticText(self.panel, label='')
###self.acterms.SetFont(self.parent.font)
###self.descbox.AddMany([(self.filename_label), (self.filename), (self.acobjs_label), (self.acobjs), (self.acterms_label), (self.acterms)])
##self.descbox.AddMany([(self.filename_label), (self.filename)])

	#def OnFileBrowse(self, event):
		#dialog = wx.FileDialog(None, style = wx.OPEN)
		#if dialog.ShowModal() == wx.ID_OK:
			#self.label_filename.SetLabel(dialog.GetPath())
			#self.filename = dialog.GetPath()
			#if (not self.filename == None) and (not self.filetype == None):
				#self.button_load.Enable()

	#def OnDone(self, event):
		#self.Hide()
		
	#def OnQuit(self, event):
		#self.OnDone(event)
		
	#def OnReset(self, event):
		#self.filename = None
		#self.filetype = None
		#self.label_filename.SetLabel("None specified.")
		#self.box_filetype.SetValue('')
		#self.params = None
		
	#def OnShowAC(self, event):
		#self.parent.ACGui.ShowModal()

	#def OnAdvanced(self, event):
		#self.advancedGui = AdvancedGui(self, self.params)
		#self.advancedGui.ShowModal()
