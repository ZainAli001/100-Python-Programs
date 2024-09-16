data = [('29','jan','2022'),
        ('33','feb','20212'),
        ('12','march','20223'),
        ('12','jan','2021')]
z = sorted(data,key=lambda x:x[0][1])
print(z)