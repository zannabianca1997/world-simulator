# contains a class defining a datafield on the globe
import numpy as np


class DataMap:
    """Define a datafield on all the globe"""
    __latlimits = (-np.pi/2,np.pi/2)
    __longlimits = (0, np.pi*2)

    def __init__(self, resolution, datatype = None, fillfunction = None):
        """inizialize datamap
        :param datatype:
        :param resolution: the resolution of this map in radiant
        :type fillfunction: func(lat, long) -> datatype
        :param fillfunction: the function used to fill the map
        """
        #consts
        self.resolution = resolution
        self.fill(fillfunction)
        if datatype:
            self.datatype = datatype
        else:
            self.datatype = type(fillfunction(0,0))

    @property
    def resolution(self):
        """the resolution of this map in radiant"""
        return self.__resolution

    @resolution.setter
    def resolution(self, resolution):
        """the resolution of this map in radiant"""
        self.__scale_data_to(resolution) #TODO: Complete scaling of datas
        self.__resolution = resolution

    def fill(self, fillfunction):
        """fill the datafield with data
        :type fillfunction: func(lat, long) -> datatype
        :param fillfunction: the function used to fill the map
        """
        pass #TODO: complete filling

    #TODO: Add indexer
