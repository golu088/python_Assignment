
from file_download import download_file as download
import tkinter as tk

root = tk.Tk()
root.title("File Downloader")
root.geometry("500x200")

def buttonCall():
    url = urlInput.get()
    fname = filenameInput.get()
    print(f"Url:{url}\nFilename:{fname}")
    download(url, fname)

#label
urlLabel = tk.Label(root, text="URL")
# urlLabel.pack(padx=10, pady=10)
urlLabel.grid(row=0, column=0)

#url entry
urlInput = tk.Entry(root)
# urlInput.pack(padx=10, pady=10)
urlInput.grid(row=0, column=1)

#Label entry filename
filenameLabel= tk.Label(root,text="FileName")
filenameLabel.grid(row=1, column=0)

#filename entry
filenameInput= tk.Entry(root)
filenameInput.grid(row=1, column=1)

# button
downloadButton= tk.Button(root,text="Download", command=buttonCall)
downloadButton.grid(row=2, column=1)


root.mainloop()
