class Television:
    # Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    
    def __init__(self):
        # Instance variables
        self._status = False  # Television is initially off
        self._muted = False  # Television is initially not muted
        self._volume = self.MIN_VOLUME  # Initial volume is set to minimum
        self._channel = self.MIN_CHANNEL  # Initial channel is set to minimum
        self._previous_volume = self._volume  # Save previous volume for muting
    
    def power(self):
        # Toggle power status
        self._status = not self._status
    
    def mute(self):
        # Toggle mute status if TV is on
        if self._status:
            if not self._muted:
                # Save current volume and set volume to 0 when muting
                self._muted = True
                self._previous_volume = self._volume  # Save the current volume
                self._volume = self.MIN_VOLUME  # Set volume to zero
            else:
                # Restore previous volume when unmuting
                self._muted = False
                self._volume = self._previous_volume  # Restore the saved volume
    
    def channel_up(self):
        # Increase channel if TV is on
        if self._status:
            self._channel = (self._channel + 1) % (self.MAX_CHANNEL + 1)
    
    def channel_down(self):
        # Decrease channel if TV is on
        if self._status:
            self._channel = (self._channel - 1) % (self.MAX_CHANNEL + 1)
    
    def volume_up(self):
        # Increase volume if TV is on and unmute TV if muted
        if self._status:
            if self._muted:
                self._muted = False
                self._volume = self._previous_volume
            if self._volume < self.MAX_VOLUME:
                self._volume += 1
    
    def volume_down(self):
        # Decrease volume if TV is on and unmute TV if muted
        if self._status:
            if self._muted:
                self._muted = False
                self._volume = self._previous_volume
            if self._volume > self.MIN_VOLUME:
                self._volume -= 1
    
    def __str__(self):
        # Return the TV status, channel, and volume as a formatted string
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"
