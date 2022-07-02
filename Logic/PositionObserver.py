class PositionObserver:
    def __init__(self):
        self._position_changed = False

    def position_updated(self):
        self._position_changed = True

    def observer_updated(self):
        self._position_changed = False