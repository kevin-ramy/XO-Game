from tkinter import *
from tkinter import messagebox

opening_window=Tk()
opening_window.title=("opening the game")
opening_window.config(bg=("#e5fa05"))
opening_window.geometry=("6000x600+600+600")

ready_label=Label(opening_window,text="are you ready to start",bg="red",padx=5,pady=5,font=("Arial",30,"bold"))
ready_label.place(x=200,y=200)

ready_btn=Button(opening_window,text="Yes",font=("Arial",30,"bold"),
                 bg="red",fg="black",command=lambda :(ready_start()))
ready_btn.place(x=200,y=300)

not_ready_btn=Button(opening_window,text="No",font=("Arial",30,"bold"),
                     bg="red",fg="black",command=lambda :(not_ready()))
not_ready_btn.place(x=500,y=300)

def ready_start ():
    level=Label(opening_window,text="choose your level",bg="red",padx=5,pady=5,font=("Arial",30,"bold"))
    level.place(x=800,y=200)

    easy_btn=Button(opening_window,text="easy",
                    bg="red",padx=5,pady=5,font=("Arial",30,"bold"),command=lambda :st_question())
    easy_btn.place(x=800,y=300)

    middle_btn=Button(opening_window,text="middle",
                    bg="red",padx=5,pady=5,font=("Arial",30,"bold"),command=lambda :st_question())
    middle_btn.place(x=800,y=400)

    hard_btn=Button(opening_window,text="hard",
                    bg="red",padx=5,pady=5,font=("Arial",30,"bold"),command=lambda :st_question())
    hard_btn.place(x=800,y=500)


def not_ready ():
    opening_window.destroy()

def next_st():
    nd_question()

def next_nd():
    rd_question()

def next_rd():
    forth_question()

def next_forth():
    fifth_question()

def next_fifth():
    sixth_question()

def next_sixth():
    sixth_question()

def next_seventh():
    eighth_question()

def previous_nd():
    st_question()

def previous_rd():
    nd_question()

def previous_forth():
    rd_question()

def previous_fifth():
    forth_question()

def previous_sixth():
    fifth_question()

def previous_seventh():
    sixth_question()

def previous_eighth():
    seventh_question()

def true_st ():
    messagebox.showinfo("true","your answer is true")
    nd_question()

def false_st():
    messagebox.showinfo("false","your answer is false")
    st_question()

def true_nd ():
    messagebox.showinfo("true",",your answer is true")
    rd_question()

def false_nd():
    messagebox.showinfo("false","your answer is false")
    nd_question()

def true_rd ():
    messagebox.showinfo("true","your answer is true")
    forth_question()

def false_rd():
    messagebox.showinfo("false","your answer is false")
    rd_question()

def true_forth ():
    messagebox.showinfo("true","your answer is true")
    fifth_question()

def false_forth():
    messagebox.showinfo("false","your answer is false")
    forth_question()

def true_fifth ():
    messagebox.showinfo("true","your answer is true")
    sixth_question()

def false_fifth():
    messagebox.showinfo("false","your answer is false")
    fifth_question()

def true_sixth ():
    messagebox.showinfo("true","your answer is true")
    seventh_question()

def false_sixth():
    messagebox.showinfo("false","your answer is false")
    sixth_question()

def true_seventh ():
    messagebox.showinfo("true","your answer is true")
    eighth_question()

def false_seventh():
    messagebox.showinfo("false","your answer is false")
    seventh_question()

def true_eighth ():
    messagebox.showinfo("true","your answer is true")
    win()

def false_eighth():
    messagebox.showinfo("false","your answer is false")
    sixth_question()

def win ():
    win=Tk()
    win.title("st question")
    win.config(bg=("#0000ff"))
    win.geometry = ("600x600+600+600")

    you_win=Label(win,text="YOU WIN YOU WIN MILLION",font=("Arial",90),bg="red",padx=15,pady=15)
    you_win.place(x=200,y=200)

def st_question ():
    st_question=Tk()
    st_question.title("st question")
    st_question.config(bg=("#0000ff"))
    st_question.geometry = ("600x600+600+600")

    stq=Label(st_question,text="كم عدد الدول في افريقيا",bg="red",padx=5,pady=5,font=("Arial",30,"bold"))
    stq.place(x=600,y=200)

    a_choose=Button(st_question,text="a) 42",font=("Arial",30),bg="orange",command=lambda :(false_st()))
    a_choose.place(x=600,y=280)

    b_choose=Button(st_question,text="b) 56",font=("Arial",30),bg="orange",command=lambda :(false_st()))
    b_choose.place(x=800,y=280)

    c_choose=Button(st_question,text="c) 54",font=("Arial",30),bg="orange",command=lambda :(true_st()))
    c_choose.place(x=600,y=400)

    d_choose=Button(st_question,text="d) 50",font=("Arial",30),bg="orange",command=lambda :(false_st()))
    d_choose.place(x=800,y=400)

    next_btn=Button(st_question,text="next",font=("Arial",30),bg="green",command=lambda :(next_st()))
    next_btn.place(x=1200,y=700)

    ststl=Label(st_question,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ststl.place(x=10,y=10)

    stndl=Label(st_question,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    stndl.place(x=10,y=110)

    strdl=Label(st_question,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    strdl.place(x=10,y=210)

    stforthl=Label(st_question,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    stforthl.place(x=10,y=310)

    stfifthl=Label(st_question,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    stfifthl.place(x=10,y=410)

    stsixthl=Label(st_question,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    stsixthl.place(x=10,y=510)

    stseventhl=Label(st_question,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    stseventhl.place(x=10,y=610)

    steighthl=Label(st_question,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    steighthl.place(x=10,y=710)


def nd_question ():
    nd_question=Tk()
    nd_question.title("st question")
    nd_question.config(bg=("#0000ff"))
    nd_question.geometry = ("600x600+600+600")

    ndq=Label(nd_question,text="اين تقع الاولمبيات الحالية",bg="red",padx=5,pady=5,font=("Arial",30,"bold"))
    ndq.place(x=600,y=200)

    a_choose=Button(nd_question,text="a) LONDON",font=("Arial",30),bg="orange",command=lambda :(false_nd()))
    a_choose.place(x=550,y=280)

    b_choose=Button(nd_question,text="b) PARIS",font=("Arial",30),bg="orange",command=lambda :(true_nd()))
    b_choose.place(x=800,y=280)

    c_choose=Button(nd_question,text="c) TOKYO",font=("Arial",30),bg="orange",command=lambda :(false_nd()))
    c_choose.place(x=550,y=400)

    d_choose=Button(nd_question,text="d) ATHINA",font=("Arial",30),bg="orange",command=lambda :(false_nd()))
    d_choose.place(x=800,y=400)

    next_btn_nd=Button(nd_question,text="next",font=("Arial",30),bg="green",command=lambda :(next_nd()))
    next_btn_nd.place(x=1200,y=700)

    previous_btn_nd=Button(nd_question,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_nd()))
    previous_btn_nd.place(x=1300,y=700)

    ndstl=Label(nd_question,text="100 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    ndstl.place(x=10,y=10)

    ndndl=Label(nd_question,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndndl.place(x=10,y=110)

    ndrdl=Label(nd_question,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndrdl.place(x=10,y=210)

    ndforthl=Label(nd_question,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndforthl.place(x=10,y=310)

    ndfifthl=Label(nd_question,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndfifthl.place(x=10,y=410)

    ndsixthl=Label(nd_question,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndsixthl.place(x=10,y=510)

    ndseventhl=Label(nd_question,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndseventhl.place(x=10,y=610)

    ndeighthl=Label(nd_question,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndeighthl.place(x=10,y=710)

def rd_question():
    rd_question = Tk()
    rd_question.title("rd question")
    rd_question.config(bg=("#0000ff"))
    rd_question.geometry = ("600x600+600+600")

    rdq = Label(rd_question, text="567+324", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    rdq.place(x=600, y=200)

    a_choose = Button(rd_question, text="a) 891", font=("Arial", 30), bg="orange", command=lambda: (true_rd()))
    a_choose.place(x=600, y=280)

    b_choose = Button(rd_question, text="b) 892", font=("Arial", 30), bg="orange", command=lambda: (false_rd()))
    b_choose.place(x=800, y=280)

    c_choose = Button(rd_question, text="c) 893", font=("Arial", 30), bg="orange", command=lambda: (false_rd()))
    c_choose.place(x=600, y=400)

    d_choose = Button(rd_question, text="d) 894", font=("Arial", 30), bg="orange", command=lambda: (false_rd()))
    d_choose.place(x=800, y=400)

    next_btn_nd=Button(rd_question,text="next",font=("Arial",30),bg="green",command=lambda :(next_rd()))
    next_btn_nd.place(x=1200,y=700)

    previous_btn_nd=Button(rd_question,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_rd()))
    previous_btn_nd.place(x=1300,y=700)

    rdstl=Label(rd_question,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdstl.place(x=10,y=10)

    rdndl=Label(rd_question,text="500 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    rdndl.place(x=10,y=110)

    rdrdl=Label(rd_question,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdrdl.place(x=10,y=210)

    rdforthl=Label(rd_question,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdforthl.place(x=10,y=310)

    rdfifthl=Label(rd_question,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdfifthl.place(x=10,y=410)

    rdsixthl=Label(rd_question,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdsixthl.place(x=10,y=510)

    rdseventhl=Label(rd_question,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdseventhl.place(x=10,y=610)

    rdeighthl=Label(rd_question,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdeighthl.place(x=10,y=710)


def forth_question():
    forth_question = Tk()
    forth_question.title("forth question")
    forth_question.config(bg=("#0000ff"))
    forth_question.geometry = ("600x600+600+600")

    forthq = Label(forth_question, text="ما هي اصغر دولة في العالم", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    forthq.place(x=600, y=200)

    a_choose = Button(forth_question, text="a) بنين", font=("Arial", 30), bg="orange", command=lambda: (false_forth()))
    a_choose.place(x=600, y=280)

    b_choose = Button(forth_question, text="b) مصر", font=("Arial", 30), bg="orange", command=lambda: (false_forth()))
    b_choose.place(x=800, y=280)

    c_choose = Button(forth_question, text="c) لتوانيا", font=("Arial", 30), bg="orange", command=lambda: (false_forth()))
    c_choose.place(x=600, y=400)

    d_choose = Button(forth_question, text="d) الفاتيكان", font=("Arial", 30), bg="orange", command=lambda: (true_forth()))
    d_choose.place(x=800, y=400)

    next_btn_nd=Button(forth_question,text="next",font=("Arial",30),bg="green",command=lambda :(next_forth()))
    next_btn_nd.place(x=1200,y=700)

    previous_btn_nd=Button(forth_question,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_forth()))
    previous_btn_nd.place(x=1300,y=700)

    forthstl=Label(forth_question,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthstl.place(x=10,y=10)

    forthndl=Label(forth_question,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthndl.place(x=10,y=110)

    forthrdl=Label(forth_question,text="1,000 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    forthrdl.place(x=10,y=210)

    forthforthl=Label(forth_question,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthforthl.place(x=10,y=310)

    forthfifthl=Label(forth_question,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthfifthl.place(x=10,y=410)

    forthsixthl=Label(forth_question,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthsixthl.place(x=10,y=510)

    forthseventhl=Label(forth_question,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthseventhl.place(x=10,y=610)

    fortheighthl=Label(forth_question,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fortheighthl.place(x=10,y=710)

def fifth_question():
    fifth_question = Tk()
    fifth_question.title("fifth question")
    fifth_question.config(bg=("#0000ff"))
    fifth_question.geometry = ("600x600+600+600")

    fifthq = Label(fifth_question, text="ما هو اطول جبل في العالم", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    fifthq.place(x=600, y=200)

    a_choose = Button(fifth_question, text="a)بيتسا", font=("Arial", 30), bg="orange", command=lambda: (false_fifth()))
    a_choose.place(x=600, y=280)

    b_choose = Button(fifth_question, text="b) نيبا ", font=("Arial", 30), bg="orange", command=lambda: (false_fifth()))
    b_choose.place(x=800, y=280)

    c_choose = Button(fifth_question, text="c) لتورس", font=("Arial", 30), bg="orange", command=lambda: (false_fifth()))
    c_choose.place(x=600, y=400)

    d_choose = Button(fifth_question, text=" افرست (d", font=("Arial", 30), bg="orange", command=lambda: (true_fifth()))
    d_choose.place(x=800, y=400)

    next_btn_nd=Button(fifth_question,text="next",font=("Arial",30),bg="green",command=lambda :(next_fifth()))
    next_btn_nd.place(x=1200,y=700)

    previous_btn_nd=Button(fifth_question,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_fifth()))
    previous_btn_nd.place(x=1300,y=700)

    fifthstl=Label(fifth_question,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthstl.place(x=10,y=10)

    fifthndl=Label(fifth_question,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthndl.place(x=10,y=110)

    fifthrdl=Label(fifth_question,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthrdl.place(x=10,y=210)

    fifthforthl=Label(fifth_question,text="50,000 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    fifthforthl.place(x=10,y=310)

    fifthfifthl=Label(fifth_question,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthfifthl.place(x=10,y=410)

    fifthsixthl=Label(fifth_question,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthsixthl.place(x=10,y=510)

    fifthseventhl=Label(fifth_question,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthseventhl.place(x=10,y=610)

    fiftheighthl=Label(fifth_question,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fiftheighthl.place(x=10,y=710)

def sixth_question():
    sixth_question = Tk()
    sixth_question.title("sixth question")
    sixth_question.config(bg=("#0000ff"))
    sixth_question.geometry = ("600x600+600+600")

    sixthq = Label(sixth_question, text="كم عدد محافظات مصر", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    sixthq.place(x=600, y=200)

    a_choose = Button(sixth_question, text="a)23", font=("Arial", 30), bg="orange", command=lambda: (false_sixth()))
    a_choose.place(x=600, y=280)

    b_choose = Button(sixth_question, text="b)26 ", font=("Arial", 30), bg="orange", command=lambda: (false_sixth()))
    b_choose.place(x=800, y=280)

    c_choose = Button(sixth_question, text="c)28", font=("Arial", 30), bg="orange", command=lambda: (false_sixth()))
    c_choose.place(x=600, y=400)

    d_choose = Button(sixth_question, text="d) 27", font=("Arial", 30), bg="orange", command=lambda: (true_sixth()))
    d_choose.place(x=800, y=400)

    next_btn_nd=Button(sixth_question,text="next",font=("Arial",30),bg="green",command=lambda :(next_sixth()))
    next_btn_nd.place(x=1200,y=700)

    previous_btn_nd=Button(sixth_question,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_sixth()))
    previous_btn_nd.place(x=1300,y=700)

    sixthstl=Label(sixth_question,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthstl.place(x=10,y=10)

    sixthndl=Label(sixth_question,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthndl.place(x=10,y=110)

    sixthrdl=Label(sixth_question,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthrdl.place(x=10,y=210)

    sixthforthl=Label(sixth_question,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthforthl.place(x=10,y=310)

    sixthfifthl=Label(sixth_question,text="100,000 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    sixthfifthl.place(x=10,y=410)

    sixthsixthl=Label(sixth_question,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthsixthl.place(x=10,y=510)

    sixthseventhl=Label(sixth_question,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthseventhl.place(x=10,y=610)

    sixtheighthl=Label(sixth_question,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixtheighthl.place(x=10,y=710)

def seventh_question():
    seventh_question = Tk()
    seventh_question.title("seventh question")
    seventh_question.config(bg=("#0000ff"))
    seventh_question.geometry = ("600x600+600+600")

    seventhq = Label(seventh_question, text="كم عدد محافظات مصر", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    seventhq.place(x=600, y=200)

    a_choose = Button(seventh_question, text="a)23", font=("Arial", 30), bg="orange", command=lambda: (false_seventh()))
    a_choose.place(x=600, y=280)

    b_choose = Button(seventh_question, text="b)26 ", font=("Arial", 30), bg="orange", command=lambda: (false_seventh()))
    b_choose.place(x=800, y=280)

    c_choose = Button(seventh_question, text="c)28", font=("Arial", 30), bg="orange", command=lambda: (false_seventh()))
    c_choose.place(x=600, y=400)

    d_choose = Button(seventh_question, text="d) 27", font=("Arial", 30), bg="orange", command=lambda: (true_seventh()))
    d_choose.place(x=800, y=400)

    next_btn_nd=Button(seventh_question,text="next",font=("Arial",30),bg="green",command=lambda :(next_seventh()))
    next_btn_nd.place(x=1200,y=700)

    previous_btn_nd=Button(seventh_question,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_seventh()))
    previous_btn_nd.place(x=1300,y=700)

    seventhstl=Label(seventh_question,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhstl.place(x=10,y=10)

    seventhndl=Label(seventh_question,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhndl.place(x=10,y=110)

    seventhrdl=Label(seventh_question,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhrdl.place(x=10,y=210)

    seventhforthl=Label(seventh_question,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhforthl.place(x=10,y=310)

    seventhfifthl=Label(seventh_question,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhfifthl.place(x=10,y=410)

    seventhseventhl=Label(seventh_question,text="500,000 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    seventhseventhl.place(x=10,y=510)

    seventhseventhl=Label(seventh_question,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhseventhl.place(x=10,y=610)

    seventheighthl=Label(seventh_question,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventheighthl.place(x=10,y=710)

def eighth_question():
    eighth_question = Tk()
    eighth_question.title("eighth question")
    eighth_question.config(bg=("#0000ff"))
    eighth_question.geometry = ("600x600+600+600")

    eighthq = Label(eighth_question, text="كم عدد روئساءالجمهورية الذين مروا على مصر", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    eighthq.place(x=600, y=200)

    a_choose = Button(eighth_question, text="a)6", font=("Arial", 30), bg="orange", command=lambda: (false_eighth()))
    a_choose.place(x=600, y=280)

    b_choose = Button(eighth_question, text="b)7 ", font=("Arial", 30), bg="orange", command=lambda: (true_eighth()))
    b_choose.place(x=800, y=280)

    c_choose = Button(eighth_question, text="c)8", font=("Arial", 30), bg="orange", command=lambda: (false_eighth()))
    c_choose.place(x=600, y=400)

    d_choose = Button(eighth_question, text="d)9", font=("Arial", 30), bg="orange", command=lambda: (false_eighth()))
    d_choose.place(x=800, y=400)

    previous_btn_nd=Button(eighth_question,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_eighth()))
    previous_btn_nd.place(x=1300,y=700)

    eighthstl=Label(eighth_question,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eighthstl.place(x=10,y=10)

    eighthndl=Label(eighth_question,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eighthndl.place(x=10,y=110)

    eighthrdl=Label(eighth_question,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eighthrdl.place(x=10,y=210)

    eighthforthl=Label(eighth_question,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eighthforthl.place(x=10,y=310)

    eighthfifthl=Label(eighth_question,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eighthfifthl.place(x=10,y=410)

    eightheighthl=Label(eighth_question,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eightheighthl.place(x=10,y=510)

    eightheighthl=Label(eighth_question,text="700,000 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    eightheighthl.place(x=10,y=610)

    eightheighthl=Label(eighth_question,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eightheighthl.place(x=10,y=710)


opening_window.mainloop()