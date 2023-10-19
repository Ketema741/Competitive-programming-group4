class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hash_set = set()
        
        for email in emails:
            local, domain = email.split("@")
            
            local = local.split("+")[0]
            local = local.replace(".", "")
            new_email = local + "@" + domain
            hash_set.add(new_email)
        
        return len(hash_set)