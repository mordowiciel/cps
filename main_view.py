from Tkinter import *
import tkMessageBox

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import signal_generator as sig_gen
import numpy as np
import plot_utils as plot_u
import signal_operations as signal_o

class BasicView:

  ListBoxReference = None
  TopPaneReference = None
  M1Reference = None
  RootReference = {}
  RRow = 1
  entries = []
  amplitudeEntry = None
  TEntry = None
  t1Entry = None
  dEntry = None
  sampFreqEntry = None
  KwEntry = None
  signalsMap = {}
  formWindow = None
  selectedFunction = None
  actionWindow = None
  signalsActionType = None
  selectedSignalsForAction = []
  FUNC_OPTIONS = {
    3: "sine",
    4: "half_wave_rect_sine",
    5: "full_wave_rect_sine",
    6: "square",
    7: "square_symmetrical",
    8: "triangular"
  }


  def __init__(self):
    self.init_basic_window()

  def init_basic_window(self):
    root = Tk()
    self.init_menubar(root)
    self.init_menu_grid(root)
    self.RootReference = root
    root.mainloop()

  def init_menubar(self, parent):
    menubar = Menu(parent)
    optionsMenu = Menu(menubar, tearoff=0)
    optionsMenu.add_command(label="New", command=self.init_form_window)
    optionsMenu.add_command(label="Save as")

    optionsMenu.add_separator()

    optionsMenu.add_command(label="Show plot", command=self.drawSelectedPlot)
    optionsMenu.add_command(label="Show histogram", command=self.drawSelectedHistogram)

    optionsMenu.add_separator()

    optionsMenu.add_command(label="Add signals", command=self.init_signal_action)

    optionsMenu.add_command(label="Exit", command=parent.quit)
    menubar.add_cascade(label="Options", menu=optionsMenu)
    parent.config(menu=menubar)

  def init_menu_grid(self, parent):
    m1 = PanedWindow(parent)
    self.M1Reference = m1
    m1.pack(fill=BOTH, expand=1)
    left = Label(m1)
    Lb1 = Listbox(left, selectmode= MULTIPLE)
    self.ListBoxReference = Lb1
    Lb1.bind('<<ListboxSelect>>', self.onselect)
    Lb1.pack(side="left", fill="y")
    m1.add(left)
    m2 = PanedWindow(m1, orient=VERTICAL)
    m1.add(m2)
    top = Label(m2, text="top pane")

    self.TopPaneReference = m2
    m2.add(top)
    self.set_top_pane_canvas()


  def set_top_pane_canvas(self, entries = None):
    top = self.TopPaneReference
    f = Figure(figsize=(5,5), dpi=100)
    canvas = FigureCanvasTkAgg(f,  top)
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
    canvas.show()
    if (entries != None):
      a = f.add_subplot(111)
      a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
      toolbar = NavigationToolbar2TkAgg(canvas, self.TopPaneReference)
      toolbar.update()
      canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

  def init_form_window(self):
    top = Toplevel()
    self.formWindow = top
    self.selectedFunction = StringVar(top)
    self.selectedFunction.set(self.FUNC_OPTIONS.values()[0]) # default value
    w = OptionMenu(top, self.selectedFunction, *self.FUNC_OPTIONS.values())
    w.config(width=25)
    w.grid(column =1, row =0, sticky="ew")

    Label(top, text="Typ funkcji").grid(row= 0)
    Label(top, text="Amplituda").grid(row=2)
    e2 = Entry(top, state=self.getState(2))
    self.amplitudeEntry = e2

    Label(top, text="Czas poczatkowy(t1)").grid(row=3)
    e3 = Entry(top, state=self.getState(3))
    self.t1Entry=e3

    Label(top, text="Czas trwania(d)").grid(row= 4)
    e4 = Entry(top, state=self.getState(4))
    self.dEntry = e4

    Label(top, text="Okres podstawowy(T)").grid(row= 5)
    e5 = Entry(top, state=self.getState(5))
    self.TEntry = e5

    Label(top, text="Wspolczynnik wypelnienia(kw)").grid(row= 6)
    e6 = Entry(top, state=self.getState(6))
    self.KwEntry = e6

    # Label(top, text="Skok jednostkowy(ts)").grid(row= 7)
    # e7 = Entry(top, state=self.getState(7))

    # Label(top, text="Nr pierwszej probki(n1)").grid(row= 8)
    # e8 = Entry(top, state=self.getState(8))

    # Label(top, text="Skok dla probki nr (ns)").grid(row= 9)
    # e9 = Entry(top, state=self.getState(9))

    Label(top, text="Czestotliwosc probkowania(f)").grid(row= 10)
    e10 = Entry(top, state=self.getState(10))
    self.sampFreqEntry = e10

    # Label(top, text="Prawdopodobienstwo(p)").grid(row= 11)
    # e11 = Entry(top, state=self.getState(11))


    # e1 = Entry(top, state=self.getState(1))

    # e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=3, column=1)
    e4.grid(row=4, column=1)
    e5.grid(row=5, column=1)
    e6.grid(row=6, column=1)
    # e7.grid(row=7, column=1)
    # e8.grid(row=8, column=1)
    # e9.grid(row=9, column=1)
    e10.grid(row=10, column=1)
    # e11.grid(row=11, column=1)
    Button(top, text='Add', width=15, command=self.generateSignal).grid(row=15, column=1, sticky=W, pady=4)

    top.mainloop()

  def add_to_menu_grid(self, obj, label):
    self.signalsMap[label] = obj
    self.ListBoxReference.insert(END, label)

  def init_signal_action(self):
    OPTIONS = [
      "add",
      "substract",
      "multiply",
      "divide"
    ]

    listBoxOptions = list(self.ListBoxReference.get(0, END))
    top = Toplevel()

    Label(top, text="Sygnal nr 1 ").grid(row=0, column=0)
    selected = StringVar(top)
    selected.set(listBoxOptions[0])
    w = OptionMenu(top, selected, *listBoxOptions)
    w.config(width=25)
    w.grid(column =1, row =0, sticky="ew")


    Label(top, text="Sygnal nr 2").grid(row=1, column=0)
    selected2 = StringVar(top)
    selected2.set(listBoxOptions[0])
    w2= OptionMenu(top, selected2, *listBoxOptions)
    w2.config(width=25)
    w2.grid(column = 1, row = 1, sticky="ew")

    Label(top, text="Akcja").grid(row=2, column=0)
    actionType = StringVar(top)
    actionType.set(OPTIONS[0])

    self.actionWindow = top
    self.actionType = actionType
    self.selectedSignalsForAction = [ selected, selected2 ]

    w3= OptionMenu(top, actionType, *OPTIONS)
    w3.config(width=25)
    w3.grid(column = 1, row = 2, sticky="ew")

    Button(top, text='Add', width=15, command=self.signalsActions).grid(row=4, column=1, sticky=W)

  def signalsActions(self):
    signal1Name = self.selectedSignalsForAction[0].get()
    signal2Name = self.selectedSignalsForAction[1].get()
    signal1 = self.signalsMap[signal1Name]
    signal2 = self.signalsMap[signal2Name]
    result = None
    label = ''

    if (self.actionType.get() == "add"):
      result = signal_o.add_signals(signal1, signal2)
      label = signal1Name + "+" + signal2Name
    elif(self.actionType=="substract"):
      result = signal_o.substract_signals(signal1, signal2)
      label = signal1Name + "-" + signal2Name
    elif(self.actionType=="multiply"):
      result = signal_o.multiply_signals(signal1, signal2)
      label = signal1Name + "*" + signal2Name
    elif(self.actionType == "divide"):
      result = signal_o.divide_signals(signal1, signal2)
      label = signal1Name + "/" + signal2Name
    self.add_to_menu_grid(result, label)

  def generateSignal(self, signal=None):
    option = self.selectedFunction.get()

    print option
    if signal == None:
      if option == "sine":
        signal = sig_gen.sine(A= float(self.amplitudeEntry.get()), T=float(self.TEntry.get()), t1=float(self.t1Entry.get()), d=float(self.dEntry.get()), sampling_freq=float(self.sampFreqEntry.get()))
      elif option == "half_wave_rect_sine":
        signal = sig_gen.half_wave_rect_sine(A=float(self.amplitudeEntry.get()), T=float(self.TEntry.get()), t1 = float(self.t1Entry.get()), d =float(self.dEntry.get()), sampling_freq=float(self.sampFreqEntry.get()))
      elif option == "full_wave_rect_sine":
        signal = sig_gen.full_wave_rect_sine(A=float(self.amplitudeEntry.get()), T=float(self.TEntry.get()), t1 = float(self.t1Entry.get()), d =float(self.dEntry.get()), sampling_freq=float(self.sampFreqEntry.get()))
      elif option == "square":
        signal = sig_gen.square(A=float(self.amplitudeEntry.get()), T=float(self.TEntry.get()), kW=float(self.KwEntry.get()), t1 = float(self.t1Entry.get()), d =float(self.dEntry.get()), sampling_freq=float(self.sampFreqEntry.get()))
      elif option == "square_symmetrical":
        signal = sig_gen.square_symmetrical(A=float(self.amplitudeEntry.get()), T=float(self.TEntry.get()), kW=float(self.KwEntry.get()), t1 = float(self.t1Entry.get()), d =float(self.dEntry.get()), sampling_freq=float(self.sampFreqEntry.get()))
      elif option == "triangular":
        signal = sig_gen.triangular(A=float(self.amplitudeEntry.get()), T=float(self.TEntry.get()), kW=float(self.KwEntry.get()), t1 = float(self.t1Entry.get()), d =float(self.dEntry.get()), sampling_freq=float(self.sampFreqEntry.get()))
    self.formWindow.destroy()
    self.add_to_menu_grid(signal, option + str(self.ListBoxReference.size()))
    self.drawSignal(signal)
    # self.drawHistogram(signal)

  def drawSelectedPlot(self):
    values = [self.ListBoxReference.get(idx) for idx in self.ListBoxReference.curselection()]
    print ', '.join(values)
    if len(values)>1:
      tkMessageBox.showinfo("Alert", "You can select only one function at time")
    else:
      self.drawSignal(self.signalsMap[self.ListBoxReference.get(ACTIVE)])

  def drawSelectedHistogram(self):
    self.drawHistogram(self.signalsMap[self.ListBoxReference.get(ACTIVE)])


  def drawSignal(self, signal, label = 'Signal'):
    if isinstance(signal, str):
      signal = self.signalsMap[signal]
    entries = plot_u.plot_signal(signal, label)
    self.set_top_pane_canvas(entries)

  def drawHistogram(self, signal, label = 'Histogram'):
    if isinstance(signal, str):
      signal = self.signalsMap[signal]
    plot_u.plot_histogram(signal, label)


  def delete_from_menu_grid(firstIndex, lastIndex):
    self.ListBoxReference.delete(firstIndex, lastIndex)


  # def showFunctionStats(self, signal):


  def onselect(self, evt):
    w = evt.widget
    # index = int(w.curselection()[0])
    # value = w.get(index)
    # self.drawHistogram(self.signalsMap[self.ListBoxReference.get(ACTIVE)])
    # self.drawSignal(self.signalsMap[self.ListBoxReference.get(ACTIVE)])

  def getState(self, labelNr):
    return NORMAL
    return DISABLED

