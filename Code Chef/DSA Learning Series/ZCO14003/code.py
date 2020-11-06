N = int(input())
phone = [int(input()) for _ in range(N)]
final = []
phone.sort()
for i in range(N):
    final.append((phone[i])*(N-i))
print(max(final))