class Solution:
    def compareVersion(self, version1, version2):
        version1=list(map(int,version1.split('.')))
        version2=list(map(int,version2.split('.')))
        n=len(version1)
        m=len(version2)
        if(n>m):
            for i in range(n-m):
                version2.append(0)
        else:
            for i in range(m-n):
                version1.append(0)

        for i in range(len(version1)):
            if(version1[i]>version2[i]):
                return 1
            if(version1[i]<version2[i]):
                return -1
        return 0