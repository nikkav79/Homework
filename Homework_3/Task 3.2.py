def user_data(name = 'Jhon', surname = 'Jackson', year = 1982, city = 'Boston', email = 'JhonJackson@ecorpmail.com', phone = '+1367298'):

    user_data = {'Name: ': name, 'Surname: ': surname,
                 'Year: ': year, 'City: ': city,
                 'email: ': email, 'phone number: ': phone}

    return user_data

personal_data = user_data(name = 'James', surname = 'Bond', year = 1980, city = 'New York', email = 'JamesBond@agent.com', phone = 'without phone')

for key, value in personal_data.items():
    print(key, value, end = ';    ')

