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

class LoadGO(wx.Frame):
	
	def __init__(self, parent):
		self.parentobj = parent
		super(LoadGO, self).__init__(self.parentobj, title="Load Gene Ontology", size=(500,200))
		self.InitUI()
	
	def InitUI(self):
		self.Bind(wx.EVT_CLOSE, self.OnQuit, id=self.GetId())
        
		panel = wx.Panel(self)
		mainbox = wx.BoxSizer(wx.VERTICAL)
		descbox = wx.FlexGridSizer(rows = 4, cols = 2, vgap = 6, hgap = 20)
		commanbox = wx.BoxSizer(wx.HORIZONTAL)
		statusbox = wx.BoxSizer(wx.HORIZONTAL)
		panel.SetSizer(mainbox)
		mainbox.Add(statusbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		mainbox.Add(descbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		mainbox.Add(commanbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		# Descbox
		self.filename_label = wx.StaticText(panel, label='File:')
		self.filename_label.SetFont(self.parentobj.font)
		self.filename = wx.StaticText(panel, label='')
		self.gonodes_label = wx.StaticText(panel, label='Nodes:')
		self.gonodes_label.SetFont(self.parentobj.font)
		self.gonodes = wx.StaticText(panel, label='')
		self.gonodes.SetFont(self.parentobj.font)
		self.goedges_label = wx.StaticText(panel, label='Edges:')
		self.goedges_label.SetFont(self.parentobj.font)
		self.goedges = wx.StaticText(panel, label='')
		self.goedges.SetFont(self.parentobj.font)
		descbox.AddMany([(self.filename_label), (self.filename), (self.gonodes_label), (self.gonodes), (self.goedges_label), (self.goedges)])

		# commanbox
		self.gochooser = wx.Button(panel, wx.ID_ANY, 'Select file...')
		self.goload = wx.Button(panel, wx.ID_ANY, 'Load...')
		self.goload.Hide()
		self.Bind(wx.EVT_BUTTON, self.OnGOBrowse, id=self.gochooser.GetId())
		self.Bind(wx.EVT_BUTTON, self.OnGOLoad, id=self.goload.GetId())
		self.doneb = wx.Button(panel, wx.ID_ANY, 'Done')
		self.Bind(wx.EVT_BUTTON, self.OnGOBrowseDone, id=self.doneb.GetId())
		commanbox.Add(self.gochooser, flag=wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		commanbox.Add(self.doneb, flag=wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		
		#statusbox
		self.status_label = wx.StaticText(panel, label='No Ontology loaded.')
		self.status_label.SetFont(self.parentobj.font)
		#self.status_label.Hide()
		statusbox.Add(self.status_label, border=10)
		

	def OnGOBrowse(self, event):
		dialog = wx.FileDialog(None, style = wx.OPEN)
		if dialog.ShowModal() == wx.ID_OK:
			#print 'Selected: ', dialog.GetPath()
			self.filename.SetLabel(dialog.GetPath())
			self.status_label.SetLabel("Loading ontology... Please wait.")
			self.status_label.Show()
			self.gochooser.Disable()
			self.doneb.Disable()
			self.gonodes.SetLabel("")
			self.goedges.SetLabel("")
			self.parentobj.acchoosecmd.Disable()
			event = wx.PyCommandEvent(wx.EVT_BUTTON.typeId, self.goload.GetId())
			wx.PostEvent(self.GetEventHandler(), event)


	def OnGOLoad(self, event):
		self.parentobj.SetGoOk(False)
		self.parentobj.update_ac = True
		self.parentobj.update_ssobject = True
		self.tree = GeneOntology.load_GO_XML(open(self.filename.GetLabel(),'r'))
		if self.tree is not None:
			#print "Ontology infos: file name: " + str(self.filename.GetLabel()) + ". Nodes: " + str(self.tree.node_num()) + ". Edges: " + str(self.tree.edge_num())
			self.gochooser.Enable()
			self.doneb.Enable()
			self.gonodes.SetLabel(str(self.tree.node_num()))
			self.goedges.SetLabel(str(self.tree.edge_num()))
			self.status_label.SetLabel("Ontology loaded.")
			self.parentobj.acchoosecmd.Enable()
			self.parentobj.go = self.tree
			self.parentobj.SetGoOk(True)

	def OnGOBrowseDone(self, event):
		self.Hide()
		
	def OnQuit(self, event):
		self.Hide()