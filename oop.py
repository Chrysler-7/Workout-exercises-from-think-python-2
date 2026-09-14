class ExitDoor:
    def open(self):
        print("The mall exit door is now open.")


class Mall:
    def __init__(self, exit_door):
        self._exit_door = exit_door  # Internal use only

    def _open_exit_door(self):
        """Use the mall's exit door internally."""
        self._exit_door.open()

    def run(self, danger):
        if danger:
            self._open_exit_door()
            print("Mall is closing due to danger. Please exit through the door.")
        else:
            print("Mall is open. Enjoy your shopping!")


if __name__ == "__main__":
    door = ExitDoor()
    mall = Mall(door)
    mall.run(False)
    mall.run(True)
