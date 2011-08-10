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
from GO import AnnotationCorpus

class loadAC(wx.Frame):
	
	def __init__(self, parent):
		self.parentobj = parent
		super(loadAC, self).__init__(self.parentobj, title="Load Annotation Corpus", size=(500,200))
		self.InitUI()
	
	def InitUI(self):
		self.Bind(wx.EVT_CLOSE, self.OnQuit, id=self.GetId())
		font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(9)
        
		panel = wx.Panel(self)
		#panel.SetBackgroundColour('#4f5049')
		mainbox = wx.BoxSizer(wx.VERTICAL)
		descbox = wx.FlexGridSizer(rows = 4, cols = 2, vgap = 6, hgap = 20)
		commanbox = wx.BoxSizer(wx.HORIZONTAL)
		statusbox = wx.BoxSizer(wx.HORIZONTAL)
		panel.SetSizerAndFit(mainbox)
		mainbox.Add(statusbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		mainbox.Add(descbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		mainbox.Add(commanbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		
		# Descbox
		self.filename_label = wx.StaticText(panel, label='AC File')
		self.filename_label.SetFont(font)
		self.filename = wx.StaticText(panel, label='')
		self.acobjs_label = wx.StaticText(panel, label='Objects')
		self.acobjs_label.SetFont(font)
		self.acobjs = wx.StaticText(panel, label='')
		self.acobjs.SetFont(font)
		self.acterms_label = wx.StaticText(panel, label='Go Terms involved')
		self.acterms_label.SetFont(font)
		self.acterms = wx.StaticText(panel, label='')
		self.acterms.SetFont(font)
		descbox.AddMany([(self.filename_label), (self.filename), (self.acobjs_label), (self.acobjs), (self.acterms_label), (self.acterms)])

		# commanbox
		self.acchooser = wx.Button(panel, wx.ID_ANY, 'Select file...')
		self.acload = wx.Button(panel, wx.ID_ANY, 'Load...')
		self.acload.Hide()
		self.Bind(wx.EVT_BUTTON, self.OnACBrowse, id=self.acchooser.GetId())
		self.Bind(wx.EVT_BUTTON, self.OnACLoad, id=self.acload.GetId())
		self.doneb = wx.Button(panel, wx.ID_ANY, 'Done')
		self.Bind(wx.EVT_BUTTON, self.OnACBrowseDone, id=self.doneb.GetId())
		commanbox.Add(self.acchooser, flag=wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		commanbox.Add(self.doneb, flag=wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		
		#statusbox
		self.status_label = wx.StaticText(panel, label='No Annotation Corpus loaded.')
		self.status_label.SetFont(font)
		#self.status_label.Hide()
		statusbox.Add(self.status_label, border=10)
		

	def OnACBrowse(self, event):
		dialog = wx.FileDialog(None, style = wx.OPEN)
		if dialog.ShowModal() == wx.ID_OK:
			#print 'Selected: ', dialog.GetPath()
			self.filename.SetLabel(dialog.GetPath())
			self.status_label.SetLabel("Loading annotation corpus... Please wait.")
			self.status_label.Show()
			self.acchooser.Disable()
			self.doneb.Disable()
			self.acobjs.SetLabel("")
			self.acterms.SetLabel("")
			#self.parentobj.acchooser.Disable()
			event = wx.PyCommandEvent(wx.EVT_BUTTON.typeId, self.acload.GetId())
			wx.PostEvent(self.GetEventHandler(), event)


	def OnACLoad(self, event):
		self.ac = AnnotationCorpus.AnnotationCorpus(self.parentobj.go) 
		self.ftype = "GOA"
		self.ac.parse(str(self.filename.GetLabel()), self.ftype)
		self.ac.sanitize()
		if True: # replace with control code
			#print "Ontology infos: file name: " + str(self.filename.GetLabel()) + ". Nodes: " + str(tree.node_num()) + ". Edges: " + str(tree.edge_num())
			self.acchooser.Enable()
			self.doneb.Enable()
			self.acobjs.SetLabel(str(len(self.ac.annotations)))
			self.acterms.SetLabel(str(len(self.ac.reverse_annotations)))
			self.parentobj.ac = self.ac
			self.parentobj.aclabel.SetLabel(self.filename.GetLabel())
			self.status_label.SetLabel("Annotation Corpus loaded.")
			#self.parentobj.acchooser.Enable()
				
	def OnACBrowseDone(self, event):
		self.Hide()
		
	def OnQuit(self, event):
		self.Hide()

class loadGO(wx.Frame):
	
	def __init__(self, parent):
		self.parentobj = parent
		super(loadGO, self).__init__(self.parentobj, title="Load Gene Ontology", size=(500,200))
		self.InitUI()
	
	def InitUI(self):
		self.Bind(wx.EVT_CLOSE, self.OnQuit, id=self.GetId())
		font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(9)
        
		panel = wx.Panel(self)
		#panel.SetBackgroundColour('#4f5049')
		mainbox = wx.BoxSizer(wx.VERTICAL)
		descbox = wx.FlexGridSizer(rows = 4, cols = 2, vgap = 6, hgap = 20)
		commanbox = wx.BoxSizer(wx.HORIZONTAL)
		statusbox = wx.BoxSizer(wx.HORIZONTAL)
		panel.SetSizer(mainbox)
		mainbox.Add(statusbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		mainbox.Add(descbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		mainbox.Add(commanbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		
		# Descbox
		self.filename_label = wx.StaticText(panel, label='GO File')
		self.filename_label.SetFont(font)
		self.filename = wx.StaticText(panel, label='')
		self.gonodes_label = wx.StaticText(panel, label='Nodes')
		self.gonodes_label.SetFont(font)
		self.gonodes = wx.StaticText(panel, label='')
		self.gonodes.SetFont(font)
		self.goedges_label = wx.StaticText(panel, label='Edges')
		self.goedges_label.SetFont(font)
		self.goedges = wx.StaticText(panel, label='')
		self.goedges.SetFont(font)
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
		self.status_label.SetFont(font)
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
			self.parentobj.acchooser.Disable()
			event = wx.PyCommandEvent(wx.EVT_BUTTON.typeId, self.goload.GetId())
			wx.PostEvent(self.GetEventHandler(), event)


	def OnGOLoad(self, event):
		self.tree = GeneOntology.load_GO_XML(open(self.filename.GetLabel(),'r'))
		if self.tree is not None:
			#print "Ontology infos: file name: " + str(self.filename.GetLabel()) + ". Nodes: " + str(self.tree.node_num()) + ". Edges: " + str(self.tree.edge_num())
			self.gochooser.Enable()
			self.doneb.Enable()
			self.gonodes.SetLabel(str(self.tree.node_num()))
			self.goedges.SetLabel(str(self.tree.edge_num()))
			self.parentobj.go = self.tree
			self.parentobj.golabel.SetLabel(self.filename.GetLabel())
			self.status_label.SetLabel("Ontology loaded.")
			self.parentobj.acchooser.Enable()

	def OnGOBrowseDone(self, event):
		self.Hide()
		
	def OnQuit(self, event):
		self.Hide()
	
	
class gui(wx.Frame):
	loadGOgui = None
	loadACgui = None

	def __init__(self, parent):
		super(gui, self).__init__(parent, title="fastSemSim GUI (src version)", size=(800,500))
		self.InitUI()   

	def InitUI(self):
		self.font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		self.font.SetPointSize(9)
        
		self.panel = wx.Panel(self)
		self.mainbox = wx.BoxSizer(wx.VERTICAL)
		self.goacbox = wx.BoxSizer(wx.VERTICAL)

		# GO File Chooser
		self.goboxline = wx.StaticBox(self, wx.ID_ANY, 'Gene Ontology')
		self.gobox = wx.StaticBoxSizer(self.goboxline, wx.HORIZONTAL)
		self.golabel = wx.StaticText(self.panel, label='Gene Ontology not loaded')
		self.golabel.SetFont(self.font)
		self.gochooser = wx.Button(self.panel, wx.ID_ANY, 'Manage GO...')
		
		self.gobox.Add(self.golabel,flag=wx.CENTER, border = 8)
		self.gobox.Add(self.gochooser,flag=wx.CENTER, border = 8)

		## Annotation Corpus File Chooser
		self.acboxline = wx.StaticBox(self, wx.ID_ANY, 'Annotation Corpus')
		self.acbox = wx.StaticBoxSizer(self.acboxline, wx.HORIZONTAL)
		self.aclabel = wx.StaticText(self.panel, label = 'Annotation Corpus not loaded')
		self.aclabel.SetFont(self.font)
		self.acchooser = wx.Button(self.panel, wx.ID_ANY, 'Manage Annotation Corpus...')
		self.acchooser.Disable()
		self.acbox.Add(self.aclabel, flag=wx.ALL|wx.CENTER, border = 8)
		self.acbox.Add(self.acchooser, flag=wx.ALL|wx.CENTER, border = 8)
		

		self.goacbox.Add ( ( 0, 0 ), 1, wx.EXPAND )
		self.goacbox.Add(self.gobox, flag=wx.EXPAND, border=5)
		self.goacbox.Add ( ( 0, 0 ), 1, wx.EXPAND )
		self.goacbox.Add(self.acbox, flag=wx.EXPAND, border=5)
		self.goacbox.Add ( ( 0, 0 ), 1, wx.EXPAND )
		self.mainbox.Add(self.goacbox, 0, flag=wx.ALIGN_CENTER)
		self.panel.SetSizerAndFit(self.mainbox)
		
		self.Bind(wx.EVT_BUTTON, self.OnGOBrowse, id=self.gochooser.GetId())
		self.Bind(wx.EVT_BUTTON, self.OnACBrowse, id=self.acchooser.GetId())
		# Load Files
		#hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		##self.aclabel = wx.StaticText(panel, label = 'Annotation Corpus File')
		##self.aclabel.SetFont(font)
		##self.acpath = wx.TextCtrl(panel)
		#self.filesloader = wx.Button(panel, wx.ID_ANY, 'Load files')
		#self.filesloader.Disable()
		##hbox2.Add(self.aclabel, flag=wx.LEFT, border = 8)
		##hbox2.Add(self.acpath, proportion = 1,  border = 8)
		#hbox3.Add(self.filesloader, flag = wx.RIGHT, border = 8)
		#self.Bind(wx.EVT_BUTTON, self.OnLoad, id=self.filesloader.GetId())
		#vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

	def OnLoad(self, event):
		#dialog = wx.FileDialog(None, style = wx.OPEN)
		#if dialog.ShowModal() == wx.ID_OK:
		print 'Load!'
			#self.gopath.SetValue(dialog.GetPath())

	def enablebutton(self):
		print self.gopath.GetValue()
		print self.acpath.GetValue()
		if (not self.gopath.GetValue() == "") and (not self.acpath.GetValue() == ""):
			self.filesloader.Enable()
	
	def OnGOBrowse(self, event):
		if self.loadGOgui is None:
			self.loadGOgui = loadGO(self)
		self.loadGOgui.Show()  
		
	def OnACBrowse(self, event):
		if self.loadACgui is None:
			self.loadACgui = loadAC(self)
		self.loadACgui.Show()  

	#def OnACBrowse(self, event):
		#dialog = wx.FileDialog(None, style = wx.OPEN)
		#if dialog.ShowModal() == wx.ID_OK:
			##print 'Selected: ', dialog.GetPath()
			#self.acpath.SetValue(dialog.GetPath())
			#self.enablebutton()

	def OnQuit(event):
		#print event
		frame.Close()

if __name__ == "__main__":
	app = wx.App()
	window = gui(None)
	window.Centre()
	window.Show()  
	app.MainLoop()
