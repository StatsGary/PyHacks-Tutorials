# =============================================================================
# Title             PyHacks - subclassing
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      12/07/2022
# =============================================================================


class Boss(object):

    """
    A class to represent a boss

    ...

    Attributes
    ----------
    name : str
        first name of the person
    attitude : str
        attitude of the boss
    behaviour : str
        how the boss behaves
    face : str
        the face of the boss

    Methods
    -------
    get_attitude(self):
        Returns the boss' attitude

    get_behaviour(self):
        Returns the boss' behaviour

    get_face(self):
        Returns the boss' face
    """
    def __init__(self, name, attitude, behaviour, face):
        """
        Constructs all the necessary attributes for the boss object.

        Parameters
        ----------
             name : str
                first name of the person
            attitude : str
                attitude of the boss
            behaviour : str
                how the boss behaves
            face : str
                the face of the boss
        """
        self.name = name
        self.attitude = attitude
        self.behaviour = behaviour
        self.face = face

    def get_attitude(self):
        """
        Prints the boss' attitude.

        If the argument 'additional' is passed, then it is appended after the main info.

        Parameters
        ----------
        additional : str, optional
            More info to be displayed (default is None)

        Returns
        -------
        None
        """
        return self.attitude

    def get_behaviour(self):
        return self.behaviour

    def get_face(self):
        return self.face


class GoodBoss(Boss):
    def __init__(self, name, attitude, behaviour, face):
        super().__init__(name, attitude, behaviour, face)

    def nurture_talent(self):
        print('The employees feel all warm and fuzzy then put their talents to good use.')

    def encourage(self):
        print('The team cheers, starts shoyting awesome slogans and then get back to work.')

class BadBoss(Boss):
    def __init__(self, name, attitude, behaviour, face):
        super().__init__(name, attitude, behaviour, face)

    def hoard_praise(self):
        print('The employees feel cheated and start plotting {}s demise while he stares at his own reflection'.format(self.name))


    def yell(self):
        print("Everyone stares while {} yells. Someone shouts, 'Won't somebody PLEASE think of the children!'".format(self.name))
        print("{} storms off, everyone comforts the victim and one person offers to arrange an 'accident' for {}.".format(self.name, self.name))