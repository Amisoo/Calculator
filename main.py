import customtkinter as ct
import sympy as sp

"""
- Ecran en haut qui affiche ce qu'on calcule est resultat
- bouton des chiffres
- bouton virgule
- bouton opération (+ - * /)
- bouton egal -> affiche le résultat

A faire : 
     ln(x)
     e(x)
     sin(x)
     cos(x)
     tan(x)

"""


class Calculator:
    def button_number(self, num):
        self.get_text(f"{num}")

        if self.state == 0:
            self.first_number += num * (10 ** self.num_state)
            self.num_state += 1
        else:
            self.second_number += num * (10 ** self.num_state)
            self.num_state += 1

    def set_comma(self):
        if self.state_comma:
            self.get_text(".")
            self.state_comma = False
        else:
            return
        if self.state == 0:
            self.comma_count1 = self.num_state

        else:
            self.comma_count2 = self.num_state


    def plus(self):
        self.erase()
        self.state = 1

    def minus(self):
        self.state = 2
        self.erase()

    def mult(self):
        self.erase()
        self.state = 3

    def div(self):
        self.erase()
        self.state = 4

    def sqrt(self):
        self.erase()
        self.state = 5

    def power(self):
        self.erase()
        self.state = 6

    def ln(self):
        self.erase()
        self.state = 7

    def exp(self):
        self.erase()
        self.state = 8

    def sin(self):
        self.erase()
        self.state = 9

    def cos(self):
        self.erase()
        self.state = 10

    def tan(self):
        self.erase()
        self.state = 11

    def change_sign(self):
        if self.state_sign:
            self.get_text("-")
            self.state_sign = False

        elif not self.state_sign:
            self.screen.delete(0, 1)
            self.state_sign = True

        if self.state == 0:
            self.first_number *= -1
        else:
            self.second_number *= -1

    def equal(self):
        self.erase()

        self.first_number = self.first_number / (10 ** self.comma_count1)
        self.second_number = self.second_number / (10 ** self.comma_count2)

        # rien
        if self.state == 0:
            self.result = self.first_number

        if self.state == 1:
            self.result = self.first_number + self.second_number

        elif self.state == 2:
            self.result = self.first_number - self.second_number

        elif self.state == 3:
            self.result = self.first_number * self.second_number

        elif self.state == 4:
            self.result = self.first_number / self.second_number
        elif self.state == 5:
            self.result = sp.root(self.first_number, self.second_number)
        elif self.state == 6:
            self.result = self.first_number ** self.second_number
        elif self.state == 7:
            self.result = sp.ln(self.first_number)
        elif self.state == 8:
            self.result = sp.exp(self.first_number)
        elif self.state == 9:
            self.result = sp.sin(self.first_number)
        elif self.state == 10:
            self.result = sp.cos(self.first_number)
        elif self.state == 11:
            self.result = sp.tan(self.first_number)

        self.get_text(self.result)
        self.state = 0

    def clear(self):
        self.second_number = 0
        self.first_number = 0
        self.state = 0
        self.erase()

    def erase(self):
        self.screen.delete(0, ct.END)
        self.num_state = 0
        self.state_comma = True

    def get_text(self, caractere):
        self.screen.insert(0, caractere)

    def __init__(self):
        # svaoir si on a min commma en state 0 ou else
        self.comma_count1 = 0
        self.comma_count2 = 0

        self.state_comma = True
        self.state_sign = True

        # first/ second number :
        self.num_state = 0
        self.first_number = 0
        self.second_number = 0
        self.result = 0

        self.state = 0

        # text in screen :
        self.text = ""
        # sert pour écrire en joli
        self.X = sp.symbols('x')
        self.Y = sp.symbols('y')

        self.padding_button = 5
        self.padding_frame = 10

        self.width_number = 90
        self.height_number = 90

        self.width_operation = 100
        self.height_operation = 110
        self.font_size = 27
        self.fgcolor_number = r"#3b3b3b"
        self.fgcolor_operation = r"#323232"
        self.back_color = r"#202020"

        self.root = ct.CTk()
        self.root.geometry("580x800")
        self.root.minsize(360, 480)
        self.root.title("Calculator")
        self.root.configure(background='#272727', fg_color=self.back_color)
        self.root.resizable(False, False)

        self.screen_frame = ct.CTkFrame(master=self.root,
                                        height=300,
                                        width=440,
                                        fg_color=self.back_color
                                        )
        self.screen_frame.grid(row=0, column=0, padx=(self.padding_frame, self.padding_frame),
                               pady=(self.padding_frame, self.padding_frame),
                               sticky="nsew"
                               )
        self.screen = ct.CTkEntry(master=self.screen_frame,
                                  corner_radius=20,
                                  width=475,
                                  height=150,
                                  font=("roboto", 40)
                                  )
        self.screen.pack(expand=True, pady=15)

        self.frame = ct.CTkFrame(master=self.root,
                                 bg_color=self.back_color,
                                 fg_color=self.back_color
                                 )
        self.frame.grid(row=1, column=0, padx=(self.padding_frame, self.padding_frame),
                        pady=(self.padding_frame, self.padding_frame),
                        sticky="ns")

        # Creation des buttons de nombres
        self.i = 0
        while self.i < 9:
            button = ct.CTkButton(
                master=self.frame,
                width=self.width_number,
                height=self.height_number,
                text=str(9 - self.i),
                font=("Roboto", self.font_size),
                command=lambda num=9 - self.i: self.button_number(num),
                fg_color=self.fgcolor_number
            )
            button.grid(row=self.i // 3 + 2, column=2 - self.i % 3)
            self.i += 1

        self.button_sign_label = ct.CTkButton(master=self.frame,
                                              width=self.width_number,
                                              height=self.height_number,
                                              text="+/-",
                                              font=("Roboto", self.font_size),
                                              command=self.change_sign,
                                              fg_color=self.fgcolor_number
                                              ).grid(row=5, column=0,
                                                     padx=(self.padding_button, self.padding_button),
                                                     pady=(self.padding_button, self.padding_button),
                                                     sticky="ns"
                                                     )
        self.button_0_label = ct.CTkButton(master=self.frame,
                                           width=self.width_number,
                                           height=self.height_number,
                                           text="0",
                                           font=("Roboto", self.font_size),
                                           command=lambda num=0: self.button_number(num),
                                           fg_color=self.fgcolor_number
                                           ).grid(row=5, column=1,
                                                  padx=(self.padding_button, self.padding_button),
                                                  pady=(self.padding_button, self.padding_button),
                                                  sticky="ns"
                                                  )
        self.button_comma_label = ct.CTkButton(master=self.frame,
                                               width=self.width_number,
                                               height=self.width_operation,
                                               text=".",
                                               font=("Roboto", self.font_size),
                                               command=self.set_comma,
                                               fg_color=self.fgcolor_number
                                               ).grid(row=5, column=2,
                                                      padx=(self.padding_button, self.padding_button),
                                                      pady=(self.padding_button, self.padding_button),
                                                      sticky="ns"
                                                      )

        self.button_erase_label = ct.CTkButton(master=self.frame,
                                               width=self.width_operation,
                                               height=self.width_operation,
                                               text="c",
                                               font=("Roboto", self.font_size),
                                               command=self.clear,
                                               fg_color=self.fgcolor_operation
                                               ).grid(row=1, column=0,
                                                      padx=(self.padding_button, self.padding_button),
                                                      pady=(self.padding_button, self.padding_button),
                                                      sticky="ns"
                                                      )

        self.expression = self.X ** self.Y
        self.expression = sp.pretty(self.expression, use_unicode=True)
        self.button_power_label = ct.CTkButton(master=self.frame,
                                               width=self.width_operation,
                                               height=self.width_operation,
                                               text="x^y",
                                               font=("Roboto", self.font_size),
                                               command=self.power,
                                               fg_color=self.fgcolor_operation
                                               ).grid(row=1, column=1,
                                                      padx=(self.padding_button, self.padding_button),
                                                      pady=(self.padding_button, self.padding_button),
                                                      sticky="ns"
                                                      )

        self.expression_sqrt = self.X ** (1/self.Y)
        self.expression_sqrt = sp.pretty(self.expression_sqrt, use_unicode=True)

        self.button_sqrt_label = ct.CTkButton(master=self.frame,
                                              width=self.width_operation,
                                              height=self.width_operation,
                                              text=self.expression_sqrt,
                                              font=("Roboto", self.font_size -15),
                                              command=self.sqrt,
                                              fg_color=self.fgcolor_operation
                                              ).grid(row=1, column=2,
                                                     padx=(self.padding_button, self.padding_button),
                                                     pady=(self.padding_button, self.padding_button),
                                                     sticky="ns"
                                                     )
        self.button_div_label = ct.CTkButton(master=self.frame,
                                             width=self.width_operation,
                                             height=self.width_operation,
                                             text="÷",
                                             font=("Roboto", self.font_size),
                                             command=self.div,
                                             fg_color=self.fgcolor_operation
                                             ).grid(row=1, column=4,
                                                    padx=(self.padding_button, self.padding_button),
                                                    pady=(self.padding_button, self.padding_button),
                                                    sticky="ns"
                                                    )
        self.button_mult_label = ct.CTkButton(master=self.frame,
                                              width=self.width_operation,
                                              height=self.width_operation,
                                              text="×",
                                              font=("Roboto", self.font_size),
                                              command=self.mult,
                                              fg_color=self.fgcolor_operation
                                              ).grid(row=2, column=4,
                                                     padx=(self.padding_button, self.padding_button),
                                                     pady=(self.padding_button, self.padding_button),
                                                     sticky="ns"
                                                     )
        self.button_minus_label = ct.CTkButton(master=self.frame,
                                               width=self.width_operation,
                                               height=self.width_operation,
                                               text="-",
                                               font=("Roboto", self.font_size),
                                               command=self.minus,
                                               fg_color=self.fgcolor_operation
                                               ).grid(row=3, column=4,
                                                      padx=(self.padding_button, self.padding_button),
                                                      pady=(self.padding_button, self.padding_button),
                                                      sticky="ns"
                                                      )
        self.button_plus_label = ct.CTkButton(master=self.frame,
                                              width=self.width_operation,
                                              height=self.width_operation,
                                              text="+",
                                              font=("Roboto", self.font_size),
                                              command=self.plus,
                                              fg_color=self.fgcolor_operation
                                              ).grid(row=4, column=4,
                                                     padx=(self.padding_button, self.padding_button),
                                                     pady=(self.padding_button, self.padding_button),
                                                     sticky="ns"
                                                     )
        self.button_equal_label = ct.CTkButton(master=self.frame,
                                               width=self.width_operation,
                                               height=self.width_operation,
                                               text="=",
                                               font=("Roboto", self.font_size),
                                               command=self.equal,
                                               fg_color="#848381"
                                               ).grid(row=5, column=4,
                                                      padx=(self.padding_button, self.padding_button),
                                                      pady=(self.padding_button, self.padding_button),
                                                      sticky="ns"
                                                      )
        self.button_equal_label = ct.CTkButton(master=self.frame,
                                               width=self.width_operation,
                                               height=self.width_operation,
                                               text="ln(x)",
                                               font=("Roboto", self.font_size -5),
                                               command=self.ln,
                                               fg_color=self.fgcolor_operation
                                               ).grid(row=1, column=3,
                                                      padx=(self.padding_button, self.padding_button),
                                                      pady=(self.padding_button, self.padding_button),
                                                      sticky="ns"
                                                      )
        self.button_equal_label = ct.CTkButton(master=self.frame,
                                               width=self.width_operation,
                                               height=self.width_operation,
                                               text="exp(x)",
                                               font=("Roboto", self.font_size -5),
                                               command=self.exp,
                                               fg_color=self.fgcolor_operation
                                               ).grid(row=2, column=3,
                                                      padx=(self.padding_button, self.padding_button),
                                                      pady=(self.padding_button, self.padding_button),
                                                      sticky="ns"
                                                      )
        self.button_equal_label = ct.CTkButton(master=self.frame,
                                               width=self.width_operation,
                                               height=self.width_operation,
                                               text="sin(x)",
                                               font=("Roboto", self.font_size -5),
                                               command=self.sin,
                                               fg_color=self.fgcolor_operation
                                               ).grid(row=3, column=3,
                                                      padx=(self.padding_button, self.padding_button),
                                                      pady=(self.padding_button, self.padding_button),
                                                      sticky="ns"
                                                      )
        self.button_equal_label = ct.CTkButton(master=self.frame,
                                               width=self.width_operation,
                                               height=self.width_operation,
                                               text="cos(x)",
                                               font=("Roboto", self.font_size -5),
                                               command=self.cos,
                                               fg_color=self.fgcolor_operation
                                               ).grid(row=4, column=3,
                                                      padx=(self.padding_button, self.padding_button),
                                                      pady=(self.padding_button, self.padding_button),
                                                      sticky="ns"
                                                      )
        self.button_equal_label = ct.CTkButton(master=self.frame,
                                               width=self.width_operation,
                                               height=self.width_operation,
                                               text="tan(x)",
                                               font=("Roboto", self.font_size -5),
                                               command=self.tan,
                                               fg_color=self.fgcolor_operation
                                               ).grid(row=5, column=3,
                                                      padx=(self.padding_button, self.padding_button),
                                                      pady=(self.padding_button, self.padding_button),
                                                      sticky="ns"
                                                      )

        self.root.mainloop()


if __name__ == "__main__":
    Calculator()

