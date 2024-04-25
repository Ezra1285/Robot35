import tkinter as tk

class DraggableIcon:
    def __init__(self, canvas, image, x, y):
        self.canvas = canvas
        self.image = image
        self.id = canvas.create_image(x, y, image=image, anchor=tk.CENTER)
        self.canvas.tag_bind(self.id, "<ButtonPress-1>", self.on_drag_start)
        self.canvas.tag_bind(self.id, "<B1-Motion>", self.on_drag_motion)
        self.canvas.tag_bind(self.id, "<ButtonRelease-1>", self.on_drag_release)
        self.slot = None
        
    def on_drag_start(self, event):
        self.drag_data = {'x': event.x, 'y': event.y}
        
    def on_drag_motion(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        self.canvas.moveto(self.id, x, y)
        
    def on_drag_release(self, event):
        self.snap_to_slot()

    def snap_to_slot(self):
        for slot in slots:
            if self.canvas.bbox(self.id, tagOrId=slot):
                x, y = self.canvas.coords(slot)
                width = 30  # Adjust this value according to the slot size
                self.canvas.moveto(self.id, x + width // 2, y + width // 2)
                self.slot = slot
                return
        # If not in any slot, move back to original position
        self.canvas.moveto(self.id, 50 + icons.index(self) * 50, 50)


def main():
    root = tk.Tk()
    root.title("Draggable Icons")

    canvas = tk.Canvas(root, width=400, height=400, bg='white')
    canvas.pack(fill=tk.BOTH, expand=True)

    # Create draggable icons
    icon_paths = [
        "motors_forward.png",
        "motors_turn.png",
        "head_tilt.png",
        "head_pan.png",
        "waist_turn.png",
        "wait_for_input.png",
        "talking.png"
    ]
    global icons
    icons = []
    for i, icon_path in enumerate(icon_paths):
        icon = tk.PhotoImage(file=icon_path)
        draggable_icon = DraggableIcon(canvas, icon, 50 + i * 50, 50)
        icons.append(draggable_icon)

    # Create slots
    global slots
    slots = []
    for i in range(9):
        slot = canvas.create_rectangle(50 + i * 50, 300, 80 + i * 50, 330, outline='black', fill='white')
        slots.append(slot)

    root.mainloop()

if __name__ == "__main__":
    main()
