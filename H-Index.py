class solution:
    def __init__(self, citations):
        citations=list(self.citations)

    def hindex(citations):
        for h in range(len(citations)-1,-1,-1):
            count=0
            # print(f"h is {h}")
            for k in citations:
                if k>=int(citations[h]):
                    count+=1
            # print(f"count is {count}")
            if count >= int(citations[h]):
                return citations[h]

print(solution.hindex(input("provide citations: ")))
