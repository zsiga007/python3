Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
WARNING: The system preference "Prefer tabs when opening documents" is set to
"Always". This will cause various problems with IDLE. For the best experience,
change this setting when running IDLE (via System Preferences -> Dock).
>>> import tkinter as tk
>>> root = tk.Tk()
>>> frame = tk.Frame(root)
>>> frame.pack()
>>> button = tk.Button(frame, text='Quit')
>>> button.pack()
>>> def quit_handler(e):
	e.widget.quit()

	
>>> button.bind('<Button-1>',quit_handler)
'4507567440quit_handler'
>>> root.mainloop()
>>> 
