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

#ready and not ready

def ready_start ():
    level=Label(opening_window,text="choose your level",bg="red",padx=5,pady=5,font=("Arial",30,"bold"))
    level.place(x=800,y=200)

    easy_btn=Button(opening_window,text="easy",
                    bg="red",padx=5,pady=5,font=("Arial",30,"bold"),command=lambda :st_question_easy())
    easy_btn.place(x=800,y=300)

    middle_btn=Button(opening_window,text="middle",
                    bg="red",padx=5,pady=5,font=("Arial",30,"bold"),command=lambda :st_question_middle())
    middle_btn.place(x=800,y=400)

    hard_btn=Button(opening_window,text="hard",
                    bg="red",padx=5,pady=5,font=("Arial",30,"bold"),command=lambda :st_question_easy())
    hard_btn.place(x=800,y=500)

def not_ready ():
    opening_window.destroy()

#next and previous in easy


def next_st_easy():
    nd_question_easy()

def next_nd_easy(): 
    rd_question_easy() 

def next_rd_easy():
    forth_question_easy()

def next_forth_easy():
    fifth_question_easy()

def next_fifth_easy():
    sixth_question_easy()

def next_sixth_easy():
    sixth_question_easy()

def next_seventh_easy():
    eighth_question_easy()

def previous_nd_easy():
    st_question_easy()

def previous_rd_easy():
    nd_question_easy()

def previous_forth_easy():
    rd_question_easy()

def previous_fifth_easy():
    forth_question_easy()

def previous_sixth_easy():
    fifth_question_easy()

def previous_seventh_easy():
    sixth_question_easy()

def previous_eighth_easy():
    seventh_question_easy()
#next and previous in middle

def next_st_middle():
    nd_question_middle()

def next_nd_middle(): 
    rd_question_middle() 

def next_rd_middle():
    forth_question_middle()

def next_forth_middle():
    fifth_question_middle()

def next_fifth_middle():
    sixth_question_middle()

def next_sixth_middle():
    seventh_question_middle()

def next_seventh_middle():
    eighth_question_middle()

def previous_nd_middle():
    st_question_middle()

def previous_rd_middle():
    nd_question_middle()

def previous_forth_middle():
    rd_question_middle()

def previous_fifth_middle():
    forth_question_middle()

def previous_sixth_middle():
    fifth_question_middle()

def previous_seventh_middle():
    sixth_question_middle()

def previous_eighth_middle():
    seventh_question_middle()

#next and previous in hard

def next_st_hard():
    nd_question_hard()

def next_nd_hard(): 
    rd_question_hard() 

def next_rd_hard():
    forth_question_hard()

def next_forth_hard():
    fifth_question_hard()

def next_fifth_hard():
    sixth_question_hard()

def next_sixth_hard():
    sixth_question_hard()

def next_seventh_hard():
    eighth_question_hard()

def previous_nd_hard():
    st_question_hard()

def previous_rd_hard():
    nd_question_hard()

def previous_forth_hard():
    rd_question_hard()

def previous_fifth_hard():
    forth_question_hard()

def previous_sixth_hard():
    fifth_question_hard()

def previous_seventh_hard():
    sixth_question_hard()

def previous_eighth_hard():
    seventh_question_hard()

#true or false in easy

def true_st_easy ():
    messagebox.showinfo("true","your answer is true")
    nd_question_easy()

def false_st_easy():
    messagebox.showinfo("false","your answer is false")
    st_question_easy()

def true_nd_easy():
    messagebox.showinfo("true",",your answer is true")
    rd_question_easy()

def false_nd_easy():
    messagebox.showinfo("false","your answer is false")
    nd_question_easy()

def true_rd_easy():
    messagebox.showinfo("true","your answer is true")
    forth_question_easy()

def false_rd_easy():
    messagebox.showinfo("false","your answer is false")
    rd_question_easy()

def true_forth_easy():
    messagebox.showinfo("true","your answer is true")
    fifth_question_easy()

def false_forth_easy():
    messagebox.showinfo("false","your answer is false")
    forth_question_easy()

def true_fifth_easy():
    messagebox.showinfo("true","your answer is true")
    sixth_question_easy()

def false_fifth_easy():
    messagebox.showinfo("false","your answer is false")
    fifth_question_easy()

def true_sixth_easy():
    messagebox.showinfo("true","your answer is true")
    seventh_question_easy()

def false_sixth_easy():
    messagebox.showinfo("false","your answer is false")
    sixth_question_easy()

def true_seventh_easy():
    messagebox.showinfo("true","your answer is true")
    eighth_question_easy()

def false_seventh_easy():
    messagebox.showinfo("false","your answer is false")
    seventh_question_easy()

def true_eighth_easy():
    messagebox.showinfo("true","your answer is true")
    win()

def false_eighth_easy():
    messagebox.showinfo("false","your answer is false")
    sixth_question_easy()
#true or false in middle


def true_st_middle ():
    messagebox.showinfo("true","your answer is true")
    nd_question_middle()

def false_st_middle():
    messagebox.showinfo("false","your answer is false")
    st_question_middle()

def true_nd_middle():
    messagebox.showinfo("true",",your answer is true")
    rd_question_middle()

def false_nd_middle():
    messagebox.showinfo("false","your answer is false")
    nd_question_middle()

def true_rd_middle():
    messagebox.showinfo("true","your answer is true")
    forth_question_middle()

def false_rd_middle():
    messagebox.showinfo("false","your answer is false")
    rd_question_middle()

def true_forth_middle():
    messagebox.showinfo("true","your answer is true")
    fifth_question_middle()

def false_forth_middle():
    messagebox.showinfo("false","your answer is false")
    forth_question_middle()

def true_fifth_middle():
    messagebox.showinfo("true","your answer is true")
    sixth_question_middle()

def false_fifth_middle():
    messagebox.showinfo("false","your answer is false")
    fifth_question_middle()

def true_sixth_middle():
    messagebox.showinfo("true","your answer is true")
    seventh_question_middle()

def false_sixth_middle():
    messagebox.showinfo("false","your answer is false")
    sixth_question_middle()

def true_seventh_middle():
    messagebox.showinfo("true","your answer is true")
    eighth_question_middle()

def false_seventh_middle():
    messagebox.showinfo("false","your answer is false")
    seventh_question_middle()

def true_eighth_middle():
    messagebox.showinfo("true","your answer is true")
    win_middle()

def false_eighth_middle():
    messagebox.showinfo("false","your answer is false")
    sixth_question_middle()

#true and false in hard

def true_st_hard ():
    messagebox.showinfo("true","your answer is true")
    nd_question_hard()

def false_st_hard():
    messagebox.showinfo("false","your answer is false")
    st_question_hard()

def true_nd_hard():
    messagebox.showinfo("true",",your answer is true")
    rd_question_hard()

def false_nd_hard():
    messagebox.showinfo("false","your answer is false")
    nd_question_hard()

def true_rd_hard():
    messagebox.showinfo("true","your answer is true")
    forth_question_hard()

def false_rd_hard():
    messagebox.showinfo("false","your answer is false")
    rd_question_hard()

def true_forth_hard():
    messagebox.showinfo("true","your answer is true")
    fifth_question_hard()

def false_forth_hard():
    messagebox.showinfo("false","your answer is false")
    forth_question_hard()

def true_fifth_hard():
    messagebox.showinfo("true","your answer is true")
    sixth_question_hard()

def false_fifth_hard():
    messagebox.showinfo("false","your answer is false")
    fifth_question_hard()

def true_sixth_hard():
    messagebox.showinfo("true","your answer is true")
    seventh_question_hard()

def false_sixth_hard():
    messagebox.showinfo("false","your answer is false")
    sixth_question_hard()

def true_seventh_hard():
    messagebox.showinfo("true","your answer is true")
    eighth_question_hard()

def false_seventh_hard():
    messagebox.showinfo("false","your answer is false")
    seventh_question_hard()

def true_eighth_hard():
    messagebox.showinfo("true","your answer is true")
    win()

def false_eighth_hard():
    messagebox.showinfo("false","your answer is false")
    sixth_question_hard()

#win

def win ():
    win=Tk()
    win.title("Win")
    win.config(bg=("#0000ff"))
    win.geometry = ("600x600+600+600")

    you_win=Label(win,text="YOU WIN YOU WIN MILLION",font=("Arial",90),bg="red",padx=15,pady=15)
    you_win.place(x=200,y=200)

def win_middle ():
    win_middle=Tk()
    win_middle.title("Win_middle")
    win_middle.config(bg=("#0000ff"))
    win_middle.geometry = ("600x600+600+600")

    you_win_middle=Label(win,text="YOU WIN YOU WIN MILLION",font=("Arial",90),bg="red",padx=15,pady=15)
    you_win_middle.place(x=200,y=200)

#easy

def st_question_easy ():
    st_question_easy=Tk()
    st_question_easy.title("st question_easy")
    st_question_easy.config(bg=("#0000ff"))
    st_question_easy.geometry = ("600x600+600+600")

    stq=Label(st_question_easy,text="كم عدد الدول في افريقيا",bg="red",padx=5,pady=5,font=("Arial",30,"bold"))
    stq.place(x=600,y=200)

    a_choose=Button(st_question_easy,text="a) 42",font=("Arial",30),bg="orange",command=lambda :(false_st_easy()))
    a_choose.place(x=600,y=280)

    b_choose=Button(st_question_easy,text="b) 56",font=("Arial",30),bg="orange",command=lambda :(false_st_easy()))
    b_choose.place(x=800,y=280)

    c_choose=Button(st_question_easy,text="c) 54",font=("Arial",30),bg="orange",command=lambda :(true_st_easy()))
    c_choose.place(x=600,y=400)

    d_choose=Button(st_question_easy,text="d) 50",font=("Arial",30),bg="orange",command=lambda :(false_st_easy()))
    d_choose.place(x=800,y=400)

    next_btn=Button(st_question_easy,text="next",font=("Arial",30),bg="green",command=lambda :(next_st_easy()))
    next_btn.place(x=1200,y=700)

    ststl=Label(st_question_easy,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ststl.place(x=10,y=10)

    stndl=Label(st_question_easy,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    stndl.place(x=10,y=110)

    strdl=Label(st_question_easy,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    strdl.place(x=10,y=210)

    stforthl=Label(st_question_easy,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    stforthl.place(x=10,y=310)

    stfifthl=Label(st_question_easy,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    stfifthl.place(x=10,y=410)

    stsixthl=Label(st_question_easy,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    stsixthl.place(x=10,y=510)

    stseventhl=Label(st_question_easy,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    stseventhl.place(x=10,y=610)

    steighthl=Label(st_question_easy,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    steighthl.place(x=10,y=710)

def nd_question_easy ():
    nd_question_easy=Tk()
    nd_question_easy.title("st question_easy")
    nd_question_easy.config(bg=("#0000ff"))
    nd_question_easy.geometry = ("600x600+600+600")

    ndq=Label(nd_question_easy,text="اين تقع الاولمبيات الحالية",bg="red",padx=5,pady=5,font=("Arial",30,"bold"))
    ndq.place(x=600,y=200)

    a_choose=Button(nd_question_easy,text="a) LONDON",font=("Arial",30),bg="orange",command=lambda :(false_nd_easy()))
    a_choose.place(x=550,y=280)

    b_choose=Button(nd_question_easy,text="b) PARIS",font=("Arial",30),bg="orange",command=lambda :(true_nd_easy()))
    b_choose.place(x=800,y=280)

    c_choose=Button(nd_question_easy,text="c) TOKYO",font=("Arial",30),bg="orange",command=lambda :(false_nd_easy()))
    c_choose.place(x=550,y=400)

    d_choose=Button(nd_question_easy,text="d) ATHINA",font=("Arial",30),bg="orange",command=lambda :(false_nd_easy()))
    d_choose.place(x=800,y=400)

    next_btn_nd=Button(nd_question_easy,text="next",font=("Arial",30),bg="green",command=lambda :(next_nd_easy()))
    next_btn_nd.place(x=1200,y=700)

    previous_btn_nd=Button(nd_question_easy,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_nd_easy()))
    previous_btn_nd.place(x=1300,y=700)

    ndstl=Label(nd_question_easy,text="100 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    ndstl.place(x=10,y=10)

    ndndl=Label(nd_question_easy,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndndl.place(x=10,y=110)

    ndrdl=Label(nd_question_easy,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndrdl.place(x=10,y=210)

    ndforthl=Label(nd_question_easy,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndforthl.place(x=10,y=310)

    ndfifthl=Label(nd_question_easy,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndfifthl.place(x=10,y=410)

    ndsixthl=Label(nd_question_easy,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndsixthl.place(x=10,y=510)

    ndseventhl=Label(nd_question_easy,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndseventhl.place(x=10,y=610)

    ndeighthl=Label(nd_question_easy,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndeighthl.place(x=10,y=710)

def rd_question_easy():
    rd_question_easy = Tk()
    rd_question_easy.title("rd question_easy")
    rd_question_easy.config(bg=("#0000ff"))
    rd_question_easy.geometry = ("600x600+600+600")

    rdq = Label(rd_question_easy, text="567+324", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    rdq.place(x=600, y=200)

    a_choose = Button(rd_question_easy, text="a) 891", font=("Arial", 30), bg="orange", command=lambda: (true_rd_easy()))
    a_choose.place(x=600, y=280)

    b_choose = Button(rd_question_easy, text="b) 892", font=("Arial", 30), bg="orange", command=lambda: (false_rd_easy()))
    b_choose.place(x=800, y=280)

    c_choose = Button(rd_question_easy, text="c) 893", font=("Arial", 30), bg="orange", command=lambda: (false_rd_easy()))
    c_choose.place(x=600, y=400)

    d_choose = Button(rd_question_easy, text="d) 894", font=("Arial", 30), bg="orange", command=lambda: (false_rd_easy()))
    d_choose.place(x=800, y=400)

    next_btn_nd=Button(rd_question_easy,text="next",font=("Arial",30),bg="green",command=lambda :(next_rd_easy()))
    next_btn_nd.place(x=1200,y=700)

    previous_btn_nd=Button(rd_question_easy,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_rd_easy()))
    previous_btn_nd.place(x=1300,y=700)

    rdstl=Label(rd_question_easy,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdstl.place(x=10,y=10)

    rdndl=Label(rd_question_easy,text="500 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    rdndl.place(x=10,y=110)

    rdrdl=Label(rd_question_easy,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdrdl.place(x=10,y=210)

    rdforthl=Label(rd_question_easy,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdforthl.place(x=10,y=310)

    rdfifthl=Label(rd_question_easy,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdfifthl.place(x=10,y=410)

    rdsixthl=Label(rd_question_easy,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdsixthl.place(x=10,y=510)

    rdseventhl=Label(rd_question_easy,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdseventhl.place(x=10,y=610)

    rdeighthl=Label(rd_question_easy,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdeighthl.place(x=10,y=710)

def forth_question_easy():
    forth_question_easy = Tk()
    forth_question_easy.title("forth question_easy")
    forth_question_easy.config(bg=("#0000ff"))
    forth_question_easy.geometry = ("600x600+600+600")

    forthq = Label(forth_question_easy, text="ما هي اصغر دولة في العالم", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    forthq.place(x=600, y=200)

    a_choose = Button(forth_question_easy, text="a) بنين", font=("Arial", 30), bg="orange", command=lambda: (false_forth_easy()))
    a_choose.place(x=600, y=280)

    b_choose = Button(forth_question_easy, text="b) مصر", font=("Arial", 30), bg="orange", command=lambda: (false_forth_easy()))
    b_choose.place(x=800, y=280)

    c_choose = Button(forth_question_easy, text="c) لتوانيا", font=("Arial", 30), bg="orange", command=lambda: (false_forth_easy()))
    c_choose.place(x=600, y=400)

    d_choose = Button(forth_question_easy, text="d) الفاتيكان", font=("Arial", 30), bg="orange", command=lambda: (true_forth_easy()))
    d_choose.place(x=800, y=400)

    next_btn_nd=Button(forth_question_easy,text="next",font=("Arial",30),bg="green",command=lambda :(next_forth_easy()))
    next_btn_nd.place(x=1200,y=700)

    previous_btn_nd=Button(forth_question_easy,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_forth_easy()))
    previous_btn_nd.place(x=1300,y=700)

    forthstl=Label(forth_question_easy,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthstl.place(x=10,y=10)

    forthndl=Label(forth_question_easy,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthndl.place(x=10,y=110)

    forthrdl=Label(forth_question_easy,text="1,000 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    forthrdl.place(x=10,y=210)

    forthforthl=Label(forth_question_easy,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthforthl.place(x=10,y=310)

    forthfifthl=Label(forth_question_easy,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthfifthl.place(x=10,y=410)

    forthsixthl=Label(forth_question_easy,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthsixthl.place(x=10,y=510)

    forthseventhl=Label(forth_question_easy,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthseventhl.place(x=10,y=610)

    fortheighthl=Label(forth_question_easy,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fortheighthl.place(x=10,y=710)

def fifth_question_easy():
    fifth_question_easy = Tk()
    fifth_question_easy.title("fifth question_easy")
    fifth_question_easy.config(bg=("#0000ff"))
    fifth_question_easy.geometry = ("600x600+600+600")

    fifthq = Label(fifth_question_easy, text="ما هو اطول جبل في العالم", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    fifthq.place(x=600, y=200)

    a_choose = Button(fifth_question_easy, text="a)بيتسا", font=("Arial", 30), bg="orange", command=lambda: (false_fifth_easy()))
    a_choose.place(x=600, y=280)

    b_choose = Button(fifth_question_easy, text="b) نيبا ", font=("Arial", 30), bg="orange", command=lambda: (false_fifth_easy()))
    b_choose.place(x=800, y=280)

    c_choose = Button(fifth_question_easy, text="c) لتورس", font=("Arial", 30), bg="orange", command=lambda: (false_fifth_easy()))
    c_choose.place(x=600, y=400)

    d_choose = Button(fifth_question_easy, text=" افرست (d", font=("Arial", 30), bg="orange", command=lambda: (true_fifth_easy()))
    d_choose.place(x=800, y=400)

    next_btn_nd=Button(fifth_question_easy,text="next",font=("Arial",30),bg="green",command=lambda :(next_fifth_easy()))
    next_btn_nd.place(x=1200,y=700)

    previous_btn_nd=Button(fifth_question_easy,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_fifth_easy()))
    previous_btn_nd.place(x=1300,y=700)

    fifthstl=Label(fifth_question_easy,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthstl.place(x=10,y=10)

    fifthndl=Label(fifth_question_easy,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthndl.place(x=10,y=110)

    fifthrdl=Label(fifth_question_easy,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthrdl.place(x=10,y=210)

    fifthforthl=Label(fifth_question_easy,text="50,000 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    fifthforthl.place(x=10,y=310)

    fifthfifthl=Label(fifth_question_easy,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthfifthl.place(x=10,y=410)

    fifthsixthl=Label(fifth_question_easy,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthsixthl.place(x=10,y=510)

    fifthseventhl=Label(fifth_question_easy,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthseventhl.place(x=10,y=610)

    fiftheighthl=Label(fifth_question_easy,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fiftheighthl.place(x=10,y=710)

def sixth_question_easy():
    sixth_question_easy = Tk()
    sixth_question_easy.title("sixth question_easy")
    sixth_question_easy.config(bg=("#0000ff"))
    sixth_question_easy.geometry = ("600x600+600+600")

    sixthq = Label(sixth_question_easy, text="كم عدد محافظات مصر", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    sixthq.place(x=600, y=200)

    a_choose = Button(sixth_question_easy, text="a)23", font=("Arial", 30), bg="orange", command=lambda: (false_sixth_easy()))
    a_choose.place(x=600, y=280)

    b_choose = Button(sixth_question_easy, text="b)26 ", font=("Arial", 30), bg="orange", command=lambda: (false_sixth_easy()))
    b_choose.place(x=800, y=280)

    c_choose = Button(sixth_question_easy, text="c)28", font=("Arial", 30), bg="orange", command=lambda: (false_sixth_easy()))
    c_choose.place(x=600, y=400)

    d_choose = Button(sixth_question_easy, text="d) 27", font=("Arial", 30), bg="orange", command=lambda: (true_sixth_easy()))
    d_choose.place(x=800, y=400)

    next_btn_nd=Button(sixth_question_easy,text="next",font=("Arial",30),bg="green",command=lambda :(next_sixth_easy()))
    next_btn_nd.place(x=1200,y=700)

    previous_btn_nd=Button(sixth_question_easy,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_sixth_easy()))
    previous_btn_nd.place(x=1300,y=700)

    sixthstl=Label(sixth_question_easy,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthstl.place(x=10,y=10)

    sixthndl=Label(sixth_question_easy,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthndl.place(x=10,y=110)

    sixthrdl=Label(sixth_question_easy,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthrdl.place(x=10,y=210)

    sixthforthl=Label(sixth_question_easy,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthforthl.place(x=10,y=310)

    sixthfifthl=Label(sixth_question_easy,text="100,000 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    sixthfifthl.place(x=10,y=410)

    sixthsixthl=Label(sixth_question_easy,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthsixthl.place(x=10,y=510)

    sixthseventhl=Label(sixth_question_easy,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthseventhl.place(x=10,y=610)

    sixtheighthl=Label(sixth_question_easy,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixtheighthl.place(x=10,y=710)

def seventh_question_easy():
    seventh_question_easy = Tk()
    seventh_question_easy.title("seventh question_easy")
    seventh_question_easy.config(bg=("#0000ff"))
    seventh_question_easy.geometry = ("600x600+600+600")

    seventhq = Label(seventh_question_easy, text="كم عدد محافظات مصر", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    seventhq.place(x=600, y=200)

    a_choose = Button(seventh_question_easy, text="a)23", font=("Arial", 30), bg="orange", command=lambda: (false_seventh_easy()))
    a_choose.place(x=600, y=280)

    b_choose = Button(seventh_question_easy, text="b)26 ", font=("Arial", 30), bg="orange", command=lambda: (false_seventh_easy()))
    b_choose.place(x=800, y=280)

    c_choose = Button(seventh_question_easy, text="c)28", font=("Arial", 30), bg="orange", command=lambda: (false_seventh_easy()))
    c_choose.place(x=600, y=400)

    d_choose = Button(seventh_question_easy, text="d) 27", font=("Arial", 30), bg="orange", command=lambda: (true_seventh_easy()))
    d_choose.place(x=800, y=400)

    next_btn_nd=Button(seventh_question_easy,text="next",font=("Arial",30),bg="green",command=lambda :(next_seventh_easy()))
    next_btn_nd.place(x=1200,y=700)

    previous_btn_nd=Button(seventh_question_easy,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_seventh_easy()))
    previous_btn_nd.place(x=1300,y=700)

    seventhstl=Label(seventh_question_easy,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhstl.place(x=10,y=10)

    seventhndl=Label(seventh_question_easy,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhndl.place(x=10,y=110)

    seventhrdl=Label(seventh_question_easy,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhrdl.place(x=10,y=210)

    seventhforthl=Label(seventh_question_easy,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhforthl.place(x=10,y=310)

    seventhfifthl=Label(seventh_question_easy,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhfifthl.place(x=10,y=410)

    seventhseventhl=Label(seventh_question_easy,text="500,000 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    seventhseventhl.place(x=10,y=510)

    seventhseventhl=Label(seventh_question_easy,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhseventhl.place(x=10,y=610)

    seventheighthl=Label(seventh_question_easy,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventheighthl.place(x=10,y=710)

def eighth_question_easy():
    eighth_question_easy = Tk()
    eighth_question_easy.title("eighth question_easy")
    eighth_question_easy.config(bg=("#0000ff"))
    eighth_question_easy.geometry = ("600x600+600+600")

    eighthq = Label(eighth_question_easy, text="كم عدد روئساءالجمهورية الذين مروا على مصر", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    eighthq.place(x=600, y=200)

    a_choose = Button(eighth_question_easy, text="a)6", font=("Arial", 30), bg="orange", command=lambda: (false_eighth_easy()))
    a_choose.place(x=600, y=280)

    b_choose = Button(eighth_question_easy, text="b)7 ", font=("Arial", 30), bg="orange", command=lambda: (true_eighth_easy()))
    b_choose.place(x=800, y=280)

    c_choose = Button(eighth_question_easy, text="c)8", font=("Arial", 30), bg="orange", command=lambda: (false_eighth_easy()))
    c_choose.place(x=600, y=400)

    d_choose = Button(eighth_question_easy, text="d)9", font=("Arial", 30), bg="orange", command=lambda: (false_eighth_easy()))
    d_choose.place(x=800, y=400)

    previous_btn_nd=Button(eighth_question_easy,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_eighth_easy()))
    previous_btn_nd.place(x=1300,y=700)

    eighthstl=Label(eighth_question_easy,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eighthstl.place(x=10,y=10)

    eighthndl=Label(eighth_question_easy,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eighthndl.place(x=10,y=110)

    eighthrdl=Label(eighth_question_easy,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eighthrdl.place(x=10,y=210)

    eighthforthl=Label(eighth_question_easy,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eighthforthl.place(x=10,y=310)

    eighthfifthl=Label(eighth_question_easy,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eighthfifthl.place(x=10,y=410)

    eightheighthl=Label(eighth_question_easy,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eightheighthl.place(x=10,y=510)

    eightheighthl=Label(eighth_question_easy,text="700,000 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    eightheighthl.place(x=10,y=610)

    eightheighthl=Label(eighth_question_easy,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eightheighthl.place(x=10,y=710)

#middle

def st_question_middle ():
    st_question_middle=Tk()
    st_question_middle.title("st question_middle")
    st_question_middle.config(bg=("#0000ff"))
    st_question_middle.geometry = ("600x600+600+600")

    stq=Label(st_question_middle,text="كم عدد الارجل التي يمتلكها العنكبوت",bg="red",padx=5,pady=5,font=("Arial",30,"bold"))
    stq.place(x=590,y=200)

    a_choose=Button(st_question_middle,text="a) 4",font=("Arial",30),bg="orange",command=lambda :(false_st_middle()))
    a_choose.place(x=600,y=280)

    b_choose=Button(st_question_middle,text="b) 6",font=("Arial",30),bg="orange",command=lambda :(false_st_middle()))
    b_choose.place(x=800,y=280)

    c_choose=Button(st_question_middle,text="c) 8",font=("Arial",30),bg="orange",command=lambda :(true_st_middle()))
    c_choose.place(x=600,y=400)

    d_choose=Button(st_question_middle,text="d) 10",font=("Arial",30),bg="orange",command=lambda :(false_st_middle()))
    d_choose.place(x=800,y=400)

    next_btn=Button(st_question_middle,text="next",font=("Arial",30),bg="green",command=lambda :(next_st_middle()))
    next_btn.place(x=1200,y=700)

    ststl=Label(st_question_middle,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ststl.place(x=10,y=10)

    stndl=Label(st_question_middle,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    stndl.place(x=10,y=110)

    strdl=Label(st_question_middle,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    strdl.place(x=10,y=210)

    stforthl=Label(st_question_middle,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    stforthl.place(x=10,y=310)

    stfifthl=Label(st_question_middle,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    stfifthl.place(x=10,y=410)

    stsixthl=Label(st_question_middle,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    stsixthl.place(x=10,y=510)

    stseventhl=Label(st_question_middle,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    stseventhl.place(x=10,y=610)

    steighthl=Label(st_question_middle,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    steighthl.place(x=10,y=710)

def nd_question_middle ():
    nd_question_middle=Tk()
    nd_question_middle.title("nd question_middle")
    nd_question_middle.config(bg=("#0000ff"))
    nd_question_middle.geometry = ("600x600+600+600")

    ndq=Label(nd_question_middle,text="ما هو الكوكب الذي يعرف بالكوكب الاحمر",bg="red",padx=5,pady=5,font=("Arial",30,"bold"))
    ndq.place(x=550,y=200)

    a_choose=Button(nd_question_middle,text="a) المشترى",font=("Arial",30),bg="orange",command=lambda :(false_nd_middle()))
    a_choose.place(x=550,y=280)

    b_choose=Button(nd_question_middle,text="b) اورانوس",font=("Arial",30),bg="orange",command=lambda :(false_nd_middle()))
    b_choose.place(x=800,y=280)

    c_choose=Button(nd_question_middle,text="c) عطارد ",font=("Arial",30),bg="orange",command=lambda :(false_nd_middle()))
    c_choose.place(x=550,y=400)

    d_choose=Button(nd_question_middle,text="d) المريخ",font=("Arial",30),bg="orange",command=lambda :(true_nd_middle()))
    d_choose.place(x=800,y=400)

    next_btn_nd_middle=Button(nd_question_middle,text="next",font=("Arial",30),bg="green",command=lambda :(next_nd_middle()))
    next_btn_nd_middle.place(x=1200,y=700)

    previous_btn_nd_middle=Button(nd_question_middle,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_nd_middle()))
    previous_btn_nd_middle.place(x=1300,y=700)

    ndstl=Label(nd_question_middle,text="100 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    ndstl.place(x=10,y=10)

    ndndl=Label(nd_question_middle,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndndl.place(x=10,y=110)

    ndrdl=Label(nd_question_middle,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndrdl.place(x=10,y=210)

    ndforthl=Label(nd_question_middle,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndforthl.place(x=10,y=310)

    ndfifthl=Label(nd_question_middle,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndfifthl.place(x=10,y=410)

    ndsixthl=Label(nd_question_middle,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndsixthl.place(x=10,y=510)

    ndseventhl=Label(nd_question_middle,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndseventhl.place(x=10,y=610)

    ndeighthl=Label(nd_question_middle,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndeighthl.place(x=10,y=710)

def rd_question_middle():
    rd_question_middle = Tk()
    rd_question_middle.title("rd question_middle")
    rd_question_middle.config(bg=("#0000ff"))
    rd_question_middle.geometry = ("600x600+600+600")

    rdq = Label(rd_question_middle, text="من الطيور التي لا تستطيع الطيران", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    rdq.place(x=600, y=200)

    a_choose = Button(rd_question_middle, text="a) الصقر", font=("Arial", 30), bg="orange", command=lambda: (false_rd_middle()))
    a_choose.place(x=600, y=280)

    b_choose = Button(rd_question_middle, text="b) العقاق", font=("Arial", 30), bg="orange", command=lambda: (false_rd_middle()))
    b_choose.place(x=800, y=280)

    c_choose = Button(rd_question_middle, text="c) النعامة", font=("Arial", 30), bg="orange", command=lambda: (true_rd_middle()))
    c_choose.place(x=600, y=400)

    d_choose = Button(rd_question_middle, text="d) الطنان", font=("Arial", 30), bg="orange", command=lambda: (false_rd_middle()))
    d_choose.place(x=800, y=400)

    next_btn_rd=Button(rd_question_middle,text="next",font=("Arial",30),bg="green",command=lambda :(next_rd_middle()))
    next_btn_rd.place(x=1200,y=700)

    previous_btn_rd=Button(rd_question_middle,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_rd_middle()))
    previous_btn_rd.place(x=1300,y=700)

    rdstl=Label(rd_question_middle,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdstl.place(x=10,y=10)

    rdndl=Label(rd_question_middle,text="500 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    rdndl.place(x=10,y=110)

    rdrdl=Label(rd_question_middle,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdrdl.place(x=10,y=210)

    rdforthl=Label(rd_question_middle,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdforthl.place(x=10,y=310)

    rdfifthl=Label(rd_question_middle,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdfifthl.place(x=10,y=410)

    rdsixthl=Label(rd_question_middle,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdsixthl.place(x=10,y=510)

    rdseventhl=Label(rd_question_middle,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdseventhl.place(x=10,y=610)

    rdeighthl=Label(rd_question_middle,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdeighthl.place(x=10,y=710)

def forth_question_middle():
    forth_question_middle = Tk()
    forth_question_middle.title("forth question_middle")
    forth_question_middle.config(bg=("#0000ff"))
    forth_question_middle.geometry = ("600x600+600+600")

    forthq = Label(forth_question_middle, text="ما هي اكبر قارة من حيث المساحة", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    forthq.place(x=600, y=200)

    a_choose = Button(forth_question_middle, text="a) اسيا", font=("Arial", 30), bg="orange", command=lambda: (true_forth_middle()))
    a_choose.place(x=600, y=280)

    b_choose = Button(forth_question_middle, text="b) امريكا الشمالية", font=("Arial", 30), bg="orange", command=lambda: (false_forth_middle()))
    b_choose.place(x=800, y=280)

    c_choose = Button(forth_question_middle, text="c) افريقيا", font=("Arial", 30), bg="orange", command=lambda: (false_forth_middle()))
    c_choose.place(x=600, y=400)

    d_choose = Button(forth_question_middle, text="d) اوروبا", font=("Arial", 30), bg="orange", command=lambda: (false_forth_middle()))
    d_choose.place(x=800, y=400)

    next_btn_nd=Button(forth_question_middle,text="next",font=("Arial",30),bg="green",command=lambda :(next_forth_middle()))
    next_btn_nd.place(x=1200,y=700)

    previous_btn_nd=Button(forth_question_middle,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_forth_middle()))
    previous_btn_nd.place(x=1300,y=700)

    forthstl=Label(forth_question_middle,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthstl.place(x=10,y=10)

    forthndl=Label(forth_question_middle,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthndl.place(x=10,y=110)

    forthrdl=Label(forth_question_middle,text="1,000 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    forthrdl.place(x=10,y=210)

    forthforthl=Label(forth_question_middle,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthforthl.place(x=10,y=310)

    forthfifthl=Label(forth_question_middle,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthfifthl.place(x=10,y=410)

    forthsixthl=Label(forth_question_middle,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthsixthl.place(x=10,y=510)

    forthseventhl=Label(forth_question_middle,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthseventhl.place(x=10,y=610)

    fortheighthl=Label(forth_question_middle,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fortheighthl.place(x=10,y=710)

def fifth_question_middle():
    fifth_question_middle = Tk()
    fifth_question_middle.title("fifth question_middle")
    fifth_question_middle.config(bg=("#0000ff"))
    fifth_question_middle.geometry = ("600x600+600+600")

    fifthq = Label(fifth_question_middle, text="ما هو الحيوان الذي ينام واقفا", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    fifthq.place(x=600, y=200)

    a_choose = Button(fifth_question_middle, text="a)الزرافة", font=("Arial", 30), bg="orange", command=lambda: (false_fifth_middle()))
    a_choose.place(x=600, y=280)

    b_choose = Button(fifth_question_middle, text="b)الحصان", font=("Arial", 30), bg="orange", command=lambda: (true_fifth_middle()))
    b_choose.place(x=800, y=280)

    c_choose = Button(fifth_question_middle, text="c)الذئب", font=("Arial", 30), bg="orange", command=lambda: (false_fifth_middle()))
    c_choose.place(x=600, y=400)

    d_choose = Button(fifth_question_middle, text=" الفهد (d", font=("Arial", 30), bg="orange", command=lambda: (false_fifth_middle()))
    d_choose.place(x=800, y=400)

    next_btn_nd=Button(fifth_question_middle,text="next",font=("Arial",30),bg="green",command=lambda :(next_fifth_middle()))
    next_btn_nd.place(x=1200,y=700)

    previous_btn_nd=Button(fifth_question_middle,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_fifth_middle()))
    previous_btn_nd.place(x=1300,y=700)

    fifthstl=Label(fifth_question_middle,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthstl.place(x=10,y=10)

    fifthndl=Label(fifth_question_middle,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthndl.place(x=10,y=110)

    fifthrdl=Label(fifth_question_middle,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthrdl.place(x=10,y=210)

    fifthforthl=Label(fifth_question_middle,text="50,000 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    fifthforthl.place(x=10,y=310)

    fifthfifthl=Label(fifth_question_middle,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthfifthl.place(x=10,y=410)

    fifthsixthl=Label(fifth_question_middle,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthsixthl.place(x=10,y=510)

    fifthseventhl=Label(fifth_question_middle,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthseventhl.place(x=10,y=610)

    fiftheighthl=Label(fifth_question_middle,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fiftheighthl.place(x=10,y=710)

def sixth_question_middle():
    sixth_question_middle = Tk()
    sixth_question_middle.title("sixth question_middle")
    sixth_question_middle.config(bg=("#0000ff"))
    sixth_question_middle.geometry = ("600x600+600+600")

    sixthq = Label(sixth_question_middle, text="كم عدد اسنان الانسان البالغ", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    sixthq.place(x=600, y=200)

    a_choose = Button(sixth_question_middle, text="a)23", font=("Arial", 30), bg="orange", command=lambda: (false_sixth_middle()))
    a_choose.place(x=600, y=280)

    b_choose = Button(sixth_question_middle, text="b)26 ", font=("Arial", 30), bg="orange", command=lambda: (false_sixth_middle()))
    b_choose.place(x=800, y=280)

    c_choose = Button(sixth_question_middle, text="c)28", font=("Arial", 30), bg="orange", command=lambda: (false_sixth_middle()))
    c_choose.place(x=600, y=400)

    d_choose = Button(sixth_question_middle, text="d) 32", font=("Arial", 30), bg="orange", command=lambda: (true_sixth_middle()))
    d_choose.place(x=800, y=400)

    next_btn_nd=Button(sixth_question_middle,text="next",font=("Arial",30),bg="green",command=lambda :(next_sixth_middle()))
    next_btn_nd.place(x=1200,y=700)

    previous_btn_nd=Button(sixth_question_middle,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_sixth_middle()))
    previous_btn_nd.place(x=1300,y=700)

    sixthstl=Label(sixth_question_middle,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthstl.place(x=10,y=10)

    sixthndl=Label(sixth_question_middle,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthndl.place(x=10,y=110)

    sixthrdl=Label(sixth_question_middle,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthrdl.place(x=10,y=210)

    sixthforthl=Label(sixth_question_middle,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthforthl.place(x=10,y=310)

    sixthfifthl=Label(sixth_question_middle,text="100,000 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    sixthfifthl.place(x=10,y=410)

    sixthsixthl=Label(sixth_question_middle,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthsixthl.place(x=10,y=510)

    sixthseventhl=Label(sixth_question_middle,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthseventhl.place(x=10,y=610)

    sixtheighthl=Label(sixth_question_middle,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixtheighthl.place(x=10,y=710)

def seventh_question_middle():
    seventh_question_middle = Tk()
    seventh_question_middle.title("seventh question_middle")
    seventh_question_middle.config(bg=("#0000ff"))
    seventh_question_middle.geometry = ("600x600+600+600")

    seventhq = Label(seventh_question_middle, text="ما هو اكبر كوكب في المظام الشمسي", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    seventhq.place(x=600, y=200)

    a_choose = Button(seventh_question_middle, text="a)الارض", font=("Arial", 30), bg="orange", command=lambda: (false_seventh_middle()))
    a_choose.place(x=600, y=280)

    b_choose = Button(seventh_question_middle, text="b)زحل", font=("Arial", 30), bg="orange", command=lambda: (false_seventh_middle()))
    b_choose.place(x=800, y=280)

    c_choose = Button(seventh_question_middle, text="c)المشتري", font=("Arial", 30), bg="orange", command=lambda: (true_seventh_middle()))
    c_choose.place(x=600, y=400)

    d_choose = Button(seventh_question_middle, text="d)عطارد", font=("Arial", 30), bg="orange", command=lambda: (false_seventh_middle()))
    d_choose.place(x=800, y=400)

    next_btn_nd=Button(seventh_question_middle,text="next",font=("Arial",30),bg="green",command=lambda :(next_seventh_middle()))
    next_btn_nd.place(x=1200,y=700)

    previous_btn_nd=Button(seventh_question_middle,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_seventh_middle()))
    previous_btn_nd.place(x=1300,y=700)

    seventhstl=Label(seventh_question_middle,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhstl.place(x=10,y=10)

    seventhndl=Label(seventh_question_middle,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhndl.place(x=10,y=110)

    seventhrdl=Label(seventh_question_middle,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhrdl.place(x=10,y=210)

    seventhforthl=Label(seventh_question_middle,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhforthl.place(x=10,y=310)

    seventhfifthl=Label(seventh_question_middle,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhfifthl.place(x=10,y=410)

    seventhseventhl=Label(seventh_question_middle,text="500,000 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    seventhseventhl.place(x=10,y=510)

    seventhseventhl=Label(seventh_question_middle,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhseventhl.place(x=10,y=610)

    seventheighthl=Label(seventh_question_middle,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventheighthl.place(x=10,y=710)

def eighth_question_middle():
    eighth_question_middle = Tk()
    eighth_question_middle.title("eighth question_middle")
    eighth_question_middle.config(bg=("#0000ff"))
    eighth_question_middle.geometry = ("600x600+600+600")

    eighthq = Label(eighth_question_middle, text="ما هي اللغة الرسمية في البرازيل", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    eighthq.place(x=600, y=200)

    a_choose = Button(eighth_question_middle, text="a)الانجليزية", font=("Arial", 30), bg="orange", command=lambda: (false_seventh_middle()))
    a_choose.place(x=600, y=280)

    b_choose = Button(eighth_question_middle, text="b)البرتغالية ", font=("Arial", 30), bg="orange", command=lambda: (true_seventh_middle()))
    b_choose.place(x=800, y=280)

    c_choose = Button(eighth_question_middle, text="c)الاسبانية", font=("Arial", 30), bg="orange", command=lambda: (false_seventh_middle()))
    c_choose.place(x=600, y=400)

    d_choose = Button(eighth_question_middle, text="d)السويدية", font=("Arial", 30), bg="orange", command=lambda: (false_seventh_middle()))
    d_choose.place(x=800, y=400)

    previous_btn_nd=Button(eighth_question_middle,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_seventh_middle()))
    previous_btn_nd.place(x=1300,y=700)

    eighthstl=Label(eighth_question_middle,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eighthstl.place(x=10,y=10)

    eighthndl=Label(eighth_question_middle,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eighthndl.place(x=10,y=110)

    eighthrdl=Label(eighth_question_middle,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eighthrdl.place(x=10,y=210)

    eighthforthl=Label(eighth_question_middle,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eighthforthl.place(x=10,y=310)

    eighthfifthl=Label(eighth_question_middle,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eighthfifthl.place(x=10,y=410)

    eightheighthl=Label(eighth_question_middle,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eightheighthl.place(x=10,y=510)

    eightheighthl=Label(eighth_question_middle,text="700,000 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    eightheighthl.place(x=10,y=610)

    eightheighthl=Label(eighth_question_middle,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eightheighthl.place(x=10,y=710)

#hard


def st_question_hard ():
    st_question_hard=Tk()
    st_question_hard.title("st question_hard")
    st_question_hard.config(bg=("#0000ff"))
    st_question_hard.geometry = ("600x600+600+600")

    stq=Label(st_question_hard,text="ما هو اكبر محيطات العالم",bg="red",padx=5,pady=5,font=("Arial",30,"bold"))
    stq.place(x=590,y=200)

    a_choose=Button(st_question_hard,text="a) الهندي",font=("Arial",30),bg="orange",command=lambda :(false_st_hard()))
    a_choose.place(x=600,y=280)

    b_choose=Button(st_question_hard,text="b)الاطلنطي",font=("Arial",30),bg="orange",command=lambda :(false_st_hard()))
    b_choose.place(x=800,y=280)

    c_choose=Button(st_question_hard,text="c)الهادي",font=("Arial",30),bg="orange",command=lambda :(true_st_hard()))
    c_choose.place(x=600,y=400)

    d_choose=Button(st_question_hard,text="d)الاطلسي",font=("Arial",30),bg="orange",command=lambda :(false_st_hard()))
    d_choose.place(x=800,y=400)

    next_btn=Button(st_question_hard,text="next",font=("Arial",30),bg="green",command=lambda :(next_st_hard()))
    next_btn.place(x=1200,y=700)

    ststl=Label(st_question_hard,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ststl.place(x=10,y=10)

    stndl=Label(st_question_hard,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    stndl.place(x=10,y=110)

    strdl=Label(st_question_hard,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    strdl.place(x=10,y=210)

    stforthl=Label(st_question_hard,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    stforthl.place(x=10,y=310)

    stfifthl=Label(st_question_hard,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    stfifthl.place(x=10,y=410)

    stsixthl=Label(st_question_hard,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    stsixthl.place(x=10,y=510)

    stseventhl=Label(st_question_hard,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    stseventhl.place(x=10,y=610)

    steighthl=Label(st_question_hard,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    steighthl.place(x=10,y=710)

def nd_question_hard ():
    nd_question_hard=Tk()
    nd_question_hard.title("nd question_hard")
    nd_question_hard.config(bg=("#0000ff"))
    nd_question_hard.geometry = ("600x600+600+600")

    ndq=Label(nd_question_hard,text="ما هو الحيوان الذي يمتلك ثلاث قلوب",bg="red",padx=5,pady=5,font=("Arial",30,"bold"))
    ndq.place(x=550,y=200)

    a_choose=Button(nd_question_hard,text="a)الاخطبوط",font=("Arial",30),bg="orange",command=lambda :(true_nd_hard()))
    a_choose.place(x=550,y=280)

    b_choose=Button(nd_question_hard,text="b)الاسد",font=("Arial",30),bg="orange",command=lambda :(false_nd_hard()))
    b_choose.place(x=800,y=280)

    c_choose=Button(nd_question_hard,text="c)الحوت الازرق",font=("Arial",30),bg="orange",command=lambda :(false_nd_hard()))
    c_choose.place(x=550,y=400)

    d_choose=Button(nd_question_hard,text="d)الفيل الاسيوي",font=("Arial",30),bg="orange",command=lambda :(false_nd_hard()))
    d_choose.place(x=800,y=400)

    next_btn_nd_hard=Button(nd_question_hard,text="next",font=("Arial",30),bg="green",command=lambda :(next_nd_hard()))
    next_btn_nd_hard.place(x=1200,y=700)

    previous_btn_nd_hard=Button(nd_question_hard,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_nd_hard()))
    previous_btn_nd_hard.place(x=1300,y=700)

    ndstl=Label(nd_question_hard,text="100 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    ndstl.place(x=10,y=10)

    ndndl=Label(nd_question_hard,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndndl.place(x=10,y=110)

    ndrdl=Label(nd_question_hard,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndrdl.place(x=10,y=210)

    ndforthl=Label(nd_question_hard,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndforthl.place(x=10,y=310)

    ndfifthl=Label(nd_question_hard,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndfifthl.place(x=10,y=410)

    ndsixthl=Label(nd_question_hard,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndsixthl.place(x=10,y=510)

    ndseventhl=Label(nd_question_hard,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndseventhl.place(x=10,y=610)

    ndeighthl=Label(nd_question_hard,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    ndeighthl.place(x=10,y=710)

def rd_question_hard():
    rd_question_hard = Tk()
    rd_question_hard.title("rd question_hard")
    rd_question_hard.config(bg=("#0000ff"))
    rd_question_hard.geometry = ("600x600+600+600")

    rdq = Label(rd_question_hard, text="ما هي اصغر قارة في العالم", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    rdq.place(x=600, y=200)

    a_choose = Button(rd_question_hard, text="a)امريكا الشمالية", font=("Arial", 30), bg="orange", command=lambda: (false_rd_hard()))
    a_choose.place(x=600, y=280)

    b_choose = Button(rd_question_hard, text="b)المريكا الجنوبية", font=("Arial", 30), bg="orange", command=lambda: (false_rd_hard()))
    b_choose.place(x=800, y=280)

    c_choose = Button(rd_question_hard, text="c)استراليا", font=("Arial", 30), bg="orange", command=lambda: (true_rd_hard()))
    c_choose.place(x=600, y=400)

    d_choose = Button(rd_question_hard, text="d)القارة القطبية", font=("Arial", 30), bg="orange", command=lambda: (false_rd_hard()))
    d_choose.place(x=800, y=400)

    next_btn_rd=Button(rd_question_hard,text="next",font=("Arial",30),bg="green",command=lambda :(next_rd_hard()))
    next_btn_rd.place(x=1200,y=700)

    previous_btn_rd=Button(rd_question_hard,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_rd_hard()))
    previous_btn_rd.place(x=1300,y=700)

    rdstl=Label(rd_question_hard,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdstl.place(x=10,y=10)

    rdndl=Label(rd_question_hard,text="500 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    rdndl.place(x=10,y=110)

    rdrdl=Label(rd_question_hard,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdrdl.place(x=10,y=210)

    rdforthl=Label(rd_question_hard,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdforthl.place(x=10,y=310)

    rdfifthl=Label(rd_question_hard,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdfifthl.place(x=10,y=410)

    rdsixthl=Label(rd_question_hard,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdsixthl.place(x=10,y=510)

    rdseventhl=Label(rd_question_hard,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdseventhl.place(x=10,y=610)

    rdeighthl=Label(rd_question_hard,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    rdeighthl.place(x=10,y=710)

def forth_question_hard():
    forth_question_hard = Tk()
    forth_question_hard.title("forth question_hard")
    forth_question_hard.config(bg=("#0000ff"))
    forth_question_hard.geometry = ("600x600+600+600")

    forthq = Label(forth_question_hard, text="ما هي اكبر دولة من حيث المساحة", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    forthq.place(x=600, y=200)

    a_choose = Button(forth_question_hard, text="a)الصين", font=("Arial", 30), bg="orange", command=lambda: (false_forth_hard()))
    a_choose.place(x=600, y=280)

    b_choose = Button(forth_question_hard, text="b)فرنسا", font=("Arial", 30), bg="orange", command=lambda: (false_forth_hard()))
    b_choose.place(x=800, y=280)

    c_choose = Button(forth_question_hard, text="c)اسبانيا", font=("Arial", 30), bg="orange", command=lambda: (false_forth_hard()))
    c_choose.place(x=600, y=400)

    d_choose = Button(forth_question_hard, text="d)روسيا", font=("Arial", 30), bg="orange", command=lambda: (true_forth_hard()))
    d_choose.place(x=800, y=400)

    next_btn_nd=Button(forth_question_hard,text="next",font=("Arial",30),bg="green",command=lambda :(next_forth_hard()))
    next_btn_nd.place(x=1200,y=700)

    previous_btn_nd=Button(forth_question_hard,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_forth_hard()))
    previous_btn_nd.place(x=1300,y=700)

    forthstl=Label(forth_question_hard,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthstl.place(x=10,y=10)

    forthndl=Label(forth_question_hard,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthndl.place(x=10,y=110)

    forthrdl=Label(forth_question_hard,text="1,000 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    forthrdl.place(x=10,y=210)

    forthforthl=Label(forth_question_hard,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthforthl.place(x=10,y=310)

    forthfifthl=Label(forth_question_hard,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthfifthl.place(x=10,y=410)

    forthsixthl=Label(forth_question_hard,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthsixthl.place(x=10,y=510)

    forthseventhl=Label(forth_question_hard,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    forthseventhl.place(x=10,y=610)

    fortheighthl=Label(forth_question_hard,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fortheighthl.place(x=10,y=710)

def fifth_question_hard():
    fifth_question_hard = Tk()
    fifth_question_hard.title("fifth question_hard")
    fifth_question_hard.config(bg=("#0000ff"))
    fifth_question_hard.geometry = ("600x600+600+600")

    fifthq = Label(fifth_question_hard, text="ما هو الكوكب الذي يسمى توام الازض", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    fifthq.place(x=600, y=200)

    a_choose = Button(fifth_question_hard, text="a)المشترى", font=("Arial", 30), bg="orange", command=lambda: (false_fifth_hard()))
    a_choose.place(x=600, y=280)

    b_choose = Button(fifth_question_hard, text="b)المريخ", font=("Arial", 30), bg="orange", command=lambda: (false_fifth_hard()))
    b_choose.place(x=800, y=280)

    c_choose = Button(fifth_question_hard, text="c)الزهرة", font=("Arial", 30), bg="orange", command=lambda: (true_fifth_hard()))
    c_choose.place(x=600, y=400)

    d_choose = Button(fifth_question_hard, text="نبتون(d", font=("Arial", 30), bg="orange", command=lambda: (false_fifth_hard()))
    d_choose.place(x=800, y=400)

    next_btn_nd=Button(fifth_question_hard,text="next",font=("Arial",30),bg="green",command=lambda :(next_fifth_hard()))
    next_btn_nd.place(x=1200,y=700)

    previous_btn_nd=Button(fifth_question_hard,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_fifth_hard()))
    previous_btn_nd.place(x=1300,y=700)

    fifthstl=Label(fifth_question_hard,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthstl.place(x=10,y=10)

    fifthndl=Label(fifth_question_hard,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthndl.place(x=10,y=110)

    fifthrdl=Label(fifth_question_hard,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthrdl.place(x=10,y=210)

    fifthforthl=Label(fifth_question_hard,text="50,000 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    fifthforthl.place(x=10,y=310)

    fifthfifthl=Label(fifth_question_hard,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthfifthl.place(x=10,y=410)

    fifthsixthl=Label(fifth_question_hard,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthsixthl.place(x=10,y=510)

    fifthseventhl=Label(fifth_question_hard,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fifthseventhl.place(x=10,y=610)

    fiftheighthl=Label(fifth_question_hard,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    fiftheighthl.place(x=10,y=710)

def sixth_question_hard():
    sixth_question_hard = Tk()
    sixth_question_hard.title("sixth question_hard")
    sixth_question_hard.config(bg=("#0000ff"))
    sixth_question_hard.geometry = ("600x600+600+600")

    sixthq = Label(sixth_question_hard, text="ما هو البحر الذي يتميز بانه الاكثر ملوحة", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    sixthq.place(x=600, y=200)

    a_choose = Button(sixth_question_hard, text="a)المتوسط", font=("Arial", 30), bg="orange", command=lambda: (false_sixth_hard()))
    a_choose.place(x=600, y=280)

    b_choose = Button(sixth_question_hard, text="b)الفلبين ", font=("Arial", 30), bg="orange", command=lambda: (false_sixth_hard()))
    b_choose.place(x=800, y=280)

    c_choose = Button(sixth_question_hard, text="c)الاحمر", font=("Arial", 30), bg="orange", command=lambda: (false_sixth_hard()))
    c_choose.place(x=600, y=400)

    d_choose = Button(sixth_question_hard, text="d)الميت", font=("Arial", 30), bg="orange", command=lambda: (true_sixth_hard()))
    d_choose.place(x=800, y=400)

    next_btn_nd=Button(sixth_question_hard,text="next",font=("Arial",30),bg="green",command=lambda :(next_sixth_hard()))
    next_btn_nd.place(x=1200,y=700)

    previous_btn_nd=Button(sixth_question_hard,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_sixth_hard()))
    previous_btn_nd.place(x=1300,y=700)

    sixthstl=Label(sixth_question_hard,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthstl.place(x=10,y=10)

    sixthndl=Label(sixth_question_hard,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthndl.place(x=10,y=110)

    sixthrdl=Label(sixth_question_hard,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthrdl.place(x=10,y=210)

    sixthforthl=Label(sixth_question_hard,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthforthl.place(x=10,y=310)

    sixthfifthl=Label(sixth_question_hard,text="100,000 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    sixthfifthl.place(x=10,y=410)

    sixthsixthl=Label(sixth_question_hard,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthsixthl.place(x=10,y=510)

    sixthseventhl=Label(sixth_question_hard,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixthseventhl.place(x=10,y=610)

    sixtheighthl=Label(sixth_question_hard,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    sixtheighthl.place(x=10,y=710)

def seventh_question_hard():
    seventh_question_hard = Tk()
    seventh_question_hard.title("seventh question_hard")
    seventh_question_hard.config(bg=("#0000ff"))
    seventh_question_hard.geometry = ("600x600+600+600")

    seventhq = Label(seventh_question_hard, text="ما هي اكبر عظمة في جسم الانسان", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    seventhq.place(x=600, y=200)

    a_choose = Button(seventh_question_hard, text="a)الذراع", font=("Arial", 30), bg="orange", command=lambda: (false_seventh_hard()))
    a_choose.place(x=600, y=280)

    b_choose = Button(seventh_question_hard, text="b)الفخذ", font=("Arial", 30), bg="orange", command=lambda: (true_seventh_hard()))
    b_choose.place(x=800, y=280)

    c_choose = Button(seventh_question_hard, text="c)الظهر", font=("Arial", 30), bg="orange", command=lambda: (false_seventh_hard()))
    c_choose.place(x=600, y=400)

    d_choose = Button(seventh_question_hard, text="d)الساق", font=("Arial", 30), bg="orange", command=lambda: (false_seventh_hard()))
    d_choose.place(x=800, y=400)

    next_btn_nd=Button(seventh_question_hard,text="next",font=("Arial",30),bg="green",command=lambda :(next_seventh_hard()))
    next_btn_nd.place(x=1200,y=700)

    previous_btn_nd=Button(seventh_question_hard,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_seventh_hard()))
    previous_btn_nd.place(x=1300,y=700)

    seventhstl=Label(seventh_question_hard,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhstl.place(x=10,y=10)

    seventhndl=Label(seventh_question_hard,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhndl.place(x=10,y=110)

    seventhrdl=Label(seventh_question_hard,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhrdl.place(x=10,y=210)

    seventhforthl=Label(seventh_question_hard,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhforthl.place(x=10,y=310)

    seventhfifthl=Label(seventh_question_hard,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhfifthl.place(x=10,y=410)

    seventhseventhl=Label(seventh_question_hard,text="500,000 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    seventhseventhl.place(x=10,y=510)

    seventhseventhl=Label(seventh_question_hard,text="700,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventhseventhl.place(x=10,y=610)

    seventheighthl=Label(seventh_question_hard,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    seventheighthl.place(x=10,y=710)

def eighth_question_hard():
    eighth_question_hard = Tk()
    eighth_question_hard.title("eighth question_hard")
    eighth_question_hard.config(bg=("#0000ff"))
    eighth_question_hard.geometry = ("600x600+600+600")

    eighthq = Label(eighth_question_hard, text="ما هو اسرع كوكب دورانا حول الشمس", bg="red", padx=5, pady=5,
                    font=("Arial", 30, "bold"))
    eighthq.place(x=600, y=200)

    a_choose = Button(eighth_question_hard, text="a)زحل", font=("Arial", 30), bg="orange", command=lambda: (false_seventh_hard()))
    a_choose.place(x=600, y=280)

    b_choose = Button(eighth_question_hard, text="b)الارض ", font=("Arial", 30), bg="orange", command=lambda: (false_seventh_hard()))
    b_choose.place(x=800, y=280)

    c_choose = Button(eighth_question_hard, text="c)عطارد", font=("Arial", 30), bg="orange", command=lambda: (true_seventh_hard()))
    c_choose.place(x=600, y=400)

    d_choose = Button(eighth_question_hard, text="d)اورانوس", font=("Arial", 30), bg="orange", command=lambda: (false_seventh_hard()))
    d_choose.place(x=800, y=400)

    previous_btn_nd=Button(eighth_question_hard,text="previous",font=("Arial",30),bg="green",command=lambda :(previous_seventh_hard()))
    previous_btn_nd.place(x=1300,y=700)

    eighthstl=Label(eighth_question_hard,text="100 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eighthstl.place(x=10,y=10)

    eighthndl=Label(eighth_question_hard,text="500 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eighthndl.place(x=10,y=110)

    eighthrdl=Label(eighth_question_hard,text="1,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eighthrdl.place(x=10,y=210)

    eighthforthl=Label(eighth_question_hard,text="50,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eighthforthl.place(x=10,y=310)

    eighthfifthl=Label(eighth_question_hard,text="100,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eighthfifthl.place(x=10,y=410)

    eightheighthl=Label(eighth_question_hard,text="500,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eightheighthl.place(x=10,y=510)

    eightheighthl=Label(eighth_question_hard,text="700,000 $",font=("Arial",30),bg="#03bafc",padx=10,pady=10)
    eightheighthl.place(x=10,y=610)

    eightheighthl=Label(eighth_question_hard,text="1,000,000 $",font=("Arial",30),bg="yellow",padx=10,pady=10)
    eightheighthl.place(x=10,y=710)


opening_window.mainloop()

