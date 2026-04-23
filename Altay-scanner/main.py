import customtkinter as ctk
from tkinter import messagebox
import threading
from altay_scanner import AltayScannerEngine  # Motorunu buraya import ediyoruz

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AltayScannerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Altay Security Suite - Network Scanner")
        self.geometry("500x550")
        
        self.setup_ui()

    def setup_ui(self):
        # Üst Panel
        self.lbl_title = ctk.CTkLabel(self, text="Altay Scanner v1.0", font=("Arial", 22, "bold"))
        self.lbl_title.pack(pady=20)

        self.entry_ip = ctk.CTkEntry(self, placeholder_text="Hedef IP (Örn: 127.0.0.1)")
        self.entry_ip.pack(pady=5, padx=20, fill="x")

        self.btn_scan = ctk.CTkButton(self, text="Taramayı Başlat", fg_color="#2980b9", command=self.start_scan_thread)
        self.btn_scan.pack(pady=10)

        # Durum Çubuğu
        self.progress = ctk.CTkProgressBar(self)
        self.progress.pack(pady=10, padx=20, fill="x")
        self.progress.set(0)

        # Sonuçlar
        self.log_box = ctk.CTkTextbox(self, height=200)
        self.log_box.pack(pady=10, padx=20, fill="both", expand=True)

    def log(self, message):
        self.log_box.insert("end", message + "\n")
        self.log_box.see("end")

    def update_progress(self, port):
        # Port bulundukça listeye ekle
        self.log(f"[+] Port Açık: {port}")

    def start_scan_thread(self):
        target = self.entry_ip.get()
        if not target:
            messagebox.showwarning("Hata", "Lütfen bir IP adresi girin.")
            return
        
        # Arayüzü dondurmamak için taramayı thread ile başlat
        self.btn_scan.configure(state="disabled")
        self.log_box.delete("0.0", "end")
        self.log(f"[*] Tarama başlatılıyor: {target}...")
        
        scan_thread = threading.Thread(target=self.run_scan, args=(target,))
        scan_thread.start()

    def run_scan(self, target):
        # Motoru çağır
        engine = AltayScannerEngine(target)
        engine.run_scan((1, 1024), callback=self.update_progress)
        
        self.log("[!] Tarama tamamlandı.")
        self.after(0, lambda: self.btn_scan.configure(state="normal"))

if __name__ == "__main__":
    app = AltayScannerApp()
    app.mainloop()