# Python3 ,By :- Harsh Udai
# Que. Defanging an IP Address

class Solution:
    def defangIPaddr(self, address: str) -> str:
        address=address.replace(".","[.]")
        return address 
