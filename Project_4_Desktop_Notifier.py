#Project_4_Desktop_Notifier

from win10toast import ToastNotifier

a = input("What is your name ? ")

Toast = ToastNotifier()
Toast.show_toast("Learning Time",f"Hello {a}. It's Time to learn Something new",duration=5)


