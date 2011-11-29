=============
IPrental Client
=============

This module uses the IPRental API for ultimate users 
to query and get proxy addresses from the service 

usage : 
    from iprental import IPRentalClient

    cl = IPrentalClient(username,password,key)
    res= cl.get_proxy()   

