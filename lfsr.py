#-*- coding: utf-8 -*-

DEBUG = False

class LFSR(object):

    def __init__(self, mask):
        # Mask of the LFSR (lsb must be 1)
        self.__m = mask | 1
        # State (to be set with self.seed)
        self.__s = None
        if DEBUG:
            print("[*] MASK: {}".format(hex(mask)))

    def seed(self, s):
        self.__s = s 
        if DEBUG:
            print("[*] SEED: {}".format(hex(s)))

    @property
    def _state(self):
        return self.__s

    @property
    def period(self):
        """
            returns the period of the LFSR

        """
        saved_s = self._state
        p = 1
        self.next()
        while self._state != saved_s and p <= 2**(len(bin(self.__m)) - 2):
            p += 1
            self.next()
        return p

    def next(self):
        if self.__s is None:
            raise ValueError("provide a seed first")
        # Get output bit
        lsb = self.__s & 1
        # Shift to the right
        self.__s /= 2
        # If output bit is 1
        if lsb:
            # XOR state with mask
            self.__s ^=  self.__m
        # Return bit
        return lsb

