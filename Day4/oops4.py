class Camera:
    def __init__(self,camera_quality):
        self.camera_quality = camera_quality

    def display_camera_details(self):
        print("Camera Quality:",self.camera_quality)

class Storage:
    def __init__(self, storage_quality):
        self.storage_quality = storage_quality

    def display_storage_details(self):
        print("Storage Quality:",self.storage_quality)

class SmartPhone(Camera, Storage):
    def __init__(self, brand, camera_quality, storage_quality):
        self.brand = brand
        Camera.__init__(self, camera_quality)
        Storage.__init__(self, storage_quality)

    def display_smartphone_details(self):
        print("Smartphone Brand:",self.brand)
        self.display_camera_details()
        self.display_storage_details()
phone = SmartPhone("Realme", "108mp", "64gb")
phone.display_smartphone_details()
