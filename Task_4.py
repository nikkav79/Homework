number = int(input('Enter a number: '))
m_number = number % 10
number = number // 10

while number > 0:
    if number % 10 > m_number:
        m_number = number % 10
    number = number // 10
    
print(m_number)


