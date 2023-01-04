class Solution(object):
    def subdomainVisits(self, cpdomains):
        res = collections.Counter()
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            for i in range(len(frags)):
                res[".".join(frags[i:])] += count
        return ["{} {}".format(count, domain) for domain, count in res.items()]