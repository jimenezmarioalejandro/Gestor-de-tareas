import tkinter as tk
from tkinter import messagebox
import json
import os


class GestorTareas:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestor de Tareas")
        self.master.geometry("400x500")

        self.tareas = []
        self.cargar_tareas()

        # ----- Widgets -----

        self.label = tk.Label(master, text="Gestor de Tareas", font=("Arial", 16, "bold"))
        self.label.pack(pady=10)

        self.entry_tarea = tk.Entry(master, width=30, font=("Arial", 12))
        self.entry_tarea.pack(pady=5)

        self.btn_agregar = tk.Button(master, text="Agregar Tarea", width=20, command=self.agregar_tarea)
        self.btn_agregar.pack(pady=5)

        self.lista = tk.Listbox(master, width=40, height=15, font=("Arial", 12))
        self.lista.pack(pady=10)

        self.btn_completar = tk.Button(master, text="Marcar como completada", width=25, command=self.completar_tarea)
        self.btn_completar.pack(pady=5)

        self.btn_eliminar = tk.Button(master, text="Eliminar Tarea", width=20, command=self.eliminar_tarea)
        self.btn_eliminar.pack(pady=5)

        self.actualizar_lista()

    # ------------------------
    #       FUNCIONES
    # ------------------------

    def agregar_tarea(self):
        tarea = self.entry_tarea.get().strip()

        if tarea == "":
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")
            return

        self.tareas.append({"texto": tarea, "completada": False})
        self.entry_tarea.delete(0, tk.END)

        self.guardar_tareas()
        self.actualizar_lista()

    def completar_tarea(self):
        seleccion = self.lista.curselection()

        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una tarea.")
            return

        index = seleccion[0]
        self.tareas[index]["completada"] = True

        self.guardar_tareas()
        self.actualizar_lista()

    def eliminar_tarea(self):
        seleccion = self.lista.curselection()

        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una tarea.")
            return

        index = seleccion[0]
        self.tareas.pop(index)

        self.guardar_tareas()
        self.actualizar_lista()

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)

        for tarea in self.tareas:
            texto = tarea["texto"]
            if tarea["completada"]:
                texto += " ✔"
            self.lista.insert(tk.END, texto)

    def guardar_tareas(self):
        with open("tareas.json", "w") as f:
            json.dump(self.tareas, f, indent=4)

    def cargar_tareas(self):
        if os.path.exists("tareas.json"):
            with open("tareas.json", "r") as f:
                self.tareas = json.load(f)


# Ejecutar programa
if __name__ == "__main__":
    root = tk.Tk()
    app = GestorTareas(root)
    root.mainloop()
