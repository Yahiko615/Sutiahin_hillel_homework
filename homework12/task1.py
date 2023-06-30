class VideoCard:
    """
       A class representing a video card.

       Attributes:
           brand (str): The brand of the video card.
           model (str): The model of the video card.
           video_ram (int): The amount of video RAM (VRAM) in gigabytes.
           power_consumption (int): The power consumption of the video card in watts.
       """

    def __init__(self, brand, model, video_ram, power_consumption):
        self.brand = brand
        self.model = model
        self.video_ram = video_ram
        self.power_consumption = power_consumption

    def __str__(self):
        return f"{self.__class__.__name__}: {{\n  brand: {self.brand}\n  model: {self.model}\n  video_ram:" \
               f" {self.video_ram}GB\n  power_consumption: {self.power_consumption}W\n}}"


if __name__ == "__main__":
    video_card = VideoCard("Nvidia", "Geforce RTX 3060", 8, 320)
    print(video_card)
