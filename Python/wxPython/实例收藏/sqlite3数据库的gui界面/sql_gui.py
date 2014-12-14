#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
# filename:     sql_gui.py
# version:      1.0.5
# description:  The Graphics User Interface for sqlite3.
# first create: ppxxyy1110
# history:
#       2012-09-22 | 0.0.1
#                    ppxxyy1110 create
#       2012-09-24 | 1.0.0
#                    ppxxyy1110 modified
#       2012-10-02 | 2.0.0
#                    ppxxyy1110 modified
#       2012-10-07 | 2.0.2
#                    ppxxyy1110 modified
# ------------------------------------------------------------------------------

"""this module offer a graphic interface for sqlite database"""
import os
import logging

import wx
import wx.grid

from wxPython.实例收藏.sqlite3数据库的gui界面 import sql


logging.basicConfig(level=logging.DEBUG)

class MyApp(wx.App):
    """my sqlite3 application"""
    
    def __init__(self):
        """this method override from parent's method
        this method will be auto called by his parent's (wx.App)"""
        
        self.logger = logging.getLogger(self.__class__.__name__)
        
        wx.App.__init__(self)
        self.frame = MainWindow(None, "SQLite3 viewer")
        self.SetTopWindow(self.frame)
        
        self.logger = logging.getLogger(self.__class__.__name__)
#    def OnInit(self):
#        """this method override from parent's method
#        this method will be auto called by his parent's (wx.App)"""
#        self.frame = MainWindow(None, "SQLite3 viewer")
#        self.SetTopWindow(self.frame)
#        return True
    
    
class MainWindow(wx.Frame):
    """this my main window gui for sqlite"""
    def __init__(self, parent, title):
        
        self.logger = logging.getLogger(self.__class__.__name__)
        
        # here initial all the vars
        self.__tables = None
        self.__infos = None
        self.__filename = None
        self.__curseltable = None
        self.__dirname = os.getcwd()
        self.pos_x, self.pos_y = (-1, -1)   #grid table current selected item initial (-1,-1)
        self.__menus = {} #all the menu in the menubar
        self.__ids = {}
        self.__tree = None
        self.database = sql.MyDB()
        
        # we select 800px width and the 600px height.
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        
        self.__init_ids()
        
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() # A Statusbar in the bottom of the window
        # Creating the menubar.
        self.__create_menu_bar()
        # Create the tree
        self.__init_tree_ctrl()
        
        self.grid = wx.grid.Grid(self)#Dbgrid(self)
        self.table = MyGridTable()
        self.__init_grid_ctrl()
        
        self.__init_layout()
        self.Show(True)
        

    def __menu_bar_data(self):
        """get menu bar data
        id, label, event_handler"""
        return ((self.__menus['filemenu'], "&File", self.__on_file_menu),
                (self.__menus['editmenu'], "&Edit", self.__on_grid_popup_item_selected),
                (self.__menus['helpmenu'], "&Help", self.__on_help_menu)
                )
    def __menu_data(self, menu_name):
        """get menu data
        event, id, label, event_handler, help or statebar string"""
        
        ids = self.__ids
        if menu_name == 'filemenu':
            return ((wx.EVT_MENU, wx.ID_OPEN, "&Open DataBase", self.__on_file_menu, " Open a file to edit"),
                    (wx.EVT_MENU, ids['id_memu_close_db'], "&Close DataBase", self.__on_file_menu,
                     "Close current database"),
                    (wx.EVT_MENU, wx.ID_EXIT, "&Exit", self.__on_file_menu, " Terminate the program")
                    )
        elif menu_name == 'editmenu':
            return ((wx.EVT_MENU, ids['id_add_row'], "&Add a row", self.__on_grid_popup_item_selected,
                     "&Add a row"),
                    (wx.EVT_MENU, ids['id_del_row'], "&Del a row", self.__on_grid_popup_item_selected,
                     "&Del a row"),
                    (wx.EVT_MENU, ids['id_update_row'], "&Update a row", self.__on_grid_popup_item_selected,
                     "&Update a row")
                    )
        elif menu_name == 'helpmenu':
            return ((wx.EVT_MENU, wx.ID_ABOUT, "&About", self.__on_help_menu, " Information about this program"),)
        
        return None
        
    def __create_menu(self, menu_name):
        """this method initial menu"""
        menu = self.__menus[menu_name] = wx.Menu()
        for eachmenudata in self.__menu_data(menu_name):
            each_evt = eachmenudata[0]
            each_id = eachmenudata[1]
            each_label = eachmenudata[2]
            each_handler = eachmenudata[3]
            each_statebar_string = eachmenudata[4]
            each_menu = menu.Append(each_id, each_label, each_statebar_string)
            self.Bind(each_evt, each_handler, each_menu)
        
    def __create_menu_bar(self):
        """create menu bar"""
        for menu_name in ['filemenu', 'editmenu', 'helpmenu']:
            self.__create_menu(menu_name)
        menubar = wx.MenuBar()
        for each_menudata in self.__menu_bar_data():
            menuid = each_menudata[0]
            menulabel = each_menudata[1]
            menubar.Append(menuid, menulabel)
        self.__menus['filemenu'].FindItemById(self.__ids['id_memu_close_db']).Enable(False)
        self.SetMenuBar(menubar)
        
    def __on_help_menu(self, evt):
        """handler function of About menu event"""
        if evt.GetId() == wx.ID_ABOUT:
            dlg = wx.MessageDialog(self, "Made by P.X.Y" , "About Sample Editor", wx.OK)
            dlg.ShowModal() # Shows it
            dlg.Destroy() # finally destroy it when finished.

    def __on_file_menu(self, evt):
        """when file menu item selected, this function called"""
        if evt.GetId() == wx.ID_OPEN:
            #open a db
            dlg = wx.FileDialog(self, "Choose a file", self.__dirname, "", "*.*", wx.OPEN)
            
            if dlg.ShowModal() == wx.ID_OK:    
                self.__filename = dlg.GetFilename()
                self.__dirname = dlg.GetDirectory()
                self.database.connect_db(os.path.join(self.__dirname, self.__filename))
                self.__update_tree()
                self.__menus['filemenu'].FindItemById(wx.ID_OPEN).Enable(False)
                self.__menus['filemenu'].FindItemById(self.__ids['id_memu_close_db']).Enable(True)
            dlg.Destroy()
        elif evt.GetId() == self.__ids['id_memu_close_db']:
            #close current db
            dlg = wx.MessageDialog(self, "Close current DB" , "Close current DB", wx.OK)
            if dlg.ShowModal() == wx.ID_OK:
                self.__menus['filemenu'].FindItemById(wx.ID_OPEN).Enable(True)
                self.__menus['filemenu'].FindItemById(self.__ids['id_memu_close_db']).Enable(False)
                self.database.close_db()
                self.__tree.DeleteAllItems()
                self.control.SetValue("")
                self.table = None
                self.grid.SetTable(self.table, True)
                self.grid.ForceRefresh()
            dlg.Destroy() # finally destroy it when finished.
        elif evt.GetId() == wx.ID_EXIT:
            #exit app
            self.Close(True)

    def __add_treenodes(self, parent_item, items):
        """
        Recursively traverses the data structure, adding tree nodes to
        match it.
        """
        for item in items:
            if type(item) == str or type(item) == unicode:
                self.__tree.AppendItem(parent_item, item)
#                self.logger.debug("str")
            elif type(item) != list:
#                self.logger.debug("is not list")
                #self.logger.debug("item = %s" %item)
                pass
            else:
                #self.logger.debug( "is list")
                new_item = self.__tree.AppendItem(parent_item, item[0])
                self.__add_treenodes(new_item, item[1])

    def __get_item_text(self, item):
        """get current tree select item text"""
        if item:
            return self.__tree.GetItemText(item)
        else:
            return ""

    def __on_item_expanded(self, evt):
        """when tree item expanded, this method would be called"""
        self.logger.debug("__on_item_expanded: %s" % self.__get_item_text(evt.GetItem()))

    def __on_item_collapsed(self, evt):
        """when tree item collapsed, this method would be called"""
        self.logger.debug("__on_item_collapsed:" % self.__get_item_text(evt.GetItem()))

    def __on_sel_changed(self, evt):
        """when tree item selected change, this method would be called"""
        select_text = self.__get_item_text(evt.GetItem())
        if os.path.join(self.__dirname, select_text) == self.database.databasename:
            return
        elif select_text in self.__tables:
            tablename = self.__curseltable = select_text
            
            self.__infos = [ (item[1], item[2]) for item in self.database.gettableinfo(tablename)]
            #self.logger.debug("self.database.gettableinfo() = %s" % info)
            self.control.SetValue(str(self.__infos))
            self.__update_table()
            self.grid.ForceRefresh()
#            v = self.database.get_table_value(self.__curseltable)
#            self.logger.debug( "v= " % v)
        else:
            self.logger.debug("no a table")
            
            return
        
        self.logger.debug("__on_sel_changed: %s" % self.__get_item_text(evt.GetItem()))
        evt.Skip()

    def __on_activated(self, evt):
        """when a tree item be double clicked, this method would be called """
#        select_text = self.__get_item_text(evt.GetItem())
#        if os.path.join(self.__dirname, select_text) == self.database.databasename:
#            self.__tree.PopupMenu(self.__menus['treepopupmenu'], (-1, -1))#(-1,-1)indicate current mouse position
#        else:
#            self.logger.debug( "select_text = " % select_text)
        self.logger.debug("__on_activated:    %s" % self.__get_item_text(evt.GetItem()))

    def __on_grid_double_click(self, evt):
        """when a grid item be double clicked, this method would be called """
        self.logger.debug("GridDoubleClick %d,%d", (evt.GetRow(), evt.GetCol()))
        self.logger.debug("table[evt.GetRow()][evt.GetCol()] = %s" % self.table[evt.GetRow()][evt.GetCol()])
        evt.Skip()

    def __on_grid_click(self, evt):
        """when a tree item be clicked, this method would be called """
        self.pos_x, self.pos_y = evt.GetRow(), evt.GetCol()
        self.logger.debug("__on_grid_click")
        evt.Skip()

    def __on_grid_popup_menu(self, evt):
        """this method make create grid popup menu when grid item be right clicked"""
        pos = evt.GetPosition()
        self.logger.debug("__on_grid_popup_menu")
        if evt.GetId() == wx.grid.EVT_GRID_CELL_LEFT_CLICK:
            return
        
        self.pos_x = evt.GetRow()
        self.pos_y = evt.GetCol()
        self.grid.PopupMenu(self.__menus['gridpopupmenu'], pos)

    def __on_tree_popup_menu(self, evt):
        """this method make create tree popup menu when tree item be right clicked"""
        select_text = self.__get_item_text(evt.GetItem())
        if os.path.join(self.__dirname, select_text) == self.database.databasename:
            self.__tree.PopupMenu(self.__menus['treepopupmenu'], (-1, -1))#(-1,-1)indicate current mouse position
        else:
            self.logger.debug( "select_text = %s" % select_text)
        return

    def __on_tree_popup_item_selected(self, evt):
        """when a tree menu item be selected, this method would be called """
        item = self.__menus['treepopupmenu'].FindItemById(evt.GetId())
        text = item.GetText()
        #wx.MessageBox("You selected item '%s'" % text)
        
        if evt.GetId() == self.__ids['id_create_table']:
            dlg = wx.TextEntryDialog(None, 'please input the new table name', 'new table name', 'table_name')
            if dlg.ShowModal() == wx.ID_OK:
                newtable = dlg.GetValue().strip()
                cols = {}
                #self.logger.debug('please input fieldname and type, if no more field, just input end')
                while True:
                    dlg = wx.TextEntryDialog(None, "filename:type or end", 'A Question', 'end')
                    #text = raw_input('format filename:type or "end": ')
                    if dlg.ShowModal() != wx.ID_OK :
                        return
                    else:
                        text = dlg.GetValue()
                        if text == "end":
                            break
                        else:
                            self.logger.debug("text = %s" % text)
                            tmp = text.strip().split(":")
                            cols[tmp[0]] = tmp[1]
                
                self.database.addatable(newtable, cols)
                self.__update_tree()
    
    def __on_grid_popup_item_selected(self, evt):
        """when a grid popup menu item be selected, this method would be called """
        self.logger.debug("__on_grid_popup_item_selected")
        tblname = self.__curseltable
        if evt.GetId() == self.__ids['id_del_row']:
            dic = {}
            i = 0
            for col in self.table.col_labels:
                dic[col] = self.table.data[self.pos_x][i]
                i += 1
            self.database.deleteitem(tblname, dic)
            self.__update_table()
            
        elif evt.GetId() == self.__ids['id_add_row']:
            tableinfo = self.database.gettableinfo(tblname)
            colname = [item[1] for item in tableinfo]
            dic = {}
            dlg = wx.TextEntryDialog(None, "set the new row field value witch splited by ','", 'A Question')
            if dlg.ShowModal() == wx.ID_OK:
                vals = dlg.GetValue().split(',')
                if len(vals) != len(colname):
                    wx.MessageBox("you enter a invalid row, please try again")
                    return
                i = 0
                for col in colname:
                    dic[col] = vals[i]
                    i += 1
                self.database.additem(tblname, dic)
                self.__update_table()
              
        elif evt.GetId() == self.__ids['id_update_row']:
            (posx, posy) = (self.pos_x, self.pos_y)
            #make where sub statement
            dic = {}
            i = 0
            for col in self.table.col_labels:
                dic[col] = self.table.data[posx][i]
                i += 1
            # make set sub statement
            setdic = {}
            dlg = wx.TextEntryDialog(None, "set the new row field value", 'A Question')
            if dlg.ShowModal() == wx.ID_OK:
                val = dlg.GetValue().strip()
                col = self.table.col_labels[posy]
                setdic[col] = val
                self.database.updateitem(tblname, dic, setdic)
                self.__update_table()
        self.grid.ForceRefresh()

    def __update_tree(self):
        """this method update treectrl"""
        
        self.__tables = self.database.gettables()
        tables = []
        for i in range(len(self.__tables)):
            cols = self.database.gettablecoltype(self.__tables[i]).keys()
            tables.append([self.__tables[i], cols])
        self.__tree.DeleteAllItems()
        root = self.__tree.AddRoot(self.__filename)
        self.__add_treenodes(root, tables)
        self.__tree.Expand(root)

    def __update_table(self):
        """this method update tablectrl"""
        tblname = self.__curseltable
        value = self.database.get_table_value(tblname)
        self.table = MyGridTable(value, [item[0] for item in self.__infos])
        self.grid.SetTable(self.table, True)
        self.grid.EnableEditing(False)

    def __init_tree_ctrl(self):
        """initial the tree ctrl"""
        self.__tree = wx.TreeCtrl(self)
        self.__tree.AddRoot("please open a database")
        
        self.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.__on_item_expanded, self.__tree)
        self.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.__on_item_collapsed, self.__tree)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.__on_sel_changed, self.__tree)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.__on_activated, self.__tree)
        self.__tree.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.__on_tree_popup_menu)
        
        self.__menus['treepopupmenu'] = wx.Menu()
        self.__tree.Bind(wx.EVT_MENU, self.__on_tree_popup_item_selected,
                       self.__menus['treepopupmenu'].Append(self.__ids['id_create_table'], "creat a table"))

    def __init_grid_ctrl(self):
        """initial the grid ctrl"""
        self.grid.SetTable(self.table, True)
        self.grid.EnableEditing(False)
        self.grid.ForceRefresh()
        # Grid Evnets
        self.Bind(wx.grid.EVT_GRID_CELL_RIGHT_DCLICK, self.__on_grid_double_click, self.grid)
        self.grid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.__on_grid_popup_menu, self.grid)

        gridpopupmenu = self.__menus['gridpopupmenu'] = wx.Menu()
        
        popupmenus = [gridpopupmenu.Append(self.__ids['id_del_row'], "del a row"),
                 gridpopupmenu.Append(self.__ids['id_add_row'], "add a row"),
                 gridpopupmenu.Append(self.__ids['id_update_row'], "update a row")
                ]
        for eachpopupmenu in popupmenus:
            self.grid.Bind(wx.EVT_MENU, self.__on_grid_popup_item_selected, eachpopupmenu)

        self.grid.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.__on_grid_click, self.grid)
        self.grid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.__on_grid_popup_menu, self.grid)
        self.grid.Bind(wx.EVT_RIGHT_DCLICK, self.__on_grid_popup_menu, self.grid)

    def __init_layout(self):
        """this method initial the main window layout"""
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer2 = wx.BoxSizer(wx.VERTICAL)
        sizer3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.__tree, 1, wx.EXPAND)
        sizer.Add(sizer2, 3, wx.EXPAND)
        sizer2.Add(sizer3, 1, wx.EXPAND)
        sizer2.Add(self.grid, 3, wx.EXPAND)
        sizer3.Add(self.control, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetAutoLayout(1)

    def __init_ids(self):
        """initial some ids"""
        self.__ids['id_memu_close_db'] = wx.NewId()    #get a new id
        wx.RegisterId(self.__ids['id_memu_close_db'])  #make sure this id be global unique
        self.__ids['id_create_table'] = wx.NewId()   #"creat a table"
        wx.RegisterId(self.__ids['id_create_table'])
        self.__ids['id_del_row'] = wx.NewId()
        wx.RegisterId(self.__ids['id_del_row'])
        self.__ids['id_add_row'] = wx.NewId()
        wx.RegisterId(self.__ids['id_add_row'])
        self.__ids['id_update_row'] = wx.NewId()
        wx.RegisterId(self.__ids['id_update_row'])

class MyGridTable(wx.grid.PyGridTableBase):
    """my table class"""
    def __init__(self, tvalue=None, tcollabels=None):
        wx.grid.PyGridTableBase.__init__(self)
        self.col_labels = []
        self.row_labels = []
        
        if tvalue is not None:
            self.col_labels = tcollabels
            self.row_labels = [str(i) for i in range(len(tvalue))]
            self.data = [];
            for item in tvalue:
                self.data.append([ite for ite in item])

        self.odd = wx.grid.GridCellAttr()
        self.odd.SetBackgroundColour("sky blue")
        self.odd.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))

        self.even = wx.grid.GridCellAttr()
        self.even.SetBackgroundColour("sea green")
        self.even.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
    
# these five are the required methods
    def GetNumberRows(self):
        return len(self.row_labels)

    def GetNumberCols(self):
        return len(self.col_labels)

    def IsEmptyCell(self, row, col):
        return row < len(self.data) and col < len(self.data[row]) and self.data[row][col] is not None

    def GetValue(self, row, col):
        value = self.data[row][col]
        if value is not None:
            return value
        else:
            return ''
    
    def SetValue(self, row, col, value):
        #self.logger.debug("in SetValue")
        if row < len(self.row_labels) and col < len(self.col_labels):
            self.data[row][col] = value
            

    # the table can also provide the attribute for each cell
    def GetAttr(self, row, col, kind):
        #self.logger.debug("in GetAttr")
        attr = [self.even, self.odd][row % 2]
        attr.IncRef()
        return attr

    def GetColLabelValue(self, col):
        #self.logger.debug("in GetColLabelValue")
        return self.col_labels[col]

    def GetRowLabelValue(self, row):
        #self.logger.debug("in GetRowLabelValue")
        return self.row_labels[row]
    
if __name__ == '__main__':
    APP = MyApp() #wx.App(False)
    APP.MainLoop()
    
