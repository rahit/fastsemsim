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
import time

class ConfigFileParser():
	tags = {'go':{'go_filename':None, 'go_format':None},
			'ac':{'ac_filename':None, 'ac_format':None, 'ac_format_params':None},
			'ss':{'ss_measure':None, 'ss_mixing_strategy':None, 'ss_measure_params':None, 'ss_mixing_strategy_params':None, 'ss_go_tree':None},
			'query':{'query_format':None, 'query_from':None, 'query_filename':None},
			'output':{'output_to':None, 'output_filename':None, 'output_format':None}}

	separator = '\t'
	
	def __init__(self, filename):
		self.filename = str(filename)

	def load(self):
		if type(self.filename) is str:
			stream = open(self.filename,'r')
		else:
			stream = self.filename
		lines_counter = 0
		for line in stream:
			line = str(line.rstrip('\n'))
			line = line.rstrip('\r')
			line = line.split(self.separator) # should be there at least 3 tokens
			if len(line) < 3:
				continue
			#if len(line) > 2:
				#continue
			if line[0] in self.tags:
				temp = self.tags[line[0]]
				if line[1] in temp:
					temp[line[1]] = line[2]
			lines_counter += 1
		if type(self.filename) is str:
			stream.close()
		return self.tags
	
	def save(self):
		if type(self.filename) is str:
			stream = open(self.filename,'w')
		else:
			stream = self.filename
		for i in self.tags:
			for j in self.tags[i]:
				if not self.tags[i][j] == None:
					stream.write(i + "\t" + j + "\t" + str(self.tags[i][j]) + "\n")
		if type(self.filename) is str:
			stream.close()
		return self.tags
		
#------------------------------------------------------------------------------------------------------------

class DummyEvent(wx.PyEvent):
	def __init__(self, data):
		wx.PyEvent.__init__(self)
		self.SetEventType(data)
		self.data = None
		
class LoadConfigGui(wx.Dialog):

	def __init__(self, parent):
		self.parentobj = parent
		super(LoadConfigGui, self).__init__(self.parentobj, title="Loading Configuration", size=(400,200))
		self.InitUI()
		self.Process()
	
	def InitUI(self):
		self.panel = wx.Panel(self, -1)
		self.mainbox = wx.BoxSizer(wx.VERTICAL)
		self.filebox = wx.BoxSizer(wx.HORIZONTAL)
		self.file_label = wx.StaticText(self.panel, label='Configuration file: ')
		self.filename_label = wx.StaticText(self.panel, label='')
		self.filebox.Add(self.file_label)
		self.filebox.Add(self.filename_label)
		self.mainbox.Add(self.filebox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		
		self.go_label = wx.StaticText(self.panel, label='Loading Gene Ontology...')
		self.ac_label = wx.StaticText(self.panel, label='Loading Annotation Corpus...')
		self.ss_label = wx.StaticText(self.panel, label='Loading Semantic Similarity parameters...')
		self.query_label = wx.StaticText(self.panel, label='Loading Query...')
		self.output_label = wx.StaticText(self.panel, label='Loading Output parameters...')
		self.go_label.SetFont(self.parentobj.font)
		self.ac_label.SetFont(self.parentobj.font)
		self.ss_label.SetFont(self.parentobj.font)
		self.query_label.SetFont(self.parentobj.font)
		self.output_label.SetFont(self.parentobj.font)
		
		self.go_label.Disable()
		self.ac_label.Disable()
		self.ss_label.Disable()
		self.query_label.Disable()
		self.output_label.Disable()
		
		self.go_pic = wx.StaticBitmap(self.panel)
		self.ac_pic = wx.StaticBitmap(self.panel)
		self.query_pic = wx.StaticBitmap(self.panel)
		self.ss_pic = wx.StaticBitmap(self.panel)
		self.output_pic = wx.StaticBitmap(self.panel)
		
		self.descbox = wx.FlexGridSizer(rows = 5, cols = 2, vgap = 6, hgap = 20)
		self.descbox.AddMany([(self.go_label), (self.go_pic), (self.ac_label), (self.ac_pic), (self.ss_label), (self.ss_pic), (self.query_label), (self.query_pic), (self.output_label), (self.output_pic)])
		
		self.mainbox.Add(self.descbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		#self.progress = wx.Gauge(self.panel, -1, 50, size=(250, 25))
		#self.mainbox.Add(self.progress, flag=wx.TOP, border = 5)
		self.panel.SetSizerAndFit(self.mainbox)
		
		self.EVT_GO_ID = wx.NewId()
		self.EVT_AC_ID = wx.NewId()
		self.EVT_SS_ID = wx.NewId()
		self.EVT_QUERY_ID = wx.NewId()
		self.EVT_OUTPUT_ID = wx.NewId()
		self.EVT_DONE_ID = wx.NewId()
		self.Connect(-1, -1, self.EVT_GO_ID, self.ProcessGO)
		self.Connect(-1, -1, self.EVT_AC_ID, self.ProcessAC)
		self.Connect(-1, -1, self.EVT_SS_ID, self.ProcessSS)
		self.Connect(-1, -1, self.EVT_QUERY_ID, self.ProcessQuery)
		self.Connect(-1, -1, self.EVT_OUTPUT_ID, self.ProcessOutput)
		self.Connect(-1, -1, self.EVT_DONE_ID, self.ProcessDone)
		
		self.Show()

	def Process(self):
		#load configuration
		if self.parentobj.config_file == None:
			return
		self.filename_label.SetLabel(self.parentobj.config_file)
		self.config = ConfigFileParser(self.parentobj.config_file)
		self.tags = self.config.load()
		print self.tags
		#process configuration

		wx.PostEvent(self, DummyEvent(self.EVT_GO_ID))
	
	def ProcessGO(self,event):
		self.go_label.Enable()
		self.parentobj.GOGui.go_filename = self.tags['go']['go_filename']
		if self.parentobj.GOGui.OnGOLoad(None):
			self.go_pic.SetBitmap(wx.Bitmap(self.parentobj.Ok_pic))
		else:
			self.go_pic.SetBitmap(wx.Bitmap(self.parentobj.Warning_pic))
		wx.PostEvent(self, DummyEvent(self.EVT_AC_ID))

	def ProcessAC(self,event):
		self.ac_label.Enable()
		self.parentobj.ACGui.filetype = self.tags['ac']['ac_format']
		self.parentobj.ACGui.plainfileorder = int(self.tags['ac']['ac_format_params'])
		self.parentobj.ACGui.ac_filename = self.tags['ac']['ac_filename']
		if self.parentobj.ACGui.OnFakeCmd(None):
			self.ac_pic.SetBitmap(wx.Bitmap(self.parentobj.Ok_pic))
		else:
			self.ac_pic.SetBitmap(wx.Bitmap(self.parentobj.Warning_pic))
		wx.PostEvent(self, DummyEvent(self.EVT_SS_ID))

	def ProcessSS(self,event):
		self.ss_label.Enable()
		self.parentobj.selectedGO = self.tags['ss']['ss_go_tree']
		self.parentobj.mixingstrategy = self.tags['ss']['ss_mixing_strategy']
		self.parentobj.ssmeasure = self.tags['ss']['ss_measure']
		self.ss_pic.SetBitmap(wx.Bitmap(self.parentobj.Ok_pic))
		self.ss_pic.SetBitmap(wx.Bitmap(self.parentobj.Warning_pic))
		wx.PostEvent(self, DummyEvent(self.EVT_QUERY_ID))

	def ProcessQuery(self,event):
		self.query_label.Enable()
		self.parentobj.query_file = self.tags['query']['query_filename']
		self.parentobj.query_type = int(self.tags['query']['query_format'])
		self.parentobj.query_from = int(self.tags['query']['query_from'])
		self.query_pic.SetBitmap(wx.Bitmap(self.parentobj.Ok_pic))
		self.query_pic.SetBitmap(wx.Bitmap(self.parentobj.Warning_pic))
		wx.PostEvent(self, DummyEvent(self.EVT_OUTPUT_ID))

	def ProcessOutput(self,event):
		self.output_label.Enable()
		self.parentobj.output_type = int(self.tags['output']['output_to'])
		self.parentobj.output_filename = self.tags['output']['output_filename']
		self.output_pic.SetBitmap(wx.Bitmap(self.parentobj.Ok_pic))
		self.output_pic.SetBitmap(wx.Bitmap(self.parentobj.Warning_pic))
		wx.PostEvent(self, DummyEvent(self.EVT_DONE_ID))
	
	def ProcessDone(self,event):
		#self.Quit()
		pass

class SaveConfigGui(wx.Dialog):
	
	def __init__(self, parent):
		self.parentobj = parent
		super(SaveConfigGui, self).__init__(self.parentobj, title="Saving Configuration", size=(400,200))
		#self.InitUI()
		self.CollectData()
		self.SaveData()
	
	#def InitUI(self):
		#self.panel = wx.Panel(self, -1)
		#self.mainbox = wx.BoxSizer(wx.VERTICAL)
		#self.filebox = wx.BoxSizer(wx.HORIZONTAL)
		#self.file_label = wx.StaticText(self.panel, label='Configuration file: ')
		#self.filename_label = wx.StaticText(self.panel, label='')
		#self.filebox.Add(self.file_label)
		#self.filebox.Add(self.filename_label)
		#self.mainbox.Add(self.filebox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		
		#self.go_label = wx.StaticText(self.panel, label='Saving Gene Ontology...')
		#self.ac_label = wx.StaticText(self.panel, label='Saving Annotation Corpus...')
		#self.ss_label = wx.StaticText(self.panel, label='Saving Semantic Similarity parameters...')
		#self.query_label = wx.StaticText(self.panel, label='Saving Query...')
		#self.output_label = wx.StaticText(self.panel, label='Saving Output parameters...')
		#self.go_label.SetFont(self.parentobj.font)
		#self.ac_label.SetFont(self.parentobj.font)
		#self.ss_label.SetFont(self.parentobj.font)
		#self.query_label.SetFont(self.parentobj.font)
		#self.output_label.SetFont(self.parentobj.font)
		
		#self.go_label.Disable()
		#self.ac_label.Disable()
		#self.ss_label.Disable()
		#self.query_label.Disable()
		#self.output_label.Disable()
		
		#self.go_pic = wx.StaticBitmap(self.panel)
		#self.ac_pic = wx.StaticBitmap(self.panel)
		#self.query_pic = wx.StaticBitmap(self.panel)
		#self.ss_pic = wx.StaticBitmap(self.panel)
		#self.output_pic = wx.StaticBitmap(self.panel)
		
		#self.descbox = wx.FlexGridSizer(rows = 5, cols = 2, vgap = 6, hgap = 20)
		#self.descbox.AddMany([(self.go_label), (self.go_pic), (self.ac_label), (self.ac_pic), (self.ss_label), (self.ss_pic), (self.query_label), (self.query_pic), (self.output_label), (self.output_pic)])
		
		#self.mainbox.Add(self.descbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		##self.progress = wx.Gauge(self.panel, -1, 50, size=(250, 25))
		##self.mainbox.Add(self.progress, flag=wx.TOP, border = 5)
		#self.panel.SetSizerAndFit(self.mainbox)
		#self.Show()
	
	def CollectData(self):
		self.config = ConfigFileParser(self.parentobj.config_file)
		temp = self.config.tags
		temp['go']['go_filename'] = self.parentobj.GOGui.go_filename
		temp['ac']['ac_filename'] = self.parentobj.ACGui.ac_filename
		temp['ac']['ac_format'] = self.parentobj.ACGui.filetype
		temp['ac']['ac_format_params'] = self.parentobj.ACGui.plainfileorder
		temp['ss']['ss_go_tree'] = self.parentobj.selectedGO
		temp['ss']['ss_mixing_strategy'] = self.parentobj.mixingstrategy
		temp['ss']['ss_measure'] = self.parentobj.ssmeasure
		temp['query']['query_filename'] = self.parentobj.query_file
		temp['query']['query_format'] = self.parentobj.query_type
		temp['query']['query_from'] = self.parentobj.query_from
		temp['output']['output_to'] = self.parentobj.output_type
		temp['output']['output_filename'] = self.parentobj.output_file

	def SaveData(self):
		self.config.save()