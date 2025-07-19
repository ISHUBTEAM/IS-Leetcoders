class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid = []

        for email in emails:
            at = email.find('@')
            atUsername = email[:at]
            
            if '+' in atUsername:
                plus = atUsername.find('+')
                atUsername = atUsername[:plus]        

            username = atUsername.replace('.', '')
            domain = email[at:]

            validEmail = username + domain

            if validEmail not in valid:
                valid.append(validEmail)

        return len(valid)
        

# solution with 30 sec at 02:00 am

# def unique():
#     emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
#     # emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
#     #2

#     valid = []

#     for email in emails:
#         at = email.find('@')
#         atUsername = email[:at]
        
#         if '+' in atUsername:
#             plus = atUsername.find('+')
#             atUsername = atUsername[:plus]        

#         username = atUsername.replace('.', '')
#         domain = email[at:]

#         validEmail = username + domain

#         if validEmail not in valid:
#             valid.append(validEmail)

#     return len(valid)

# print(unique())