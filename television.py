class Television:
    # Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    
    def __init__(self) -> None:
        # Instance variables
        self._status = False  # Television is initially off
        self._muted = False  # Television is initially not muted
        self._volume = self.MIN_VOLUME  # Initial volume is set to minimum
        self._channel = self.MIN_CHANNEL  # Initial channel is set to minimum
    
    def power(self) -> None:
        # Toggle power status
        self._status = not self._status
    
    def mute(self) -> None:
        # Toggle mute status if TV is on
        if self._status:
            if not self._muted:
                # Save current volume and set volume to 0 when muting
                self._previous_volume = self._volume  # Save the current volume
                self._muted = True
                self._volume = self.MIN_VOLUME  # Set volume to zero
            else:
                # Restore previous volume when unmuting
                self._muted = False
                self._volume = self._previous_volume  # Restore the saved volume
        else:
            self._muted = False
    
    def channel_up(self) -> None:
        # Increase channel if TV is on
        if self._status:
            self._channel = (self._channel + 1) % (Television.MAX_CHANNEL + 1)
    
    def channel_down(self) -> None:
        # Decrease channel if TV is on
        if self._status:
            self._channel = (self._channel - 1) % (Television.MAX_CHANNEL + 1)
    
    def volume_up(self) -> None:
        # Increase volume if TV is on and unmute TV if muted
        if self._status:
            if self._muted:
                self._muted = False
                self._volume = self._previous_volume
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1
    
    def volume_down(self) -> None:
        # Decrease volume if TV is on and unmute TV if muted
        if self._status:
            if self._muted:
                self._muted = False
                self._volume = self._previous_volume
            if self._volume > Television.MIN_VOLUME:
                self._volume -= 1
    
    def __str__(self) -> str:
        # Return the TV status, channel, and volume as a formatted string
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"

