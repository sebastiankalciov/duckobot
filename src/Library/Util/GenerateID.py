
import secrets

def generateID():
    """
    ## Generates an unique ID for an user when is creating a profile.
    """

    duckobotID = secrets.token_urlsafe(32)

    
    return duckobotID