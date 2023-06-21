class ShapeArea:

    def triangle( self, base, height ):
        area = base * height * 0.50
        return area
    
    def rectangle( self, base, height ):
        area = base * height 
        return area
    
    def square( self, side ):
        area = side * side
        return area