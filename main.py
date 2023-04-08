# =======LOST CITY CALCULATOR========
print("=======LOST CITY CALCULATOR========")

# ========CALCULATE LINE=======
def cal_line(result):
  score = 0
  hands = result[0]
  nums = result[1:]
  score += (hands + 1) * sum(nums)
  return score

# ========USER INPUT=======
def user_input():
  c_1 = list(map(int, input("RED의 결과를 입력하세요: ").split()))
  c_2 = list(map(int, input("BLUE의 결과를 입력하세요: ").split()))
  c_3 = list(map(int, input("GREEN의 결과를 입력하세요: ").split()))
  c_4 = list(map(int, input("YELLOW의 결과를 입력하세요: ").split()))
  c_5 = list(map(int, input("WHITE의 결과를 입력하세요: ").split()))
  c_6 = list(map(int, input("PURPLE의 결과를 입력하세요: ").split()))
  result = [c_1, c_2, c_3, c_4, c_5, c_6]
  return result

player1 = 0
player2 = 0

for i in range(2):
  print(f"\n=======PLAYER {i+1} INPUT=======")
  for j in user_input():
    globals()["player{}".format(i+1)] += cal_line(j)
  result = [] # result 초기화

print("\n=======GAME RESULT=======")
print(f"PLAYER 1: {player1} || PLAYER 2: {player2}")
if player1 > player2:
  print("PLAYER 1 WIN!")
elif player1 < player2:
  print("PLAYER 2 WIN!")
else:
  print("DRAW!")