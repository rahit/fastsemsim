import wx

class QueryPanel(wx.Panel):
	def __init__( self, real_parent, parent, id, pos, size, style):
		wx.Panel.__init__ ( self, parent, id, pos, size, style)
		self.query_panel = self # temporary workaround

		bSizer50 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer36 = wx.StaticBoxSizer( wx.StaticBox( self.query_panel, wx.ID_ANY, u"Input method" ), wx.VERTICAL )
		
		self.query_input_method_box = wx.Choicebook( self.query_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CHB_DEFAULT )
		self.m_panel22 = wx.Panel( self.query_input_method_box, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer512 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer312 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel22, wx.ID_ANY, u"Input field" ), wx.VERTICAL )
		
		self.query_field_text = wx.TextCtrl( self.m_panel22, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,250 ), wx.TE_MULTILINE )
		self.query_field_text.SetMinSize( wx.Size( 250,250 ) )
		
		sbSizer312.Add( self.query_field_text, 0, wx.ALL, 5 )
		
		bSizer512.Add( sbSizer312, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer54 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer32 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel22, wx.ID_ANY, u"Input format" ), wx.VERTICAL )
		
		query_field_type_boxChoices = []
		self.query_field_type_box = wx.ComboBox( self.m_panel22, wx.ID_ANY, u"List", wx.DefaultPosition, wx.Size( 120,-1 ), query_field_type_boxChoices, wx.CB_READONLY )
		sbSizer32.Add( self.query_field_type_box, 0, wx.ALL, 5 )
		
		bSizer54.Add( sbSizer32, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		sbSizer33 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel22, wx.ID_ANY, u"Help" ), wx.VERTICAL )
		
		self.m_staticText53 = wx.StaticText( self.m_panel22, wx.ID_ANY, u"You can either specify a list of object or a set of pairs of objects. In the former case, the semantic similarity will be evaluated between each pair of objects in the list. In the latter, each pair will be considered", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText53.Wrap( -1 )
		sbSizer33.Add( self.m_staticText53, 0, wx.ALL, 5 )
		
		bSizer54.Add( sbSizer33, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		self.query_reset_button = wx.Button( self.m_panel22, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer54.Add( self.query_reset_button, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		bSizer512.Add( bSizer54, 1, wx.EXPAND, 5 )
		
		self.m_panel22.SetSizer( bSizer512 )
		self.m_panel22.Layout()
		bSizer512.Fit( self.m_panel22 )
		self.query_input_method_box.AddPage( self.m_panel22, u"Manual input", False )
		self.m_panel23 = wx.Panel( self.query_input_method_box, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer521 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer32 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer34 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel23, wx.ID_ANY, u"Source file" ), wx.HORIZONTAL )
		
		self.query_input_file_label = wx.StaticText( self.m_panel23, wx.ID_ANY, u"No file selected.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.query_input_file_label.Wrap( -1 )
		sbSizer34.Add( self.query_input_file_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer22.Add( sbSizer34, 1, wx.LEFT|wx.RIGHT, 5 )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.query_load_button = wx.Button( self.m_panel23, wx.ID_ANY, u"Select file...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.query_load_button, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		bSizer22.Add( bSizer20, 0, wx.ALIGN_RIGHT|wx.RIGHT|wx.TOP, 5 )
		
		bSizer32.Add( bSizer22, 0, wx.ALIGN_CENTER|wx.EXPAND|wx.TOP, 5 )
		
		bSizer55 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer56 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer29 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel23, wx.ID_ANY, u"Options" ), wx.VERTICAL )
		
		fgSizer8 = wx.FlexGridSizer( 3, 3, 15, 5 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText30 = wx.StaticText( self.m_panel23, wx.ID_ANY, u"Separator", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		fgSizer8.Add( self.m_staticText30, 0, wx.ALL, 5 )
		
		bSizer46 = wx.BoxSizer( wx.VERTICAL )
		
		self.query_sep_tab_radio = wx.RadioButton( self.m_panel23, wx.ID_ANY, u"[tab]  '\\t'", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer46.Add( self.query_sep_tab_radio, 0, wx.LEFT|wx.RIGHT|wx.TOP, 5 )
		
		self.query_sep_space_radio = wx.RadioButton( self.m_panel23, wx.ID_ANY, u"[space]", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer46.Add( self.query_sep_space_radio, 0, wx.LEFT|wx.RIGHT, 5 )
		
		bSizer47 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.query_sep_custom_radio = wx.RadioButton( self.m_panel23, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer47.Add( self.query_sep_custom_radio, 0, wx.LEFT|wx.RIGHT, 5 )
		
		self.query_sep_custom_text = wx.TextCtrl( self.m_panel23, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 35,-1 ), 0 )
		bSizer47.Add( self.query_sep_custom_text, 0, wx.RIGHT, 5 )
		
		bSizer46.Add( bSizer47, 1, wx.EXPAND, 5 )
		
		fgSizer8.Add( bSizer46, 1, wx.EXPAND, 5 )
		
		self.m_staticText48 = wx.StaticText( self.m_panel23, wx.ID_ANY, u"Character used to separate fields within each row.", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText48.Wrap( -1 )
		fgSizer8.Add( self.m_staticText48, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText511 = wx.StaticText( self.m_panel23, wx.ID_ANY, u"Input type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )
		fgSizer8.Add( self.m_staticText511, 0, wx.ALL, 5 )
		
		query_file_type_boxChoices = [ u"Pairs", u"List" ]
		self.query_file_type_box = wx.ComboBox( self.m_panel23, wx.ID_ANY, u"Pairs", wx.DefaultPosition, wx.Size( 100,-1 ), query_file_type_boxChoices, wx.CB_READONLY )
		fgSizer8.Add( self.query_file_type_box, 0, wx.ALL, 5 )
		
		self.m_staticText52 = wx.StaticText( self.m_panel23, wx.ID_ANY, u"Select whether the input is a list of objects or a set of pairs first field of each row is an object or a GO Term.", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText52.Wrap( -1 )
		fgSizer8.Add( self.m_staticText52, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		sbSizer29.Add( fgSizer8, 1, wx.EXPAND, 5 )
		
		bSizer56.Add( sbSizer29, 1, wx.EXPAND, 5 )
		
		bSizer55.Add( bSizer56, 1, wx.EXPAND, 5 )
		
		bSizer32.Add( bSizer55, 0, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer18 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel23, wx.ID_ANY, u"Help" ), wx.VERTICAL )
		
		self.m_staticText311 = wx.StaticText( self.m_panel23, wx.ID_ANY, u"Select a file", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText311.Wrap( -1 )
		self.m_staticText311.SetMaxSize( wx.Size( 500,-1 ) )
		
		sbSizer18.Add( self.m_staticText311, 0, wx.ALL, 5 )
		
		bSizer32.Add( sbSizer18, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		bSizer521.Add( bSizer32, 1, wx.EXPAND, 5 )
		
		self.m_panel23.SetSizer( bSizer521 )
		self.m_panel23.Layout()
		bSizer521.Fit( self.m_panel23 )
		self.query_input_method_box.AddPage( self.m_panel23, u"Load query from file", True )
		self.m_panel24 = wx.Panel( self.query_input_method_box, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer53 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer181 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel24, wx.ID_ANY, u"Help" ), wx.VERTICAL )
		
		self.m_staticText3111 = wx.StaticText( self.m_panel24, wx.ID_ANY, u"All the objects in the annotation corpus will be used as input list. Pairwise Semantic Similarity will be evaluated on such list", wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		self.m_staticText3111.Wrap( -1 )
		self.m_staticText3111.SetMaxSize( wx.Size( 500,-1 ) )
		
		sbSizer181.Add( self.m_staticText3111, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		bSizer53.Add( sbSizer181, 0, wx.EXPAND, 5 )
		
		self.m_panel24.SetSizer( bSizer53 )
		self.m_panel24.Layout()
		bSizer53.Fit( self.m_panel24 )
		self.query_input_method_box.AddPage( self.m_panel24, u"Annotation Corpus", False )
		sbSizer36.Add( self.query_input_method_box, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer50.Add( sbSizer36, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.query_panel.SetSizer( bSizer50 )
		self.query_panel.Layout()
		bSizer50.Fit( self.query_panel )
#