import tkinter as tk
from tkinter import ttk
import subprocess
import os
import ctypes
import sys
import win32print
import threading
import time

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def list_printers():
    result = subprocess.run(['wmic', 'printer', 'get', 'name'], capture_output=True, text=True)
    printers = [line.strip() for line in result.stdout.split('\n') if line.strip() and line.strip() != 'Name']
    return printers

def get_printer_status(printer_name):
    try:
        handle = win32print.OpenPrinter(printer_name)
        status = win32print.GetPrinter(handle, 2)['Status']
        win32print.ClosePrinter(handle)
        return "Online" if status & win32print.PRINTER_STATUS_ONLINE else "Offline"
    except:
        return "Tidak diketahui"

def clear_print_queue(output_text, loader_label, root):
    def clear_queue_thread():
        try:
            for i in range(4): 
                output_text.insert(tk.END, f'Langkah {i+1}...\n')
                subprocess.Popen(['net', 'stop', 'spooler'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                os.system('del /Q /F /S "%systemroot%\\System32\\spool\\PRINTERS\\*.*"')
                subprocess.Popen(['net', 'start', 'spooler'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                loader_label.config(text='. . . '[:i % 4]) 
                root.update_idletasks()
                time.sleep(1) 
            output_text.insert(tk.END, 'Antrian printer berhasil dihapus.\n')
        except subprocess.CalledProcessError as e:
            output_text.insert(tk.END, f'Gagal menghapus antrian printer: {e}\n')
        except Exception as e:
            output_text.insert(tk.END, f'Error: {e}\n')
        finally:
            loader_label.config(text='') 
    threading.Thread(target=clear_queue_thread).start()

def main():
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        return

    root = tk.Tk()
    root.title('Pembersih Antrian Printer')

    printers = list_printers()
    printer_listbox = tk.Listbox(root, width=60) 
    for printer in printers:
        status = get_printer_status(printer)
        printer_listbox.insert(tk.END, f"{printer} ({status})")
    printer_listbox.pack()

    def refresh_printers():
        new_printers = list_printers()
        printer_listbox.delete(0, tk.END)
        for printer in new_printers:
            status = get_printer_status(printer)
            printer_listbox.insert(tk.END, f"{printer} ({status})")
        output_text.insert(tk.END, 'Daftar printer diupdate.\n')

    loader_label = ttk.Label(root, text='')
    loader_label.pack()

    clear_button = ttk.Button(root, text='Hapus Semua Antrian', 
                              command=lambda: clear_print_queue(output_text, loader_label, root))
    clear_button.pack()

    refresh_button = ttk.Button(root, text='Refresh', command=refresh_printers)
    refresh_button.pack()

    exit_button = ttk.Button(root, text='Keluar', command=root.destroy)
    exit_button.pack()

    output_text = tk.Text(root, height=5)
    output_text.pack()

    copyright_label = ttk.Label(root, text='© 2024 - instagram@sedotphp')
    copyright_label.pack()

    root.mainloop()

if __name__ == '__main__':
    main()
