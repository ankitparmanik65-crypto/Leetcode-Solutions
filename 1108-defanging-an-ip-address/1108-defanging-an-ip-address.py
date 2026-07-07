class Solution:
    def defangIPaddr(self, address: str) -> str:
        #With Inbuilt Function
        # return address.replace(".","[.]")

        #Without Inbuilt Function
        ans = ""
        for i in address:
            if i!=".":
                ans+=i
            else:
                ans+="[.]"
        return ans
        