from wxPython.wx import *

class Window ( wxFrame ):

	def __init__ ( self ):

		wxFrame.__init__ ( self, None, -1, 'Static Box', size = ( 300, 300 ) )

		# Create a panel to house everything

		self.panel = wxPanel ( self, -1 )

		# Create vertical box sizer

		self.sizer = wxBoxSizer ( wxVERTICAL )

		# Create a horizontal box sizer -- we're going to center everything

		self.horizontal = wxBoxSizer ( wxHORIZONTAL )

		# Create the wxStaticBox

		self.box = wxStaticBox ( self.panel, -1, 'Just a Box' )

		# Create our wxStaticBoxSizer

		self.boxSizer = wxStaticBoxSizer ( self.box, wxHORIZONTAL )

		# Create some buttons

		self.button1 = wxButton ( self.panel, -1, 'Just a button' )

		self.button2 = wxButton ( self.panel, -1, 'Another.' )

		# Add the buttons to the sizer

		self.boxSizer.Add ( self.button1 )

		self.boxSizer.Add ( self.button2 )

		# Configure the box sizers

		self.horizontal.Add ( ( 0, 0 ), 1, wxEXPAND )

		self.horizontal.Add ( self.boxSizer )

		self.horizontal.Add ( ( 0, 0 ), 1, wxEXPAND )

		self.sizer.Add ( ( 0, 0 ), 1, wxEXPAND )

		self.sizer.Add ( self.horizontal, 0, wxALIGN_CENTER )

		self.sizer.Add ( ( 0, 0 ), 1, wxEXPAND )

		# Attach everything

		self.panel.SetSizerAndFit ( self.sizer )

		self.Show ( True )

application = wxPySimpleApp()

Window()

application.MainLoop()