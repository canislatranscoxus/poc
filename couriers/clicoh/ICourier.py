from abc import ABC, abstractmethod

class ICourier( ABC ):

    _tracking_number = None

    @property
    def tracking_number( self ):
        pass

    @abstractmethod
    def get_rates( self, params ):
        '''use the api and get the prices. The data usually is row and we need to parse and clean.'''
        pass

    @abstractmethod
    def get_menu_rates( self, params ):
        ''' Get the rates from the courier and clean the data to be ready to use in a
        radio button menu in a web page. The output is a dictionary
        { 
            rate_id : { 
                        'desc'      : ...,
                        'price'     : ...,
                        'courier'   : ...,
                      }
            .
            .
            .
        }
        '''
        pass
    
    @abstractmethod
    def create_shipment( self, params ):
        pass

    @abstractmethod
    def create_tracking_number( self, params ):
        '''Crear guia'''
        pass

