class Planet():
    def rotate(self):
        print("Rotate")

    def revolve(self):
        print("revolve")

    def spin(self):
        print("Spining")

    def rotate_and_revolve(self):
        self.rotate()
        self.revolve()
        self.spin()

earth = Planet()
earth.rotate_and_revolve()