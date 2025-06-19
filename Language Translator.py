import tkinter as tk
from tkinter import ttk, messagebox

class Translator:
    def __init__(self, translation_dict):
        self.translation_dict = translation_dict
    
    def translate(self, text):
        return self.translation_dict.get(text.lower(), "Translation not found")

    def add_translation(self, word, translation):
        self.translation_dict[word.lower()] = translation

class FrenchTranslator(Translator):
    def __init__(self):
        super().__init__({
            "hello": "bonjour",
            "how are you?": "comment ça va ?",
            "good morning": "bonjour",
            "goodbye": "au revoir",
            "thank you": "merci",
            "yes": "oui",
            "no": "non",
            "please": "s'il vous plaît",
            "sorry": "pardon"
        })

class SpanishTranslator(Translator):
    def __init__(self):
        super().__init__({
            "hello": "hola",
            "how are you?": "¿cómo estás?",
            "good morning": "buenos días",
            "goodbye": "adiós",
            "thank you": "gracias",
            "yes": "sí",
            "no": "no",
            "please": "por favor",
            "sorry": "lo siento"
        })

class TranslatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Language Translator")
        
        self.french_translator = FrenchTranslator()
        self.spanish_translator = SpanishTranslator()
        
        self.source_frame = tk.Frame(self)
        self.source_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        self.source_label = tk.Label(self.source_frame, text="Source Text:")
        self.source_label.pack(anchor=tk.W)
        
        self.source_text_box = tk.Text(self.source_frame, height=10, wrap=tk.WORD)
        self.source_text_box.pack(fill=tk.BOTH, expand=True)
        
        self.options_frame = tk.Frame(self)
        self.options_frame.pack(padx=10, pady=5, fill=tk.X)
        
        self.target_language_label = tk.Label(self.options_frame, text="Target Language:")
        self.target_language_label.pack(side=tk.LEFT)
        
        self.target_language_var = tk.StringVar(value="French")
        self.target_language_menu = ttk.Combobox(self.options_frame, textvariable=self.target_language_var)
        self.target_language_menu['values'] = ["French", "Spanish"]
        self.target_language_menu.pack(side=tk.LEFT, padx=5)
        
        self.translate_button = tk.Button(self.options_frame, text="Translate", command=self.translate_text)
        self.translate_button.pack(side=tk.RIGHT)
        
        self.result_frame = tk.Frame(self)
        self.result_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        self.result_label = tk.Label(self.result_frame, text="Translated Text:")
        self.result_label.pack(anchor=tk.W)
        
        self.result_text_box = tk.Text(self.result_frame, height=10, wrap=tk.WORD, state=tk.DISABLED)
        self.result_text_box.pack(fill=tk.BOTH, expand=True)
    
    def translate_text(self):
        source_text = self.source_text_box.get("1.0", tk.END).strip()
        if not source_text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return
        
        target_language = self.target_language_var.get()
        if target_language == "French":
            translator = self.french_translator
        elif target_language == "Spanish":
            translator = self.spanish_translator
        
        translated_text = translator.translate(source_text)
        
        self.result_text_box.config(state=tk.NORMAL)
        self.result_text_box.delete("1.0", tk.END)
        self.result_text_box.insert(tk.END, translated_text)
        self.result_text_box.config(state=tk.DISABLED)

if __name__ == "__main__":
    app = TranslatorApp()
    app.mainloop()
