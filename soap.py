from spyne import Application, rpc, ServiceBase, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class CalculatorService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(ctx, a, b):
        return a + b

    @rpc(Integer, Integer, _returns=Integer)
    def subtract(ctx, a, b):
        return a - b

    @rpc(Integer, Integer, _returns=Integer)
    def multiply(ctx, a, b):
        return a * b

    @rpc(Integer, Integer, _returns=Integer)
    def divide(ctx, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a // b

# Create the SOAP application
application = Application(
    [CalculatorService],
    tns="calculator.soap.service",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11()
)

# WSGI Application for running the service
wsgi_app = WsgiApplication(application)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    # Start the server on localhost:8000
    server = make_server("127.0.0.1", 8000, wsgi_app)
    print("SOAP Calculator Service is running on http://127.0.0.1:8000")
    server.serve_forever()
























    #http://www.dneonline.com/calculator.asmx?WSDL
