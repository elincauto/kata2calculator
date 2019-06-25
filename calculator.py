from tkinter import *
from tkinter import ttk

_heightBtn = 50
_widthBtn = 68

class CalcDisplay(ttk.Frame):

    _value=0

    def __init__(self, parent, **kwargs):
        
        ttk.Frame.__init__(self, parent, height=_heightBtn, width=_widthBtn*4)

        self.pack_propagate(0)

        s = ttk.Style()
        s.theme_use('alt')
        s.configure('my.TLabel', font="Helvetica 42")

        self.lblDisplay = ttk.Label(self, text=self._value, style='my.TLabel', anchor=E, foreground="white",background="black")
        self.lblDisplay.pack(fill=BOTH, expand=True)
    
    def addDigit(self, digito):
        if len(self._value)==10:
            return    

        if self._value =="0":
            self._value= digito
        else:
            self._value += digito

        self.pintar()


    def pintar(self):
        self.lblDisplay.configure(text=self._value)

    def reset(self):
        self._value="0"
        self.pintar()
    
    def signo(self):

        if self._value =="0":
            return

        if self._espositivo:
            self._value="-"+self._value
            
        else:
            self._value=self._value[1:]
        
        self._espositivo= not self._espositivo

        self.pintar()


class CalcButton(ttk.Frame):
    def __init__(self, parent, **kwargs):
        '''
        if 'bw' in kwargs:
            bw = kwargs['bw']
        else:
            bw = 1
        '''
        bw = kwargs['bw'] if 'bw' in kwargs else 1

        ttk.Frame.__init__(self, parent, height=_heightBtn, width=_widthBtn * bw)
        self.pack_propagate(0) #(los componentes hijos no controlan su tamaño)

        self.button = ttk.Button(self, text=kwargs['text'], command=kwargs['command'])
        self.button.pack(fill=BOTH, expand=True)


class Calculator(ttk.Frame):
    _op1=None
    _op2=None
    _operador= None


    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, height=kwargs['height'], width=kwargs['width'])
        self.display = CalcDisplay(self)
        self.display.grid(column=0, row=0, columnspan=4)
        CalcButton(self, text='C', command=self.display.reset).grid(column=0, row=1)
        CalcButton(self, text='+/-', command=self.display.signo).grid(column=1, row=1)
        CalcButton(self, text='%', command=None).grid(column=2, row=1)
        CalcButton(self, text='÷', command=None).grid(column=3, row=1)
        CalcButton(self, text='7', command=lambda: self.display.addDigit('7')).grid(column=0, row=2)
        CalcButton(self, text='8', command=lambda: self.display.addDigit('8')).grid(column=1, row=2)
        CalcButton(self, text='9', command=lambda: self.display.addDigit('9')).grid(column=2, row=2)
        CalcButton(self, text='x', command=None).grid(column=3, row=2)
        CalcButton(self, text='4', command=lambda: self.display.addDigit('4')).grid(column=0, row=3)
        CalcButton(self, text='5', command=lambda: self.display.addDigit('5')).grid(column=1, row=3)
        CalcButton(self, text='6', command=lambda: self.display.addDigit('6')).grid(column=2, row=3)
        CalcButton(self, text='-', command=None).grid(column=3, row=3)
        CalcButton(self, text='1', command=lambda: self.display.addDigit('1')).grid(column=0, row=4)
        CalcButton(self, text='2', command=lambda: self.display.addDigit('2')).grid(column=1, row=4)
        CalcButton(self, text='3', command=lambda: self.display.addDigit('3')).grid(column=2, row=4)
        CalcButton(self, text='+', command=None).grid(column=3, row=4)
        CalcButton(self, text='0', command=lambda: self.display.pintar('0'), bw=2).grid(column=0, row=5, columnspan=2)
        CalcButton(self, text=",", command=None).grid(column=2, row=5)
        CalcButton(self, text="=", command=None).grid(column=3, row=5)
    
    def opera(self,_operador):
        if self._op1 is None:
            self._op1 = self.display._value
            self._operador=_operador
            self.display.reset()
        else:
            self._op2


    def enviar(self, value):
        self.display.pintar(value)




class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calculator")
        self.geometry("{}x{}".format(_widthBtn*4, _heightBtn*6))

        self.calculator = Calculator(self, height=_heightBtn*6, width=_widthBtn*4)
        self.calculator.place(x=0, y=0)

    def start(self):
        self.mainloop()


if __name__ == '__main__':
    app = MainApp()
    app.start()