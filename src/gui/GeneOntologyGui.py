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
import WorkProcess
import os

#class AnnotationCorpusGui(wx.Dialog):
	#filetype = None
	#filename = None
		
class GeneOntologyGui(wx.Dialog):
	filename  = None
	
	def __init__(self, parent):
		self.parent = parent
		super(GeneOntologyGui, self).__init__(self.parent, title="Load Gene Ontology",style=wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER)
		self.InitUI()
	
	def InitUI(self):
		self.Bind(wx.EVT_CLOSE, self.OnQuit, id=self.GetId())

		self.panel = wx.Panel(self)
		self.mainbox = wx.BoxSizer(wx.HORIZONTAL)
		self.panel.SetSizer(self.mainbox)

# COMMAND BOX
		self.commandbox = wx.BoxSizer(wx.VERTICAL)
		self.button_selectfile = wx.Button(self.panel, wx.ID_ANY, 'Select file...')
		self.button_reset = wx.Button(self.panel, wx.ID_ANY, 'Reset')
		self.button_done = wx.Button(self.panel, wx.ID_ANY, 'Close')
		self.Bind(wx.EVT_BUTTON, self.OnQuit, id=self.button_done.GetId())
		self.Bind(wx.EVT_BUTTON, self.OnFileBrowse, id=self.button_selectfile.GetId())
		self.Bind(wx.EVT_BUTTON, self.OnReset, id=self.button_reset.GetId())

		#self.commandboxs = wx.StdDialogButtonSizer(wx.VERTICAL)
		#self.commandboxs.Add(self.button_selectfile)
		#self.commandboxs.Add(self.button_reset)
		#self.commandboxs.Add(self.button_done)
		#self.commandboxs.Realize()
		#self.commandbox.Add(self.commandboxs)
   
		self.commandbox.Add(self.button_selectfile, flag=wx.LEFT | wx.RIGHT, border=10)
		self.commandbox.Add(self.button_reset, flag=wx.LEFT|wx.RIGHT, border=10)
		self.commandbox.Add(self.button_done, flag=wx.LEFT|wx.RIGHT, border=10)

# STATISTICS
		self.gostatsboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Statistics')
		self.gostatsbox = wx.StaticBoxSizer(self.gostatsboxline, wx.HORIZONTAL)
		self.label_statuslabel = wx.StaticText(self.panel, label = "File loaded:")
		self.label_status = wx.StaticText(self.panel, label = "")
		self.label_termslabel = wx.StaticText(self.panel, label = "GO Terms:")
		self.label_terms = wx.StaticText(self.panel, label = "")
		self.statusgridbox= wx.FlexGridSizer(rows = 4, cols = 3, vgap = 10, hgap = 10)
		self.statusgridbox.AddMany([wx.Size(5,2), wx.Size(5,2), wx.Size(15,2), self.label_statuslabel, self.label_status,wx.Size(5,2), self.label_termslabel, self.label_terms, wx.Size(5,2),wx.Size(5,2),wx.Size(5,2)])
		self.gostatsbox.Add(self.statusgridbox)

		self.mainbox.Add(self.gostatsbox, flag=wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		self.mainbox.Add(self.commandbox, flag=wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		
		#w,h =  self.text8.GetTextExtent(self.text8.GetValue())
		#self.text8.SetSize(wx.Size(w+10, -1)) 
		#w,h = self.text8.GetSizeTuple()
		#self.mainbox.SetItemMinSize(self.text8, w,h)
		#self.mainbox.Layout()

		self.InitMainUI()
		self.OnReset(None)
		return True

#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
	def OnAnyUpdate(self):
		self.statusgridbox.Fit(self)
		self.gostatsbox.Fit(self)
		self.commandbox.Fit(self)
		self.mainbox.Fit(self)
		w,h = self.commandbox.GetSizeTuple()
		self.mainbox.SetItemMinSize(self.commandbox, w,h)
		#self.GetBestSize()
		self.mainbox.Layout()
		
	def InitMainUI(self):
		#### Populate GO section in main window
		#self.parent.go_status_pic = wx.StaticBitmap(self.parent.panel)
		self.parent.SetGoOk(False)
		self.parent.go_cmd = wx.Button(self.parent.panel, wx.ID_ANY, 'Load Gene Ontology...')
		self.parent.go_box.Add(self.parent.go_cmd,flag=wx.ALL|wx.CENTER, border = 8)
		#self.parent.go_box.Add(self.parent.go_status_pic,flag=wx.ALL|wx.CENTER, border = 8)
		self.parent.Bind(wx.EVT_BUTTON, self.OnGOBrowse, id=self.parent.go_cmd.GetId())

###############################################################################################################
###############################################################################################################

	def OnQuit(self, event):
		self.Hide()
		
	def OnGOBrowse(self, event):
			self.parent.GOGui.ShowModal()

	def OnFileBrowse(self, event):
		dialog = wx.FileDialog(None, style = wx.OPEN)
		if dialog.ShowModal() == wx.ID_OK:
			self.filename = dialog.GetPath()
			self.OnLoad()

	def OnLoad(self):
			self.loadGOGui = LoadGOGui(self)
			self.loadGOGui.ShowModal()
			self.OnLoadDone()

	def OnLoadDone(self):
		if self.go_status:
			self.label_status.SetLabel(os.path.basename(self.filename))
			self.label_terms.SetLabel(str(self.go_terms))
			self.parent.SetGoOk(True)
			self.parent.update_ac = True
		else:
			self.label_status.SetLabel(' - ')
			self.label_terms.SetLabel('')
			self.parent.SetGoOk(False)
		self.OnAnyUpdate()

	def OnReset(self, event):
		self.filename = None
		self.go_status = False
		self.label_status.SetLabel(' - ')
		self.label_terms.SetLabel('')
		print "Fix Me. Should Reset go in main process!!"
		self.OnAnyUpdate()
		self.OnLoadDone()


	def batch_save(self):
		save = {}
		save['go_filename'] = self.filename
		return save

	def batch_load(self, save):
		if 'go_filename' in save:
			self.filename = save['go_filename']
		self.OnLoad()

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

class LoadGOGui(wx.Dialog):

	def __init__(self, parent):
		self.parent = parent
		super(LoadGOGui, self).__init__(self.parent, title="Loading Gene Ontology",style=wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER)
		self.InitUI()

	def InitUI(self):
		self.panel = wx.Panel(self)
		self.mainbox = wx.BoxSizer(wx.VERTICAL)
		self.loadbarboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Progress Bar')
		self.loadbarbox = wx.StaticBoxSizer(self.loadbarboxline, wx.HORIZONTAL)
		self.gauge_loadprogress = wx.Gauge(self.panel, -1, 50, size=(250, 25))
		self.loadbarbox.Add(self.gauge_loadprogress, flag=wx.EXPAND | wx.ALIGN_CENTER | wx.TOP, border = 5)
		
		self.statsbox = wx.BoxSizer(wx.HORIZONTAL)
		self.label_status = wx.StaticText(self.panel, wx.ID_ANY, 'Loading Gene Ontology. Please wait...')
		self.statsbox.Add(self.label_status, flag = wx.ALIGN_CENTER)
		
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
		self.OnAnyUpdate()

	def OnAnyUpdate(self):
		#self.load.Fit(self)
		#self.gostatsbox.Fit(self)
		#self.commandbox.Fit(self)
		self.mainbox.Fit(self)
		#w,h = self.commandbox.GetSizeTuple()
		#self.mainbox.SetItemMinSize(self.commandbox, w,h)
		#self.GetBestSize()
		self.mainbox.Layout()
		
	def OnOk(self, event):
		self.Close()
	
	def OnAbort(self, event):
		print "OnAbort. Fix Me."
		#self.Close()

	def OnStart(self):
		self.parent.parent.lock()
		self.parent.parent.gui2ssprocess_queue.put((WorkProcess.CMD_LOAD_GO, self.parent.filename))
		self.TIMER_ID = 1000
		self.timer = wx.Timer(self.panel, self.TIMER_ID)
		wx.EVT_TIMER(self.panel, self.TIMER_ID, self.GO_timer)
		self.timer.Start(1000)
		return False

	def GO_timer(self, event):
		if not self.parent.parent.ssprocess2gui_queue.empty():
			data = self.parent.parent.ssprocess2gui_queue.get(False)
			if data[0] == WorkProcess.CMD_LOAD_GO:
				if data[1] == WorkProcess.LOAD_GO_END:
					self.parent.parent.unlock()
					self.timer.Stop()
					self.button_ok.Enable()
					self.button_abort.Disable()
					if data[2]:
						self.label_status.SetLabel("Task correctly completed.")
						self.parent.go_status = True
						self.parent.go_terms = data[3]
						self.gauge_loadprogress.SetValue(self.gauge_loadprogress.GetRange())
					else:
						self.label_status.SetLabel("Error. Please check parse parameters.")
						self.parent.go_status = False
						self.parent.go_terms = None
						self.gauge_loadprogress.SetValue(0)
				elif data[1] == WorkProcess.LOAD_GO_STATUS:
					print "Status"
					gaugerange = self.gauge_loadprogress.GetRange()
					self.gauge_loadprogress.SetValue((float(data[2]))*gaugerange)
		self.OnAnyUpdate()
