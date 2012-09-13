import wx

class OutputCtrlPanel(wx.Panel):
	def __init__( self, real_parent, parent, id, pos, size, style):
		wx.Panel.__init__ ( self, parent, id, pos, size, style)
		self.output_ctrl_panel = self # temporary workaround

		
		bSizer93 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer511 = wx.StaticBoxSizer( wx.StaticBox( self.output_ctrl_panel, wx.ID_ANY, u"Output parameters" ), wx.VERTICAL )
		
		sbSizer291 = wx.StaticBoxSizer( wx.StaticBox( self.output_ctrl_panel, wx.ID_ANY, u"Filter Options" ), wx.VERTICAL )
		
		gbSizer9 = wx.GridBagSizer( 0, 0 )
		gbSizer9.SetFlexibleDirection( wx.BOTH )
		gbSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1081 = wx.StaticText( self.output_ctrl_panel, wx.ID_ANY, u"Remove pairs with Semantic Similarity", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText1081.Wrap( -1 )
		gbSizer9.Add( self.m_staticText1081, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer111 = wx.BoxSizer( wx.VERTICAL )
		
		self.output_filter_none_check = wx.CheckBox( self.output_ctrl_panel, wx.ID_ANY, u"= 'None'", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer111.Add( self.output_filter_none_check, 0, 0, 5 )
		
		self.output_filter_0_check = wx.CheckBox( self.output_ctrl_panel, wx.ID_ANY, u"= 0.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer111.Add( self.output_filter_0_check, 0, 0, 5 )
		
		bSizer112 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.query_filter_less_check = wx.CheckBox( self.output_ctrl_panel, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer112.Add( self.query_filter_less_check, 0, 0, 5 )
		
		self.query_filter_less_text = wx.TextCtrl( self.output_ctrl_panel, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.query_filter_less_text.SetMaxSize( wx.Size( 70,-1 ) )
		
		bSizer112.Add( self.query_filter_less_text, 0, 0, 5 )
		
		bSizer111.Add( bSizer112, 1, wx.EXPAND, 5 )
		
		gbSizer9.Add( bSizer111, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		sbSizer291.Add( gbSizer9, 1, wx.EXPAND, 5 )
		
		sbSizer511.Add( sbSizer291, 0, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer52 = wx.StaticBoxSizer( wx.StaticBox( self.output_ctrl_panel, wx.ID_ANY, u"Redirect output to" ), wx.VERTICAL )
		
		self.output_to_box = wx.Choicebook( self.output_ctrl_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CHB_DEFAULT )
		self.m_panel29 = wx.Panel( self.output_to_box, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer95 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel29.SetSizer( bSizer95 )
		self.m_panel29.Layout()
		bSizer95.Fit( self.m_panel29 )
		self.output_to_box.AddPage( self.m_panel29, u"Output Form", False )
		self.m_panel30 = wx.Panel( self.output_to_box, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer94 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer321 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer221 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer341 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel30, wx.ID_ANY, u"Destination file" ), wx.HORIZONTAL )
		
		self.output_file_label = wx.StaticText( self.m_panel30, wx.ID_ANY, u"No file selected.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.output_file_label.Wrap( -1 )
		sbSizer341.Add( self.output_file_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer221.Add( sbSizer341, 1, wx.LEFT|wx.RIGHT, 5 )
		
		bSizer201 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.output_file_select_button = wx.Button( self.m_panel30, wx.ID_ANY, u"Select file...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer201.Add( self.output_file_select_button, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		bSizer221.Add( bSizer201, 0, wx.ALIGN_RIGHT|wx.RIGHT|wx.TOP, 5 )
		
		bSizer321.Add( bSizer221, 0, wx.ALIGN_CENTER|wx.EXPAND|wx.TOP, 5 )
		
		bSizer551 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer561 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer551.Add( bSizer561, 1, wx.EXPAND, 5 )
		
		bSizer321.Add( bSizer551, 0, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer2911 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel30, wx.ID_ANY, u"Options" ), wx.VERTICAL )
		
		gbSizer91 = wx.GridBagSizer( 0, 0 )
		gbSizer91.SetFlexibleDirection( wx.BOTH )
		gbSizer91.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText3011 = wx.StaticText( self.m_panel30, wx.ID_ANY, u"Separator", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3011.Wrap( -1 )
		gbSizer91.Add( self.m_staticText3011, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		bSizer4611 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.output_sep_tab_radio = wx.RadioButton( self.m_panel30, wx.ID_ANY, u"[tab]  '\\t'", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4611.Add( self.output_sep_tab_radio, 0, wx.ALL, 5 )
		
		self.output_sep_space_radio = wx.RadioButton( self.m_panel30, wx.ID_ANY, u"[space]", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4611.Add( self.output_sep_space_radio, 0, wx.ALL, 5 )
		
		bSizer4711 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.output_sep_custom_radio = wx.RadioButton( self.m_panel30, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4711.Add( self.output_sep_custom_radio, 0, wx.ALL|wx.LEFT|wx.RIGHT, 5 )
		
		self.output_sep_custom_text = wx.TextCtrl( self.m_panel30, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 35,-1 ), 0 )
		bSizer4711.Add( self.output_sep_custom_text, 0, wx.ALL|wx.RIGHT, 5 )
		
		bSizer4611.Add( bSizer4711, 1, wx.EXPAND, 5 )
		
		gbSizer91.Add( bSizer4611, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		sbSizer2911.Add( gbSizer91, 1, wx.EXPAND, 5 )
		
		bSizer321.Add( sbSizer2911, 1, wx.EXPAND, 5 )
		
		bSizer94.Add( bSizer321, 1, wx.EXPAND, 5 )
		
		self.m_panel30.SetSizer( bSizer94 )
		self.m_panel30.Layout()
		bSizer94.Fit( self.m_panel30 )
		self.output_to_box.AddPage( self.m_panel30, u"File", True )
		sbSizer52.Add( self.output_to_box, 0, wx.EXPAND |wx.ALL, 5 )
		
		sbSizer511.Add( sbSizer52, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer93.Add( sbSizer511, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.output_ctrl_panel.SetSizer( bSizer93 )
		self.output_ctrl_panel.Layout()
		bSizer93.Fit( self.output_ctrl_panel )
#


class OutputPanel(wx.Panel):
	def __init__( self, real_parent, parent, id, pos, size, style):
		wx.Panel.__init__ ( self, parent, id, pos, size, style)
#
