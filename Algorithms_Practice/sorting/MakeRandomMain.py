import MakeRandom

print("파일 이름")
file_name = input()
print("사이즈")
_size = int(input())
print("정수형 최대 범위")
_range = int(input())

myRand = MakeRandom.MakeRandom(file_name, _size, _range)
myRand.run()

