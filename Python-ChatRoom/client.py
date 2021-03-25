import tkinter
from socket import *
from threading import Thread

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(("127.0.0.1",55552))
BUFFER_SIZE = 64000


def send_message():
    message = message_box.get()
    message_box.set("")
    sock.send(bytes(message, "utf8"))
    if message == "-1":
        sock.close()
        top.quit()



def receive_message():
    while True:
        message = sock.recv(BUFFER_SIZE).decode("utf8")
        list_box.insert(tkinter.END, message)


def on_window_close():
    message_box.set("-1")
    send_message()

top = tkinter.Tk()
top.title("LAB-2")
messages_frame = tkinter.Frame(top)

message_box = tkinter.StringVar()  # For the messages to be sent.
message_box.set("")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
list_box = tkinter.Listbox(messages_frame, height=18, width=73, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
list_box.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
list_box.pack()

messages_frame.pack()

button_label = tkinter.Label(top, text="Enter Message:")
button_label.pack()
entry_field = tkinter.Entry(top, textvariable=message_box, foreground="Red")
entry_field.bind("<Return>", send_message)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send_message)
send_button.pack()


quit_button = tkinter.Button(top, text="Quit", command=on_window_close)
quit_button.pack()

top.protocol("WM_DELETE_WINDOW", on_window_close)

receive_thread = Thread(target=receive_message)
receive_thread.start()
tkinter.mainloop() 
