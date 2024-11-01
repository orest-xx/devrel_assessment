from algopy import ARC4Contract, Box, Bytes, Global, String, gtxn
from algopy.arc4 import abimethod


class DevrelAssessment(ARC4Contract):
    def __init__(self) -> None:
        self.box = Box(Bytes, key=b"B")

    @abimethod()
    def fund_account(self, payment: gtxn.PaymentTransaction) -> None:
        assert (
            payment.receiver == Global.current_application_address
        ), "Payment receiver must be the application address"

  
    @abimethod()
    def hello(self, name: String) -> String:
        greetings = "Hello, " + name
        self.box_put(response=greetings)
        return greetings
    
    @abimethod()
    def box_put(self, response: String) -> None:
        self.box.value = response.bytes
