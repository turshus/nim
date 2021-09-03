import random
import time
#move(n) takes in the current number of stones and returns how many stones to take.  This function will always win 2/3rds of the time
def move(n):
  if n % 3 == 2:
    print(f'The Computer took 1 stone')
    return 1
  elif n % 3 == 0:
    print(f'The Computer took 2 stones')
    return 2
  else:
    returnStoneNum = random.randint(1, 2)
    print(f'The Computer took {returnStoneNum} stone(s)')
    return returnStoneNum

#prompts user to enter the number of stones.  Returns number of stones
def playerMove():
  while True:
    try:
      numStones = int(input('How many stones will you take? (1 or 2): '))
      if numStones > 2 or numStones < 1:
        raise ValueError
      break
    except:
      print('Sorry, incorrect input.  Enter either 1 or 2...')
      continue

  print(f'You took {numStones} stones')
  return numStones

def checkWinCondition(stones):
  if stones == 0:
    return True
  elif stones == 1:
    return False
  else:
    return None

#this function will return back the result of the game 
#given the number of stones on the table and given that it is currently your turn
def determineWinner(n):
  if n % 3 == 2 or n % 3 == 0:
    return True
  else:
    return False

#Win is the function solved in class that utilizes recursion to solve a game of Nim
def playRound(a_numStones):
  if a_numStones == 0:
    return True
  elif a_numStones == 1:
    return False
  
  return not (playRound(a_numStones-1) and playRound(a_numStones-2))

if __name__ == "__main__":
  print('###################################################')
  print('#I will test 100 calls of each type of algorithm. #')
  print('###################################################\n\n')


  print('Starting recursive algorithm...\n=============================\n\n')
  recursiveTimeStart = time.perf_counter()
  for l_numStones in range(0, 60):
    print(f'  | stones = {l_numStones}, result: {playRound(l_numStones)}, time: {time.perf_counter() - recursiveTimeStart} sec')
  recursiveTimeFinish = time.perf_counter()
  print(f'\nTotal time: {round(recursiveTimeFinish - recursiveTimeStart)} seconds')

  print('Starting Easy Mode algorithm...\n==============================\n\n')
  easyStartTime = time.perf_counter()
  for l_numStones in range(0, 60):
    print(f'  | stones = {l_numStones}, result: {determineWinner(l_numStones)}, time: {time.perf_counter() - easyStartTime} sec')
  easyFinishTime = time.perf_counter()
  print(f'\nTotal time: {round(easyFinishTime - easyStartTime)}')

  #loop to play again
  keepPlaying = True
  while keepPlaying:
    #Intro and get number of stones in pile
    print('\nI will now let you play Nims for fun!\nEnter in how many stones you would like initially in the center in the form of a number:')
    try:
      stones = int(input('Number of stones: '))
      if stones < 0:
        raise ValueError
    except:
      print('**Invalid input** Enter a number greater than 0 please')
      continue

    #Determine who goes first
    isPlayersTurn = False
    print('\nWould you  like to go first, or your opponent?')
    if input("Type '1' to go first, or hit Enter to go second: ") == '1':
      isPlayersTurn = True
    
    roundNum = 1
    #Explanation & Play
    print('\nThe game is simple.  Enter either a 1 or 2 to indicate how many stones you want to take.\nRepeat until someone wins\n')
    while True:
      print('\n#######################')
      print(f'#       Round {roundNum}       #')
      print(f'#    Stones left: {stones}   #')
      print('#######################\n')

      #Check win condition
      winResult = checkWinCondition(stones)
      if (isPlayersTurn and winResult == 1) or (not isPlayersTurn and winResult == 0):
        print('You won!  Congrats!')
        break
      elif (isPlayersTurn and winResult == 0) or (not isPlayersTurn and winResult == 1):
        print('You lost!  Sorry :/')
        break
      
      if isPlayersTurn:  #Player goes first
        stones -= playerMove()

        winResult = checkWinCondition(stones)
        if winResult == 1:
          print('You lost!  Sorry :/')
        elif winResult == 0:
          print('You won!  Congrats!')
          break

        stones -= move(stones)
        winResult = checkWinCondition(stones)
        if winResult == 1:
          print('You won!  Congrats!')
        elif winResult == 0:
          print('You lost!  Sorry :/')
      else: #Computer goes first
        stones -= move(stones)
        winResult = checkWinCondition(stones)
        if winResult == 1:
          print('You won!  Congrats!')
          break
        elif winResult == 0:
          print('You lost!  Sorry :/')
          break

        stones -= playerMove()
        winResult = checkWinCondition(stones)
        if winResult == 1:
          print('You lose!  Sorry :/')
          break
        elif winResult == 0:
          print('You won!  Congrats!')
          break
        
        roundNum += 1

    if input('Good game!\nWould you like to play again? (Enter / n): ').lower() == 'n':
      break
