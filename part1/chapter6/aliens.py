alien_0 = {'color': 'green', 'point': 5}
alien_1 = {'color': 'yellow', 'point': 10}
alien_2 = {'color': 'red', 'point': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

aliens = []

#创建30个外星人
for alien_number in range(30):
    new_alien = {'color': "green", 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

print(f"创建了的外星人个数：{len(aliens)}")