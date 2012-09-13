import wx

class SSPanel(wx.Panel):
	def __init__( self, real_parent, parent, id, pos, size, style):
		wx.Panel.__init__ ( self, parent, id, pos, size, style)
		self.SS_panel = self # temporary workaround

		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer26 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer15 = wx.StaticBoxSizer( wx.StaticBox( self.SS_panel, wx.ID_ANY, u"Semantic Measure" ), wx.HORIZONTAL )
		
		SS_measure_boxChoices = []
		self.SS_measure_box = wx.ComboBox( self.SS_panel, wx.ID_ANY, u"Resnik", wx.DefaultPosition, wx.DefaultSize, SS_measure_boxChoices, 0 )
		sbSizer15.Add( self.SS_measure_box, 0, wx.ALL, 5 )
		
		self.SS_measure_settings_button = wx.BitmapButton( self.SS_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		sbSizer15.Add( self.SS_measure_settings_button, 0, wx.ALL, 5 )
		
		bSizer26.Add( sbSizer15, 1, wx.EXPAND|wx.RIGHT, 5 )
		
		sbSizer16 = wx.StaticBoxSizer( wx.StaticBox( self.SS_panel, wx.ID_ANY, u"Mixing Strategy" ), wx.HORIZONTAL )
		
		SS_mix_boxChoices = []
		self.SS_mix_box = wx.ComboBox( self.SS_panel, wx.ID_ANY, u"BMA", wx.DefaultPosition, wx.DefaultSize, SS_mix_boxChoices, 0 )
		sbSizer16.Add( self.SS_mix_box, 0, wx.ALL, 5 )
		
		self.SS_mix_settings_button = wx.BitmapButton( self.SS_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		sbSizer16.Add( self.SS_mix_settings_button, 0, wx.ALL, 5 )
		
		bSizer26.Add( sbSizer16, 1, wx.EXPAND|wx.RIGHT|wx.TOP, 5 )
		
		bSizer27.Add( bSizer26, 0, 0, 5 )
		
		sbSizer17 = wx.StaticBoxSizer( wx.StaticBox( self.SS_panel, wx.ID_ANY, u"Ontology" ), wx.VERTICAL )
		
		self.SS_GO_MF_radio = wx.RadioButton( self.SS_panel, wx.ID_ANY, u"Molecular Function (MF)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer17.Add( self.SS_GO_MF_radio, 0, wx.ALL, 5 )
		
		self.SS_GO_CC_radio = wx.RadioButton( self.SS_panel, wx.ID_ANY, u"Cellular Component (CC)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer17.Add( self.SS_GO_CC_radio, 0, wx.ALL, 5 )
		
		self.SS_GO_BP_radio = wx.RadioButton( self.SS_panel, wx.ID_ANY, u"Biological Process (BP)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer17.Add( self.SS_GO_BP_radio, 0, wx.ALL, 5 )
		
		bSizer27.Add( sbSizer17, 0, wx.LEFT, 5 )
		
		bSizer25.Add( bSizer27, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.SS_panel.SetSizer( bSizer25 )
		self.SS_panel.Layout()
		bSizer25.Fit( self.SS_panel )

#