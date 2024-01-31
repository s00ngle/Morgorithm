N = int(input())
M = int(input())
broken = list(map(int, input().split()))

buttons = [True] * 10
for button in broken:
    buttons[button] = False

def possible(channel):
    if channel == 0:
        return buttons[0]
    else:
        while channel > 0:
            if not buttons[channel % 10]:
                return False
            channel //= 10
        return True
    
min_count = abs(N - 100)

for channel in range(1000001):
    if possible(channel):
        min_count = min(min_count, len(str(channel)) + abs(N - channel))

print(min_count)