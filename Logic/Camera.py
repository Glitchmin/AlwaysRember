from enum import Enum


class CameraMode(Enum):
    Free = 0
    Follow = 1

    @staticmethod
    def toggle(current: "CameraMode"):
        match current:
            case CameraMode.Free:
                return CameraMode.Follow
            case CameraMode.Follow:
                return CameraMode.Free
