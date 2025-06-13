# text1="This is "python" tutorial" --- error
text1 = "This is 'python' tutorial"
text2 = 'This is "python" tutorial'
text3 = "This is 'python\" tutorial"
text4 = 'This is "python\' tutorial'


print(text1)
print(text2)
print(text3)
print(text4)

text5 = "this is \\  python tutorial"  # using double \\
print(text5)

text6 = "this is \n python tutorial"  # \n new line
print(text6)
