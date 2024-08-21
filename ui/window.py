import customtkinter


class List(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.labels = []
        self.grid_columnconfigure(0, weight=1)

    def update_list(self, characters):
        for label in self.labels:
            label.destroy()
        self.labels.clear()

        for i, char in enumerate(characters):
            label = customtkinter.CTkLabel(self, text=char)
            label.grid(row=i, column=0, sticky="we")
            self.labels.append(label)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.characters = []
        self.title("my app")
        self.geometry("1280x720")
        self.grid_columnconfigure((0, 1), weight=1)

        self.button = customtkinter.CTkButton(
            self, text="my button", command=self.add_character)
        self.button.grid(row=0, column=1, padx=20, pady=20,
                         sticky="nsew", columnspan=1)
        self.input = customtkinter.CTkEntry(master=self)
        self.input.grid_configure(
            row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.list = List(self)
        self.list.grid_configure(
            row=1, column=0, sticky="we", columnspan=2)

    def add_character(self):
        new_character = self.input.get()
        if new_character:
            self.characters.append(new_character)
            self.list.update_list(self.characters)
            self.input.delete(0, 'end')
