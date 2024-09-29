import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os
import logging

class FaviconCreatorGUI:
    def __init__(self, master, image_processor):
        self.master = master
        self.image_processor = image_processor
        self.master.title("Favicon Creator")
        self.master.geometry("550x450")
        self.setup_ui()

    def setup_ui(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')  # You can change 'clam' to other themes like 'alt', 'default', 'classic'

        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        # Title
        title_label = ttk.Label(main_frame, text="Favicon Creator", font=("Arial", 20, "bold"))
        title_label.grid(column=0, row=0, columnspan=3, pady=10)

        # File Selection
        ttk.Label(main_frame, text="Input Image:").grid(column=0, row=1, sticky=tk.W, pady=5)
        self.file_entry = ttk.Entry(main_frame, width=40)
        self.file_entry.grid(column=1, row=1, sticky=(tk.W, tk.E), pady=5)
        ttk.Button(main_frame, text="Browse", command=self.browse_file).grid(column=2, row=1, sticky=tk.W, padx=5, pady=5)

        # Save Location
        ttk.Label(main_frame, text="Save Location:").grid(column=0, row=2, sticky=tk.W, pady=5)
        self.save_entry = ttk.Entry(main_frame, width=40)
        self.save_entry.grid(column=1, row=2, sticky=(tk.W, tk.E), pady=5)
        ttk.Button(main_frame, text="Browse", command=self.browse_save_location).grid(column=2, row=2, sticky=tk.W, padx=5, pady=5)

        # Size Options
        ttk.Label(main_frame, text="Favicon Sizes:").grid(column=0, row=3, sticky=tk.W, pady=5)
        self.size_var = tk.StringVar(value="16,32,48,64")
        size_entry = ttk.Entry(main_frame, textvariable=self.size_var, width=20)
        size_entry.grid(column=1, row=3, sticky=tk.W, pady=5)
        ttk.Label(main_frame, text="(comma-separated list)").grid(column=2, row=3, sticky=tk.W, pady=5)

        # Convert Button
        convert_button = ttk.Button(main_frame, text="Convert to Favicon", command=self.convert_to_favicon)
        convert_button.grid(column=0, row=4, columnspan=3, pady=20)

        # Progress Bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(main_frame, length=400, variable=self.progress_var, maximum=100)
        self.progress_bar.grid(column=0, row=5, columnspan=3, pady=10)

        # Preview
        self.preview_frame = ttk.LabelFrame(main_frame, text="Preview", padding="5")
        self.preview_frame.grid(column=0, row=6, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        self.preview_label = ttk.Label(self.preview_frame)
        self.preview_label.pack()

        # Status
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(self.master, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(column=0, row=1, sticky=(tk.W, tk.E))

    def browse_file(self):
        filetypes = [('Image files', '*.png;*.jpg;*.jpeg;*.gif;*.bmp')]
        filename = filedialog.askopenfilename(title="Select an image file", filetypes=filetypes)
        if filename:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, filename)
            self.show_preview(filename)
            self.status_var.set(f"Selected file: {os.path.basename(filename)}")
            logging.info(f"File selected: {filename}")

    def browse_save_location(self):
        directory = filedialog.askdirectory(title="Select save location")
        if directory:
            self.save_entry.delete(0, tk.END)
            self.save_entry.insert(0, directory)
            self.status_var.set(f"Save location: {directory}")
            logging.info(f"Save location selected: {directory}")

    def show_preview(self, filename):
        try:
            image = Image.open(filename)
            image.thumbnail((150, 150))  # Resize for preview
            photo = ImageTk.PhotoImage(image)
            self.preview_label.config(image=photo)
            self.preview_label.image = photo  # Keep a reference
        except Exception as e:
            logging.error(f"Error creating preview: {str(e)}")
            messagebox.showerror("Preview Error", "Unable to create image preview.")

    def convert_to_favicon(self):
        input_path = self.file_entry.get()
        save_location = self.save_entry.get()
        sizes = [int(s.strip()) for s in self.size_var.get().split(',')]

        if not input_path or not save_location:
            messagebox.showwarning("Missing Information", "Please select both an input file and save location.")
            return

        try:
            output_path = os.path.join(save_location, os.path.splitext(os.path.basename(input_path))[0] + '.ico')
            
            def progress_callback(progress):
                self.progress_var.set(progress)
                self.master.update_idletasks()

            self.image_processor.convert_to_favicon(input_path, output_path, sizes, progress_callback)
            
            self.status_var.set("Conversion complete!")
            logging.info(f"Favicon created: {output_path}")
            messagebox.showinfo("Success", f"Favicon created successfully: {output_path}")
        except Exception as e:
            logging.error(f"Error creating favicon: {str(e)}")
            messagebox.showerror("Conversion Error", f"An error occurred: {str(e)}")
        finally:
            self.progress_var.set(0)

def create_gui(image_processor):
    root = tk.Tk()
    gui = FaviconCreatorGUI(root, image_processor)
    return root

if __name__ == "__main__":
    # This is just for testing the GUI separately
    class DummyImageProcessor:
        def convert_to_favicon(self, input_path, output_path, sizes, progress_callback):
            for i in range(101):
                progress_callback(i)
                root.after(20)  # Simulate processing time

    root = create_gui(DummyImageProcessor())
    root.mainloop()
