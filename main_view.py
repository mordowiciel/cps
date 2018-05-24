# coding: utf-8

from Tkinter import *
import tkMessageBox

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

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
import sampling as sampling
import quantization as quantization

class BasicView:
  optionMenu = None
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
  tsEntry = None
  pEntry = None
  n1Entry = None
  nSEntry = None
  lEntry = None
  signalsMap = {}
  formWindow = None
  selectedFunction = None
  actionWindow = None
  otherActionWindow = None
  signalsActionType = None
  otherActionType = None
  samplingVal = None
  selectedSignalForOtherAction = None
  selectedSignalsForAction = []

  FUNC_OPTIONS = {
    1: "szum o rozkładzie jednostajnym",
    2: "szum gaussowski",
    3: "sinusoidalny",
    4: "sin. wyprostowany jednopołówkowo",
    5: "sin. wyprostowany dwupołówkowo",
    6: "prostokątny",
    7: "prostokątny symetryczny",
    8: "trójkątny",
    9: "skok jednostkowy",
    10: "impuls jednostkowy",
    11: "szum impulsowy"
  }


  def __init__(self):
    self.init_basic_window()

  def init_basic_window(self):
    root = Tk()
    root.winfo_toplevel().title("Aplikacja do generowania sygnałów")
    self.init_menubar(root)
    self.init_menu_grid(root)
    root.mainloop()

  def init_menubar(self, parent):
    menubar = Menu(parent)
    optionsMenu = Menu(menubar, tearoff=0)
    optionsMenu.add_command(label="Dodaj sygnał", command=self.init_form_window)
    optionsMenu.add_command(label="Usuń sygnał", command=self.delete_from_menu_grid)

    optionsMenu.add_command(label="Eksportuj sygnał", command=self.serialize_signals)
    optionsMenu.add_command(label="Importuj sygnały", command=self.deserialize_signals)

    optionsMenu.add_separator()

    optionsMenu.add_command(label="Operacje mat. na sygnałach", command=self.init_signal_action)
    optionsMenu.add_command(label="Pozostałe", command=self.init_other_actions)

    optionsMenu.add_command(label="Wyjście", command=parent.quit)
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


  def init_other_actions(self):
    OPTIONS = [
      "Próbkowanie ZOH", "Próbkowanie FOH", "Interpolacja w oparciu o sinus",
      "Kwantyzacja", "Kwantyzacja z zaokr."
    ]

    listBoxOptions = list(self.ListBoxReference.get(0, END))
    top = Toplevel()

    Label(top, text="Sygnał").grid(row=0, column=0)
    selected = StringVar(top)
    selected.set(listBoxOptions[0])
    w = OptionMenu(top, selected, *listBoxOptions)
    w.config(width=25)
    w.grid(column =1, row =0, sticky="ew")

    Label(top, text="Działanie").grid(row=2, column=0)
    actionType = StringVar(top)
    actionType.set(OPTIONS[0])

    Label(top, text="Nazwa").grid(row=3, column=0)
    e1 = Entry(top)
    e1.grid(row=3, column=1)
    self.samplingVal = e1

    self.otherActionWindow = top
    self.otherActionType = actionType

    self.selectedSignalForOtherAction = selected

    w3= OptionMenu(top, actionType, *OPTIONS)
    w3.config(width=25)
    w3.grid(column = 1, row = 2, sticky="ew")

    Button(top, text='Wykonaj', width=15, command=lambda: [self.signals_other_actions(), top.destroy()]).grid(row=4, column=1, sticky=W)


  def signals_other_actions(self):
    signalName = self.selectedSignalForOtherAction.get()
    signal = self.signalsMap[signalName]
    sampling_val = int(self.samplingVal.get())
    result = None
    label = ''
    action = self.otherActionType.get()

    if(action == u"Próbkowanie ZOH"):
      sampled_signal = sampling.sample_signal(signal, sampling_val)
      result = sampling.zero_order_hold(sampled_signal, signal.t_values)
      label = 'ZOH_' + signalName
    elif(action == u"Próbkowanie FOH"):
      sampled_signal = sampling.sample_signal(signal, sampling_val)
      result = sampling.first_order_hold(sampled_signal, signal.t_values)
      label = 'FOH_' + signalName
    elif(action == u"Interpolacja w oparciu o sinus"):
      sampled_signal = sampling.sample_signal(signal, sampling_val)
      result = sampling.sinc_interpolation(sampled_signal, signal.t_values)
      label = 'interpolacja_sin_' + signalName
    elif(action == u"Kwantyzacja"):
      result = quantization.quantize_signal(signal)
      label = "kwant_" + signalName
    elif(action == u"Kwantyzacja z zaokr."):
      result = round_quantize_signal(signal)
      label = "kwant_" + signalName
      label = "kwant_zaokr_" + signalName

    self.add_to_menu_grid(result, label)

  def set_top_pane_canvas(self, entries = None, canvasType = None, discret=False):
    top = self.TopPaneReference
    for child in top.winfo_children():
      child.destroy()

    if (entries != None):
      buttonsFrame = Frame(top)
      buttonsFrame.pack(side='top')
      Button(buttonsFrame, text="Pokaż wykres", command=self.show_current_function_plot).pack(side="left")
      Button(buttonsFrame, text="Pokaż histogram", command=self.show_current_function_histogram).pack(side="left")
      statsFrame = Frame(top)
      statsFrame.pack(side='top')
      if(canvasType == 'signal'):
        avg = round(signal_utils.calculate_average(int(entries[0][0]), int(entries[0][-1]), entries[1]), 3)
        avg_abs = round(signal_utils.calculate_abs_average(int(entries[0][0]), int(entries[0][-1]), entries[1]),3)
        avg_power = round(signal_utils.calculate_avg_power(int(entries[0][0]), int(entries[0][-1]), entries[1]), 3)
        variance = round(signal_utils.calculate_variance(int(entries[0][0]), int(entries[0][-1]), entries[1]),3)
        root_mean_sq = round(signal_utils.calculate_root_mean_square(int(entries[0][0]), int(entries[0][-1]), entries[1]),3)

        Label(statsFrame, text="Wartość średnia: {0}".format(avg).replace(")", "").replace("(", "").replace("+0j", "")).grid(row=1)
        Label(statsFrame, text="Wartość średnia bezwzględna: {0}".format(avg_abs).replace(")", "").replace("(", "").replace("+0j", "")).grid(row=2)
        Label(statsFrame, text="Wartość skuteczna: {0}".format(root_mean_sq).replace(")", "").replace("(", "").replace("+0j", "")).grid(row=3)
        Label(statsFrame, text="Wariancja: {0}".format(variance).replace(")", "").replace("(", "").replace("+0j", "")).grid(row=4)
        Label(statsFrame, text="Moc średnia: {0}".format(avg_power).replace(")", "").replace("(", "").replace("+0j", "")).grid(row=5)

    f = Figure(figsize=(5,5), dpi=100)
    canvas = FigureCanvasTkAgg(f,  top)
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
    canvas.show()

    if (entries != None):
      a = f.add_subplot(111)

      if (canvasType == 'signal'):
        a.set_xlabel('czas (t)')
        a.set_ylabel(u'wartość (y)')
        a.grid(color='b', linestyle='-', linewidth=0.1)
        a.scatter(entries[0], entries[1]) if discret == True else a.plot(entries[0], entries[1])

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
    w = OptionMenu(top, self.selectedFunction, *self.FUNC_OPTIONS.values(), command=self.init_labels)
    w.config(width=25)
    w.grid(column=1, row =0, sticky="ew")
    self.optionMenu = w

    self.init_labels(None)
    top.mainloop()

  def init_labels(self, values):
    option = self.selectedFunction.get()
    option = option.encode('ascii', 'ignore')
    options = {
      "szum o rozkadzie jednostajnym":[1,2,3,4,10],
      "szum gaussowski": [1,2,3,4,10],
      "sinusoidalny":  [1,2,3,4,5,10],
      "sin. wyprostowany jednopowkowo":  [1,2,3,4,5,10],
      "sin. wyprostowany dwupowkowo":  [1,2,3,4,5,10],
      "prostoktny":  [1,2,3,4,5,10,6],
      "prostoktny symetryczny":  [1,2,3,4,5,10,6],
      "trjktny":  [1,2,3,4,5,10,6],
      "skok jednostkowy": [1,2,3,4,7,10],
      "impuls jednostkowy": [1,2,4,10,8,9,5],
      "szum impulsowy": [1,2,3,4,10,11]
    }

    top = self.formWindow
    for child in top.winfo_children():
      if (child != self.optionMenu):
        child.destroy()
    row_number = 2

    Label(top, text="Typ funkcji").grid(row= 0)
    Label(top, text="Nazwa").grid(row=row_number)
    e1 = Entry(top, state=self.get_state(1))
    self.nameEntry = e1
    e1.grid(row=row_number, column=1)
    row_number += 1

    if (2 in options[unicode(option)]):
      Label(top, text="Amplituda").grid(row=row_number)
      e2 = Entry(top, state=self.get_state(2))
      self.amplitudeEntry = e2
      e2.grid(row=row_number, column=1)
      row_number += 1

    if (3 in options[unicode(option)]):
      Label(top, text="Czas początkowy").grid(row=row_number)
      e3 = Entry(top, state=self.get_state(3))
      self.t1Entry=e3
      e3.grid(row=row_number, column=1)
      row_number += 1


    if (4 in options[unicode(option)]):
      Label(top, text="Czas trwania").grid(row= row_number)
      e4 = Entry(top, state=self.get_state(4))
      self.dEntry = e4
      e4.grid(row=row_number, column=1)
      row_number += 1



    if (5 in options[unicode(option)]):
      Label(top, text="Okres podstawowy").grid(row= row_number)
      e5 = Entry(top, state=self.get_state(5))
      self.TEntry = e5
      e5.grid(row=row_number, column=1)
      row_number += 1


    if (6 in options[unicode(option)]):
      Label(top, text="Współczynnik wypełnienia").grid(row=row_number)
      e6 = Entry(top, state=self.get_state(6))
      self.KwEntry = e6
      e6.grid(row=row_number, column=1)
      row_number += 1


    if (7 in options[unicode(option)]):
      Label(top, text="Skok jednostkowy").grid(row= row_number)
      e7 = Entry(top, state=self.get_state(7))
      self.tsEntry = e7
      e7.grid(row=row_number, column=1)
      row_number += 1


    if (8 in options[unicode(option)]):
      Label(top, text="Nr pierwszej próbki").grid(row= row_number)
      e8 = Entry(top, state=self.get_state(8))
      self.n1Entry = e8
      e8.grid(row=row_number, column=1)
      row_number += 1


    if (9 in options[unicode(option)]):
      Label(top, text="Skok dla próbki").grid(row=row_number)
      e9 = Entry(top, state=self.get_state(9))
      self.nSEntry = e9
      e9.grid(row=row_number, column=1)
      row_number += 1


    if (10 in options[unicode(option)]):
      Label(top, text="Częstotliwość próbkowania").grid(row= row_number)
      e10 = Entry(top, state=self.get_state(10))
      self.sampFreqEntry = e10
      e10.grid(row=row_number, column=1)
      row_number += 1


    if (11 in options[unicode(option)]):
      Label(top, text="Prawdopodobieństwo").grid(row= row_number)
      e11 = Entry(top, state=self.get_state(11))
      self.pEntry = e11
      e11.grid(row=row_number, column=1)
      row_number += 1

    Button(top, text='Dodaj', width=15, command=self.generate_signal).grid(row=row_number + 2, column=1, sticky=W, pady=4)

  def add_to_menu_grid(self, obj, label):

    self.signalsMap[label] = obj
    self.ListBoxReference.insert(END, label)

  def init_signal_action(self):

    OPTIONS = [
      "Dodaj",
      "Odejmij",
      "Pomnóż",
      "Podziel"
    ]

    listBoxOptions = list(self.ListBoxReference.get(0, END))
    if len(listBoxOptions) == 0:
      messagebox.showinfo("Uwaga", "Musisz dodać przynajmniej jeden sygnał")
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

    Label(top, text="Działanie").grid(row=2, column=0)
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
    elif(self.actionType.get() == u"Pomnóż"):
      result = signal_operations.multiply_signals(signal1, signal2)
      label = signal1.name + "*" + signal2.name
    elif(self.actionType.get() == "Podziel"):
      result = signal_operations.divide_signals(signal1, signal2)
      label = signal1.name + "/" + signal2.name

    self.add_to_menu_grid(result, label)

  def generate_signal(self, signal=None):
    option = self.selectedFunction.get()
    option = option.encode('ascii', 'ignore')
    if signal == None:
      if option == "szum gaussowski":
        signal = noise_generator.gaussian(name = self.nameEntry.get(), A= number_parser.parse(self.amplitudeEntry.get()), t1=number_parser.parse(self.t1Entry.get()), d=number_parser.parse(self.dEntry.get()), sampling_freq=number_parser.parse(self.sampFreqEntry.get()))
      elif option == "szum o rozkadzie jednostajnym":
        signal = noise_generator.uniform(name = self.nameEntry.get(), A= number_parser.parse(self.amplitudeEntry.get()), t1=number_parser.parse(self.t1Entry.get()), d=number_parser.parse(self.dEntry.get()), sampling_freq=number_parser.parse(self.sampFreqEntry.get()))
      elif option == "sinusoidalny":
        signal = sig_gen.sine(name = self.nameEntry.get(), A= number_parser.parse(self.amplitudeEntry.get()), T=number_parser.parse(self.TEntry.get()), t1=number_parser.parse(self.t1Entry.get()), d=number_parser.parse(self.dEntry.get()), sampling_freq=number_parser.parse(self.sampFreqEntry.get()))
      elif option == "sin. wyprostowany jednopowkowo":
        signal = sig_gen.half_wave_rect_sine(name = self.nameEntry.get(), A=number_parser.parse(self.amplitudeEntry.get()), T=number_parser.parse(self.TEntry.get()), t1 = number_parser.parse(self.t1Entry.get()), d =number_parser.parse(self.dEntry.get()), sampling_freq=number_parser.parse(self.sampFreqEntry.get()))
      elif option == "sin. wyprostowany dwupowkowo":
        signal = sig_gen.full_wave_rect_sine(name = self.nameEntry.get(), A=number_parser.parse(self.amplitudeEntry.get()), T=number_parser.parse(self.TEntry.get()), t1 = number_parser.parse(self.t1Entry.get()), d =number_parser.parse(self.dEntry.get()), sampling_freq=number_parser.parse(self.sampFreqEntry.get()))
      elif option == "prostoktny":
        signal = sig_gen.square(name = self.nameEntry.get(), A=number_parser.parse(self.amplitudeEntry.get()), T=number_parser.parse(self.TEntry.get()), kW=number_parser.parse(self.KwEntry.get()), t1 = number_parser.parse(self.t1Entry.get()), d =number_parser.parse(self.dEntry.get()), sampling_freq=number_parser.parse(self.sampFreqEntry.get()))
      elif option == "prostoktny symetryczny":
        signal = sig_gen.square_symmetrical(name = self.nameEntry.get(), A=number_parser.parse(self.amplitudeEntry.get()), T=number_parser.parse(self.TEntry.get()), kW=number_parser.parse(self.KwEntry.get()), t1 = number_parser.parse(self.t1Entry.get()), d =number_parser.parse(self.dEntry.get()), sampling_freq=number_parser.parse(self.sampFreqEntry.get()))
      elif option == "trójktny":
        signal = sig_gen.triangular(name = self.nameEntry.get(), A=number_parser.parse(self.amplitudeEntry.get()), T=number_parser.parse(self.TEntry.get()), kW=number_parser.parse(self.KwEntry.get()), t1 = number_parser.parse(self.t1Entry.get()), d =number_parser.parse(self.dEntry.get()), sampling_freq=number_parser.parse(self.sampFreqEntry.get()))
      elif option == "skok jednostkowy":
        signal = sig_gen.step_function(name = self.nameEntry.get(), A=number_parser.parse(self.amplitudeEntry.get()), t1 = number_parser.parse(self.t1Entry.get()), d =number_parser.parse(self.dEntry.get()), sampling_freq=number_parser.parse(self.sampFreqEntry.get()), tS=number_parser.parse(self.tsEntry.get()))
      elif option == "impuls jednostkowy":
        signal = sig_gen.kronecker(name = self.nameEntry.get(), A=number_parser.parse(self.amplitudeEntry.get()), nS=number_parser.parse(self.nSEntry.get()), n1=number_parser.parse(self.n1Entry.get()), l=number_parser.parse(self.dEntry.get()), sampling_freq=number_parser.parse(self.sampFreqEntry.get()))
      elif option == "szum impulsowy":
        signal = noise_generator.impulse(name = self.nameEntry.get(), A= number_parser.parse(self.amplitudeEntry.get()), t1=number_parser.parse(self.t1Entry.get()), d=number_parser.parse(self.dEntry.get()), sampling_freq=number_parser.parse(self.sampFreqEntry.get()), p=number_parser.parse(self.pEntry.get()))

    self.formWindow.destroy()
    self.add_to_menu_grid(signal, signal.name)
    self.draw_signal(signal)

  def draw_signal(self, signal, label = 'Signal'):
    if isinstance(signal, str):
      signal = self.signalsMap[signal]
    # entries = plot_u.plot_signal(signal, label)
    entries = [signal.t_values, signal.values]
    self.set_top_pane_canvas(entries, 'signal', signal.discret)

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

  def serialize_signals(self):
    # signals = self.signalsMap.values()
    # for signal in signals:
    signal = self.signalsMap[self.ListBoxReference.get(ACTIVE)]
    signal_serializer.serialize_signal(signal, signal.name)

  def deserialize_signals(self):
    signals = signal_serializer.deserialize_signals()
    for signal in signals:
      self.add_to_menu_grid(signal, signal.name)

  def get_state(self, labelNr):
    return NORMAL
