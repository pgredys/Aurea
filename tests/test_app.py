import tkinter
import unittest
from tkinter import ttk

import _tkinter


class TKinterTestCase(unittest.TestCase):
    """These methods are going to be the same for every GUI test,
    so refactored them into a separate class
    """
    def setUp(self):
        self.root=tkinter.Tk()
        self.pump_events()

    def tearDown(self):
        if self.root:
            self.root.destroy()
            self.pump_events()

    def pump_events(self):
        while self.root.dooneevent(_tkinter.ALL_EVENTS | _tkinter.DONT_WAIT):
            pass

class TestViewAskText(TKinterTestCase):
    def test_enter(self):
        v = View_AskText(self.root,value=u"йцу")
        self.pump_events()
        v.e.focus_set()
        v.e.insert(tkinter.END,u'кен')
        v.e.event_generate('<Return>')
        self.pump_events()

        self.assertRaises(tkinter.TclError, lambda: v.top.winfo_viewable())
        self.assertEqual(v.value,u'йцукен')


# ###########################################################
# The class being tested (normally, it's in a separate module
# and imported at the start of the test's file)
# ###########################################################

class View_AskText(object):
    def __init__(self, master, value=u""):
        self.value=None

        top = self.top = tkinter.Toplevel(master)
        top.grab_set()
        self.l = ttk.Label(top, text=u"Value:")
        self.l.pack()
        self.e = ttk.Entry(top)
        self.e.pack()
        self.b = ttk.Button(top, text='Ok', command=self.save)
        self.b.pack()

        if value: self.e.insert(0,value)
        self.e.focus_set()
        top.bind('<Return>', self.save)

    def save(self, *_):
        self.value = self.e.get()
        self.top.destroy()


if __name__ == '__main__':
    import unittest
    unittest.main()