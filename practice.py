from tkinter import *

import speech_recognition as sr


addTwoNumbersJava = """
import java.util.Scanner;

public class Main {

    static int a,b;

    public static void main(String[] args) {
	// write your code here

        Scanner scanner=new Scanner(System.in);


        System.out.println("Enter A : ");

        a=scanner.nextInt();

        System.out.println("Enter B : ");

        b=scanner.nextInt();

        System.out.println("Sum is : "+(a+b));


    }
}

"""

def createJavaFile():
    file=open("AddTwoNumbers.java","w+")

    file.write(addTwoNumbersJava)
    label['text']="File Created Successfully"
    print("File Created Successfully")



addTwoNumbersC = """
#include<iostream>
using namespace std;
int a,b;
int main(){

  cout<<"Enter A : ";
  cin>>a;
  cout<<"Enter B : ";
  cin>>b;

  cout<<"Sum is ";
  cout<<(a+b);

  return 0;
} 
"""

def createCppFile():
    file=open("AddTwoNumbers.cpp","w+")

    file.write(addTwoNumbersC)

    label['text']="File Created Successfully"
    print("File Created Successfully")




def onClick():



    r = sr.Recognizer()

    # harvard = sr.AudioFile('harvard.wav')

    # with harvard as source:
    #     audio = r.record(source)

    # print(r.recognize_google(audio))

    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        label['text']="Say Something!"
        print("Say Something!")
        audio = r.listen(source)
    try:
        text=r.recognize_google(audio)
        label['text']="Okay so you said ",text
        print("Okay so you said ",text)
    except Exception as e:
        text="Not Audible"
        label['text']=text
        print(text)
        print(e)

    

    if "java" in text.lower()  and "add" in text.lower():
        createJavaFile()

    elif "c plus plus" in text.lower() and "add" in text.lower():
        createCppFile()

    else:
        label['text']="Sorry not programmed for this right now"
        print("Sorry not programmed for this right now");






window=Tk()
window.geometry("500x500")
label=Label(window,text="Press Below button to code")
label.pack()

label.place(relx=0.5, rely=0.5, anchor=CENTER)

button=Button(window,text="Speak",command=onClick)
button.pack()

button.place(relx=0.5, rely=0.6, anchor=CENTER)



window.mainloop()