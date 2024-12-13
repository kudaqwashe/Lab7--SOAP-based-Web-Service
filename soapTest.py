from zeep import Client


client = Client(wsdl="http://127.0.0.1:8000/?wsdl")
print(client.service.Add(5, 3))          
print(client.service.Subtract(10, 4))   
print(client.service.Multiply(6, 7))    
print(client.service.Divide(20, 4)) 