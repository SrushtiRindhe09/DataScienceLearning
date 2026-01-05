'''
The provided code stub reads an integer,n, from STDIN. For all non-negative 
integers i < n, print i^2 .
'''

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i * i)

'''
Output
i/p : 5
o/p : 0 1 4 9 16
'''