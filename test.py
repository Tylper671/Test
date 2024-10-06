from ftplib import parse150
from msilib.schema import Property
from typing import override
from Number import numbers

class BaseQueue:

    def __init__(self, lamda: (int, float, tuple), mu: (int, float)):
        self._lamda:float = lamda
        self._mu:float = mu

    @Property
    def lamda(self):
        return self._lamda

    @Property
    def mu(self):
        return self._mu

    @Property
    def lq(self):
        return self._lq

    @Property
    def p0(self):
        return self._p0


    def calc_metrics(self):
        return math.nan

    def is_valid(self):
        """
        Ensures that inputs are numbers or tuples and greater than zero.
        Args:
            lamda: (tuple, list, float, int)
                Arrival rate - the average number of entities arriving
                per time unit
            mu: (float)
                Service Rate - the average number of entities served
                per time unit
            c: (int)
                Servers - the number of available service channels

        Returns: (bool)
            True if inputs are valid, otherwise False
        """
        # Check to see that mu and c are numbers before comparing to 0.
        if not isinstance(mu, numbers.Number):
            return False
        if not mu > 0:
            return False

        if not isinstance(c, numbers.Number):
            return False
        if not c > 0:
            return False

        # If lamda is a tuple, check if each element in lamda is a number
        # before we compare to 0.
        #penis
        if isinstance(lamda, (tuple, list)):
            for i in range(len(lamda)):
                if not isinstance(lamda[i], numbers.Number) or not lamda[i] > 0:
                    return False

        # If lamda isn't a tuple or number, it is an invalid input.
        if not isinstance(lamda, (tuple, list)):
            if not isinstance(lamda, numbers.Number):
                return False

        # If scaler lamda is less than or equal to 0, it is invalid.
        if isinstance(lamda, numbers.Number):
            if not lamda > 0:
                return False

        # If inputs have cleared all the return False if statements,
        # lamda is valid.
        return True


    def is_feasible(self):
        """
            If is_valid is True, is_feasible ensures utilization (ro)
                is less than 1.
            Args:
                lamda: (tuple, list, float, int)
                    Arrival rate - the average number of entities arriving
                mu: (float)
                    Service Rate - the average number of entities served
                c: (int)
                    Servers - the number of available service channels

            Returns: (bool)
                True if the system is feasible (ro < 1) and valid,
                False otherwise.
            """
        # Ensure input is valid before performing operations with the input
        if not is_valid(lamda, mu, c):
            return False

        # Differing ro calculation for when lamda is a tuple or scaler
        if isinstance(lamda, (tuple, list)):
            ro = lam_agg(lamda, mu, c) / (c * mu)
        else:
            ro = lamda / (c * mu)

        # Ro = system utilization
        #
        # A system that is never used would be ro = 0.
        # A system in use 99% of the time would have a ro of 0.99.
        # Ro must be less than 1 because queues with a ro of 1+
        # become infinity over time.
        if ro < 1:
            return True
        else:
            return False

    def simplify_lamda(self, lamda):
        if isinstance(lamda, tuple, list):
            simp_lamda = 0
            for i in range(len(lamda)):
                simp_lamda += lamda[i]
            return simp_lamda




class MM1Queue(BaseQueue):
    def calc_metrics(self):
        print("Metric")
        print(super().is_feasible())

b_queue = BaseQueue(10,4)
print(b_queue.lamda())
b_queue.lamda(12)
print(b_queue.lamda())
