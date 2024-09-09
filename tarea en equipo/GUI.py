import tkinter as tk
from tkinter import messagebox

def mergeSort(arr):
    if len(arr) == 1:
        return arr

    middle = len(arr) // 2
    left_array = arr[:middle]
    right_array = arr[middle:]

    sorted_left_array = mergeSort(left_array)
    sorted_right_array = mergeSort(right_array)

    return Merge(sorted_left_array, sorted_right_array)

def Merge(left_arr, right_arr):
    arr_result = []
    while len(left_arr) > 0 and len(right_arr) > 0:
        if left_arr[0] > right_arr[0]:
            arr_result.append(right_arr[0])
            right_arr.pop(0)
        else:
            arr_result.append(left_arr[0])
            left_arr.pop(0)

    while len(left_arr) > 0:
        arr_result.append(left_arr[0])
        left_arr.pop(0)

    while len(right_arr) > 0:
        arr_result.append(right_arr[0])
        right_arr.pop(0)

    return arr_result

def sort_array():
    try:
        
        input_array = entry.get()
        array = list(map(int, input_array.split(',')))
        sorted_array = mergeSort(array)
        result_label.config(text=f"Array ordenado: {sorted_array}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese una lista de números válidos separados por comas.")


ventana = tk.Tk()
ventana.title("Merge Sort GUI")


entry_label = tk.Label(ventana, text="Ingrese los números separados por comas:")
entry_label.pack(pady=10)

entry = tk.Entry(ventana, width=50)
entry.pack(pady=10)

sort_button = tk.Button(ventana, text="Ordenar", command=sort_array)
sort_button.pack(pady=20)

result_label = tk.Label(ventana, text="")
result_label.pack(pady=10)

ventana.mainloop()
