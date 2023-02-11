class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hash_set = set()
        
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            
            hash_set.add((local, domain))
        
        return len(hash_set)