'''
Created on 27-Nov-2011

@author: syedah
'''
from suds.client import Client

class IPRentalClient:
    """ Base calass which implements a simple soap client to communicate with 
    IPRental 
    
    usage : 

        from iprental import IPRentalClient

        cl = IPrentalClient(username,password,key)
        res= cl.get_proxy()   

    """
        
    key = None
    password = None
    username = None
   
    wsdl = 'https://secure.iprental.com/protocols/4.0/public_api.php?wsdl'
    
    def __init__(self,username , password ,key):
        self.username = username
        self.password = password
        self.key = key
        self.client = Client(self.wsdl)
        
    def get_proxy(self):
            resp = self.client.service.PublicAPI(self.key,self.username,self.password, '4.0' , '0' , '' )
            if resp['Response'] < 0 :
                raise ValueError("Auth Failure")
            if resp['Response'] == 202 or resp['Response'] == 203 :
                return resp
            else :
                raise ValueError('Error while getting proxy')
                
