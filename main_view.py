# coding: utf-8

from Tkinter import *
import tkMessageBox

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import signal_generator as sig_gen
import numpy as np
import plot_utils as plot_u
import signal_utils as signal_utils
import noise_generator as noise_generator
import signal_operations as signal_operations
import signal_serializer as signal_serializer
import number_parser as number_parser

class BasicView:

  ListBoxReference = None
  TopPaneReference = None
  entries = []
  amplitudeEntry = None
  nameEntry = ''
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
    1: "szum o rozkładzie jednostajnym",
    2: "szum gaussowski",
    3: "sinusoidalny",
    4: "sinusoidalny wyprostowany jednopołówkowo",
    5: "sinusoidalny wyprostowany dwupołówkowo",
    6: "prostokątny",
    7: "prostokątny symetryczny",
    8: "trójkątny",
  }


  def __init__(self):
    self.init_basic_window()

  def init_basic_window(self):
    root = Tk()

    self.init_menubar(root)
    self.init_menu_grid(root)
    root.mainloop()

  def init_menubar(self, parent):
    menubar = Menu(parent)
    optionsMenu = Menu(menubar, tearoff=0)
    optionsMenu.add_command(label="Dodaj funkcje", command=self.init_form_window)
    optionsMenu.add_command(label="Usuń funkcje", command=self.delete_from_menu_grid)

    optionsMenu.add_command(label="Eksportuj sygnały", command=self.serialize_signals)
    optionsMenu.add_command(label="Importuj sygnały", command=self.deserialize_signals)

    optionsMenu.add_separator()

    optionsMenu.add_command(label="Operacje na sygnałąch", command=self.init_signal_action)

    optionsMenu.add_command(label="Wyjscie", command=parent.quit)
    menubar.add_cascade(label="Opcje", menu=optionsMenu)
    parent.config(menu=menubar)

  def init_menu_grid(self, parent):
    m1 = PanedWindow(parent)
    m1.pack(fill=BOTH, expand=1)
    left = Label(m1)
    Lb1 = Listbox(left, selectmode= SINGLE, borderwidth=0.5)
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


  def set_top_pane_canvas(self, entries = None, canvasType = None):
    top = self.TopPaneReference
    for child in top.winfo_children():
      child.destroy()

    if (entries != None):
      buttonsFrame = Frame(top)
      buttonsFrame.pack(side='top')
      Button(buttonsFrame, text="Pokaz wykres", command=self.show_current_function_plot).pack(side="left")
      Button(buttonsFrame, text="Pokaz histogram", command=self.show_current_function_histogram).pack(side="left")
      statsFrame = Frame(top)
      statsFrame.pack(side='top')
      if(canvasType == 'signal'):
        avg = signal_utils.calculate_average(int(entries[0][0]), int(entries[0][-1]), entries[1])
        avg_abs = signal_utils.calculate_abs_average(int(entries[0][0]), int(entries[0][-1]), entries[1])
        avg_power = signal_utils.calculate_avg_power(int(entries[0][0]), int(entries[0][-1]), entries[1])
        variance = signal_utils.calculate_variance(int(entries[0][0]), int(entries[0][-1]), entries[1])
        root_mean_sq = signal_utils.calculate_root_mean_square(int(entries[0][0]), int(entries[0][-1]), entries[1])

        Label(statsFrame, text="Wartosc srednia: {0}".format(avg).replace(")", "").replace("(", "").replace("+0j", "")).grid(row=1)
        Label(statsFrame, text="Wartosc srednia bezwzgledna: {0}".format(avg_abs).replace(")", "").replace("(", "").replace("+0j", "")).grid(row=2)
        Label(statsFrame, text="Wartosc skuteczna: {0}".format(root_mean_sq).replace(")", "").replace("(", "").replace("+0j", "")).grid(row=3)
        Label(statsFrame, text="Wariancja: {0}".format(variance).replace(")", "").replace("(", "").replace("+0j", "")).grid(row=4)
        Label(statsFrame, text="Moc srednia: {0}".format(avg_power).replace(")", "").replace("(", "").replace("+0j", "")).grid(row=5)

    f = Figure(figsize=(5,5), dpi=100)
    canvas = FigureCanvasTkAgg(f,  top)
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
    canvas.show()

    if (entries != None):
      a = f.add_subplot(111)

      if (canvasType == 'signal'):
        a.plot(entries[0], entries[1])

      if (canvasType=='histogram'):
        a.hist(entries, alpha=0.5, histtype='bar', ec='black')

      toolbar = NavigationToolbar2TkAgg(canvas, self.TopPaneReference)
      toolbar.update()
      canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)


  def show_current_function_plot(self):
    signalName = self.ListBoxReference.get(ACTIVE)
    signal = self.signalsMap[signalName]
    self.draw_signal(signal)


  def show_current_function_histogram(self):
    signalName = self.ListBoxReference.get(ACTIVE)
    signal = self.signalsMap[signalName]
    self.draw_histogram(signal)


  def init_form_window(self):
    top = Toplevel()
    self.formWindow = top
    self.selectedFunction = StringVar(top)
    self.selectedFunction.set(list(self.FUNC_OPTIONS.values())[0])
    w = OptionMenu(top, self.selectedFunction, *self.FUNC_OPTIONS.values())
    w.config(width=25)
    w.grid(column =1, row =0, sticky="ew")

    Label(top, text="Typ funkcji").grid(row= 0)
    Label(top, text="Nazwa").grid(row=2)
    e1 = Entry(top, state=self.get_state(1))
    self.nameEntry = e1


    Label(top, text="Amplituda").grid(row=3)
    e2 = Entry(top, state=self.get_state(2))
    self.amplitudeEntry = e2

    Label(top, text="Czas poczatkowy").grid(row=4)
    e3 = Entry(top, state=self.get_state(3))
    self.t1Entry=e3

    Label(top, text="Czas trwania").grid(row= 5)
    e4 = Entry(top, state=self.get_state(4))
    self.dEntry = e4

    Label(top, text="Okres podstawowy").grid(row= 6)
    e5 = Entry(top, state=self.get_state(5))
    self.TEntry = e5

    Label(top, text="Wspolczynnik wypelnienia").grid(row=7)
    e6 = Entry(top, state=self.get_state(6))
    self.KwEntry = e6

    # Label(top, text="Skok jednostkowy(ts)").grid(row= 7)
    # e7 = Entry(top, state=self.get_state(7))

    # Label(top, text="Nr pierwszej probki(n1)").grid(row= 8)
    # e8 = Entry(top, state=self.get_state(8))

    # Label(top, text="Skok dla probki nr (ns)").grid(row= 9)
    # e9 = Entry(top, state=self.get_state(9))

    Label(top, text="Czestotliwosc probkowania").grid(row= 10)
    e10 = Entry(top, state=self.get_state(10))
    self.sampFreqEntry = e10

    # Label(top, text="Prawdopodobienstwo(p)").grid(row= 11)
    # e11 = Entry(top, state=self.get_state(11))


    # e1 = Entry(top, state=self.get_state(1))

    e1.grid(row=2, column=1)
    e2.grid(row=3, column=1)
    e3.grid(row=4, column=1)
    e4.grid(row=5, column=1)
    e5.grid(row=6, column=1)
    e6.grid(row=7, column=1)
    # e7.grid(row=7, column=1)
    # e8.grid(row=8, column=1)
    # e9.grid(row=9, column=1)
    e10.grid(row=10, column=1)
    # e11.grid(row=11, column=1)
    Button(top, text='Dodaj', width=15, command=self.generate_signal).grid(row=15, column=1, sticky=W, pady=4)

    top.mainloop()

  def add_to_menu_grid(self, obj, label):
    self.signalsMap[label] = obj
    self.ListBoxReference.insert(END, label)

  def init_signal_action(self):

    OPTIONS = [
      "Dodaj",
      "Odejmij",
      "Pomnóz",
      "Podziel"
    ]

    listBoxOptions = list(self.ListBoxReference.get(0, END))
    if len(listBoxOptions) == 0:
      messagebox.showinfo("Uwaga", "Musisz dodać przynajmniej jedną funkcję")
      return
    top = Toplevel()

    Label(top, text="Pierwszy sygnał").grid(row=0, column=0)
    selected = StringVar(top)
    selected.set(listBoxOptions[0])
    w = OptionMenu(top, selected, *listBoxOptions)
    w.config(width=25)
    w.grid(column =1, row =0, sticky="ew")


    Label(top, text="Drugi sygnał").grid(row=1, column=0)
    selected2 = StringVar(top)
    selected2.set(listBoxOptions[0])
    w2= OptionMenu(top, selected2, *listBoxOptions)
    w2.config(width=25)
    w2.grid(column = 1, row = 1, sticky="ew")

    Label(top, text="Action type").grid(row=2, column=0)
    actionType = StringVar(top)
    actionType.set(OPTIONS[0])

    self.actionWindow = top
    self.actionType = actionType
    self.selectedSignalsForAction = [ selected, selected2 ]

    w3= OptionMenu(top, actionType, *OPTIONS)
    w3.config(width=25)
    w3.grid(column = 1, row = 2, sticky="ew")

    Button(top, text='Wykonaj', width=15, command=lambda: [self.signals_actions(), top.destroy()]).grid(row=4, column=1, sticky=W)

  def signals_actions(self):
    signal1Name = self.selectedSignalsForAction[0].get()
    signal2Name = self.selectedSignalsForAction[1].get()
    signal1 = self.signalsMap[signal1Name]
    signal2 = self.signalsMap[signal2Name]
    result = None
    label = ''
    if (self.actionType.get() == "Dodaj"):
      result = signal_operations.add_signals(signal1, signal2)
      label = signal1.name + "+" + signal2.name
    elif(self.actionType.get() == "Odejmij"):
      result = signal_operations.substract_signals(signal1, signal2)
      label = signal1.name + "-" + signal2.name
    elif(self.actionType.get() == "Pomnoz"):
      result = signal_operations.multiply_signals(signal1, signal2)
      label = signal1.name + "*" + signal2.name
    elif(self.actionType.get() == "Podziel"):
      result = signal_operations.divide_signals(signal1, signal2)
      label = signal1.name + "/" + signal2.name

    self.add_to_menu_grid(result, label)

  def generate_signal(self, signal=None):
    option = self.selectedFunction.get()
    if signal == None:
      if option == "szum gaussowski":
        signal = noise_generator.gaussian(name = self.nameEntry.get(), A= number_parser.parse(self.amplitudeEntry.get()), t1=number_parser.parse(self.t1Entry.get()), d=number_parser.parse(self.dEntry.get()), sampling_freq=number_parser.parse(self.sampFreqEntry.get()))
      elif option == "szum o rozkładzie jednostajnym":
        signal = noise_generator.uniform(name = self.nameEntry.get(), A= number_parser.parse(self.amplitudeEntry.get()), t1=number_parser.parse(self.t1Entry.get()), d=number_parser.parse(self.dEntry.get()), sampling_freq=number_parser.parse(self.sampFreqEntry.get()))
      elif option == "sinusoidalny":
        signal = sig_gen.sine(name = self.nameEntry.get(), A= number_parser.parse(self.amplitudeEntry.get()), T=number_parser.parse(self.TEntry.get()), t1=number_parser.parse(self.t1Entry.get()), d=number_parser.parse(self.dEntry.get()), sampling_freq=number_parser.parse(self.sampFreqEntry.get()))
      elif option == "sinusoidalny wyprostowany jednopołówkowo":
        signal = sig_gen.half_wave_rect_sine(name = self.nameEntry.get(), A=number_parser.parse(self.amplitudeEntry.get()), T=number_parser.parse(self.TEntry.get()), t1 = number_parser.parse(self.t1Entry.get()), d =number_parser.parse(self.dEntry.get()), sampling_freq=number_parser.parse(self.sampFreqEntry.get()))
      elif option == "sinusoidalny wyprostowany dwupołówkowo":
        signal = sig_gen.full_wave_rect_sine(name = self.nameEntry.get(), A=number_parser.parse(self.amplitudeEntry.get()), T=number_parser.parse(self.TEntry.get()), t1 = number_parser.parse(self.t1Entry.get()), d =number_parser.parse(self.dEntry.get()), sampling_freq=number_parser.parse(self.sampFreqEntry.get()))
      elif option == "prostokątny":
        signal = sig_gen.square(name = self.nameEntry.get(), A=number_parser.parse(self.amplitudeEntry.get()), T=number_parser.parse(self.TEntry.get()), kW=number_parser.parse(self.KwEntry.get()), t1 = number_parser.parse(self.t1Entry.get()), d =number_parser.parse(self.dEntry.get()), sampling_freq=number_parser.parse(self.sampFreqEntry.get()))
      elif option == "prostokątny symetryczny":
        signal = sig_gen.square_symmetrical(name = self.nameEntry.get(), A=number_parser.parse(self.amplitudeEntry.get()), T=number_parser.parse(self.TEntry.get()), kW=number_parser.parse(self.KwEntry.get()), t1 = number_parser.parse(self.t1Entry.get()), d =number_parser.parse(self.dEntry.get()), sampling_freq=number_parser.parse(self.sampFreqEntry.get()))
      elif option == "trójkątny":
        signal = sig_gen.triangular(name = self.nameEntry.get(), A=number_parser.parse(self.amplitudeEntry.get()), T=number_parser.parse(self.TEntry.get()), kW=number_parser.parse(self.KwEntry.get()), t1 = number_parser.parse(self.t1Entry.get()), d =number_parser.parse(self.dEntry.get()), sampling_freq=number_parser.parse(self.sampFreqEntry.get()))

    self.formWindow.destroy()
    self.add_to_menu_grid(signal, signal.name)
    self.draw_signal(signal)

  def draw_signal(self, signal, label = 'Signal'):
    if isinstance(signal, str):
      signal = self.signalsMap[signal]
    entries = plot_u.plot_signal(signal, label)
    self.set_top_pane_canvas(entries, 'signal')

  def draw_histogram(self, signal, label = 'Histogram'):
    if isinstance(signal, str):
      signal = self.signalsMap[signal]
    entries = plot_u.plot_histogram(signal, label)
    self.set_top_pane_canvas(entries, 'histogram')


  def delete_from_menu_grid(self):
    self.ListBoxReference.delete(ACTIVE)
    self.set_top_pane_canvas()

  def onselect(self, evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    self.draw_signal(self.signalsMap[self.ListBoxReference.get(index)])

  def get_state(self, labelNr):
    return NORMAL

  def serialize_signals(self):
    # signals = self.signalsMap.values()
    # for signal in signals:
    signal = self.signalsMap[self.ListBoxReference.get(ACTIVE)]
    signal_serializer.serialize_signal(signal, signal.name)

  def deserialize_signals(self):
    signals = signal_serializer.deserialize_signals()
    for signal in signals:
      self.add_to_menu_grid(signal, signal.name)



