import math 

class Tire:
    """
    tire class
    """

    def __init__(self, tire_type, width, ratio, diameter, brand='', construction='R'):
        self.tire_type = tire_type
        self.width = width
        self.ratio = ratio
        self.diameter = diameter
        self.brand = brand
        self.construction = construction

    def __repr__(self):
        """
        representation of a tire notation
        example: 'P215/65R15'
        """
        return (f"{self.tire_type}{self.width}/{self.ratio}{self.construction}{self.diameter}")

    def circumference(self):
        """
        The circunference of the tire in inches.
        
        >>> tire = Tire('P',205,65,15)
        >>> tire.circumference()
        80.1
        """
        # inside formula or using method
        # side_wall_inches = (self.width * (self.ratio/100))/ 25.4
        # total_diameter = side_wall_inches * 2 + self.diameter
        total_diameter = self._side_wall_inches() * 2 + self.diameter
        return round(total_diameter * math.pi, 1)

    def _side_wall_inches(self):
        return (self.width * (self.ratio/100))/ 25.4

#inheritance 

class SnowTire(Tire):
    def __init__(self,tire_type, width, ratio, diameter, chain_thickness, brand='', construction='R'):
        super().__init__(tire_type, width, ratio, diameter, brand, construction)
        # use super python3
        # python2.7
        # Tire.__init__(self, tire_type, width, ratio, diameter, brand='', construction='R')
        self.chain_thickness = chain_thickness


    def circumference(self):
        """
        the circumference of a tire w/ snow chains in inches
        
        >>> tire = SnowTire('P',205,65,15,2)
        >>> tire.circumference()
        92.7
        """
        total_diameter = (self._side_wall_inches() + self.chain_thickness) *2 + self.diameter
        return round(total_diameter *math.pi, 1)


    def __repr__(self):
        return super().__repr__() + " (Snow)"