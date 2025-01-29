import psutil
import tkinter as tk
from tkinter import ttk

def update_stats():
    # Get CPU and memory usage
    cpu_usage = psutil.cpu_percent(interval=0)
    memory = psutil.virtual_memory()
    memory_usage = memory.percent

    # Update labels
    cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
    memory_label.config(text=f"Memory Usage: {memory_usage}%")

    # Update progress bars
    cpu_progress["value"] = cpu_usage
    memory_progress["value"] = memory_usage

    # Refresh every second
    root.after(1000, update_stats)

# Create the main GUI window
root = tk.Tk()
root.title("System Monitor")
root.geometry("300x150")

# Labels
cpu_label = ttk.Label(root, text="CPU Usage: 0%", font=("Arial", 12))
cpu_label.pack(pady=5)

cpu_progress = ttk.Progressbar(root, length=250, mode="determinate", maximum=100)
cpu_progress.pack()

memory_label = ttk.Label(root, text="Memory Usage: 0%", font=("Arial", 12))
memory_label.pack(pady=5)

memory_progress = ttk.Progressbar(root, length=250, mode="determinate", maximum=100)
memory_progress.pack()

# Start updating stats
update_stats()

# Run the GUI loop
root.mainloop()