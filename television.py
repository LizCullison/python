class Television:
    # Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    
    def __init__(self) -> None:
        # Instance variables
        self.__status = False  # Television is initially off
        self.__muted = False  # Television is initially not muted
        self.__volume = self.MIN_VOLUME  # Initial volume is set to minimum
        self.__channel = self.MIN_CHANNEL  # Initial channel is set to minimum
    
    def power(self) -> None:
        # Toggle power status
        self.__status = not self.__status
    
    def mute(self) -> None:
        # Toggle mute status if TV is on
        if self.__status:
            if not self.__muted:
                # Save current volume and set volume to 0 when muting
                self.__previous_volume = self.__volume  # Save the current volume
                self.__muted = True
                self.__volume = self.MIN_VOLUME  # Set volume to zero
            else:
                # Restore previous volume when unmuting
                self.__muted = False
                self.__volume = self.__previous_volume  # Restore the saved volume
        else:
            self.__muted = False
    
    def channel_up(self) -> None:
        # Increase channel if TV is on
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)
    
    def channel_down(self) -> None:
        # Decrease channel if TV is on
        if self.__status:
            self.__channel = (self.__channel - 1) % (Television.MAX_CHANNEL + 1)
    
    def volume_up(self) -> None:
        # Increase volume if TV is on and unmute TV if muted
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
    
    def volume_down(self) -> None:
        # Decrease volume if TV is on and unmute TV if muted
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
    
    def __str__(self) -> str:
        # Return the TV status, channel, and volume as a formatted string
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"

