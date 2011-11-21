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
import wx
from fastSemSim.GO import GeneOntology
from fastSemSim.GO import AnnotationCorpus
from fastSemSim.GO import PlainAnnotationCorpus
from fastSemSim.GO import GAF2AnnotationCorpus
import WorkProcess
import os

GAF2_FILE_TYPE = 'GAF 2.0 (GOA)'
GAF2_FILE_TYPE_REF = 'gaf-2.0'
PLAIN_FILE_TYPE = 'Plain'
PLAIN_FILE_TYPE_REF = 'plain'
AC_FILE_TYPES = [ GAF2_FILE_TYPE, PLAIN_FILE_TYPE]

class AnnotationCorpusGui(wx.Dialog):
	filetype = None
	filename = None
		
	def __init__(self, parent):
		self.parent = parent
		super(AnnotationCorpusGui, self).__init__(self.parent, title="Load Annotation Corpus", size=(500,300))
		self.InitUI()
	
	def InitUI(self):
		self.panel = wx.Panel(self)
		self.Bind(wx.EVT_CLOSE, self.OnQuit, id=self.GetId())
#------------------------------------------------------------------------------------------------------------------
		#main box
		self.mainbox = wx.BoxSizer(wx.VERTICAL)
		self.fileboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Input file')
		self.filebox = wx.StaticBoxSizer(self.fileboxline, wx.VERTICAL)
		self.filegridbox= wx.FlexGridSizer(rows = 3, cols = 3, vgap = 10, hgap = 10)
		self.filebox.Add(self.filegridbox,wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=15)
		#self.filenamebox = wx.BoxSizer(wx.HORIZONTAL)
		#self.filetypebox= wx.BoxSizer(wx.HORIZONTAL)
		#self.acboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Annotation Corpus')
		#self.acbox = wx.StaticBoxSizer(self.acboxline, wx.HORIZONTAL)
		self.acstatsboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Statistics')
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
		self.label_filename = wx.StaticText(self.panel, label='', size=(250,20), style = wx.ST_NO_AUTORESIZE) #style= wx.ST_ELLIPSIZE_MIDDLE | 
		self.button_selectfile = wx.Button(self.panel, wx.ID_ANY, 'Select...')
		self.Bind(wx.EVT_BUTTON, self.OnFileBrowse, id=self.button_selectfile.GetId())

#FILE TYPE CHOOSER
		self.box_filetype = wx.ComboBox(self.panel, wx.ID_ANY, choices=AC_FILE_TYPES, style=wx.CB_READONLY) #size=(100,30)
		self.label_filetypelabel = wx.StaticText(self.panel, label='File type')
		self.Bind(wx.EVT_COMBOBOX, self.OnSelectType, id=self.box_filetype.GetId())
		self.button_filetypeparams = wx.Button(self.panel, wx.ID_ANY, 'Advanced...')
		self.Bind(wx.EVT_BUTTON, self.OnAdvanced, id=self.button_filetypeparams.GetId())

# STATISTICS
		self.label_statuslabel = wx.StaticText(self.panel, label = "File loaded")
		self.label_status = wx.StaticText(self.panel, label = "", size=(250,30))
		self.label_objslabel = wx.StaticText(self.panel, label = "Annotated Genes/Proteins")
		self.label_objs = wx.StaticText(self.panel, label = "")
		self.label_termslabel = wx.StaticText(self.panel, label = "GO Terms involved")
		self.label_terms = wx.StaticText(self.panel, label = "")
		self.statusgridbox= wx.FlexGridSizer(rows = 4, cols = 2, vgap = 10, hgap = 10)
		self.statusgridbox.AddMany([wx.Size(5,2), wx.Size(5,2), self.label_statuslabel, self.label_status, self.label_objslabel, self.label_objs, self.label_termslabel, self.label_terms])
		self.acstatsbox.Add(self.statusgridbox)

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

		self.filegridbox.AddMany([wx.Size(5,2), wx.Size(5,2), wx.Size(5,2), (self.label_filenamelabel), (self.label_filename), (self.button_selectfile), (self.label_filetypelabel), (self.box_filetype), (self.button_filetypeparams)])
		
		self.commandbox.Add(self.button_load, flag=wx.LEFT|wx.RIGHT, border=10)
		self.commandbox.Add(self.button_reset, flag=wx.LEFT|wx.RIGHT, border=10)
		self.commandbox.Add(self.button_done, flag=wx.LEFT|wx.RIGHT, border=10)


		#statusbox
		#self.statusbox = wx.BoxSizer(wx.HORIZONTAL)
		#self.status_label = wx.StaticText(self.panel, label='No Annotation Corpus loaded.')
		#self.status_label.SetFont(self.parent.font)
		#self.statusbox.Add(self.status_label, border=10)

		#self.mainbox.Add(self.statusbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		
		self.panel.SetSizerAndFit(self.mainbox)
		self.InitMainUI()
		self.OnReset(None)
		self.OnLoadDone()
		return True


	def OnFileBrowse(self, event):
		dialog = wx.FileDialog(None, style = wx.OPEN)
		if dialog.ShowModal() == wx.ID_OK:
			self.filename = dialog.GetPath()
			self.label_filename.SetLabel(os.path.basename(self.filename))
			self.OnCanStart()

	def OnDone(self, event):
		self.Hide()
		
	def OnQuit(self, event):
		self.OnDone(event)
		
	def OnReset(self, event):
		self.filename = None
		self.filetype = None
		self.ac_status = False
		self.label_filename.SetLabel("None specified.")
		self.box_filetype.SetValue('')
		self.params = None
		self.button_load.Disable()
		self.button_filetypeparams.Disable()
		self.filetypesel = None
		self.OnLoadDone()
		print "Fix Me. Should Reset ac in main process!!"

	def OnAdvanced(self, event):
		self.advancedGui = AdvancedGui(self)
		self.advancedGui.ShowModal()

	def OnSelectType(self, event):
		if self.filetypesel == AC_FILE_TYPES[self.box_filetype.GetSelection()]:
			pass
		else:
			self.filetypesel = AC_FILE_TYPES[self.box_filetype.GetSelection()]
			if self.filetypesel == PLAIN_FILE_TYPE:
				self.filetype = PLAIN_FILE_TYPE_REF
			elif self.filetypesel == GAF2_FILE_TYPE:
				self.filetype = GAF2_FILE_TYPE_REF
			else:
				self.filetype = None
			self.params = None
		self.button_filetypeparams.Enable()
		self.OnCanStart()

	def OnCanStart(self):
		if (not self.filename == None) and (not self.filetype == None):
			self.button_load.Enable()
			return True
		else:
			self.button_load.Disable()
			return False

	def OnLoad(self, event):
		self.loadACGui = LoadACGui(self)
		self.loadACGui.ShowModal()
		self.OnLoadDone()
		
	def OnLoadDone(self):
		if self.ac_status:
			self.label_status.SetLabel(os.path.basename(self.filename))
			self.label_objs.SetLabel(str(self.ac_objs))
			self.label_terms.SetLabel(str(self.ac_terms))
			self.parent.SetAcOk(True)
			self.parent.update_ac = False
		else:
			self.label_status.SetLabel('')
			self.label_objs.SetLabel('')
			self.label_terms.SetLabel('')
			self.parent.SetAcOk(False)
			self.parent.update_ac = False

#------------------------------------------------------------------------------------------------------------------
	def InitMainUI(self):
		#self.parent.ac_status_pic= wx.StaticBitmap(self.parent.panel)
		self.parent.SetAcOk(False)
		self.parent.ac_cmd = wx.Button(self.parent.panel, wx.ID_ANY, 'Annotation Corpus...')
		self.parent.ac_box.Add(self.parent.ac_cmd, flag=wx.ALL|wx.CENTER, border = 8)
		#self.parent.ac_box.Add(self.parent.ac_status_pic,flag=wx.ALL|wx.CENTER, border = 8)
		self.parent.Bind(wx.EVT_BUTTON, self.OnShowAC, id=self.parent.ac_cmd.GetId())
		
	def OnShowAC(self, event):
		self.parent.ACGui.ShowModal()
#---------------------------------------------------------------------------------------------------------------

	def batch_save(self):
		save = {}
		save['ac_filename'] = self.filename
		save['ac_filetype'] = self.filetype
		save['ac_params'] = self.params
		return save

	def batch_load(self, save):
		if 'ac_filename' in save:
			self.filename = save['ac_filename']
		if 'ac_filetype' in save:
			self.filetype = save['ac_filetype']
		if 'ac_params' in save:
			self.params = save['ac_params']
		if self.OnCanStart():
			self.OnLoad()

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

class AdvancedGui(wx.Dialog):

	def __init__(self, parent):
		self.parent = parent
		super(AdvancedGui, self).__init__(self.parent, title="Advanced settings", size=(800,600))
		self.InitUI()
	
	def InitUI(self):
		self.panel = wx.Panel(self)
		self.mainbox = wx.BoxSizer(wx.HORIZONTAL)

		if self.parent.filetypesel == PLAIN_FILE_TYPE:
			self.fileformatboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Parse parameters')
			self.fileformatbox = wx.StaticBoxSizer(self.fileformatboxline, wx.VERTICAL)
			self.gridbox= wx.FlexGridSizer(rows = 4, cols = 3, vgap = 15, hgap = 20)
			self.mainbox.Add(self.fileformatbox, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
			self.fileformatbox.Add(self.gridbox, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

			self.label_separatorlabel = wx.StaticText(self.panel, wx.ID_ANY, 'Separator')
			self.separatorbox = wx.BoxSizer(wx.VERTICAL)
			self.separatoroptions = ['[tab] (\\t)','[space]','']
			self.radius_separator_1 = wx.RadioButton(self.panel, wx.ID_ANY, self.separatoroptions[0], (10, 10), style=wx.RB_GROUP)
			self.radius_separator_2 = wx.RadioButton(self.panel, wx.ID_ANY, self.separatoroptions[1], (10, 10))
			self.customseparatorbox = wx.BoxSizer(wx.HORIZONTAL)
			self.radius_separator_3 = wx.RadioButton(self.panel, wx.ID_ANY, self.separatoroptions[2], (10, 10))
			self.text_separator = wx.TextCtrl(self.panel) #size=(20,20))
			self.text_separator.SetValue("     ")
			self.text_separator.SetValue("")
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
			self.rowformatoptions = ['Gene -> GO Term','GO Term -> Gene']
			self.radius_rowformat_1 = wx.RadioButton(self.panel, wx.ID_ANY, self.rowformatoptions[0], (10, 10), style=wx.RB_GROUP)
			self.radius_rowformat_2 = wx.RadioButton(self.panel, wx.ID_ANY, self.rowformatoptions[1], (10, 10))
			self.rowformatbox.Add(self.radius_rowformat_1)
			self.rowformatbox.Add(self.radius_rowformat_2)
			self.label_rowformatexplanation = wx.StaticText(self.panel, wx.ID_ANY, 'Select whether the first field of each row is a protein\gene or a GO Term.', size=(250,60))
			
			self.gridbox.AddMany([wx.Size(5,10), wx.Size(5,10), wx.Size(5,10), (self.label_separatorlabel), (self.separatorbox), (self.label_separatorexplanation), (self.label_rowtypelabel), (self.check_manyperline), (self.label_rowtypeexplanation), self.label_rowformatlabel, self.rowformatbox, self.label_rowformatexplanation])

		elif self.parent.filetypesel == GAF2_FILE_TYPE:
			#self.fileformatboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Annotation Corpus file')
			#self.filebox = wx.StaticBoxSizer(self.fileboxline, wx.VERTICAL)
			#self.filebox.Add(self.filegridbox,wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=15)
			##self.filenamebox = wx.BoxSizer(wx.HORIZONTAL)
			##self.filetypebox= wx.BoxSizer(wx.HORIZONTAL)
			##self.acboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Annotation Corpus')
			##self.acbox = wx.StaticBoxSizer(self.acboxline, wx.HORIZONTAL)
			#self.acstatsboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Annotation Corpus statistics')
			#self.acstatsbox = wx.StaticBoxSizer(self.acstatsboxline, wx.HORIZONTAL)
			#self.commandbox = wx.BoxSizer(wx.HORIZONTAL)

			#self.simplifyboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Simplification')
			#self.simplifybox = wx.StaticBoxSizer(self.simplifyboxline, wx.HORIZONTAL)

			#self.label_simplifylabel = wx.StaticText(self.panel, wx.ID_ANY, 'Simplify')
			self.check_simplify = wx.CheckBox(self.panel, wx.ID_ANY, 'Simplify annotation corpus')
			#self.Bind(wx.EVT_CHECKBOX, self.OnSimplify, id=self.check_simplify.GetId())
			self.check_simplify.SetValue(False)
			self.label_simplifyexplanation = wx.StaticText(self.panel, wx.ID_ANY, 'Check this option if want to remove EC and other information relative to annotations after data have been parsed. This might be a good idea if the annotation corpus is HUGE. It does not affect computation results.', size=(250,60))
			#self.simplifybox.Add(self.label_simplifylabel)
			#self.simplifybox.Add(wx.Size(10,2))
			#self.simplifybox.Add(self.check_simplify)
			#self.simplifybox.Add(wx.Size(10,2))
			#self.simplifybox.Add(self.label_simplifyexplanation)

			self.filterboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Filters')
			self.filterbox = wx.StaticBoxSizer(self.filterboxline, wx.VERTICAL)

			self.gridbox= wx.FlexGridSizer(rows = 3, cols = 3, vgap = 15, hgap = 20)
			self.filterbox.Add(self.gridbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
			
			self.check_filterEC = wx.CheckBox(self.panel, wx.ID_ANY, 'Ignore IEA')
			#self.Bind(wx.EVT_CHECKBOX, self.OnSimplify, id=self.check_simplify.GetId())
			self.check_filterEC.SetValue(False)
			self.label_filterECexplanation = wx.StaticText(self.panel, wx.ID_ANY, 'Check this option if you want to ignore IEA (Inferred Electronically Annotations).', size=(250,60))
			
			self.check_filtertax = wx.CheckBox(self.panel, wx.ID_ANY, 'Restrict to Taxonomy')
			self.Bind(wx.EVT_CHECKBOX, self.OnFilterTax, id=self.check_filtertax.GetId())
			self.label_taxlabel = wx.StaticText(self.panel, wx.ID_ANY, 'Taxonomy Id:')
			self.text_filtertax = wx.TextCtrl(self.panel, size=(50,20))
			self.taxbox = wx.BoxSizer(wx.HORIZONTAL)
			self.taxbox.Add(self.label_taxlabel)
			self.taxbox.Add(self.text_filtertax)
			self.check_filtertax.SetValue(False)
			self.label_filtertaxexplanation = wx.StaticText(self.panel, wx.ID_ANY, 'Check this option to discard all the proteins/genes not belonging to the taxonomy that you have to specify in the text field.', size=(250,60))

			self.gridbox.AddMany([wx.Size(5,10), wx.Size(5,10), wx.Size(5,10), self.check_simplify, wx.Size(5,10), self.label_simplifyexplanation, (self.check_filterEC), wx.Size(5,10), (self.label_filterECexplanation), (self.check_filtertax), (self.taxbox), (self.label_filtertaxexplanation)])
			
			#self.mainbox.Add(wx.Size(5,20))
			#self.mainbox.Add(self.simplifybox, flag = wx.LEFT , border=10)
			self.mainbox.Add(wx.Size(5,20))
			self.mainbox.Add(self.filterbox)
			self.OnFilterTax(None)

		self.commandbox= wx.BoxSizer(wx.VERTICAL)
		self.button_save = wx.Button(self.panel, wx.ID_ANY, 'Save')
		self.button_cancel = wx.Button(self.panel, wx.ID_ANY, 'Cancel')
		self.Bind(wx.EVT_BUTTON, self.OnSave, id=self.button_save.GetId())
		self.Bind(wx.EVT_BUTTON, self.OnCancel, id=self.button_cancel.GetId())
		
		self.commandbox.Add(wx.Size(5,20))
		self.commandbox.Add(self.button_save, flag=wx.LEFT|wx.RIGHT|wx.TOP)
		self.commandbox.Add(self.button_cancel, flag=wx.LEFT|wx.RIGHT|wx.TOP)
		self.mainbox.Add(self.commandbox, flag= wx.EXPAND |wx.LEFT|wx.RIGHT|wx.TOP)

		self.panel.SetSizerAndFit(self.mainbox)
		self.OnRestore()

	def OnManyperline(self, event):
		pass

	def OnFilterTax(self, event):
		if self.check_filtertax.GetValue():
			self.text_filtertax.Enable()
			self.text_filtertax.SetFocus()
		else:
			self.text_filtertax.Disable()

	def OnRestore(self):
		if not self.parent.params == None:
			if self.parent.filetypesel == PLAIN_FILE_TYPE:
				if self.parent.params[PlainAnnotationCorpus.SEPARATOR] == '\t':
					self.radius_separator_1.SetValue(True)
				elif self.parent.params[PlainAnnotationCorpus.SEPARATOR] == ' ':
					self.radius_separator_2.SetValue(True)
				else:
					self.radius_separator_3.SetValue(True)
					self.text_separator.SetValue(self.parent.params[PlainAnnotationCorpus.SEPARATOR])
				self.check_manyperline.SetValue(self.parent.params[PlainAnnotationCorpus.MANYASSPERROW])
				self.radius_rowformat_1.SetValue(self.parent.params[PlainAnnotationCorpus.TERMFIRST])
				self.radius_rowformat_2.SetValue(not self.parent.params[PlainAnnotationCorpus.TERMFIRST])
				self.OnSelectSeparator(None)
			elif self.parent.filetypesel == GAF2_FILE_TYPE:
				if GAF2AnnotationCorpus.SIMPLIFY in self.parent.params:
					self.check_simplify.SetValue(self.parent.params[GAF2AnnotationCorpus.SIMPLIFY])
				if AnnotationCorpus.FILTER_PARAM in self.parent.params:
					if 'EC' in self.parent.params[AnnotationCorpus.FILTER_PARAM]:
						self.check_filterEC.SetValue(True)
					if 'taxonomy' in self.parent.params[AnnotationCorpus.FILTER_PARAM]:
						self.check_filtertax.SetValue(True)
						self.text_filtertax.SetValue(str(self.parent.params[AnnotationCorpus.FILTER_PARAM]['taxonomy']))
						self.OnFilterTax(None)

	def OnSave(self, event):
		self.parent.params = {}
		if self.parent.filetypesel == PLAIN_FILE_TYPE:
			if self.radius_separator_1.GetValue():
				self.parent.params[PlainAnnotationCorpus.SEPARATOR] = '\t'
			elif self.radius_separator_2.GetValue():
				self.parent.params[PlainAnnotationCorpus.SEPARATOR] = ' '
			else:
				if len(self.text_separator.GetValue())>0:
					self.parent.params[PlainAnnotationCorpus.SEPARATOR] = self.text_separator.GetValue()
				else:
					wx.MessageDialog(self, "Please insert a separator.", "Missing separator", style = wx.OK | wx.CENTRE | wx.ICON_EXCLAMATION).ShowModal()
					self.text_separator.SetFocus()
					return
			self.parent.params[PlainAnnotationCorpus.MANYASSPERROW] = self.check_manyperline.GetValue()
			self.parent.params[PlainAnnotationCorpus.TERMFIRST] = self.radius_rowformat_2.GetValue()
		elif self.parent.filetypesel == GAF2_FILE_TYPE:
			self.parent.params[GAF2AnnotationCorpus.SIMPLIFY] = self.check_simplify.GetValue()
			self.parent.params[AnnotationCorpus.FILTER_PARAM] = {}
			if self.check_filterEC.GetValue():
				self.parent.params[AnnotationCorpus.FILTER_PARAM]['EC'] = 'IEA'
			if self.check_filtertax.GetValue() and len(self.text_filtertax.GetValue())>0:
				try:
					self.parent.params[AnnotationCorpus.FILTER_PARAM]['taxonomy'] = int(self.text_filtertax.GetValue())
				except Exception:
					wx.MessageDialog(self, "Please insert a numeric taxonomic id.", "Wrong or missing taxonomic id", style = wx.OK | wx.CENTRE | wx.ICON_EXCLAMATION).ShowModal()
					self.text_filtertax.SetFocus()
					return
					
		self.Close()

	def OnCancel(self, event):
		self.Close()

	def OnSelectSeparator(self, event):
			if self.radius_separator_1.GetValue() or self.radius_separator_2.GetValue():
				self.text_separator.Disable()
			else:
				self.text_separator.Enable()
				self.text_separator.SetFocus()

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

class LoadACGui(wx.Dialog):

	def __init__(self, parent):
		self.parent = parent
		super(LoadACGui, self).__init__(self.parent, title="Loading Annotation Corpus", size=(300,250))
		self.InitUI()
	
	def InitUI(self):
		self.panel = wx.Panel(self)
		self.mainbox = wx.BoxSizer(wx.VERTICAL)
		self.loadbarboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Progress Bar')
		self.loadbarbox = wx.StaticBoxSizer(self.loadbarboxline, wx.HORIZONTAL)
		self.gauge_loadprogress = wx.Gauge(self.panel, -1, 50, size=(250, 25))
		self.loadbarbox.Add(self.gauge_loadprogress, flag=wx.EXPAND | wx.ALIGN_CENTER | wx.TOP, border = 5)
		
		self.statsbox = wx.BoxSizer(wx.HORIZONTAL)
		self.label_status = wx.StaticText(self.panel, wx.ID_ANY, 'Loading Annotation Corpus. Please wait...')
		self.statsbox.Add(self.label_status, flag = wx.ALIGN_CENTER )
		
		self.commandbox = wx.BoxSizer(wx.HORIZONTAL)
		self.button_abort = wx.Button(self.panel, wx.ID_ANY, 'Abort')
		self.button_ok = wx.Button(self.panel, wx.ID_ANY, 'Ok')
		self.button_ok.Disable()
		self.button_abort.Disable()
		self.commandbox.Add(self.button_abort, flag = wx.ALIGN_CENTER )
		self.commandbox.Add(self.button_ok, flag = wx.ALIGN_CENTER )
		self.Bind(wx.EVT_BUTTON, self.OnAbort, id=self.button_abort.GetId())
		self.Bind(wx.EVT_BUTTON, self.OnOk, id=self.button_ok.GetId())
		
		
		self.mainbox.Add(self.loadbarbox, flag = wx.ALIGN_CENTER)
		self.mainbox.Add(wx.Size(5,10), flag = wx.ALIGN_CENTER)
		self.mainbox.Add(self.statsbox, flag = wx.ALIGN_CENTER)
		self.mainbox.Add(wx.Size(5,10), flag = wx.ALIGN_CENTER)
		self.mainbox.Add(self.commandbox, flag = wx.ALIGN_CENTER)
		self.panel.SetSizerAndFit(self.mainbox)
		self.OnStart()

	def OnOk(self, event):
		self.Close()
	
	def OnAbort(self, event):
		print "OnAbort. Fix Me."
		#self.Close()

	def OnStart(self):

		#self.parent.parent.SetAcOk(False)
		#self.parent.update_ac = True
		#self.parent.update_ssobject = True
		#self.parent.update_query = True
		#print "Begin"
		self.parent.parent.lock()
		#print self.parent.filename
		#print self.parent.filetype
		#print self.parent.params
		self.parent.parent.gui2ssprocess_queue.put((WorkProcess.CMD_LOAD_AC, self.parent.filename, self.parent.filetype, self.parent.params))
		self.TIMER_ID = 1000
		self.timer = wx.Timer(self.panel, self.TIMER_ID)
		wx.EVT_TIMER(self.panel, self.TIMER_ID, self.AC_timer)
		self.timer.Start(1000)
		return False

	def AC_timer(self, event):
		if not self.parent.parent.ssprocess2gui_queue.empty():
			data = self.parent.parent.ssprocess2gui_queue.get(False)
			if data[0] == WorkProcess.CMD_LOAD_AC:
				if data[1] == WorkProcess.LOAD_AC_END:
					#print "End"
					self.parent.parent.unlock()
					self.timer.Stop()
					self.button_ok.Enable()
					self.button_abort.Disable()
					if data[2]:
						#print "Well"
						self.label_status.SetLabel("Task correctly completed.")
						self.parent.ac_status = True
						self.parent.ac_objs = data[3]
						self.parent.ac_terms = data[4]
						#self.parent.parent.SetAcOk(True)
						#self.parent.parent.update_ac = False
						self.gauge_loadprogress.SetValue(self.gauge_loadprogress.GetRange())
					else:
						self.label_status.SetLabel("Error. Please check parse parameters.")
						#self.parent.parent.SetAcOk(False)
						#self.parent.parent.update_ac = False
						self.parent.ac_status = False
						self.parent.ac_objs = None
						self.parent.ac_terms = None
						self.gauge_loadprogress.SetValue(0)
				elif data[1] == WorkProcess.LOAD_AC_STATUS:
					print "Status"
					gaugerange = self.gauge_loadprogress.GetRange()
					self.gauge_loadprogress.SetValue((float(data[2]))*gaugerange)
