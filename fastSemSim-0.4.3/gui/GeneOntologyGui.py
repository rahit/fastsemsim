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
from GO import GeneOntology
from gui import WorkProcess

class GeneOntologyGui(wx.Frame):
	go_filename  = None
	
	def __init__(self, parent):
		self.parentobj = parent
		super(GeneOntologyGui, self).__init__(self.parentobj, title="Load Gene Ontology", size=(500,200))
		self.InitUI()
	
	def InitUI(self):
		self.Bind(wx.EVT_CLOSE, self.OnQuit, id=self.GetId())
        
		self.panel = wx.Panel(self)
		self.mainbox = wx.BoxSizer(wx.VERTICAL)
		self.descbox = wx.FlexGridSizer(rows = 4, cols = 2, vgap = 6, hgap = 20)
		self.commanbox = wx.BoxSizer(wx.HORIZONTAL)
		self.statusbox = wx.BoxSizer(wx.HORIZONTAL)
		self.mainbox.Add(self.statusbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		self.mainbox.Add(self.descbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		self.mainbox.Add(self.commanbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		# Descbox
		self.filename_label = wx.StaticText(self.panel, label='File:')
		self.filename_label.SetFont(self.parentobj.font)
		self.filename = wx.StaticText(self.panel, label='')
		self.gonodes_label = wx.StaticText(self.panel, label='Nodes:')
		self.gonodes_label.SetFont(self.parentobj.font)
		self.gonodes = wx.StaticText(self.panel, label='')
		self.gonodes.SetFont(self.parentobj.font)
		self.goedges_label = wx.StaticText(self.panel, label='Edges:')
		self.goedges_label.SetFont(self.parentobj.font)
		self.goedges = wx.StaticText(self.panel, label='')
		self.goedges.SetFont(self.parentobj.font)
		self.descbox.AddMany([(self.filename_label), (self.filename), (self.gonodes_label), (self.gonodes), (self.goedges_label), (self.goedges)])

		# commanbox
		self.gochooser = wx.Button(self.panel, wx.ID_ANY, 'Select file...')
		self.goload = wx.Button(self.panel, wx.ID_ANY, 'Load...')
		self.goload.Hide()
		self.Bind(wx.EVT_BUTTON, self.OnFileBrowse, id=self.gochooser.GetId())
		self.Bind(wx.EVT_BUTTON, self.OnGOLoad, id=self.goload.GetId())
		self.doneb = wx.Button(self.panel, wx.ID_ANY, 'Done')
		self.Bind(wx.EVT_BUTTON, self.OnGOBrowseDone, id=self.doneb.GetId())
		self.commanbox.Add(self.gochooser, flag=wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		self.commanbox.Add(self.doneb, flag=wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		
		#statusbox
		self.status_label = wx.StaticText(self.panel, label='No Ontology loaded.')
		self.status_label.SetFont(self.parentobj.font)
		#self.status_label.Hide()
		self.statusbox.Add(self.status_label, border=10)

		self.panel.SetSizerAndFit(self.mainbox)
		self.InitMainUI()
		return True


#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
	def InitMainUI(self):
		#### Populate GO section in main window
		#self.parentobj.go_status_pic = wx.StaticBitmap(self.parentobj.panel)
		self.parentobj.SetGoOk(False)
		self.parentobj.go_cmd = wx.Button(self.parentobj.panel, wx.ID_ANY, 'Load Gene Ontology...')
		self.parentobj.go_box.Add(self.parentobj.go_cmd,flag=wx.ALL|wx.CENTER, border = 8)
		#self.parentobj.go_box.Add(self.parentobj.go_status_pic,flag=wx.ALL|wx.CENTER, border = 8)
		self.parentobj.Bind(wx.EVT_BUTTON, self.OnGOBrowse, id=self.parentobj.go_cmd.GetId())

###############################################################################################################
###############################################################################################################

	def OnFileBrowse(self, event):
		dialog = wx.FileDialog(None, style = wx.OPEN)
		if dialog.ShowModal() == wx.ID_OK:
			#print 'Selected: ', dialog.GetPath()
			self.filename.SetLabel(dialog.GetPath())
			self.go_filename = dialog.GetPath()
			self.status_label.SetLabel("Loading ontology... Please wait.")
			self.status_label.Show()
			self.gochooser.Disable()
			self.doneb.Disable()
			self.gonodes.SetLabel("")
			self.goedges.SetLabel("")
			#self.parentobj.acchoosecmd.Disable()
			event = wx.PyCommandEvent(wx.EVT_BUTTON.typeId, self.goload.GetId())
			wx.PostEvent(self.GetEventHandler(), event)


	def OnGOLoad(self, event):
		self.parentobj.go_running = True
		self.parentobj.SetGoOk(False)
		#self.parentobj.update_ac = True
		#self.parentobj.update_ssobject = True
		#self.OnGOLoad()
		self.status_label.SetLabel("Loading ontology from file " + str(self.go_filename))
		self.gochooser.Disable()
		self.doneb.Disable()
		self.parentobj.ac_cmd.Disable()
		self.parentobj.lock()
		self.parentobj.gui2ssprocess_queue.put((WorkProcess.CMD_LOAD_GO, self.go_filename))
		self.TIMER_ID = 1000
		self.timer = wx.Timer(self.parentobj.panel, self.TIMER_ID)
		wx.EVT_TIMER(self.parentobj.panel, self.TIMER_ID, self.GO_timer)
		self.timer.Start(self.parentobj.UPDATE_INTERVAL)
		return False

	def GO_timer(self, event):
		try:
			data = self.parentobj.ssprocess2gui_queue.get(False)
			self.timer.Stop()
			self.parentobj.unlock()
			#self.parentobj.process_busy_lock.release()
			if data[0] == WorkProcess.CMD_LOAD_GO:
				if data[1]:
					self.gochooser.Enable()
					self.doneb.Enable()
					self.gonodes.SetLabel(str(data[2]))
					self.goedges.SetLabel(str(data[3]))
					self.status_label.SetLabel("Ontology loaded from file " + str(self.go_filename))
					self.parentobj.ac_cmd.Enable()
					#self.parentobj.go = self.tree
					self.parentobj.SetGoOk(True)
					self.parentobj.go_running = False
					return True
		except Exception:
			#self.parentobj.unlock() #### add a clean
			#self.parentobj.process_busy_lock.release()
			#self.parentobj.go_running = False
			return False
		
	def OnGOBrowseDone(self, event):
		self.Hide()
		
	def OnQuit(self, event):
		self.Hide()
		
	def OnGOBrowse(self, event):
			self.parentobj.GOGui.Show()