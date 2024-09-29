
import os
import sys
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import logging

# Setup logging
logging.basicConfig(filename='favicon_creator.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class FaviconCreator:
    def __init__(self, root):
        self.root = root
        self.root.title("Favicon Creator")
        self.root.geometry("500x400")
        
        # Set icon for the application window
        if getattr(sys, 'frozen', False):
            # If the application is run as a bundle, the PyInstaller bootloader
            # extends the sys module by a flag frozen=True and sets the app 
            # path into variable _MEIPASS'.
            application_path = sys._MEIPASS
        else:
            application_path = os.path.dirname(os.path.abspath(__file__))
        
        icon_path = os.path.join(application_path, 'assets', 'fiiltered.ico')
        self.root.iconbitmap(icon_path)

        self.setup_ui()

    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Widgets
        ttk.Label(main_frame, text="Favicon Creator", font=("Arial", 18)).grid(column=0, row=0, columnspan=2, pady=10)

        ttk.Button(main_frame, text="Browse Images", command=self.browse_files).grid(column=0, row=1, pady=5, padx=5, sticky=tk.W)
        self.file_label = ttk.Label(main_frame, text="No file selected")
        self.file_label.grid(column=1, row=1, pady=5, padx=5, sticky=tk.W)

        ttk.Button(main_frame, text="Select Save Location", command=self.select_save_location).grid(column=0, row=2, pady=5, padx=5, sticky=tk.W)
        self.save_label = ttk.Label(main_frame, text="No location selected")
        self.save_label.grid(column=1, row=2, pady=5, padx=5, sticky=tk.W)

        ttk.Button(main_frame, text="Convert to Favicon", command=self.convert_to_favicon).grid(column=0, row=3, columnspan=2, pady=10)

        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(main_frame, length=300, variable=self.progress_var, maximum=100)
        self.progress_bar.grid(column=0, row=4, columnspan=2, pady=10)

        # Image preview
        self.preview_label = ttk.Label(main_frame)
        self.preview_label.grid(column=0, row=5, columnspan=2, pady=10)

    def browse_files(self):
        filetypes = [('Image files', '*.png;*.jpg;*.jpeg;*.gif;*.bmp')]
        filename = filedialog.askopenfilename(title="Select an image file", filetypes=filetypes)
        if filename:
            self.file_label.config(text=os.path.basename(filename))
            self.show_preview(filename)
            logging.info(f"File selected: {filename}")

    def select_save_location(self):
        directory = filedialog.askdirectory(title="Select save location")
        if directory:
            self.save_label.config(text=directory)
            logging.info(f"Save location selected: {directory}")

    def show_preview(self, filename):
        try:
            image = Image.open(filename)
            image.thumbnail((100, 100))  # Resize for preview
            photo = ImageTk.PhotoImage(image)
            self.preview_label.config(image=photo)
            self.preview_label.image = photo  # Keep a reference
        except Exception as e:
            logging.error(f"Error creating preview: {str(e)}")
            messagebox.showerror("Preview Error", "Unable to create image preview.")

    def convert_to_favicon(self):
        input_path = self.file_label.cget("text")
        save_location = self.save_label.cget("text")

        if input_path == "No file selected" or save_location == "No location selected":
            messagebox.showwarning("Missing Information", "Please select both an input file and save location.")
            return

        try:
            input_path = os.path.join(os.path.dirname(self.file_label.cget("text")), input_path)
            output_path = os.path.join(save_location, os.path.splitext(os.path.basename(input_path))[0] + '.ico')

            original = Image.open(input_path)
            icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
            
            self.progress_var.set(0)
            self.root.update_idletasks()

            icons = []
            for size in icon_sizes:
                self.progress_var.set((icon_sizes.index(size) + 1) / len(icon_sizes) * 100)
                self.root.update_idletasks()
                
                icon = original.copy()
                icon.thumbnail(size, Image.LANCZOS)
                icons.append(icon)

            icons[0].save(output_path, format='ICO', sizes=icon_sizes, append_images=icons[1:])
            
            self.progress_var.set(100)
            logging.info(f"Favicon created: {output_path}")
            messagebox.showinfo("Success", f"Favicon created successfully: {output_path}")
        except Exception as e:
            logging.error(f"Error creating favicon: {str(e)}")
            messagebox.showerror("Conversion Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    FaviconCreator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
